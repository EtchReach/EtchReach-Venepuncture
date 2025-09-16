"use client";

import React, { useRef, useEffect, useState } from "react";
import { Canvas, useFrame, useThree } from "@react-three/fiber";
import { OrbitControls } from "@react-three/drei";
import * as THREE from "three";
import { Grid } from "@react-three/drei";

function CameraZoom({ zoom }: { zoom: number }) {
  const { camera } = useThree();
  camera.position.set(0, 0, zoom); // move camera in/out
  camera.updateProjectionMatrix();
  return null;
}

function CubeWithAngle() {
  const meshRef = useRef<THREE.Mesh>(null!);
  const [pitch, setPitch] = useState(0);
  const [yaw, setYaw] = useState(0);
  const [roll, setRoll] = useState(0);

  // Fetch angle from Flask every second
  useEffect(() => {
    const interval = setInterval(async () => {
      try {
        const res = await fetch("http://localhost:5000/imu");
        const data = await res.json();
        setPitch((data.pitch * Math.PI) / 180); // convert degrees → radians
        setYaw((data.yaw * Math.PI) / 180); // convert degrees → radians
        setRoll((data.roll * Math.PI) / 180); // convert degrees → radians
      } catch (err) {
        console.error("Failed to fetch angle:", err);
      }
    }, 100);

    return () => clearInterval(interval);
  }, []);

  const fPitch = useRef(0);
  const fYaw   = useRef(0);
  const fRoll  = useRef(0);

  const prevPitch = useRef(0);
  const prevYaw = useRef(0);
  const prevRoll = useRef(0);

  // Apply the angle from backend
  useFrame((state) => {

    const velPitch = pitch - prevPitch.current;
    const velYaw   = yaw   - prevYaw.current;
    const velRoll  = roll  - prevRoll.current;

    fPitch.current += (pitch - fPitch.current) * 0.1 + velPitch * 0.05;
    fYaw.current   += (yaw   - fYaw.current) * 0.1 + velYaw * 0.05;
    fRoll.current  += (roll  - fRoll.current) * 0.1 + velRoll * 0.05;

    prevPitch.current = pitch
    prevYaw.current = yaw
    prevRoll.current = roll


    if (meshRef.current) {
      meshRef.current.rotation.x = fPitch.current; // rotate around X axis
      meshRef.current.rotation.y = fYaw.current; // rotate around Y axis
      meshRef.current.rotation.z = fRoll.current; // rotate around Z axis
    }
  });

  return (
    <group ref={meshRef}>
      <mesh>
        <coneGeometry args={[1, 30, 40]} />
        <meshStandardMaterial color="tomato" />
      </mesh>
      <mesh scale={1.05}>
        <coneGeometry args={[1,30,40]} />
        <meshStandardMaterial color="black" side={THREE.BackSide} />
      </mesh>
    </group>
  );
}

export default function ThreeScene() {
  const [zoom, setZoom] = useState(60);
  return (
      <>
        <div
          style={{
            position: "absolute",
            top: 16,
            left: 16,
            zIndex: 1000,           // ⬅ makes sure it stays above canvas
            background: "rgba(0,0,0,0.5)",
            padding: 8,
            borderRadius: 8,
            color: "white",
          }}
        >
          <input
            type="range"
            min="30"
            max="80"
            value={zoom}
            onChange={(e) => setZoom(Number(e.target.value))}
            style={{ position: "absolute", top: 20, left: 20 }}
          />
        </div>
        <Canvas
          // Fill parent; DPR keeps it crisp but not too heavy
          style={{ width: "100%", height: "100%" }}
          dpr={[1, 2]}
          camera={{ position: [0, 0, 40], fov: 50, near: 0.1, far: 100 }}
        >
          <ambientLight intensity={0.5} />
          <pointLight position={[5, 5, 5]} />
          <CubeWithAngle />
          <OrbitControls enableRotate={false} enablePan={false} enableZoom={false} />
          <Grid
            args={[100, 100]}            // size of grid [width, height]
            rotation={[Math.PI / 2,0,0]}
            cellSize={1}               // size of each square
            cellThickness={1}          // line thickness
            cellColor="#6f6f6f"
            sectionSize={5}
            sectionThickness={1.5}
            sectionColor="#9d4b4b"
            fadeDistance={10000}          // fade out distance
            fadeStrength={1}
            followCamera={false}       // keep it static
          />
          <CameraZoom zoom={110-zoom} />
        </Canvas>
    </>
  );
}
