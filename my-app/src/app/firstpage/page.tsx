"use client";

import { useEffect } from "react";
import Link from "next/link";
import { Button } from "@/components/ui/button";
import { Calendar } from "@/components/ui/calendar";
import cardData from "@/data/card";
import {
  Card,
  CardAction,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import React from "react";

export default function FirstPage() {
  const [date, setDate] = React.useState<Date | undefined>(new Date());

  useEffect(() => {
    localStorage.setItem("progress", "1");
  }, []);

  return (
    <div>
      <h1 className="flex justify-center p-8 text-[60px]">
        Venepuncture Training
      </h1>

      {/* Calendar */}
      <div className="flex items-center justify-center space-x-4 mb-8">
        <Calendar
          mode="single"
          selected={date}
          onSelect={setDate}
          className="rounded-md border"
        />
      </div>

      {/* Cards */}
      <div className="md:col-span-2 grid grid-cols-1 md:grid-cols-2 gap-4 max-w-4xl mx-auto">
        {cardData.map(
          ({ cardTitle, cardDescription, cardContent, cardFooter }, index) => (
            <Card key={index}>
              <CardHeader>
                <CardTitle>{cardTitle}</CardTitle>
                <CardDescription>{cardDescription}</CardDescription>
                <CardAction>Action</CardAction>
              </CardHeader>
              <CardContent>
                <p>{cardContent}</p>
              </CardContent>
              <CardFooter>
                <p>{cardFooter}</p>
              </CardFooter>
            </Card>
          )
        )}
      </div>

      {/* Next Button */}
      <div className="flex justify-center mt-8">
        <Button asChild variant="secondary">
          <Link href="/secondpage">Next</Link>
        </Button>
      </div>
    </div>
  );
}
