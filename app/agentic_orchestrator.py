# agentic_orchestrator.py

from langchain.agents import AgentExecutor, Tool
from langchain.agents.agent_toolkits import create_python_agent
from langchain.agents.format_scratchpad import format_to_openai_functions
from langchain.chat_models import ChatOpenAI
from langchain.tools import tool
import os

# Example Tool 1: Calculator
@tool
def add_numbers(a: int, b: int) -> int:
    """Adds two numbers."""
    return a + b

# Example Tool 2: Dummy Search
@tool
def search_facts(query: str) -> str:
    """Returns a fake search result."""
    return f"Search result for '{query}': LLMs are powerful tools for automation."

# Create tool list
tools = [add_numbers, search_facts]

# LLM setup
llm = ChatOpenAI(model_name="gpt-3.5-turbo-0613", temperature=0)

# Agent Executor setup
agent_executor = AgentExecutor.from_agent_and_tools(
    agent=create_python_agent(llm=llm, tools=tools),
    tools=tools,
    verbose=True
)

def run_agentic_orchestrator(prompt: str):
    print("🔁 Running agentic orchestration...")
    response = agent_executor.run(prompt)
    print("✅ Done! Response:")
    print(response)

if __name__ == "__main__":
    user_prompt = input("🧠 Ask the agent something: ")
    run_agentic_orchestrator(user_prompt)

