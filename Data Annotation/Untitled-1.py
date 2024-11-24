from pathlib import Path
file_path = Path('C:/Users/rwilc/OneDrive/Documents/GitHub/GithubTest/Data Annotation/annodata.txt')
print(file_path)

with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()
print(content)
