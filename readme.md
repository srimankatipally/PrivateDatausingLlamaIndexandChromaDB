# ChromaDB and LlamaIndex Integration

**Authors:** Sriman Katipally, Chandish Somu

This project demonstrates how to integrate ChromaDB with LlamaIndex for Private document embedding and querying. The setup uses HuggingFace for embedding and Ollama as the LLM with Llama 3.2.

## Installation
Ensure you have the required dependencies installed:
```bash
pip install llama-index chromadb ollama transformers
```

Additionally, install LLM Llama 3.2 using Ollama and ensure the model endpoints are running at:
```
http://localhost:11434/
```

## Usage
1. **Load Documents**
   - The script loads documents from `Essay.txt`.
2. **Initialize ChromaDB**
   - A persistent ChromaDB collection is created to store embeddings.
3. **Embed Documents & Store in ChromaDB**
   - The documents are embedded using HuggingFaceEmbedding and stored in ChromaDB.
4. **Query the Persisted Index**
   - The script allows querying using Llama 3.2 via Ollama.

## Running the Script
Execute the script:
```bash
python script.py
```

## Expected Output
The response will extract and return relevant information based on the query from the stored document embeddings.

## Notes
- Ensure `Essay.txt` exists in the script directory.
- Modify the query in the script to extract different insights from the document.
