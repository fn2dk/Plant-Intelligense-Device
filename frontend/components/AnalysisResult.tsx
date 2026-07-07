"use client";

import { AnalysisResponse } from "@/lib/api";

type Props = {
  analysis: AnalysisResponse | null;
};

export function AnalysisResult({ analysis }: Props) {
  if (!analysis) {
    return (
      <div className="card">
        <h2>Analysis output</h2>
        <p style={{ color: "var(--muted)" }}>
          Upload a PDF to see the first structured engineering analysis.
        </p>
      </div>
    );
  }

  return (
    <div className="card">
      <h2>Analysis result</h2>

      <div className="stat-row"><span>Status</span><strong>{analysis.status}</strong></div>
      <div className="stat-row"><span>Pages</span><strong>{analysis.stats.page_count}</strong></div>
      <div className="stat-row"><span>Legend pages</span><strong>{analysis.stats.legend_page_count}</strong></div>
      <div className="stat-row"><span>Components detected</span><strong>{analysis.stats.component_count}</strong></div>
      <div className="stat-row"><span>Extracted characters</span><strong>{analysis.stats.extracted_character_count}</strong></div>

      <h3>Page classification</h3>
      {analysis.page_classifications.map((page) => (
        <span className="badge" key={`${page.page_number}-${page.page_type}`}>
          Page {page.page_number}: {page.page_type} ({Math.round(page.confidence * 100)}%)
        </span>
      ))}

      <h3>Legend terms</h3>
      {analysis.legend_items.slice(0, 40).map((item) => (
        <span className="badge" key={`${item.page_number}-${item.name}`}>
          {item.name} / p.{item.page_number}
        </span>
      ))}

      <h3>Detected components</h3>
      <div style={{ maxHeight: 280, overflow: "auto" }}>
        {analysis.detected_components.slice(0, 150).map((component) => (
          <div className="stat-row" key={component.tag}>
            <span>{component.tag}</span>
            <strong>{component.component_type}</strong>
          </div>
        ))}
      </div>

      <h3>Text preview</h3>
      <pre>{analysis.extracted_text_preview}</pre>
    </div>
  );
}
