"""
AI Code Fix Core — Powered by ChatGPT Pro / OpenAI Codex
Note: Standard free-tier GPT cannot handle long-file full refactoring.
Large context & professional code analysis require Pro capability.
"""
import openai
import os
from config import AI_MODEL, AI_FIX_RULES

openai.api_key = os.getenv("OPENAI_API_KEY")

def build_system_prompt() -> str:
    rules = "\n".join([f"- {r}" for r in AI_FIX_RULES])
    prompt = (
        "You are a professional code linter and refactor engineer powered by OpenAI Codex.\n"
        "Only return fixed code, NO extra explanation.\n"
        f"Follow rules strictly:\n{rules}\n"
        "Keep all original business logic, function names and entry interfaces."
    )
    return prompt

def fix_code_with_ai(raw_code: str, file_path: str) -> tuple[str, bool]:
    """Return (fixed_code, is_changed)"""
    if not raw_code.strip():
        return raw_code, False

    try:
        resp = openai.ChatCompletion.create(
            model=AI_MODEL,
            messages=[
                {"role": "system", "content": build_system_prompt()},
                {"role": "user", "content": f"File: {file_path}\nCode:\n{raw_code}"}
            ],
            temperature=0.1
        )
        fixed = resp.choices[0].message.content.strip()
        return fixed, (fixed != raw_code.strip())
    except Exception as e:
        print(f"AI API Error: {e}")
        return raw_code, False