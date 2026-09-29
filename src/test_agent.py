from dotenv import load_dotenv
from langchain.agents import create_agent
from pathlib import Path


def init_agent():
    global system_prompt
    global agent

    print("log: Initialize Agent...")
    load_dotenv()

    print("log: Loading system prompt...")

    with open(f"{Path.cwd()}\system_prompt.md", "r", encoding="utf-8") as file:
        system_prompt = file.read()
        print("log: System prompt loaded successfully")

    agent = create_agent(
    model="google_genai:gemini-flash-lite-latest",
    tools=[check_stock],
    system_prompt=system_prompt)

    print("log: Agent initialization done.")
    return agent

def get_response_from_agent(prompt: str) -> str:
    response = agent.invoke({"messages": [prompt]})
    clean_response = response["messages"][-1].text

    return clean_response

def check_stock(item: str, color: str) -> str:
    """
    Check stock availability and return details
    """
    fake_stock = {
        ("hoodie", "blue"): 4,
        ("hoodie", "black"): 12,
        ("t-shirt", "blue"): 30,
    }

    if (item.lower(), color.lower()) in fake_stock:
        return f"We have {color} {item} in stock! Do you want to order one today?"
    else:
        return f"{color} {item} is currently out of stock... Check other items!"


def main():
    init_agent()
    while True:
        try:
            prompt = input()
            if prompt == "exit": break
            response = get_response_from_agent(prompt)
        except EOFError:
            break
        print(response)


if __name__ == "__main__":
    main()