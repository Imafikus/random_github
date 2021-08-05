from pydantic import BaseModel


{
    "name": ".gitignore",
    "path": ".gitignore",
    "sha": "b6e47617de110dea7ca47e087ff1347cc2646eda",
    "size": 1799,
    "url": "https: //api.github.com/repos/Imafikus/random_github/contents/.gitignore?ref=master",
    "html_url": "https://github.com/Imafikus/random_github/blob/master/.gitignore",
    "git_url": "https://api.github.com/repos/Imafikus/random_github/git/blobs/b6e47617de110dea7ca47e087ff1347cc2646eda",
    "download_url": "https://raw.githubusercontent.com/Imafikus/random_github/master/.gitignore",
    "type": "file",
    "_links": {
        "self": "https://api.github.com/repos/Imafikus/random_github/contents/.gitignore?ref=master",
        "git": "https://api.github.com/repos/Imafikus/random_github/git/blobs/b6e47617de110dea7ca47e087ff1347cc2646eda",
        "html": "https://github.com/Imafikus/random_github/blob/master/.gitignore"
    }
}

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
    download_url: str 
    type: str
    _links: LinksType

    