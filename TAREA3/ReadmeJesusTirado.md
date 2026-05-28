# Curso de LLMs y Aplicaciones de IA

## Descripción

Este readme conotiene una breve descripción de la Tarea 3 de Jesús Tirado García para la asignatura INTELIGENCIA ARTIFICIAL, ENFOQUE PRÁCTICO Y METODOLÓGICO
Se ha "adaptado" el readme.md a la contruccion real de mi entorno en MAC. 

## Estructura del Curso

| Notebook | Tema | 
|----------|------|
| 00 | Introducción a NLP con HuggingFace 
| 00 | PyTorch vs Tensorflow 
| 01 | Introducción a NLP y Embeddings Básicos 
| 02 | Embeddings con Transformers 
| 03 | Ingeniería de Prompts 
| 04 | Chatbots Básicos 
| 05 | Vector Stores y Retrieval 
| 06 | Introducción a RAG 
| 07 | Reranking y Optimización 


## Progresión recomendada

```
Introducción (00)
       ↓
Fundamentos (01-04)
       ↓
Retrieval (05-07)
       
```

## Requisitos

### APIs (Gratuitas)
- **Groq API** (gratis): https://console.groq.com/keys
  - Tier gratuito generoso para modelos Llama 3.3
- **HuggingFace** (gratis): Modelos de embeddings open source

### Configuración del Entorno 

Cabe mencionar que dada las caracterisitcas de mi equipo MAC ventura, se trabajo especialmente para configurar un entorno que permitiera correr todas las 
librerias en python 3.12.9

 Puedes gestionar las dependencias usando **pip** (con `requirements.txt`)



## Opción 1: Instalación con pip (tradicional)

### 1. Crear el entorno virtual

```
# Linux/Mac
python3.12.9 -m venv .venv
```

### 2. Activar el entorno 


**Linux/Mac:**
```bash
source conda activate IA_MUBA
```

### 3. Instalar dependencias

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Desactivar el entorno

Cuando termines de trabajar:

```bash
deactivate
```

### Librerías principales

Las dependencias están definidas en `requirements.txt` (para pip) 

- **PyTorch** - Framework de deep learning
- **Transformers** - Modelos de Hugging Face
- **Sentence-Transformers** - Embeddings de oraciones
- **LangChain** - Framework para aplicaciones LLM
- **LangGraph** - Flujos de trabajo con grafos
- **FAISS** - Búsqueda de vectores similares
- **Gensim** - Word2Vec, GloVe
- **spaCy** - Procesamiento de lenguaje natural
- **Jupyter** - Notebooks interactivos


## Características

- **Sin costos de API**: Usa Groq (gratis) y modelos HuggingFace
- **Standalone**: Cada notebook es independiente
- **Práctico**: Código ejecutable con ejemplos reales
- **Progresivo**: De conceptos básicos a sistemas avanzados
- **Bilingüe**: Explicaciones en español, código en inglés

## Contenido por notebook (existe un ejercicio asociado a cada módulo que se entrega resuelto.)

### 00 - Introducción a NLP con HuggingFace
- Ecosistema HuggingFace
- Casos de uso de NLP
- Clasificación de texto y análisis de sentimiento
- Named Entity Recognition (NER)
- Topic Modeling
- Componentes de pipelines de NLP
- Ejemplos prácticos con corpus real

### 00 - PyTorch vs Tensorflow
- Comparativa de frameworks de Deep Learning
- Funciones de activación
- Construcción de modelos
- Entrenamiento y explotación
- Diferencias y similitudes

### 01 - Introducción a NLP y Embeddings Básicos
- One-Hot Encoding (Scikit-Learn, Keras)
- Word2Vec (modelo propio y pre-entrenados)
- GloVe
- Visualización con PCA

### 02 - Embeddings con Transformers
- BERT y BETO (español)
- Sentence Transformers
- Búsqueda semántica
- Visualización 3D con UMAP

### 03 - Ingeniería de Prompts
- Zero-shot y Few-shot
- Prompts con rol
- Chain of Thought
- Formato de salida
- Temperatura y diversidad

### 04 - Chatbots Básicos
- Chatbot basado en reglas
- Chatbot con LLM
- Memoria conversacional
- Interfaces con Streamlit

### 05 - Vector Stores y Retrieval
- FAISS
- Document Loaders
- Text Splitters
- Similarity Search
- Persistencia

### 06 - Introducción a RAG
- Arquitectura RAG
- Implementación paso a paso
- RAG con LangChain
- Memoria conversacional

### 07 - Reranking y Optimización
- Cross-Encoder
- Bi-Encoder
- LLM como Reranker
- Estrategias combinadas