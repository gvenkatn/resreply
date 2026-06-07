chrome.runtime.onMessage.addListener((message, _sender, sendResponse) => {
    if (message?.type === "GET_SELECTED_TEXT") {
      sendResponse({
        selectedText: window.getSelection()?.toString().trim() || "",
      });
    }
  
    return true;
  });