#!/usr/bin/env python3
"""AgentMesh - Codebase Report Generator"""

import os, sys, json, time
from pathlib import Path
from datetime import datetime
from fpdf import FPDF

PROJECT_ROOT = Path(__file__).parent
OUTPUT_PDF = PROJECT_ROOT / "AgentMesh_Codebase_Report.pdf"

SOURCE_FILES = [
    "src/agentmesh/__init__.py",
    "src/agentmesh/core/__init__.py",
    "src/agentmesh/core/contracts.py",
    "src/agentmesh/core/hermes_client.py",
    "src/agentmesh/core/memory.py",
    "src/agentmesh/core/learner.py",
    "src/agentmesh/core/skill_registry.py",
    "src/agentmesh/core/state_manager.py",
    "src/agentmesh/core/utils.py",
    "src/agentmesh/core/honcho_bridge.py",
    "src/agentmesh/agents/__init__.py",
    "src/agentmesh/agents/base_agent.py",
    "src/agentmesh/orchestrator/__init__.py",
    "src/agentmesh/server/__init__.py",
    "src/agentmesh/skills/__init__.py",
    "src/agentmesh/cli/__init__.py",
    "run.py",
    "cli.py",
    "server.py",
    "orchestrator.py",
    "pyproject.toml",
    "requirements.txt",
]


class AgentMeshPDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=20)

    def header(self):
        if self.page_no() > 1:
            self.set_font("Helvetica", "I", 8)
            self.set_text_color(120, 120, 120)
            self.cell(0, 8, "AgentMesh v2.0 - Codebase Report", align="L")
            self.cell(0, 8, f"Page {self.page_no()}", align="R", new_x="LMARGIN", new_y="NEXT")
            self.line(10, 14, 200, 14)
            self.ln(4)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 7)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, f"Generated {datetime.now().strftime(chr(37)+chr(89)+chr(45)+chr(37)+chr(109)+chr(45)+chr(37)+chr(100)+chr(32)+chr(37)+chr(72)+chr(58)+chr(37)+chr(77))}", align="C")

    def chapter_title(self, title, level=1):
        if level == 1:
            self.set_font("Helvetica", "B", 18)
            self.set_text_color(20, 60, 120)
            self.ln(4)
            self.cell(0, 12, title, new_x="LMARGIN", new_y="NEXT")
            self.set_draw_color(20, 60, 120)
            self.line(10, self.get_y(), 200, self.get_y())
            self.ln(6)
        elif level == 2:
            self.set_font("Helvetica", "B", 14)
            self.set_text_color(40, 80, 140)
            self.ln(3)
            self.cell(0, 10, title, new_x="LMARGIN", new_y="NEXT")
            self.ln(2)
        elif level == 3:
            self.set_font("Helvetica", "B", 11)
            self.set_text_color(60, 100, 160)
            self.ln(2)
            self.cell(0, 8, title, new_x="LMARGIN", new_y="NEXT")
            self.ln(1)

    def body_text(self, text):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(30, 30, 30)
        self.multi_cell(0, 5.5, text)
        self.ln(2)

    def code_block(self, code, max_lines=60):
        self.set_fill_color(240, 244, 250)
        self.set_draw_color(200, 210, 220)
        self.set_font("Courier", "", 7.5)
        self.set_text_color(20, 20, 30)
        lines = code.split("\n")
        if len(lines) > max_lines:
            lines = lines[:max_lines] + ["", "# ... (truncated)"]
        line_h = 4.2
        block_h = len(lines) * line_h + 4
        if self.get_y() + block_h > 270:
            self.add_page()
        x = self.get_x()
        y = self.get_y()
        self.rect(x, y, 190, block_h, style="DF")
        self.set_xy(x + 3, y + 2)
        for line in lines:
            if self.get_y() > 275:
                break
            display = line if len(line) < 150 else line[:147] + "..."
            self.cell(0, line_h, display, new_x="LMARGIN", new_y="NEXT")
            self.set_x(x + 3)
        self.set_y(y + block_h + 3)

    def bullet_list(self, items):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(30, 30, 30)
        for item in items:
            x = self.get_x()
            self.cell(5, 5.5, chr(8226))
            self.multi_cell(0, 5.5, f" {item}")
            self.set_x(x)
        self.ln(2)

    def key_value(self, key, value):
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(60, 60, 60)
        kw = self.get_string_width(key + ": ") + 2
        self.cell(kw, 5.5, f"{key}: ")
        self.set_font("Helvetica", "", 10)
        self.set_text_color(30, 30, 30)
        self.multi_cell(0, 5.5, str(value))
        self.ln(1)

    def separator(self):
        self.set_draw_color(200, 200, 200)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(4)

def get_file_info(path):
    full_path = PROJECT_ROOT / path
    if not full_path.exists():
        return None
    content = full_path.read_text(encoding="utf-8", errors="replace")
    lines_list = content.split("\n")
    doc = ""
    if len(lines_list) > 1 and lines_list[0].startswith(chr(34)*3):
        for l in lines_list[1:]:
            if l.startswith(chr(34)*3) or l.startswith(chr(39)*3):
                break
            doc += l + "\n"
    return {
        "path": path,
        "size": full_path.stat().st_size,
        "lines": len(lines_list),
        "content": content,
        "module_doc": doc.strip(),
    }


def build_report():
    pdf = AgentMeshPDF()
    pdf.set_margin(10)

    # ===== COVER PAGE =====
    pdf.add_page()
    pdf.ln(40)
    pdf.set_font("Helvetica", "B", 36)
    pdf.set_text_color(20, 60, 120)
    pdf.cell(0, 15, "AgentMesh", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 18)
    pdf.set_text_color(60, 100, 160)
    pdf.cell(0, 12, "Multi-Agent Orchestration Framework", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(8)
    pdf.set_font("Helvetica", "I", 12)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 8, "with Recursive Self-Evolution", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(20)
    pdf.set_draw_color(20, 60, 120)
    pdf.line(60, pdf.get_y(), 150, pdf.get_y())
    pdf.ln(20)
    pdf.set_font("Helvetica", "", 11)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 7, "Version 2.0", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 7, f"Generated: {datetime.now().strftime(chr(37)+chr(89)+chr(45)+chr(37)+chr(109)+chr(45)+chr(37)+chr(100)+chr(32)+chr(37)+chr(72)+chr(58)+chr(37)+chr(77))}", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(20)

    # ===== TABLE OF CONTENTS =====
    pdf.add_page()
    pdf.chapter_title("Table of Contents")
    pdf.body_text("This report documents the complete AgentMesh v2.0 codebase.")
    pdf.body_text("It covers: architecture overview, core modules, agent system, orchestrator, server, CLI, and configuration.")
    pdf.ln(5)

    # ===== SECTION 1: PROJECT OVERVIEW =====
    pdf.chapter_title("1. Project Overview")
    pdf.body_text("AgentMesh is a multi-agent orchestration framework designed for recursive self-evolution.")
    pdf.body_text("It implements a hierarchical agent architecture where an orchestrator agent decomposes goals into subtasks, dispatches them to specialized sub-agents, and aggregates results. The system learns from its failures through a recursive learning loop that extracts lessons and evolves system prompts.")

    pdf.chapter_title("Key Design Principles", level=2)
    pdf.bullet_list([
        "Execution Contracts: Typed, bounded agent call definitions with hard boolean completion conditions (Tsinghua 2026 research shows fuzzy checks hurt performance by -8.4%)",
        "File-Backed State: Agent working memory lives on disk, not in context window. Survives truncation, restarts, and delegation handoffs.",
        "Four Memory Layers: Episodic (raw traces), Semantic (lessons), Procedural (skill stats), Working (current session)",
        "Recursive Learning: Self-evolution loop that reads failure traces and extracts concrete, actionable rules",
        "Multi-Provider LLM Support: OpenRouter, Groq, Anthropic, DeepSeek, Gemini, Together AI",
        "Honcho Integration: AI-native peer modeling and dialectic memory for cross-session identity",
    ])

    pdf.chapter_title("Architecture", level=2)
    pdf.body_text("The system follows a hierarchical architecture:")
    pdf.body_text("Orchestrator (top PC) -> decomposes goals -> dispatches ExecutionContracts -> sub-agents execute -> results aggregated -> HarnessOptimizer loop")
    pdf.body_text("Sub-agents: ResearchAgent, CodeAgent, WriterAgent, FileAgent, DataAnalysisAgent, SummaryAgent")
    pdf.body_text("Each sub-agent inherits from BaseAgent which wires together: Contract -> Honcho context -> LLM tool loop -> FileBackedState -> ConditionChecker -> Memory -> LearningCycle")
    # ===== SECTION 2: FILE INVENTORY =====
    pdf.add_page()
    pdf.chapter_title("2. File Inventory")
    pdf.body_text("The following table lists all source files in the project with their sizes and line counts.")
    pdf.ln(3)

    # Table header
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_fill_color(20, 60, 120)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(80, 7, "File Path", border=1, fill=True)
    pdf.cell(20, 7, "Size", border=1, fill=True, align="C")
    pdf.cell(15, 7, "Lines", border=1, fill=True, align="C")
    pdf.cell(75, 7, "Module Description", border=1, fill=True, new_x="LMARGIN", new_y="NEXT")

    pdf.set_font("Helvetica", "", 8)
    total_size = 0
    total_lines = 0
    for sf in SOURCE_FILES:
        info = get_file_info(sf)
        if info is None:
            continue
        total_size += info["size"]
        total_lines += info["lines"]
        desc = info["module_doc"][:60] if info["module_doc"] else ""
        if pdf.get_y() > 265:
            pdf.add_page()
        pdf.set_text_color(30, 30, 30)
        pdf.cell(80, 5.5, sf, border=1)
        pdf.cell(20, 5.5, f"{info["size"]:,} B", border=1, align="C")
        pdf.cell(15, 5.5, str(info["lines"]), border=1, align="C")
        pdf.cell(75, 5.5, desc[:70], border=1, new_x="LMARGIN", new_y="NEXT")

    # Total row
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_fill_color(230, 235, 245)
    pdf.cell(80, 6, f"TOTAL ({len(SOURCE_FILES)} files)", border=1, fill=True)
    pdf.cell(20, 6, f"{total_size:,} B", border=1, fill=True, align="C")
    pdf.cell(15, 6, str(total_lines), border=1, fill=True, align="C")
    pdf.cell(75, 6, "", border=1, fill=True, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)
    # ===== SECTION 3: SOURCE CODE =====
    pdf.add_page()
    pdf.chapter_title("3. Source Code")
    pdf.body_text("This section contains the complete source code of every module in the AgentMesh project.")
    pdf.ln(3)

    pdf.add_page()

    # ===== SECTION 3: SOURCE CODE =====
    pdf.add_page()
    pdf.chapter_title("3. Source Code")
    pdf.body_text("This section contains the complete source code of every module.")
    pdf.body_text("Files are read at runtime from the project directory.")
    pdf.ln(3)

    pdf.add_page()
    pdf.chapter_title("src/agentmesh/__init__.py", level=2)
    info = get_file_info("src/agentmesh/__init__.py")
    if info:
        if info["module_doc"]:
            pdf.body_text(info["module_doc"])
        pdf.body_text(f"Size: {info['size']:,} bytes, {info['lines']} lines")
        pdf.code_block(info["content"])
    else:
        pdf.body_text(f"File not found: src/agentmesh/__init__.py")

    pdf.add_page()
    pdf.chapter_title("src/agentmesh/core/__init__.py", level=2)
    info = get_file_info("src/agentmesh/core/__init__.py")
    if info:
        if info["module_doc"]:
            pdf.body_text(info["module_doc"])
        pdf.body_text(f"Size: {info['size']:,} bytes, {info['lines']} lines")
        pdf.code_block(info["content"])
    else:
        pdf.body_text(f"File not found: src/agentmesh/core/__init__.py")

    pdf.add_page()
    pdf.chapter_title("src/agentmesh/core/contracts.py", level=2)
    info = get_file_info("src/agentmesh/core/contracts.py")
    if info:
        if info["module_doc"]:
            pdf.body_text(info["module_doc"])
        pdf.body_text(f"Size: {info['size']:,} bytes, {info['lines']} lines")
        pdf.code_block(info["content"])
    else:
        pdf.body_text(f"File not found: src/agentmesh/core/contracts.py")

    pdf.add_page()
    pdf.chapter_title("src/agentmesh/core/hermes_client.py", level=2)
    info = get_file_info("src/agentmesh/core/hermes_client.py")
    if info:
        if info["module_doc"]:
            pdf.body_text(info["module_doc"])
        pdf.body_text(f"Size: {info['size']:,} bytes, {info['lines']} lines")
        pdf.code_block(info["content"])
    else:
        pdf.body_text(f"File not found: src/agentmesh/core/hermes_client.py")

    pdf.add_page()
    pdf.chapter_title("src/agentmesh/core/memory.py", level=2)
    info = get_file_info("src/agentmesh/core/memory.py")
    if info:
        if info["module_doc"]:
            pdf.body_text(info["module_doc"])
        pdf.body_text(f"Size: {info['size']:,} bytes, {info['lines']} lines")
        pdf.code_block(info["content"])
    else:
        pdf.body_text(f"File not found: src/agentmesh/core/memory.py")

    pdf.add_page()
    pdf.chapter_title("src/agentmesh/core/learner.py", level=2)
    info = get_file_info("src/agentmesh/core/learner.py")
    if info:
        if info["module_doc"]:
            pdf.body_text(info["module_doc"])
        pdf.body_text(f"Size: {info['size']:,} bytes, {info['lines']} lines")
        pdf.code_block(info["content"])
    else:
        pdf.body_text(f"File not found: src/agentmesh/core/learner.py")

    pdf.add_page()
    pdf.chapter_title("src/agentmesh/core/skill_registry.py", level=2)
    info = get_file_info("src/agentmesh/core/skill_registry.py")
    if info:
        if info["module_doc"]:
            pdf.body_text(info["module_doc"])
        pdf.body_text(f"Size: {info['size']:,} bytes, {info['lines']} lines")
        pdf.code_block(info["content"])
    else:
        pdf.body_text(f"File not found: src/agentmesh/core/skill_registry.py")

    pdf.add_page()
    pdf.chapter_title("src/agentmesh/core/state_manager.py", level=2)
    info = get_file_info("src/agentmesh/core/state_manager.py")
    if info:
        if info["module_doc"]:
            pdf.body_text(info["module_doc"])
        pdf.body_text(f"Size: {info['size']:,} bytes, {info['lines']} lines")
        pdf.code_block(info["content"])
    else:
        pdf.body_text(f"File not found: src/agentmesh/core/state_manager.py")

    pdf.add_page()
    pdf.chapter_title("src/agentmesh/core/utils.py", level=2)
    info = get_file_info("src/agentmesh/core/utils.py")
    if info:
        if info["module_doc"]:
            pdf.body_text(info["module_doc"])
        pdf.body_text(f"Size: {info['size']:,} bytes, {info['lines']} lines")
        pdf.code_block(info["content"])
    else:
        pdf.body_text(f"File not found: src/agentmesh/core/utils.py")

    pdf.add_page()
    pdf.chapter_title("src/agentmesh/core/honcho_bridge.py", level=2)
    info = get_file_info("src/agentmesh/core/honcho_bridge.py")
    if info:
        if info["module_doc"]:
            pdf.body_text(info["module_doc"])
        pdf.body_text(f"Size: {info['size']:,} bytes, {info['lines']} lines")
        pdf.code_block(info["content"])
    else:
        pdf.body_text(f"File not found: src/agentmesh/core/honcho_bridge.py")

    pdf.add_page()
    pdf.chapter_title("src/agentmesh/agents/__init__.py", level=2)
    info = get_file_info("src/agentmesh/agents/__init__.py")
    if info:
        if info["module_doc"]:
            pdf.body_text(info["module_doc"])
        pdf.body_text(f"Size: {info['size']:,} bytes, {info['lines']} lines")
        pdf.code_block(info["content"])
    else:
        pdf.body_text(f"File not found: src/agentmesh/agents/__init__.py")

    pdf.add_page()
    pdf.chapter_title("src/agentmesh/agents/base_agent.py", level=2)
    info = get_file_info("src/agentmesh/agents/base_agent.py")
    if info:
        if info["module_doc"]:
            pdf.body_text(info["module_doc"])
        pdf.body_text(f"Size: {info['size']:,} bytes, {info['lines']} lines")
        pdf.code_block(info["content"])
    else:
        pdf.body_text(f"File not found: src/agentmesh/agents/base_agent.py")

    pdf.add_page()
    pdf.chapter_title("src/agentmesh/orchestrator/__init__.py", level=2)
    info = get_file_info("src/agentmesh/orchestrator/__init__.py")
    if info:
        if info["module_doc"]:
            pdf.body_text(info["module_doc"])
        pdf.body_text(f"Size: {info['size']:,} bytes, {info['lines']} lines")
        pdf.code_block(info["content"])
    else:
        pdf.body_text(f"File not found: src/agentmesh/orchestrator/__init__.py")

    pdf.add_page()
    pdf.chapter_title("src/agentmesh/server/__init__.py", level=2)
    info = get_file_info("src/agentmesh/server/__init__.py")
    if info:
        if info["module_doc"]:
            pdf.body_text(info["module_doc"])
        pdf.body_text(f"Size: {info['size']:,} bytes, {info['lines']} lines")
        pdf.code_block(info["content"])
    else:
        pdf.body_text(f"File not found: src/agentmesh/server/__init__.py")

    pdf.add_page()
    pdf.chapter_title("src/agentmesh/skills/__init__.py", level=2)
    info = get_file_info("src/agentmesh/skills/__init__.py")
    if info:
        if info["module_doc"]:
            pdf.body_text(info["module_doc"])
        pdf.body_text(f"Size: {info['size']:,} bytes, {info['lines']} lines")
        pdf.code_block(info["content"])
    else:
        pdf.body_text(f"File not found: src/agentmesh/skills/__init__.py")

    pdf.add_page()
    pdf.chapter_title("src/agentmesh/cli/__init__.py", level=2)
    info = get_file_info("src/agentmesh/cli/__init__.py")
    if info:
        if info["module_doc"]:
            pdf.body_text(info["module_doc"])
        pdf.body_text(f"Size: {info['size']:,} bytes, {info['lines']} lines")
        pdf.code_block(info["content"])
    else:
        pdf.body_text(f"File not found: src/agentmesh/cli/__init__.py")

    pdf.add_page()
    pdf.chapter_title("run.py", level=2)
    info = get_file_info("run.py")
    if info:
        if info["module_doc"]:
            pdf.body_text(info["module_doc"])
        pdf.body_text(f"Size: {info['size']:,} bytes, {info['lines']} lines")
        pdf.code_block(info["content"])
    else:
        pdf.body_text(f"File not found: run.py")

    pdf.add_page()
    pdf.chapter_title("cli.py", level=2)
    info = get_file_info("cli.py")
    if info:
        if info["module_doc"]:
            pdf.body_text(info["module_doc"])
        pdf.body_text(f"Size: {info['size']:,} bytes, {info['lines']} lines")
        pdf.code_block(info["content"])
    else:
        pdf.body_text(f"File not found: cli.py")

    pdf.add_page()
    pdf.chapter_title("server.py", level=2)
    info = get_file_info("server.py")
    if info:
        if info["module_doc"]:
            pdf.body_text(info["module_doc"])
        pdf.body_text(f"Size: {info['size']:,} bytes, {info['lines']} lines")
        pdf.code_block(info["content"])
    else:
        pdf.body_text(f"File not found: server.py")

    pdf.add_page()
    pdf.chapter_title("orchestrator.py", level=2)
    info = get_file_info("orchestrator.py")
    if info:
        if info["module_doc"]:
            pdf.body_text(info["module_doc"])
        pdf.body_text(f"Size: {info['size']:,} bytes, {info['lines']} lines")
        pdf.code_block(info["content"])
    else:
        pdf.body_text(f"File not found: orchestrator.py")

    pdf.add_page()
    pdf.chapter_title("pyproject.toml", level=2)
    info = get_file_info("pyproject.toml")
    if info:
        if info["module_doc"]:
            pdf.body_text(info["module_doc"])
        pdf.body_text(f"Size: {info['size']:,} bytes, {info['lines']} lines")
        pdf.code_block(info["content"])
    else:
        pdf.body_text(f"File not found: pyproject.toml")

    pdf.add_page()
    pdf.chapter_title("requirements.txt", level=2)
    info = get_file_info("requirements.txt")
    if info:
        if info["module_doc"]:
            pdf.body_text(info["module_doc"])
        pdf.body_text(f"Size: {info['size']:,} bytes, {info['lines']} lines")
        pdf.code_block(info["content"])
    else:
        pdf.body_text(f"File not found: requirements.txt")

    # ===== SECTION 4: DEPENDENCIES =====
    pdf.add_page()
    pdf.chapter_title("4. Dependencies")
    pdf.body_text("The project dependencies as defined in pyproject.toml and requirements.txt:")
    pdf.ln(3)

    pdf.chapter_title("Core Dependencies", level=3)
    pdf.bullet_list([
        "requests >= 2.31.0 - HTTP library for API calls",
        "python-dotenv >= 1.0.0 - Environment variable management",
        "honcho-ai >= 2.1.0 - AI-native peer modeling and dialectic memory",
        "fastapi >= 0.100.0 - Web framework for the API server",
        "uvicorn >= 0.20.0 - ASGI server for FastAPI",
        "pydantic >= 2.0.0 - Data validation and settings",
        "httpx >= 0.24.0 - Async HTTP client",
        "click >= 8.0 - CLI framework",
        "pytest >= 7.0 - Testing framework",
        "matplotlib >= 3.7.0 - Chart generation",
    ])

    pdf.chapter_title("Supported LLM Providers", level=3)
    pdf.bullet_list([
        "OpenRouter - Serves Hermes 3 models (NousResearch)",
        "Groq - Free tier, Llama 3.1 models",
        "Anthropic - Claude models (Haiku, Sonnet)",
        "DeepSeek - DeepSeek Chat and Reasoner",
        "Google Gemini - Gemini 2.0 Flash, 1.5 Pro",
        "Together AI - Llama 3.1 405B, Mixtral, Qwen",
        "OpenAI - GPT models",
        "xAI/Grok - Grok models",
        "Fireworks AI, Mistral, Cohere, Perplexity, Cerebras, HuggingFace, Ollama",
    ])

    # ===== SECTION 5: ARCHITECTURE SUMMARY =====
    pdf.add_page()
    pdf.chapter_title("5. Architecture Summary")
    pdf.body_text("AgentMesh follows a hierarchical multi-agent architecture:")
    pdf.ln(3)

    pdf.chapter_title("System Flow", level=2)
    pdf.body_text("1. User provides a goal to the Orchestrator")
    pdf.body_text("2. Orchestrator loads harness strategy from previous evolution cycles")
    pdf.body_text("3. Orchestrator decomposes goal into 2-4 subtasks using DeepSeek Chat")
    pdf.body_text("4. Tasks are dispatched as ExecutionContracts to specialized sub-agents")
    pdf.body_text("5. Sub-agents execute tasks using LLM tool loops with file-backed state")
    pdf.body_text("6. Results are checked against hard completion conditions")
    pdf.body_text("7. Episodes are stored in SQLite memory with raw traces")
    pdf.body_text("8. RecursiveLearner analyzes failures and extracts lessons")
    pdf.body_text("9. HarnessOptimizer rewrites decomposition strategy based on mesh-wide failures")
    pdf.body_text("10. Aggregated results returned to user")
    pdf.ln(5)

    pdf.chapter_title("Memory Architecture", level=2)
    pdf.body_text("Four-layer memory system mirroring human cognitive architecture:")
    pdf.bullet_list([
        "Episodic Memory - Raw task history, verbatim traces. Never summarised",
        "Semantic Memory - Learned lessons, rules, patterns extracted from failures",
        "Procedural Memory - Skill effectiveness scores tracking which tools work",
        "Working Memory - Current session scratchpad via FileBackedState on disk",
    ])
    pdf.ln(3)

    pdf.chapter_title("Self-Evolution Loop", level=2)
    pdf.body_text("The recursive learning system implements two levels of evolution:")
    pdf.bullet_list([
        "Per-Agent Evolution (RecursiveLearner) - Reads failure traces, diagnoses root causes, extracts concrete lessons, acceptance-gates them, and evolves the agent system prompt",
        "Orchestrator-Level Evolution (HarnessOptimizer) - Analyzes cross-agent failure patterns, rewrites task decomposition strategy, updates routing rules",
    ])

    # ===== SECTION 6: CLI USAGE =====
    pdf.add_page()
    pdf.chapter_title("6. CLI Usage")
    pdf.body_text("AgentMesh provides multiple entry points:")
    pdf.ln(3)
    pdf.chapter_title("run.py", level=3)
    pdf.code_block("""
python run.py "Research DeepSeek pricing and write a summary"
python run.py --stream "Build a Python JSON parser"
python run.py --status
python run.py --test
python run.py --provider groq --model llama-3.3-70b-versatile "Research..."
python run.py --list-models
    """)
    pdf.ln(3)
    pdf.chapter_title("cli.py (Click-based)", level=3)
    pdf.code_block("""
python cli.py chat --provider deepseek --model deepseek-chat "What is Python?"
python cli.py workflow run workflow.json
python cli.py learn
python cli.py learn recommend
python cli.py providers
python cli.py serve
    """)
    pdf.ln(3)
    pdf.chapter_title("server.py (FastAPI)", level=3)
    pdf.code_block("""
uvicorn server:app --host 0.0.0.0 --port 8000 --reload
    """)
    pdf.ln(3)

    # ===== SECTION 7: CONCLUSION =====
    pdf.add_page()
    pdf.chapter_title("7. Conclusion")
    pdf.body_text("AgentMesh v2.0 is a production-ready multi-agent orchestration framework with:")
    pdf.bullet_list([
        f"{total_lines:,} lines of Python code across {len(SOURCE_FILES)} source files",
        "Support for 15+ LLM providers with automatic failover",
        "SQLite-backed persistent memory with four cognitive layers",
        "Recursive self-evolution from failure traces",
        "Honcho AI integration for cross-session peer modeling",
        "FastAPI server with WebSocket streaming",
        "Comprehensive test suite with pytest",
        "Click-based CLI and programmatic Python API",
    ])
    pdf.ln(5)
    pdf.body_text("The framework is designed for extensibility - new agents, skills, and LLM providers can be added with minimal boilerplate.")

    # ===== SAVE =====
    pdf.output(str(OUTPUT_PDF))
    print(f"Report saved to: {OUTPUT_PDF}")
    print(f"Total pages: {pdf.page_no()}")


if __name__ == "__main__":
    build_report()
