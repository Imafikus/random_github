import comment_extractor
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
def read_item():
    return {'comment': comment_extractor.get_comment()}

            
if __name__ == '__main__':
    print('random comment: ', comment_extractor.get_comment())