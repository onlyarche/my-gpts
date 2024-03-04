#!/bin/bash



# Embedding model configuration
export OPENAI_API_KEY="your_OpenAI_API_key"

export EMBEDDING_MODEL="text-embedding-3-small" # edit this value based on the model you want to use e.g. text-embedding-3-large, text-embedding-3-small, text-embedding-ada-002
export EMBEDDING_DIMENSION=1536 # replace with your model embedding dims e.g. 1536, 2048


# Datastore configuration
export DATASTORE="pinecone"

# Pinecone configuration
export PINECONE_API_KEY="your_Pinecone_API_key"
export PINECONE_ENVIRONMENT="gcp-starter" # free tier
export PINECONE_INDEX="your_Pinecone_index_name"


# Google custom search
export GOOGLE_CX="your_Google_customsearch_cx"
export GOOGLE_KEY="your_Google_API_key"


# Bearer token for authentication - This is a secret token that you need to authenticate your requests to the API.(https://jwt.io)
export BEARER_TOKEN="your_bearer_token"


export RUN_PORT=8888


# Start the server
poetry run start
