export type Tone =
  | "professional"
  | "technical"
  | "recruiter-safe"
  | "supportive"
  | "witty";

export type Suggestion = {
  label: string;
  text: string;
};

export type GenerateRequest = {
  selectedText: string;
  tone: Tone;
};

export type GenerateResponse = {
  summary: string;
  postType: string;
  replyScore: number;
  strategy: string;
  suggestions: Suggestion[];
  warnings: string[];
};