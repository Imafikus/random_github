from models import SingleGetContentObj
import api 
from typing import List


def get_all_file_urls(data: List[SingleGetContentObj]):
    for item in data:
        if item.type == 'file':
            print(f'File url: {item.download_url}')

if __name__ == "__main__":
    data = api.get_repo_contents('imafikus', 'random_github')
    
    # get_all_file_urls(data)
    
    print(api.get_raw_data('https://raw.githubusercontent.com/Imafikus/random_github/master/.gitignore'))
