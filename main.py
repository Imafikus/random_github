import data_extractor
import comment_extractor
import github_api
import os
from dotenv import load_dotenv
import random

load_dotenv()

MAX_COMMENT_NUMBER = int(os.environ['MAX_COMMENT_NUMBER'])

if __name__ == "__main__":
    chosen_comments = []
    repos = data_extractor.get_repos_with_supported_languages()
    for repo in repos:
        files = data_extractor.get_all_files(repo)
        language_specific_files = data_extractor.extract_all_language_files(files, repo.language)
        for f in language_specific_files:
            file_content = github_api.get_raw_data(f.download_url)
            chosen_comments += comment_extractor.extract_python_comments(file_content)
        
        if len(chosen_comments) >= MAX_COMMENT_NUMBER:
            break
    
    print('chosen_comment: ', random.choice(chosen_comments))
            
        