import os
import ast
import subprocess
import sys

def extract_imports(file_path):
    with open(file_path, 'r') as file:
        tree = ast.parse(file.read(), filename=file_path)
    imports = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.add(alias.name)
        elif isinstance(node, ast.ImportFrom):
            imports.add(node.module)
    return imports

def detect_and_install_modules(directory):
    modules = set()
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                modules.update(extract_imports(file_path))

    # インポートされたモジュールをインストール
    for module in modules:
        if module:
            subprocess.run([sys.executable, '-m', 'pip', 'install', module])

def generate_requirements_txt():
    subprocess.run([sys.executable, '-m', 'pip', 'freeze', '>', 'requirements.txt'], shell=True)

if __name__ == "__main__":
    repo_path = "/app"  # コンテナ内の作業ディレクトリ
    detect_and_install_modules(repo_path)
    generate_requirements_txt()
    print("requirements.txt has been generated successfully.")