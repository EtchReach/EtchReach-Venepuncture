"use client";

import Link from "next/link";

export default function HomePage() {
  return (
    <main style={{ textAlign: "center", marginTop: "100px" }}>
      <h1>Venepuncture Training</h1>
      <Link href="/firstpage">
        <button style={{ padding: "10px 20px", fontSize: "16px", marginTop: "20px" }}>
          Start
        </button>
      </Link>
    </main>
  );
}
