import os

def generate_folder_structure(dir_path, prefix=''):
    structure = ''
    for entry in sorted(os.listdir(dir_path)):
        full_path = os.path.join(dir_path, entry)
        if os.path.isdir(full_path):
            structure += f'{prefix}- {entry}/\n'
            structure += generate_folder_structure(full_path, prefix + '  ')
        else:
            structure += f'{prefix}- {entry}\n'
    return structure

def update_readme(structure):
    readme_path = 'README.md'
    with open(readme_path, 'r', encoding='utf-8') as f:
        readme_content = f.read()

    new_readme_content = readme_content.split('## 폴더 구조\n\n')[0] + f'## 폴더 구조\n\n{structure}'

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_readme_content)

if __name__ == "__main__":
    folder_structure = generate_folder_structure('.')
    update_readme(folder_structure)
