#!/usr/bin/env python3
"""
AgentMesh · run.py
Entry point.

Usage:
    python run.py "Research DeepSeek pricing and write a summary"
    python run.py --stream "Build a Python JSON parser"   # stream responses
    python run.py --status        # show memory stats
    python run.py --test          # run smoke tests
"""

import sys, os, argparse, json
from core.model_catalogue import CATALOGUE, get_providers, get_models_for_provider, get_default_model, get_providers_with_keys, resolve_model

from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


def cmd_run(goal: str, workspace: str, stream: bool = False,
                 provider_str: str = None, model_str: str = None):
    from orchestrator import Orchestrator
    from core.hermes_client import Provider

    provider_str = provider_str or os.environ.get("AGENTMESH_PROVIDER", "deepseek").lower()
    provider_map = {
        "deepseek":   Provider.DEEPSEEK,
        "groq":       Provider.GROQ,
        "openrouter": Provider.OPENROUTER,
        "anthropic":  Provider.ANTHROPIC,
        "gemini":     Provider.GEMINI,
        "together":   Provider.TOGETHER,
    }
    if provider_str not in provider_map:
        print(f"Unknown provider: {provider_str}")
        print(f"Available: {', '.join(provider_map.keys())}")
        return
    provider = provider_map[provider_str]

    orch = Orchestrator(provider=provider, workspace=workspace, stream=stream,
                        agent_model=model_str)
    result = orch.run(goal)

    print("\n── Final Output ─────────────────────────────────────")
    print(json.dumps({k: v for k, v in result.items() if k != "outputs"}, indent=2))
    print(f"\nFull output: {result.get('output_file')}")


def cmd_status(workspace: str):
    from core.memory import AgentMemory
    from core.honcho_bridge import get_honcho_bridge

    mem = AgentMemory(f"{workspace}/memory.db")
    stats = mem.stats()
    print("\n── AgentMesh Status ─────────────────────────────────")
    print(f"  Episodes:       {stats['total_episodes']} (success rate: {stats['success_rate']:.0%})")
    print(f"  Lessons:        {stats['total_lessons']}")
    print(f"  Tracked skills: {stats['tracked_skills']}")

    skill_stats = mem.get_skill_stats()
    if skill_stats:
        print("\n  Skill effectiveness:")
        for s in skill_stats[:8]:
            bar = "█" * int(s.success_rate * 10) + "░" * (10 - int(s.success_rate * 10))
            print(f"    {s.skill_name:<18} {bar} {s.success_rate:.0%} ({s.total_calls} calls)")

    honcho = get_honcho_bridge()
    print(f"\n  Honcho: {'connected' if honcho.is_available() else 'not configured (set HONCHO_API_KEY)'}")


def cmd_test():
    print("Running AgentMesh smoke tests...\n")
    import subprocess, sys
    for test in ("test_step1.py", "test_step2_memory.py", "test_step2_honcho.py"):
        subprocess.run([sys.executable, test], check=False)


def list_models():
    """Print available providers and models."""
    providers = get_providers_with_keys()
    print("\n--- Available Providers & Models ---")
    for p in providers:
        if not p["has_key"]:
            continue
        print(f"\n  {p['name']} [{p['key']}]  <- default: {p['default_model']}")
        for m in p["models"]:
            tag = " <- default" if m["id"] == p["default_model"] else ""
            print(f"    * {m['name']:<35} {m['id']}{tag}")
    print()


def main():
    parser = argparse.ArgumentParser(description="AgentMesh — Multi-Agent Harness")
    parser.add_argument("goal", nargs="?", help="Goal for the agent mesh to accomplish")
    parser.add_argument("--workspace", default="workspace", help="Workspace directory")
    parser.add_argument("--status", action="store_true", help="Show memory + skill stats")
    parser.add_argument("--test", action="store_true", help="Run smoke tests")
    parser.add_argument("--stream", action="store_true", help="Stream agent responses in real-time")
    parser.add_argument("--provider", "-p", default=None, help="Provider (deepseek, groq, openrouter, etc.)")
    parser.add_argument("--model", "-m", default=None, help="Model ID (see --list-models)")
    parser.add_argument("--list-models", action="store_true", help="List available providers and models")
    args = parser.parse_args()

    if args.test:
        cmd_test()
    elif args.status:
        cmd_status(args.workspace)
    elif args.list_models:
        list_models()
    elif args.goal:
        cmd_run(args.goal, args.workspace, stream=args.stream,
                provider_str=args.provider, model_str=args.model)
    else:
        parser.print_help()
        print("\nExamples:")
        print('  python run.py "Research LLM memory systems and write a summary"')
        print('  python run.py --provider groq --model llama-3.3-70b-versatile "Research..."')
        print('  python run.py --list-models')
        print('  python run.py --status')


if __name__ == "__main__":
    main()
