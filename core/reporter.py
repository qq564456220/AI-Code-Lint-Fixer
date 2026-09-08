import time

def gen_report(total_scan: int, total_fixed: int):
    """Generate local fix report for open-source record"""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    content = (
        "===== AI-Code-Lint-FIXER REPORT =====\n"
        f"Time: {timestamp}\n"
        f"Total Scanned Files: {total_scan}\n"
        f"Total Fixed Files: {total_fixed}\n"
        "======================================\n"
        "Powered by ChatGPT Pro / OpenAI Codex\n"
    )
    with open("fix_report.txt", "w", encoding="utf-8") as f:
        f.write(content)
    print("[REPORT] Saved to fix_report.txt")