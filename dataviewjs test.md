---
aliases:
  - Dataviewjs Test
date created: 수요일, 3월 12일 2025, 4:57:07 오후
date modified: 수요일, 3월 12일 2025, 4:58:28 오후
linter-yaml-title-alias: Dataviewjs Test
title: Dataviewjs Test
---

# Dataviewjs Test

```dataviewjs
const data = dv.pages();

let countMap = {}; 

data.forEach((page) => {
  if (page.file && page.file.name && page.file.path) {
    const fileName = page.file.name;
    const filePath = page.file.path;

    if (!countMap.hasOwnProperty(fileName)) {
      countMap[fileName] = { count: 1, paths: [filePath] };
    } else {
      countMap[fileName].count += 1;
      countMap[fileName].paths.push(filePath);
    }
  }
});

let duplicateFound = false;
let duplicateCount = 0; 
Object.keys(countMap).forEach(key => {
  const element = countMap[key];
  if (element.count > 1) {
    duplicateCount += element.count - 1; 
    if (!duplicateFound) {
      dv.paragraph("==중복 파일이 있습니다==");
      duplicateFound = true;
    }
    dv.span(`《${key}》 파일이 ${element.count}개 발견되었습니다.`);
    const pathsToLink = element.paths.map(path => `[[${path}]]`);
    dv.list(pathsToLink);
  }
});

if (duplicateFound) {
  dv.paragraph(`총 ${duplicateCount}개의 중복 파일이 있습니다.`);
} else {
  dv.span("중복 파일이 없습니다.");
}
```
