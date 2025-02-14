import chromadb
from llama_index.core import SimpleDirectoryReader
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import VectorStoreIndex
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext
from llama_index.llms.ollama import Ollama

#Load documents
documents = SimpleDirectoryReader(input_files= ["Essay.txt"]).load_data()
#Load embedding model
embed_model = HuggingFaceEmbedding()
# create client
db = chromadb.PersistentClient(path="./chroma_db")
chroma_collection = db.get_or_create_collection("paul_collection")
# save embedding to disk
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
# create index
index = VectorStoreIndex.from_documents(
    documents, storage_context=storage_context, embed_model=embed_model
)
# load from disk
db2 = chromadb.PersistentClient(path="./chroma_db")
chroma_collection = db2.get_or_create_collection("paul_collection")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
index = VectorStoreIndex.from_vector_store(
    vector_store,
    embed_model=embed_model,
)
#Initialize Ollama and create LLM with Llama3.2
llm = Ollama(model="llama3.2", request_timeout=420.0)
# Query Data from the persisted index
query_engine = index.as_query_engine(llm=llm)
response = query_engine.query("to whom author is said Thanks")
print(response)