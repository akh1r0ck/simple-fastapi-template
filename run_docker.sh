#!/bin/bash

# Dockerイメージの名前
IMAGE_NAME="generate-requirements"

# Dockerfileの名前
DOCKERFILE_NAME="Dockerfile.PackageSearcher"

# Dockerイメージをビルド
docker build -t $IMAGE_NAME -f $DOCKERFILE_NAME .

# Dockerコンテナを実行してrequirements.txtを生成
docker run --rm -v $(pwd):/app $IMAGE_NAME

# Dockerイメージを削除してクリーンアップ
docker rmi $IMAGE_NAME

echo "requirements.txt has been generated and Docker image has been cleaned up."