"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { Button } from "@/components/ui/button";
import Link from "next/link";

export default function ThirdPage() {
  const router = useRouter();
  const [isAuthorized, setIsAuthorized] = useState(false);

  useEffect(() => {
    const progress = localStorage.getItem("progress");
    if (progress !== "2") {
      router.push("/secondpage"); // redirect back if they skip
    } else {
      setIsAuthorized(true);
    }
  }, [router]);

  useEffect(() => {
    if (isAuthorized) {
      localStorage.setItem("progress", "3");
    }
  }, [isAuthorized]);

  return (
    <div className="flex flex-col items-center justify-center mt-16">
      <h1 className="text-4xl mb-8">Third Page</h1>
      <p className="mb-8">Congratulations! You’ve reached the end of the training flow.</p>
      <Button asChild variant="secondary">
        <Link href="/">Finish</Link>
      </Button>
    </div>
  );
}
