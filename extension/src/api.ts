import type { GenerateRequest, GenerateResponse } from "./types";

const API_BASE_URL = "http://localhost:8000";

export async function generateReplies(
  request: GenerateRequest,
): Promise<GenerateResponse> {
  const response = await fetch(`${API_BASE_URL}/generate`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(request),
  });

  if (!response.ok) {
    throw new Error("Failed to generate replies");
  }

  return response.json();
}