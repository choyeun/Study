---
aliases:
  - Dataviewjs Test
date created: 수요일, 3월 12일 2025, 4:57:07 오후
date modified: 수요일, 3월 12일 2025, 6:06:00 오후
linter-yaml-title-alias: Dataviewjs Test
title: Dataviewjs Test
---

# Dataviewjs Test

## Toc

```dataviewjs
const content = await dv.io.load(dv.current().file.path);
const headings = content.match(/^#+ \S.*$/mg);
if (headings && headings.length > 0) {
    const firstHeadingLevel = headings[0].match(/^(#+)/)[1].length;
    const toc = headings.map(heading => {
        const [_, level, text] = heading.match(/^(#+) (.+)$/);
        const link = dv.current().file.path + '#' + text;
        const indentCount = Math.max(0, level.length - firstHeadingLevel);
        return '\t'.repeat(indentCount) + `1. [[${link}|${text}]]`;
    });
    dv.header(5, '목차');
    dv.paragraph(toc.join('\n'));
}
```

## 단일 태그 노트

```dataview
TABLE WITHOUT ID 
file.link as "노트명"
FROM #태그명
WHERE length(file.tags) = 1
```

## 북마크한 노트

### List

```dataview
LIST 
WHERE file.starred
```

### Table

```dataview
TABLE WITHOUT ID 
file.link AS "문서"
WHERE file.starred
```

## 태그당 노트 수

```dataview
TABLE 
length(rows.file.link) as "Number"
FLATTEN file.tags as tag
GROUP BY tag
```

## 최근 7일동안 편집된 노트

```dataview
TABLE dateformat(file.mtime, "yyyy/MM/dd") AS "Last Modified" 
WHERE date(today) - file.mtime <= dur(7 days) SORT file.mtime DESC
```

## 중복 파일 검사

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

## 미해결 링크 검사

```dataviewjs
const unresolvedLinks = dv.app.metadataCache.unresolvedLinks;
let links = [];

for (let file in unresolvedLinks) {
    for (let link in unresolvedLinks[file]) {
        const fileName = file.split('/').pop().replace('.md', '');
        const fileLink = `[[${file}|${fileName}]]`;
        links.push([fileLink, link, unresolvedLinks[file][link]]);
    }
}

dv.table(["파일", "미해결 링크", "언급 횟수"], links);

```

## 고립된 노트

### 백링크가 없는 노트

```dataview
TABLE WHERE length(file.inlinks) = 0
```

### 링크가 없는 노트

```dataview
TABLE WHERE length(file.outlinks) = 0
```
## wordcloud 
```wordcloud
```
## linkcloud 
```linkcloud
```
## unlinkedcloud
```linkcloud
type: resolved
```

```linkcloud
type: unresolved
```
![](https://i.imgur.com/CKH2sYj.png)
![](https://i.imgur.com/30Cl8nh.png)
