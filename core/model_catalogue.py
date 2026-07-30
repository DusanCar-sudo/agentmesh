"""
AgentMesh · core/model_catalogue.py
Single source of truth for all providers and their models.

Import this everywhere instead of hardcoding model lists.

Usage:
    from core.model_catalogue import CATALOGUE, get_models_for_provider, get_providers_with_keys
"""

from __future__ import annotations
from typing import Optional

# ── Master catalogue ──────────────────────────────────────────────────────────
# Structure: provider_key -> { display_name, endpoint, env_key, models, no_key? }

CATALOGUE = {
    "openai": {
        "name": "OpenAI",
        "endpoint": "https://api.openai.com/v1/chat/completions",
        "env_key": "OPENAI_API_KEY",
        "models": {
            "gpt-4o":              "GPT-4o",
            "gpt-4o-mini":         "GPT-4o Mini",
            "gpt-4-turbo":         "GPT-4 Turbo",
            "gpt-3.5-turbo":       "GPT-3.5 Turbo",
            "o1":                  "o1",
            "o3-mini":             "o3-mini",
        },
        "default_model": "gpt-4o-mini",
    },
    "anthropic": {
        "name": "Anthropic",
        "endpoint": "https://api.anthropic.com/v1/messages",
        "env_key": "ANTHROPIC_API_KEY",
        "native": True,
        "models": {
            "claude-sonnet-4-6":         "Claude Sonnet 4",
            "claude-haiku-4-5-20251001": "Claude Haiku 4.5",
            "claude-3-5-sonnet-20241022":"Claude 3.5 Sonnet",
            "claude-3-haiku-20240307":   "Claude 3 Haiku",
        },
        "default_model": "claude-haiku-4-5-20251001",
    },
    "gemini": {
        "name": "Google Gemini",
        "endpoint": "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions",
        "env_key": "GEMINI_API_KEY",
        "models": {
            "gemini-2.0-flash":       "Gemini 2.0 Flash",
            "gemini-2.5-pro-exp":     "Gemini 2.5 Pro (exp)",
            "gemini-1.5-pro-latest":  "Gemini 1.5 Pro",
            "gemini-1.5-flash":       "Gemini 1.5 Flash",
        },
        "default_model": "gemini-2.0-flash",
    },
    "deepseek": {
        "name": "DeepSeek",
        "endpoint": "https://api.deepseek.com/v1/chat/completions",
        "env_key": "DEEPSEEK_API_KEY",
        "models": {
            "deepseek-chat":    "DeepSeek V3 (Chat)",
            "deepseek-reasoner":"DeepSeek R1 (Reasoner)",
        },
        "default_model": "deepseek-chat",
    },
    "groq": {
        "name": "Groq",
        "endpoint": "https://api.groq.com/openai/v1/chat/completions",
        "env_key": "GROQ_API_KEY",
        "models": {
            "llama-3.3-70b-versatile":   "Llama 3.3 70B",
            "llama-3.1-8b-instant":      "Llama 3.1 8B (Instant)",
            "mixtral-8x7b-32768":        "Mixtral 8x7B",
            "gemma2-9b-it":              "Gemma 2 9B",
            "deepseek-r1-distill-llama-70b": "DeepSeek R1 Distill 70B",
        },
        "default_model": "llama-3.3-70b-versatile",
    },
    "together": {
        "name": "Together AI",
        "endpoint": "https://api.together.xyz/v1/chat/completions",
        "env_key": "TOGETHER_API_KEY",
        "models": {
            "meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo":  "Llama 3.1 405B",
            "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo":   "Llama 3.1 70B",
            "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo":    "Llama 3.1 8B",
            "mistralai/Mixtral-8x7B-Instruct-v0.1":           "Mixtral 8x7B",
            "Qwen/Qwen2.5-72B-Instruct-Turbo":                "Qwen 2.5 72B",
        },
        "default_model": "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
    },
    "openrouter": {
        "name": "OpenRouter",
        "endpoint": "https://openrouter.ai/api/v1/chat/completions",
        "env_key": "OPENROUTER_API_KEY",
        "models": {
            "deepseek/deepseek-chat":        "DeepSeek V3",
            "deepseek/deepseek-r1":          "DeepSeek R1",
            "anthropic/claude-sonnet-4-6":   "Claude Sonnet 4",
            "openai/gpt-4o":                 "GPT-4o",
            "google/gemini-2.0-flash-001":   "Gemini 2.0 Flash",
            "meta-llama/llama-3.3-70b-instruct": "Llama 3.3 70B",
            "nousresearch/hermes-3-llama-3.1-70b": "Hermes 3 70B",
            "nousresearch/hermes-3-llama-3.1-8b":  "Hermes 3 8B",
            "mistralai/mistral-large":       "Mistral Large",
            "qwen/qwen-2.5-72b-instruct":    "Qwen 2.5 72B",
        },
        "default_model": "deepseek/deepseek-chat",
    },
    "xai": {
        "name": "xAI / Grok",
        "endpoint": "https://api.x.ai/v1/chat/completions",
        "env_key": "XAI_API_KEY",
        "models": {
            "grok-2":       "Grok 2",
            "grok-2-mini":  "Grok 2 Mini",
        },
        "default_model": "grok-2",
    },
    "fireworks": {
        "name": "Fireworks AI",
        "endpoint": "https://api.fireworks.ai/inference/v1/chat/completions",
        "env_key": "FIREWORKS_API_KEY",
        "models": {
            "accounts/fireworks/models/llama-v3p3-70b-instruct":   "Llama 3.3 70B",
            "accounts/fireworks/models/llama-v3p2-3b-instruct":    "Llama 3.2 3B",
            "accounts/fireworks/models/deepseek-v3":                "DeepSeek V3",
            "accounts/fireworks/models/mixtral-8x7b-instruct":     "Mixtral 8x7B",
        },
        "default_model": "accounts/fireworks/models/llama-v3p3-70b-instruct",
    },
    "mistral": {
        "name": "Mistral AI",
        "endpoint": "https://api.mistral.ai/v1/chat/completions",
        "env_key": "MISTRAL_API_KEY",
        "models": {
            "mistral-large-latest":   "Mistral Large",
            "mistral-small-latest":   "Mistral Small",
            "open-mistral-nemo":      "Mistral Nemo",
        },
        "default_model": "mistral-small-latest",
    },
    "cohere": {
        "name": "Cohere",
        "endpoint": "https://api.cohere.com/compatibility/v1/chat/completions",
        "env_key": "COHERE_API_KEY",
        "models": {
            "command-r-plus": "Command R+",
            "command-r":      "Command R",
        },
        "default_model": "command-r-plus",
    },
    "perplexity": {
        "name": "Perplexity",
        "endpoint": "https://api.perplexity.ai/chat/completions",
        "env_key": "PERPLEXITY_API_KEY",
        "models": {
            "sonar-pro":         "Sonar Pro",
            "sonar":             "Sonar",
            "llama-3.1-sonar-huge-128k": "Sonar Huge",
        },
        "default_model": "sonar-pro",
    },
    "cerebras": {
        "name": "Cerebras",
        "endpoint": "https://api.cerebras.ai/v1/chat/completions",
        "env_key": "CEREBRAS_API_KEY",
        "models": {
            "llama3.1-8b":    "Llama 3.1 8B",
            "llama3.1-70b":   "Llama 3.1 70B",
        },
        "default_model": "llama3.1-8b",
    },
    "huggingface": {
        "name": "HuggingFace",
        "endpoint": "https://api-inference.huggingface.co/v1/chat/completions",
        "env_key": "HUGGINGFACE_API_KEY",
        "models": {
            "meta-llama/Llama-3.3-70B-Instruct":       "Llama 3.3 70B",
            "meta-llama/Llama-3.1-8B-Instruct":        "Llama 3.1 8B",
            "mistralai/Mistral-7B-Instruct-v0.3":       "Mistral 7B",
            "Qwen/Qwen2.5-72B-Instruct":               "Qwen 2.5 72B",
        },
        "default_model": "meta-llama/Llama-3.3-70B-Instruct",
    },
    "ollama": {
        "name": "Ollama (Local)",
        "endpoint": "http://localhost:11434/v1/chat/completions",
        "env_key": "",
        "no_key": True,
        "models": {
            "llama3.2":     "Llama 3.2",
            "llama3.1":     "Llama 3.1",
            "mistral":      "Mistral",
            "gemma2":       "Gemma 2",
            "deepseek-r1":  "DeepSeek R1",
            "phi4":         "Phi 4",
        },
        "default_model": "llama3.2",
    },
    "mimo": {
        "name": "Xiaomi MiMo",
        "endpoint": "https://api.xiaomimimo.com/v1/chat/completions",
        "env_key": "MIMO_API_KEY",
        "models": {
            "MiMo": "MiMo",
        },
        "default_model": "MiMo",
    },
}


# ── Helpers ───────────────────────────────────────────────────────────────────

def get_providers() -> list[str]:
    """Return all provider keys."""
    return list(CATALOGUE.keys())


def get_provider_info(provider: str) -> Optional[dict]:
    """Get info dict for a provider, or None."""
    return CATALOGUE.get(provider)


def get_models_for_provider(provider: str) -> dict[str, str]:
    """Get {model_id: display_name} for a provider."""
    info = CATALOGUE.get(provider)
    return dict(info["models"]) if info else {}


def get_default_model(provider: str) -> Optional[str]:
    """Get the default model ID for a provider."""
    info = CATALOGUE.get(provider)
    return info["default_model"] if info else None


def get_display_name(provider: str, model_id: str) -> str:
    """Get human-friendly display name for a model."""
    info = CATALOGUE.get(provider)
    if info:
        return info["models"].get(model_id, model_id)
    return model_id


def get_endpoint(provider: str) -> Optional[str]:
    """Get API endpoint for a provider."""
    info = CATALOGUE.get(provider)
    return info["endpoint"] if info else None


def get_env_key(provider: str) -> str:
    """Get the env var name for a provider's API key."""
    info = CATALOGUE.get(provider)
    return info["env_key"] if info else f"{provider.upper()}_API_KEY"


def is_native_anthropic(provider: str) -> bool:
    """Whether the provider uses Anthropic-native API format."""
    info = CATALOGUE.get(provider)
    return bool(info and info.get("native"))


def needs_api_key(provider: str) -> bool:
    """Whether this provider needs an API key (vs local like Ollama)."""
    info = CATALOGUE.get(provider)
    return not (info and info.get("no_key"))


def get_providers_with_keys(env_vars: Optional[dict] = None) -> list[dict]:
    """
    Return all providers with their models, filtering by available keys.

    Returns list of:
        { "key": "deepseek", "name": "DeepSeek", "models": [...],
          "default_model": "deepseek-chat", "has_key": True/False }
    """
    if env_vars is None:
        import os as _os
        env_vars = _os.environ

    result = []
    for pkey, info in CATALOGUE.items():
        no_key = info.get("no_key", False)
        if no_key:
            has_key = True
        else:
            env_key = info["env_key"]
            has_key = bool(env_vars.get(env_key))

        models_list = [
            {"id": mid, "name": mname}
            for mid, mname in info["models"].items()
        ]

        result.append({
            "key": pkey,
            "name": info["name"],
            "models": models_list,
            "default_model": info["default_model"],
            "has_key": has_key,
            "no_key": no_key,
        })

    # Sort: providers with keys first
    result.sort(key=lambda x: (0 if x["has_key"] else 1, x["name"]))
    return result


def resolve_model(provider: str, model: Optional[str] = None) -> str:
    """Return the resolved model ID, falling back to the provider default."""
    if model:
        return model
    default = get_default_model(provider)
    return default or "default"
