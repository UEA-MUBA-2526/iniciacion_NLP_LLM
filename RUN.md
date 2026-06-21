# Instrucciones de Ejecución Rápida, Calidad y Limitaciones (RUN.md)

## 1. Orden Recomendado de Ejecución
Para entender el flujo completo del proyecto y la evolución de los modelos, se debe seguir estrictamente este orden:
1. `notebook/00_Introducción_a_NLP_con_HuggingFace.ipynb` (Fundamentos y Pipelines básicos)
2. `notebook/02_Embeddings_Transformers.ipynb` (Generación de embeddings y búsqueda semántica)
3. `notebook/07_Reranking_Optimizacion.ipynb` (Optimización de la relevancia con Cross-Encoders)
4. `notebook/08_Introduccion_Agentes.ipynb` (Primeros pasos con lógica agéntica)
5. `notebook/11_RAG_Avanzado_Agentico.ipynb` (Sistema final completo con memoria y herramientas)

---

## 2. Cómo Lanzar la Demo Final (Pasos Concretos)
Para verificar que todo el ecosistema de IA y Agentes funciona de principio a fin, ejecute la demo rápida integrada:

1. Asegúrese de tener el entorno virtual activo y las dependencias instaladas (`pip install -r requirements.txt`).
2. Abra el notebook de la demo final: `notebook/11_RAG_Avanzado_Agentico.ipynb`.
3. Ejecute la celda principal del agente de prueba con el siguiente código básico:
```python
# Demo simplificada End-to-End
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
sentences = ["El análisis de negocio usa IA", "Los LLMs automatizan tareas", "RAG mejora las respuestas"]
query = model.encode("¿Qué ventajas tiene el análisis de negocio moderno?")
embeddings = model.encode(sentences)

cos_scores = util.cos_sim(query, embeddings)[0]
print(f"Resultado de la Demo Semántica: {sentences[cos_scores.argmax()]}")