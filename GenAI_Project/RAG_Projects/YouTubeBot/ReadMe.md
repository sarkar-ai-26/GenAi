### Communicate with this APP to get to know about the youtube video.

- Youtube Video should have captions or Transcript included in it

> Captions -> Document loader -> TextLoaders (RecursiveCharacterTextSplitter)-> Embedding (OllamEmbedding) -> VectorStore -> FAISS -> Retreiver -> Vector Store Retriever -> Prompt+Context (Prompt Template) -> LLM -> Answer