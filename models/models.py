from pydantic import BaseModel
from typing import List, Optional
from enum import Enum


class Source(str, Enum):
    email = "email"
    file = "file"
    chat = "chat"


class DocumentMetadata(BaseModel):
    source: Optional[Source] = None
    source_id: Optional[str] = None
    url: Optional[str] = None
    created_at: Optional[str] = None
    author: Optional[str] = None


class DocumentChunkMetadata(DocumentMetadata):
    document_id: Optional[str] = None


class DocumentChunk(BaseModel):
    id: Optional[str] = None
    text: str
    metadata: DocumentChunkMetadata
    embedding: Optional[List[float]] = None


class DocumentChunkWithScore(DocumentChunk):
    score: float


class Document(BaseModel):
    id: Optional[str] = None
    text: str
    metadata: Optional[DocumentMetadata] = None


class DocumentWithChunks(Document):
    chunks: List[DocumentChunk]


class DocumentMetadataFilter(BaseModel):
    document_id: Optional[str] = None
    source: Optional[Source] = None
    source_id: Optional[str] = None
    author: Optional[str] = None
    start_date: Optional[str] = None  # any date string format
    end_date: Optional[str] = None  # any date string format


class Query(BaseModel):
    query: str
    filter: Optional[DocumentMetadataFilter] = None
    top_k: Optional[int] = 3


class QueryWithEmbedding(Query):
    embedding: List[float]


class QueryResult(BaseModel):
    query: str
    results: List[DocumentChunkWithScore]


class WebDocument(BaseModel):
    title: str
    link: str
    snippet: str
    formattedUrl: str
# {
#     "title": "[연합뉴스] 메시 '홍콩 노쇼' 파장 어디까지…中, 아르헨 대표팀 친선 ...",
#     "link": "https://www.fmkorea.com/best/6707198183",
#     "snippet": "2 days ago ... 구토새끼들 존나역하네 ㅋㅋ 똑같은 쓰레기빨면서 우리메시는 신성불가침이고 어떤일이든 다 이유가있는거고 인성도좋은 축구선수고 이런포지션이길 바라나봄 ㅋㅋ.",
#     "formattedUrl": "https://www.fmkorea.com/best/6707198183",
# }

class WebResult(BaseModel):
    query: str
    results: List[WebDocument]

