import aiohttp
import json
from config import OLLAMA_URL

async def generate_insult(prompt: str) -> str:
    system_prompt = "You are an aggressive, insulting productivity coach. Keep it short, mean, and demanding."
    full_prompt = f"{system_prompt}\nUser: {prompt}\nCoach:"
    return await _call_ollama(full_prompt)

async def generate_proactive_insult() -> str:
    prompt = "Give me a random, short, very aggressive insult to get back to work."
    return await generate_insult(prompt)

async def _call_ollama(prompt: str) -> str:
    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(OLLAMA_URL, json=payload) as response:
                if response.status == 200:
                    data = await response.json()
                    return data.get("response", "Get back to work, you lazy bum!")
                return "Ollama error. Stop slacking anyway!"
    except Exception as e:
        return f"Error: {e}. But seriously, work!"
