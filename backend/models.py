from pydantic import BaseModel
class LinksType(BaseModel):
    self: str 
    git: str 
    html: str
    
class SingleGetContentObj(BaseModel):
    name: str
    path: str
    sha:str 
    size: int
    url: str
    html_url: str
    git_url: str 
    download_url: str = None
    type: str
    _links: LinksType

    
class ChoosenComment(BaseModel):
    content: str
    url: str