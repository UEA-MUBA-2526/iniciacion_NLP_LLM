"""Stakeholder demo: lightweight RAG with citations.

Run:
    streamlit run demo_stakeholder_rag.py

The demo works without external model downloads. If GROQ_API_KEY is available,
it uses Groq for generation; otherwise it falls back to an extractive answer.
"""

from __future__ import annotations

import os
from dataclasses import dataclass

import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


@dataclass
class KnowledgeItem:
    source: str
    text: str


KNOWLEDGE_BASE = [
    KnowledgeItem(
        "products",
        "TechCorp ofrece tres productos: AIAssist para asistentes virtuales, "
        "DataVision para analitica de datos y CloudBrain para procesamiento en la nube.",
    ),
    KnowledgeItem(
        "pricing",
        "Los planes de TechCorp son Basico por 99 euros al mes, Profesional por "
        "299 euros al mes y Enterprise con precio personalizado.",
    ),
    KnowledgeItem(
        "support",
        "El soporte atiende de lunes a viernes de 9:00 a 18:00. El email de "
        "soporte es soporte@techcorp.es y el telefono es 900 123 456.",
    ),
    KnowledgeItem(
        "returns",
        "La politica de devoluciones permite cancelar durante los primeros 30 dias "
        "con reembolso completo si el servicio no cumple expectativas.",
    ),
    KnowledgeItem(
        "offices",
        "TechCorp tiene oficinas en Madrid, Barcelona y Valencia. La sede central "
        "esta en Madrid.",
    ),
    KnowledgeItem(
        "security",
        "TechCorp aplica cifrado en transito, controles de acceso por rol y "
        "auditorias trimestrales para clientes Enterprise.",
    ),
]


def retrieve(question: str, top_k: int = 3):
    corpus = [item.text for item in KNOWLEDGE_BASE]
    vectorizer = TfidfVectorizer().fit(corpus + [question])
    doc_vectors = vectorizer.transform(corpus)
    query_vector = vectorizer.transform([question])
    scores = cosine_similarity(query_vector, doc_vectors)[0]
    ranked = scores.argsort()[::-1][:top_k]
    return [(KNOWLEDGE_BASE[i], float(scores[i])) for i in ranked]


def extractive_answer(question: str, retrieved) -> str:
    if not retrieved or retrieved[0][1] < 0.05:
        return "No tengo informacion suficiente en la base de conocimiento para responder con seguridad."

    bullets = []
    for idx, (item, score) in enumerate(retrieved, 1):
        bullets.append(f"- {item.text} [{idx}]")
    return "\n".join(bullets)


def groq_answer(question: str, retrieved) -> str | None:
    if not os.environ.get("GROQ_API_KEY"):
        return None

    try:
        from langchain_groq import ChatGroq
    except Exception:
        return None

    context = "\n".join(
        f"[{idx}] source={item.source}: {item.text}"
        for idx, (item, _) in enumerate(retrieved, 1)
    )
    prompt = f"""Eres un asistente de demostracion RAG para stakeholders.
Responde en espanol usando solo el contexto y cita fuentes con [n].

Contexto:
{context}

Pregunta: {question}

Respuesta:"""

    llm = ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0)
    return llm.invoke(prompt).content


st.set_page_config(page_title="Demo RAG TechCorp", layout="wide")
st.title("Demo RAG TechCorp")
st.caption("Retrieval con citas, fallback local y generacion opcional con Groq.")

with st.sidebar:
    st.header("Configuracion")
    api_key = st.text_input("GROQ_API_KEY opcional", type="password")
    if api_key:
        os.environ["GROQ_API_KEY"] = api_key
    top_k = st.slider("Documentos recuperados", min_value=1, max_value=5, value=3)

question = st.text_input(
    "Pregunta para la demo",
    value="Cuales son los planes y como contacto con soporte?",
)

if st.button("Responder", type="primary"):
    retrieved = retrieve(question, top_k=top_k)
    answer = groq_answer(question, retrieved) or extractive_answer(question, retrieved)

    st.subheader("Respuesta")
    st.write(answer)

    st.subheader("Fuentes recuperadas")
    for idx, (item, score) in enumerate(retrieved, 1):
        st.markdown(f"**[{idx}] {item.source}** - score `{score:.3f}`")
        st.write(item.text)

st.divider()
st.subheader("Casos sugeridos")
st.markdown(
    """
- Cuales son los planes de precios?
- Como contacto con soporte?
- Donde estan las oficinas?
- Que seguridad ofrece TechCorp?
- Cual es la politica de vacaciones? (debe abstenerse)
"""
)
