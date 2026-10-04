import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

import streamlit as st
from agno.agent import Agent
from agno.knowledge.embedder.fastembed import FastEmbedEmbedder
from agno.knowledge.knowledge import Knowledge
from agno.vectordb.chroma import ChromaDb
from common import EMBEDDING_MODEL, make_model

FAQ_PATH = ROOT / "05_rag" / "data" / "college_faq.md"

st.set_page_config(page_title="Campus AI Buddy", page_icon="🤖")
st.title("🤖 Campus AI Buddy")
st.caption("AGENT-M final demo: Python + Agno + RAG + Streamlit")


@st.cache_resource
def build_agent():
    knowledge = Knowledge(
        vector_db=ChromaDb(
            collection="agent_m_streamlit",
            path=str(ROOT / "tmp" / "streamlit_chroma"),
            persistent_client=True,
            embedder=FastEmbedEmbedder(id=EMBEDDING_MODEL),
        )
    )
    knowledge.insert(path=str(FAQ_PATH), skip_if_exists=True)

    return Agent(
        model=make_model(),
        knowledge=knowledge,
        search_knowledge=True,
        instructions=[
            "You are Campus AI Buddy.",
            "Answer workshop-specific questions using the knowledge base.",
            "For general questions, be concise.",
            "Never fabricate college or workshop facts.",
        ],
        markdown=True,
    )


agent = build_agent()

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

question = st.chat_input("Ask Campus AI Buddy...")

if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            result = agent.run(question)
            answer = str(result.content)
            st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})
