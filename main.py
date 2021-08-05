from models import SingleGetContentObj
import api 
from typing import List


def get_all_raw_file_urls(data: List[SingleGetContentObj]):
    
    raw_urls = []
    
    for item in data:
        if item.type == 'file':
            raw_urls.append(item.download_url)

if __name__ == "__main__":
    data = api.get_repo_contents('imafikus', 'random_github')
    
    raw_urls = get_all_raw_file_urls(data)
    
    print(raw_urls)
