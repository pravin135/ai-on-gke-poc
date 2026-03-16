import requests

def ask_agent(question):

    print("Sending request to Ollama...")

    prompt = f"""
You are a Kubernetes troubleshooting expert.

User problem:
{question}

Explain the root cause and suggest possible fixes.
"""

    response = requests.post(
        "http://ollamma-service:11434/api/generate",
        json={
            "model": "tinyllama",
            "prompt": prompt,
            "stream": False
        },
        timeout=300
    )

    print("Response received from Ollama")

    data = response.json()

    return data["response"]
