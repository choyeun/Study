import os

EXCLUDE_DIRS = {".git", ".github"}
EXCLUDE_FILES = {".gitignore", "generate_folder_structure.py"}


def generate_folder_structure(dir_path, prefix=""):
    structure = ""
    for entry in sorted(os.listdir(dir_path)):
        full_path = os.path.join(dir_path, entry)
        relative_path = os.path.relpath(full_path, start=".")
        url_path = relative_path.replace(os.path.sep, "%20")
        if os.path.isdir(full_path) and entry not in EXCLUDE_DIRS:
            structure += f"{prefix}- [{entry}]({url_path})/\n"
            structure += generate_folder_structure(full_path, prefix + "  ")
        elif os.path.isfile(full_path) and entry not in EXCLUDE_FILES:
            structure += f"{prefix}- [{entry}]({url_path})\n"
    return structure


def update_readme(structure):
    readme_path = "README.md"
    with open(readme_path, "r", encoding="utf-8") as f:
        readme_content = f.read()

    if "## 폴더 구조" in readme_content:
        new_readme_content = (
            readme_content.split("## 폴더 구조\n\n")[0] + f"## 폴더 구조\n\n{structure}"
        )
        if "##" in new_readme_content.split("## 폴더 구조\n\n")[1]:
            new_readme_content += (
                "\n" + new_readme_content.split("## 폴더 구조\n\n")[1].split("\n", 1)[1]
            )
    else:
        new_readme_content = readme_content + f"\n## 폴더 구조\n\n{structure}"

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_readme_content)


if __name__ == "__main__":
    folder_structure = generate_folder_structure(".")
    update_readme(folder_structure)
