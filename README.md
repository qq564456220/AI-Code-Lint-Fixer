# AI-Code-Lint-Fixer

**An open-source AI-powered automatic code lint & fix tool for developers, built for OpenAI Codex ecosystem.**

## 🌐 Language / 多语言
- [简体中文](./docs/README_zh-CN.md)
- [日本語](./docs/README_ja.md)
- [한국어](./docs/README_ko.md)

## Project Overview
AI-Code-Lint-Fixer is a lightweight, cross-platform code standardization tool.
It batch scans local project code, automatically fixes hidden bugs, unifies code style, supplements missing comments, and optimizes redundant logic.

This project is **open-source driven and continuously maintained**, aiming to improve the maintenance quality and readability of open-source projects.

## Why ChatGPT Pro / Codex is Required
This project **cannot run effectively with free-tier models**:
- Batch full-file code refactoring requires **large context window** (Pro exclusive)
- Precise hidden bug analysis relies on **Codex professional code model**
- Stable high-frequency batch processing requires Pro API capability

Free models lack context length and code-domain accuracy for industrial-level project batch optimization.

## Features
- Batch scan `.py` / `.js` project files recursively
- Auto-fix syntax errors and hidden logical bugs
- Unify indentation and coding style
- Auto complete file & function comments
- Simplify redundant code without changing business logic
- Generate standardized fix report for development records
- Zero-config, one-click run

## Installation
```bash
pip install openai
```

## Usage
1. Set your OpenAI API key environment variable
2. Run the entry script
```bash
python main.py
```

## Open Source & Maintenance Plan
This project supports **6-month continuous iteration**:
- Month 1: Stable core release & community document improvement
- Month 2: Add Golang support & custom rule config
- Month 3: Add diff preview & selective fix
- Month 4: Large file chunk optimization for Pro large context
- Month 5: IDE integration & cross-platform adaptation
- Month 6: Official stable release & long-term maintenance

## License
MIT License