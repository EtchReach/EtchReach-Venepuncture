import ThreeScene from "./ThreeScene";
import Camera from "./Camera";

export default function Home() {
  return (
    <>
      <div style={{
        position: "absolute",   // float on screen
        top: "40px",            // 20px from top
        left: "40px",           // 20px from left
        width: "500px",         // box size
        height: "500px",
        border: "1px solid white", // optional border
        borderRadius: "4px",   // rounded edges
        overflow: "hidden",     // keep canvas clipped
        background: "#c6c6c6ff"      // background behind canvas
      }}>
        <ThreeScene />
      </div>

      <div style={{
        position: "absolute",   // float on screen
        top: "40px",            // 20px from top
        left: "540px",           // 20px from left
        width: "500px",         // box size
        height: "500px",
        border: "1px solid white", // optional border
        borderRadius: "4px",   // rounded edges
        overflow: "hidden",     // keep canvas clipped
        background: "#c6c6c6ff"      // background behind canvas
      }}>
        <Camera />
      </div> 
    </>
  );
}
