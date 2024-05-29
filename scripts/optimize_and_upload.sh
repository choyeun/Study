#!/bin/bash

IMGUR_CLIENT_ID=${1}
TEMP_DIR="optimized_images"

# 임시 디렉토리 생성
mkdir -p $TEMP_DIR

# 파일 크기 제한 정의 (바이트 단위)
MAX_IMAGE_SIZE=$((10 * 1024 * 1024))  # 10MB
MAX_GIF_SIZE=$((200 * 1024 * 1024))   # 200MB

upload_to_imgur() {
  local file=$1
  local response=$(curl -s -H "Authorization: Client-ID $IMGUR_CLIENT_ID" -F "image=@$file" https://api.imgur.com/3/image)
  local link=$(echo $response | jq -r '.data.link')
  echo $link
}

optimize_image() {
  local file=$1
  local optimized_file="$TEMP_DIR/$(basename "$file")"
  npx imagemin "$file" > "$optimized_file"
  echo "$optimized_file"
}

find . -type f \( -iname \*.jpg -o -iname \*.png -o -iname \*.jpeg -o -iname \*.gif -o -iname \*.webp \) | while read file; do
  file_size=$(stat -c%s "$file")

  # 파일 크기 확인 및 최적화
  if [[ $file == *.gif ]]; then
    if [ $file_size -gt $MAX_GIF_SIZE ]; then
      echo "Optimizing $file: exceeds maximum GIF size limit of 200MB."
      optimized_file=$(optimize_image "$file")
      file=$optimized_file
    fi
  else
    if [ $file_size -gt $MAX_IMAGE_SIZE ]; then
      echo "Optimizing $file: exceeds maximum image size limit of 10MB."
      optimized_file=$(optimize_image "$file")
      file=$optimized_file
    fi
  fi

  echo "Uploading $file to Imgur..."
  link=$(upload_to_imgur "$file")

  if [ -n "$link" ]; then
    # Markdown 파일 내 링크 대체 (전체 경로 사용)
    find . -type f -name "*.md" -exec sed -i "s|![]($(realpath --relative-to=. "$file"))|![${file##*/}]($link)|g" {} +
    # 원본 파일 삭제
    rm -f "$file"
  else
    echo "Failed to upload $file to Imgur. Exiting."
    exit 1
  fi
done

# 임시 디렉토리 제거
rm -rf $TEMP_DIR
