"use client";

import { useState } from "react";
import { UploadPanel } from "@/components/UploadPanel";
import { AnalysisResult } from "@/components/AnalysisResult";
import { AnalysisResponse } from "@/lib/api";

export default function Home() {
  const [analysis, setAnalysis] = useState<AnalysisResponse | null>(null);

  return (
    <main>
      <div style={{ marginBottom: 24 }}>
        <h1>Plant Intelligense Device</h1>
        <p style={{ color: "var(--muted)", maxWidth: 900 }}>
          Engineering Diagram Intelligence Platform. Upload a P&ID or engineering PDF and run the first analysis pipeline.
        </p>
      </div>

      <div className="grid">
        <UploadPanel onAnalysis={setAnalysis} />
        <AnalysisResult analysis={analysis} />
      </div>
    </main>
  );
}
