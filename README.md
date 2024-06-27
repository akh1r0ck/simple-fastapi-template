# simple-fastapi-template

下記のコマンドを走らせることでローカル環境を汚さずにrequrements.txtを作成する．

```bash
chmod +x run_docker.sh
./run_docker.sh
```

ローカル環境で行うと環境が汚れてしまう＆OS依存があったりするため，Dockerで行う（OSもLinuxに固定される，というラッキーもある）．

- run_docker.sh：Dockerイメージの生成，実行，クリーンアップを行う
- Dockerfile.PackageSearcher：パッケージ検出を実行するための仮想環境
- detect_and_generate_requirements.py：Pythonファイルをスキャンしてモジュールを検出して，最終的にrequirements.txtを作成するプログラム
  - extract_imports：指定されたPythonファイルからインポートされたモジュールを抽出します。
  - detect_and_install_modules：プロジェクトディレクトリ内のすべてのPythonファイルをスキャンし、検出されたモジュールを仮想環境にインストールします。
  - generate_requirements_txt：現在の仮想環境にインストールされているパッケージをrequirements.txtファイルにエクスポートします。
