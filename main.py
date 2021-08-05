from api import get_repo_contents
import data_extractor

if __name__ == "__main__":
    repos = data_extractor.get_repos_with_supported_languages()
    test = repos[0]
    
    for f in data_extractor.extract_all_language_files(test):
        print(f)