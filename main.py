"""
AI-Code-Lint-Fixer
Auto lint, optimize, bug fix and comment completion for Python/JS code
Powered by ChatGPT Pro / OpenAI Codex
"""
import os
from core.scanner import scan_project_files
from core.ai_fixer import fix_code_with_ai
from core.reporter import gen_report
from config import TARGET_DIR, SUFFIX_WHITELIST

def main():
    print("=== AI Code Lint & Fixer (Powered by ChatGPT Pro/Codex) ===")
    file_list = scan_project_files(TARGET_DIR, SUFFIX_WHITELIST)
    if not file_list:
        print("No target code files found.")
        return

    total_files = 0
    total_fixed = 0

    for file_path in file_list:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                raw_code = f.read()
            if not raw_code.strip():
                continue

            fixed_code, changed = fix_code_with_ai(raw_code, file_path)
            if changed:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(fixed_code)
                total_fixed += 1
                print(f"[FIXED] {file_path}")
            total_files += 1
        except Exception as e:
            print(f"[SKIP ERROR] {file_path}: {str(e)}")

    gen_report(total_files, total_fixed)
    print(f"\nDone! Scanned: {total_files} | Fixed: {total_fixed}")

if __name__ == "__main__":
    main()