from typing import List


import re

def extract_python_comments(file_content) -> List[str]:
    return re.findall(r'#.*', file_content)