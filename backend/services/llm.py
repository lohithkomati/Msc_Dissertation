"""
services/llm.py

Groq LLM Service
----------------

This file replaces the previous Ollama implementation.

Every part of the project imports only

    llm_complete(...)

Therefore the rest of the application never needs to know
which LLM provider is being used.
"""

from __future__ import annotations

import asyncio
import logging
from typing import List
from typing import Dict

from groq import AsyncGroq
from django.conf import settings

logger = logging.getLogger(__name__)


# ---------------------------------------------------------
# Create Groq Client
# ---------------------------------------------------------

client = AsyncGroq(
    api_key=settings.GROQ_API_KEY
)


# ---------------------------------------------------------
# Default Parameters
# ---------------------------------------------------------

DEFAULT_MODEL = settings.GROQ_MODEL

DEFAULT_TEMPERATURE = 0.35

DEFAULT_MAX_TOKENS = 300

DEFAULT_TOP_P = 0.9


# ---------------------------------------------------------
# Internal Builder
# ---------------------------------------------------------

def build_messages(
    system_prompt: str,
    messages: List[Dict]
) -> List[Dict]:

    chat = []

    if system_prompt:

        chat.append(
            {
                "role": "system",
                "content": system_prompt,
            }
        )

    for m in messages:

        role = m.get("role", "user")

        content = m.get("content", "")

        chat.append(
            {
                "role": role,
                "content": content,
            }
        )

    return chat


# ---------------------------------------------------------
# Completion
# ---------------------------------------------------------

async def llm_complete(
    messages: List[Dict],
    system_prompt: str,
    temperature: float = DEFAULT_TEMPERATURE,
    max_tokens: int = DEFAULT_MAX_TOKENS,
    top_p: float = DEFAULT_TOP_P,
) -> str:

    chat = build_messages(
        system_prompt,
        messages,
    )

    try:

        response = await client.chat.completions.create(

            model=DEFAULT_MODEL,

            messages=chat,

            temperature=temperature,

            max_tokens=max_tokens,

            top_p=top_p,

            stream=False,

        )

        text = response.choices[0].message.content

        if text is None:

            return ""

        return text.strip()

    except Exception as exc:

        logger.exception(exc)

        return (
            "I'm sorry, I couldn't generate a response "
            "at the moment."
        )


# ---------------------------------------------------------
# Streaming
# ---------------------------------------------------------

async def llm_stream(
    messages: List[Dict],
    system_prompt: str,
    temperature: float = DEFAULT_TEMPERATURE,
):

    chat = build_messages(
        system_prompt,
        messages,
    )

    stream = await client.chat.completions.create(

        model=DEFAULT_MODEL,

        messages=chat,

        temperature=temperature,

        stream=True,

    )

    async for chunk in stream:

        if not chunk.choices:

            continue

        delta = chunk.choices[0].delta.content

        if delta:

            yield delta


# ---------------------------------------------------------
# JSON Helper
# ---------------------------------------------------------

async def llm_json(
    messages: List[Dict],
    system_prompt: str,
    temperature: float = 0.1,
    max_tokens: int = 800,
):

    response = await llm_complete(

        messages=messages,

        system_prompt=system_prompt,

        temperature=temperature,

        max_tokens=max_tokens,

    )

    return response


# ---------------------------------------------------------
# Embedding Placeholder
# ---------------------------------------------------------

async def embedding(text: str):

    """
    Reserved for future RAG.

    If later you move to OpenAI embeddings
    or Voyage AI embeddings,
    only this function changes.
    """

    return text


# ---------------------------------------------------------
# Health Check
# ---------------------------------------------------------

async def ping():

    try:

        result = await llm_complete(

            messages=[
                {
                    "role": "user",
                    "content": "Reply with OK"
                }
            ],

            system_prompt="You are a test assistant.",

            max_tokens=5,

        )

        return result

    except Exception:

        return "FAILED"


# ---------------------------------------------------------
# Benchmark
# ---------------------------------------------------------

async def benchmark():

    import time

    start = time.perf_counter()

    await ping()

    end = time.perf_counter()

    return round(end - start, 2)


# ---------------------------------------------------------
# Standalone Test
# ---------------------------------------------------------

if __name__ == "__main__":

    async def test():

        answer = await llm_complete(

            messages=[
                {
                    "role": "user",
                    "content": "Introduce yourself."
                }
            ],

            system_prompt="You are a friendly assistant.",

        )

        print(answer)

    asyncio.run(test())