import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from agno.agent import Agent
from agno.knowledge.embedder.fastembed import FastEmbedEmbedder
from agno.knowledge.knowledge import Knowledge
from agno.vectordb.chroma import ChromaDb
from common import EMBEDDING_MODEL, make_model

DB_PATH = ROOT / "tmp" / "chromadb"
FAQ_PATH = Path(__file__).parent / "data" / "college_faq.md"

knowledge = Knowledge(
    vector_db=ChromaDb(
        collection="agent_m_college_faq",
        path=str(DB_PATH),
        persistent_client=True,
        embedder=FastEmbedEmbedder(id=EMBEDDING_MODEL),
    )
)

# Safe to run repeatedly.
knowledge.insert(path=str(FAQ_PATH), skip_if_exists=True)

agent = Agent(
    model=make_model(),
    knowledge=knowledge,
    search_knowledge=True,
    instructions=[
        "Answer workshop questions from the supplied knowledge base.",
        "If the answer is not in the knowledge base, say you do not know.",
    ],
    markdown=True,
)

if __name__ == "__main__":
    print("Try: What should I bring to the workshop?")
    while True:
        question = input("\nYou: ").strip()
        if question.lower() in {"quit", "exit"}:
            break
        agent.print_response(question, stream=True)
