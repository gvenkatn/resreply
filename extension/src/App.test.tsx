import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { App } from "./App";
import { generateReplies } from "./api";

vi.mock("./api", () => ({
  generateReplies: vi.fn(),
}));

beforeEach(() => {
  vi.clearAllMocks();

  Object.assign(navigator, {
    clipboard: {
      writeText: vi.fn(),
    },
  });

  global.chrome = {
    tabs: {
      query: vi.fn().mockResolvedValue([{ id: 1 }]),
      sendMessage: vi.fn((_tabId, _message, callback) => {
        callback({ selectedText: "Selected post text" });
      }),
    },
  } as unknown as typeof chrome;
});

test("generates and renders reply suggestions", async () => {
  vi.mocked(generateReplies).mockResolvedValue({
    summary: "Post summary",
    postType: "generic",
    replyScore: 7,
    strategy: "Respond thoughtfully.",
    suggestions: [{ label: "Short", text: "Great point." }],
    warnings: ["Review before posting."],
  });

  render(<App />);

  await waitFor(() => {
    expect(screen.getByLabelText("Selected text")).toHaveValue(
      "Selected post text",
    );
  });

  fireEvent.click(screen.getByText("Generate replies"));

  await waitFor(() => {
    expect(screen.getByText("Reply score: 7/10")).toBeInTheDocument();
    expect(screen.getByText("Great point.")).toBeInTheDocument();
  });
});

test("renders error when generation fails", async () => {
  vi.mocked(generateReplies).mockRejectedValue(new Error("Backend failed"));

  render(<App />);

  await waitFor(() => {
    expect(screen.getByLabelText("Selected text")).toHaveValue(
      "Selected post text",
    );
  });

  fireEvent.click(screen.getByText("Generate replies"));

  await waitFor(() => {
    expect(screen.getByRole("alert")).toHaveTextContent(
      "Failed to generate replies.",
    );
  });
});