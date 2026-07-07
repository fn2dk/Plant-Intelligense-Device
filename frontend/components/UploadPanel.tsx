"use client";

import { useState } from "react";
import { analyzeDocument, AnalysisResponse, uploadPdf } from "@/lib/api";

type Props = {
  onAnalysis: (analysis: AnalysisResponse) => void;
};

export function UploadPanel({ onAnalysis }: Props) {
  const [file, setFile] = useState<File | null>(null);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [documentId, setDocumentId] = useState<string | null>(null);

  async function runUpload() {
    if (!file) return;

    setBusy(true);
    setError(null);

    try {
      const upload = await uploadPdf(file);
      setDocumentId(upload.document_id);
      const analysis = await analyzeDocument(upload.document_id);
      onAnalysis(analysis);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Unknown upload error");
    } finally {
      setBusy(false);
    }
  }

  return (
    <div className="card">
      <h2>Upload P&ID / engineering PDF</h2>
      <p style={{ color: "var(--muted)" }}>
        v0.3 performs first-pass PDF text extraction, page classification, legend detection and tag detection.
      </p>

      <input
        type="file"
        accept="application/pdf"
        onChange={(event) => setFile(event.target.files?.[0] ?? null)}
      />

      <div style={{ marginTop: 16 }}>
        <button disabled={!file || busy} onClick={runUpload}>
          {busy ? "Analyserer..." : "Upload og analysér"}
        </button>
      </div>

      {documentId && (
        <p style={{ color: "var(--muted)" }}>
          Document ID: <code>{documentId}</code>
        </p>
      )}

      {error && <div className="error">{error}</div>}
    </div>
  );
}
