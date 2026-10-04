import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from agno.agent import Agent
from common import make_model

agent = Agent(model=make_model(), markdown=True)

weak_prompt = "Tell me about solar energy."

better_prompt = """
ROLE:
You are an energy consultant and engineering educator.

TASK:
Explain solar energy.

AUDIENCE:
First-year engineering students in India.

COVER:
- photovoltaic principle
- inverter
- battery
- advantages
- limitations

CONSTRAINTS:
- fewer than 250 words
- simple language
- avoid unnecessary jargon

OUTPUT:
Finish with 3 questions that test understanding.
"""

if __name__ == "__main__":
    print("\n========== WEAK PROMPT ==========\n")
    agent.print_response(weak_prompt)

    input("\nPress Enter for the improved prompt...\n")

    print("\n========== BETTER PROMPT ==========\n")
    agent.print_response(better_prompt)
