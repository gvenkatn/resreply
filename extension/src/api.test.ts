import { generateReplies } from "./api";

test("generateReplies calls backend generate endpoint", async () => {
  const mockResponse = {
    summary: "Post summary",
    postType: "generic",
    replyScore: 7,
    strategy: "Respond thoughtfully.",
    suggestions: [{ label: "Short", text: "Great point." }],
    warnings: ["Review before posting."],
  };

  global.fetch = vi.fn().mockResolvedValue({
    ok: true,
    json: vi.fn().mockResolvedValue(mockResponse),
  }) as unknown as typeof fetch;

  const response = await generateReplies({
    selectedText: "Interesting post.",
    tone: "professional",
  });

  expect(fetch).toHaveBeenCalledWith(
    "http://localhost:8000/generate",
    expect.objectContaining({
      method: "POST",
    }),
  );
  expect(response).toEqual(mockResponse);
});

test("generateReplies throws on failed response", async () => {
  global.fetch = vi.fn().mockResolvedValue({
    ok: false,
  }) as unknown as typeof fetch;

  await expect(
    generateReplies({
      selectedText: "Interesting post.",
      tone: "professional",
    }),
  ).rejects.toThrow("Failed to generate replies");
});