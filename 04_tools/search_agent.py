import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from common import make_model

agent = Agent(
    name="Search Agent",
    model=make_model(),
    tools=[DuckDuckGoTools()],
    instructions=[
        "Search the web when the question requires current information.",
        "Mention the source names in the answer.",
        "Keep the answer compact for a live workshop.",
    ],
    markdown=True,
)

if __name__ == "__main__":
    agent.print_response(
        "Find one recent development in AI agents and summarize it in 5 bullets.",
        stream=True,
    )
