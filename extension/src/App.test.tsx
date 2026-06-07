import { render, screen, waitFor } from "@testing-library/react";
import { App } from "./App";

beforeEach(() => {
  global.chrome = {
    tabs: {
      query: vi.fn().mockResolvedValue([{ id: 1 }]),
      sendMessage: vi.fn((_tabId, _message, callback) => {
        callback({ selectedText: "Selected post text" });
      }),
    },
  } as unknown as typeof chrome;
});

test("loads selected text from active tab", async () => {
  render(<App />);

  expect(screen.getByText("ResReply")).toBeInTheDocument();

  await waitFor(() => {
    expect(screen.getByLabelText("Selected text")).toHaveValue(
      "Selected post text",
    );
  });
});