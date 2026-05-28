# Instrucciones de Ejecución Rápida (Demo Mínima)

## 1. Qué notebook ejecutar primero
Para comenzar con el proyecto y entender el flujo inicial de la asignatura, se debe ejecutar primero el notebook:
`notebook/00_Introducción_a_NLP_con_HuggingFace.ipynb`

## 2. Demo mínima (Ejecución en 1 celda)
Para comprobar que todo el entorno, las librerías y los Transformers funcionan de principio a fin (End-to-End) sin necesidad de configurar APIs externas, abre el notebook `notebook/02_Embeddings_Transformers.ipynb` y ejecuta la celda con el siguiente código de prueba:

```python
from sentence_transformers import SentenceTransformer, util

# 1. Cargar modelo ligero de HuggingFace
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# 2. Definir textos de prueba y una consulta
sentences = ["El análisis de negocio usa IA", "Me gusta el fútbol", "Los LLMs son potentes"]
query_embedding = model.encode("¿Qué tecnologías se usan en analítica?")
embeddings = model.encode(sentences)

# 3. Calcular similitud semántica
cos_scores = util.cos_sim(query_embedding, embeddings)[0]
print(f"Resultado más cercano: {sentences[cos_scores.argmax()]}")