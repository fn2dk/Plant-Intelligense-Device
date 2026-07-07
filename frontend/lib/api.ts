export type UploadResponse = {
  document_id: string;
  filename: string;
  content_type: string;
  stored_path: string;
};

export type AnalysisResponse = {
  document_id: string;
  status: string;
  stats: {
    page_count: number;
    legend_page_count: number;
    component_count: number;
    extracted_character_count: number;
  };
  page_classifications: Array<{
    page_number: number;
    page_type: string;
    confidence: number;
    reason: string;
  }>;
  legend_items: Array<{
    name: string;
    page_number: number;
    confidence: number;
    source: string;
  }>;
  detected_components: Array<{
    tag: string;
    component_type: string;
    page_number: number | null;
    confidence: number;
    source: string;
  }>;
  extracted_text_preview: string;
  next_actions: string[];
};

const API_BASE = process.env.NEXT_PUBLIC_API_BASE ?? "http://127.0.0.1:8000";

export async function uploadPdf(file: File): Promise<UploadResponse> {
  const formData = new FormData();
  formData.append("file", file);

  const response = await fetch(`${API_BASE}/documents/upload`, {
    method: "POST",
    body: formData,
  });

  if (!response.ok) {
    throw new Error(await response.text());
  }

  return response.json();
}

export async function analyzeDocument(documentId: string): Promise<AnalysisResponse> {
  const response = await fetch(`${API_BASE}/analysis/${documentId}`, {
    method: "POST",
  });

  if (!response.ok) {
    throw new Error(await response.text());
  }

  return response.json();
}
