import sys
from pathlib import Path
from typing import Optional

sys.path.append(str(Path(__file__).resolve().parents[1]))

from agno.agent import Agent
from pydantic import BaseModel, Field
from rich.pretty import pprint
from common import make_model


class Event(BaseModel):
    name: str = Field(description="Name of the event")
    venue: str = Field(description="Venue or institution")
    start_date: str
    end_date: str
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    registration_fee_inr: Optional[int] = None


agent = Agent(
    model=make_model(),
    description="Extract event information exactly from the supplied text.",
    output_schema=Event,
)

text = """
AGENT-M, a hands-on AI workshop, will be held at SCT College in
Thiruvananthapuram on October 3 and 4, 2026.
Sessions run from 9:30 AM to 4:30 PM.
Registration is ₹500.
"""

if __name__ == "__main__":
    response = agent.run(f"Extract the event information from this text:\n{text}")

    if isinstance(response.content, Event):
        pprint(response.content.model_dump())
    else:
        print("Structured parsing did not succeed:")
        print(response.content)
