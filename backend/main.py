import comment_extractor
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import datastore_db as db

origins = [
    "http://localhost:3000",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/comment')
def get_comment():
    comment = comment_extractor.get_comment()
    return {
        'content': comment.content,
        'url': comment.url
    }

@app.get('/all_comments')
def get_comment():
    all_comments = comment_extractor.get_all_choosen_comments()
    return {
        'all_comments': all_comments,
    }
            
if __name__ == '__main__':
    db.insert_entity('whatever')