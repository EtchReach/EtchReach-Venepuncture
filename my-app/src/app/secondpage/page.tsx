"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import Link from "next/link";
import { Button } from "@/components/ui/button";

export default function SecondPage() {
  const router = useRouter();
  const [isAuthorized, setIsAuthorized] = useState(false);

  useEffect(() => {
    const progress = localStorage.getItem("progress");
    if (progress !== "1") {
      router.push("/firstpage"); // redirect back if they skip
    } else {
      setIsAuthorized(true);
    }
  }, [router]);

  useEffect(() => {
    if (isAuthorized) {
      localStorage.setItem("progress", "2");
    }
  }, [isAuthorized]);

  return (
    <div className="flex flex-col items-center justify-center mt-16">
      <h1 className="text-4xl mb-8">Second Page</h1>
      <Button asChild variant="secondary">
        <Link href="/thirdpage">Next</Link>
      </Button>
    </div>
  );
}
