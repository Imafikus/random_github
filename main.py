import requests
from models import SingleGetContentObj
from pydantic import parse_obj_as
from typing import List

BASE_URL = 'https://api.github.com'


if __name__ == "__main__":
    data = requests.get(f'https://api.github.com/repos/imafikus/random_github/contents/')    
    
    res = parse_obj_as(List[SingleGetContentObj], data.json())
    
    print(res)
