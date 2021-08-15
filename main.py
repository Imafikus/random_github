import comment_extractor
from fastapi import FastAPI

app = FastAPI()

@app.get('/comment')
def read_item():
    return {'comment': comment_extractor.get_comment()}

            
        