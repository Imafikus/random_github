from api import get_repo_contents
import data_extractor

if __name__ == "__main__":
    repos = data_extractor.get_repos_with_supported_languages()
    test = repos[0]
    
    
    files = data_extractor.get_all_files(test)
    language_specific_files = data_extractor.extract_all_language_files(files, test.language)
    for f in language_specific_files:
        print(f.download_url)
        