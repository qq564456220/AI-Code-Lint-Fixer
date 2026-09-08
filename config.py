"""
Project Config for AI-Code-Lint-Fixer
"""
# Scan target directory (current dir by default)
TARGET_DIR = "."

# Support file types
SUFFIX_WHITELIST = [".py", ".js"]

# AI Model config (Pro / Codex required)
AI_MODEL = "gpt-4o"
USE_CODEX_FALLBACK = True

# AI Fix rules (stable standard)
AI_FIX_RULES = [
    "Fix syntax errors and hidden logical bugs",
    "Unify code style and indentation",
    "Add missing file-level and function-level docstring/comments",
    "Simplify redundant code without changing business logic",
    "Optimize readability and maintainability",
    "Do NOT change original function behavior"
]