# Guía de Ejecución Rápida 🚀

Este documento detalla el orden recomendado para revisar y ejecutar los notebooks de la asignatura, asegurando que las dependencias, los modelos de embeddings locales y las bases de datos vectoriales se carguen en la secuencia correcta.

## 📌 Índice y Orden de Ejecución de los Notebooks

Para replicar el flujo completo del aprendizaje y el funcionamiento de los sistemas RAG, ejecuta los notebooks en este orden:

### Bloque 1: Fundamentos de NLP y Frameworks
1. **00_Frameworks_Pytorch_vs_Tensorflow.ipynb**: Comparativa técnica de uso de las dos librerías principales de Deep Learning, funciones de activación y flujos de entrenamiento.
2. **00_Introduccion_NLP_casos_de_uso.ipynb**: Introducción al ecosistema de HuggingFace y exploración de tareas clásicas (Clasificación, NER, Topic Modeling).
3. **01_Introduccion_NLP_Embeddings_Basicos.ipynb**: Evolución de la vectorización de texto desde One-Hot Encoding hasta el entrenamiento de modelos Word2Vec.

### Bloque 2: Transformers y Embeddings Contextuales
4. **02_Embeddings_Transformers.ipynb**: Uso de modelos BERT y Sentence Transformers para generación de embeddings contextuales y visualizaciones semánticas.

### Bloque 3: Ingeniería de Prompts y Chatbots
5. **03_Ingenieria_de_Prompts.ipynb**: Técnicas avanzadas de optimización de instrucciones (Zero-Shot, Few-Shot, Chain of Thought (CoT)).
6. **04_Chatbots_Basicos.ipynb**: Desarrollo de asistentes conversacionales (modelos de reglas vs LLM API) e implementación de memoria conversacional con Streamlit.

### Bloque 4: Arquitectura RAG Avanzada y Optimización
7. **05_Vectorstores_Retrieval.ipynb**: Segmentación de documentos (Text Splitters) e indexación en base de datos vectorial local con FAISS.
8. **06_Introduccion_RAG.ipynb**: Construcción del pipeline básico de Generación Aumentada por Recuperación utilizando LangChain.
9. **07_Reranking_Optimizacion.ipynb**: Optimización del motor de búsqueda mediante la comparación técnica de rankings (Bi-Encoder vs Cross-Encoder vs LLM).

---

## ⚡ Demo Mínima (Ejecución en 1 Celda)

Para comprobar el correcto funcionamiento del sistema completo de recuperación y generación (RAG) optimizado con filtrado por metadatos o reordenación:

1. Abre el notebook 07_Reranking_Optimizacion.ipynb (o en su defecto el 06_Introduccion_RAG.ipynb).
2. Asegúrate de que el archivo requirements.txt esté instalado y añade tu GROQ_API_KEY en la celda de login.
3. Dirígete a la celda final de pruebas y ejecútala para comprobar el sistema en acción.
