import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from agno.agent import Agent
from common import make_model

agent = Agent(
    model=make_model(),
    instructions="Answer clearly and briefly for an engineering student.",
    markdown=True,
)

if __name__ == "__main__":
    agent.print_response(
        "Explain quantum computing to a 10-year-old in 5 sentences.",
        stream=True,
    )
