---
date created: 20250316T051551
date modified: 20250519T171017
title: HTML
---

# HTML

HTML(HyperText Markup Language)은 웹페이지를 만들기 위해 사용되는 언어

## HTML의 특징

- **마크업 언어** - 태그를 사용하여 문서의 구조를 정의
- **정적 웹 페이지 작성** - [[CSS]], [[JS]]와 같이 웹 개발에 사용
- **웹 표준** - W3C(World Wide Web Consortium)에서 표준 규격 관리
- **하이퍼텍스트 기능** - 링크를 통해 웹 페이지 간 이동 가능

## HTML 기본 구조

```js
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HTML 문서 예제</title>
</head>
<body>
    <h1>안녕하세요!</h1>
    <p>이것은 HTML 기본 구조입니다.</p>
    <a href="https://example.com">링크</a>
</body>
</html>
```

## HTML 주요 태그

|                        |                             |                                        |
| ---------------------- | --------------------------- | -------------------------------------- |
| 태그                     | 설명                          | 예제                                     |
| `<h1> ~ <h6>`          | 제목(Header)                  | `<h1>제목</h1>`                          |
| `<p>`                  | 문단(Paragraph)               | `<p>문단 내용</p>`                         |
| `<a>`                  | 링크(Anchor)                  | `<a href="https://example.com">이동</a>` |
| `<img>`                | 이미지 삽입                      | `<img src="image.jpg" alt="이미지">`      |
| `<ul>`, `<ol>`, `<li>` | 목록(Unordered, Ordered List) | `<ul><li>항목</li></ul>`                 |
| `<table>`              | 표(Table)                    | `<table><tr><td>셀</td></tr></table>`   |
| `<form>`               | 입력 폼(Form)                  | `<form><input type="text"></form>`     |
| `<div>`                | 블록 요소                       | `<div>내용</div>`                        |
| `<span>`               | 인라인 요소                      | `<span>텍스트</span>`                     |
