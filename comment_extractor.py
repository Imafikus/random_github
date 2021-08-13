from typing import List


import re
import data_extractor
import github_api
import os
import random

from dotenv import load_dotenv

load_dotenv()

MAX_COMMENT_NUMBER = int(os.environ['MAX_COMMENT_NUMBER'])


def extract_python_comments(file_content) -> List[str]:
    return re.findall(r'#.*', file_content)
    
def get_comment() -> str:
    chosen_comments = []
    repos = data_extractor.get_repos_with_supported_languages()
    for repo in repos:
        files = data_extractor.get_all_files(repo)
        language_specific_files = data_extractor.extract_all_language_files(files, repo.language)
        for f in language_specific_files:
            file_content = github_api.get_raw_data(f.download_url)
            chosen_comments += extract_python_comments(file_content)
        
        if len(chosen_comments) >= MAX_COMMENT_NUMBER:
            break
    
    return random.choice(chosen_comments)