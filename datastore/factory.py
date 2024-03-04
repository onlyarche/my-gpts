from datastore.datastore import DataStore
import os


async def get_datastore() -> DataStore:
    datastore = os.environ.get("DATASTORE")
    if datastore is not None:
        from datastore.providers.pinecone_datastore import PineconeDataStore
        return PineconeDataStore()

    match datastore:
        case "pinecone":
            from datastore.providers.pinecone_datastore import PineconeDataStore
            return PineconeDataStore()
        case _:
            raise ValueError(
                f"Unsupported vector database: {datastore}. "
                f"Try one of the following: llama, elasticsearch, pinecone, weaviate, milvus, zilliz, redis, azuresearch, or qdrant"
            )
