import os
import webbrowser
from dotenv import load_dotenv
from langchain.agents import create_agent

with open("system_prompt.md", "r", encoding="utf-8") as file:
    SYSTEM_PROMPT = file.read()

def init_agent():
    print("log: Initialize Agent...")
    agent = create_agent(
    model="google_genai:gemini-flash-lite-latest",
    tools=[],
    system_prompt=SYSTEM_PROMPT)

    print("log: Agent initialization done.")
    return agent

def get_response_from_agent(prompt: str) -> str:
    agent = init_agent()

    response = agent.invoke({"messages": [prompt]})
    clean_response = response["messages"][-1].text

    return clean_response


def main():
    while True:
        with open("system_prompt.md", "r", encoding="utf-8") as file:
            SYSTEM_PROMPT = file.read()
        try:
            init_agent()
            prompt = input("What Deutsch Word you want to look up? \nEnter 'exit' to end the chat.")
            if prompt == "exit": break
            response = get_response_from_agent(prompt)
        except EOFError:
            break
        print(response)


if __name__ == "__main__":
    main()