import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from common import make_model

db = SqliteDb(db_file=str(ROOT / "tmp" / "memory_demo.db"))

agent = Agent(
    model=make_model(),
    db=db,
    learning=True,
    instructions="Be concise and remember useful facts the user explicitly tells you.",
    markdown=True,
)

USER_ID = "student-001"

if __name__ == "__main__":
    print("\nSESSION 1")
    agent.print_response(
        "My name is Maya. I am an electronics student and I enjoy Python.",
        user_id=USER_ID,
        session_id="session-1",
    )

    print("\nSESSION 2")
    agent.print_response(
        "What do you remember about me?",
        user_id=USER_ID,
        session_id="session-2",
    )

    print("\nRun this file again to demonstrate persistence.")
