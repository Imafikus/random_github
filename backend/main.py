from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import datastore_db as db
import random

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
    all_comments = db.get_choosen_comments()
    comment = random.choice(all_comments)
    return {
        'content': comment.content,
        'url': comment.url
    }

@app.get('/all_comments')
def get_comment():
    all_comments = db.get_choosen_comments()
    return {
        'all_comments': all_comments,
    }
            
if __name__ == '__main__':
    print(db.get_choosen_comments())
