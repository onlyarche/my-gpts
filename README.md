# my-gpts

openai에서 제공하는 예제(plugin template)를 기반으로 작성된 예제입니다.

```
https://github.com/openai/chatgpt-retrieval-plugin.git
```

2024 Langcon에서 공유된 내용의 git입니다. 본인의 서비스를 만들기 위해 chatgpt-plugin 기반으로 웹검색 API를 추가한 코드입니다.

gpts등록을 진행할 경우 Openai Plus 결제를 해야합니다.(gpts create & use를 위해서 필요합니다.)

## 환경설정
1. git clone this.
   ```
    pip3 install poetry
    ```

2. install environment using poetry.
    Install poetry:

    ```
    pip install poetry
    ```
    
    Create a new virtual environment that uses Python 3.10:
    
    ```
    poetry env use python3.10
    poetry shell
    ```
    
    Install app dependencies using poetry:
    
    ```
    poetry install
    ```

3. edit run script file(run_server.sh).
    ```
    # Embedding model configuration
    export OPENAI_API_KEY="your_OpenAI_API_key"
    export EMBEDDING_MODEL="text-embedding-3-small" # select the model you want to use e.g. text-embedding-3-large, text-embedding-ada-002
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
    
    # web server port setting 
    export RUN_PORT=8888
    
    poetry run start
    
    ```

4. ngrok을 이용한 포워딩
    ```
    ngrok http http://localhost:8888
    ```
    다음 주소에 접속하여 현재 포워딩한 포트에 대한 in/out 정보를 확인할 수 있습니다.
    http://127.0.0.1:4040

5. 설정파일들 수정
    1. .well-known/ai-plugin.json
    ```
    "api": {
        "type": "openapi",
        "url": "https://"ngrok실행을_통해_포워딩된_주소"/.well-known/openapi.yaml",
        "has_user_authentication": false
     },
    "logo_url": "https://"ngrok실행을_통해_포워딩된_주소"/.well-known/logo.png",
    ```
    2. .well-known/openapi.yaml
    ```
    servers:
      - url: https://"ngrok실행을_통해_포워딩된_주소"
    ```

6. 서버 실행
    ```
    bash run_server.sh
    ```

7. 파일 업로드는 fastapi를 이용해 진행합니다.(https://"ngrok실행을_통해_포워딩된_주소"/docs)
    1. https://"ngrok실행을_통해_포워딩된_주소"/docs 접속합니다.
    2. Authorize 버튼을 눌러 본인의 Bearer 토큰을 설정합니다.
    3. Upsert-file의 API 기능 테스트를 통해 파일을 업로드할 수 있습니다.
    4. 그 외에 만든 API들의 동작을 확인할 수 있으며, gpts에서 해당 동작을 확인할 수 있습니다.
