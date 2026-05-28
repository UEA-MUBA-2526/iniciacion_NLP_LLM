Proyecto de Aprendizaje: Prompts, Chatbots y RAG (Entrega Paula Domínguez)
Este repositorio contiene las soluciones completas a los bloques prácticos desarrollados hasta la fecha en la asignatura, abarcando desde los fundamentos de NLP hasta arquitecturas avanzadas de recuperación y optimización de búsqueda (RAG).

Requisitos e Instalación
Para replicar este entorno de desarrollo localmente, activa tu entorno virtual e instala las dependencias añadidas ejecutando:

pip install -r requirements.txt

Estructura de la Entrega (Bloques Completados)
El contenido desarrollado incluye 9 notebooks organizados de la siguiente manera:

Bloque 1: Fundamentos de NLP y Frameworks
00_Frameworks_Pytorch_vs_Tensorflow.ipynb: Comparativa técnica de uso, funciones de activación y flujos de trabajo en deep learning.

00_Introduccion_NLP_casos_de_uso.ipynb: Exploración del ecosistema de HuggingFace y tareas clásicas (Análisis de sentimiento, NER, Topic Modeling).

01_Introduccion_NLP_Embeddings_Basicos.ipynb: Vectorización clásica, uso de Word2Vec (propio y pre-entrenados) y GloVe.

Bloque 2: Transformers y Embeddings Contextuales
02_Embeddings_Transformers.ipynb: Modelos BERT/BETO y Sentence Transformers para búsqueda semántica con visualización 3D en UMAP.

Bloque 3: Ingeniería de Prompts y Chatbots
03_Ingenieria_de_Prompts.ipynb: Técnicas avanzadas de diseño de instrucciones (Zero-Shot, Few-Shot, Chain of Thought (CoT)).

04_Chatbots_Basicos.ipynb: Creación de asistentes conversacionales con LLM, gestión de memoria e interfaces en Streamlit.

Bloque 4: Arquitectura RAG Avanzada y Optimización
05_Vectorstores_Retrieval.ipynb: Document Loaders, Text Splitters y persistencia en base de datos vectorial local con FAISS.

06_Introduccion_RAG.ipynb: Construcción del pipeline completo de Generación Aumentada por Recuperación usando LangChain.

07_Reranking_Optimizacion.ipynb: Estrategias de optimización de recuperación comparando técnicas de ranking (Bi-Encoder vs Cross-Encoder vs LLM).

Guía de Ejecución Rápida
Para conocer el orden técnico recomendado para lanzar los cuadernos y ejecutar una de las demostraciones en una sola celda, consulta nuestro documento de instrucciones:

Ver instrucciones detalladas en RUN.md