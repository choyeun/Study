---
aliases:
  - 중간 점검
date created: 토요일, 10월 19일 2024, 8:17:39 오후
date modified: 수요일, 3월 12일 2025, 8:06:28 오전
linter-yaml-title-alias: 중간 점검
title: 중간 점검
---

# 중간 점검

## 메모리는 어떤 단위를 기준으로 주소가 매겨지는가?

4byte

## 포인터도 변수인가?

True

## 변수의 주소를 추출하는데 사용되는 연산자는 무엇인가?

&

## 변수 X 의 주소를 추출하여 변수 P 에 대입하는 문장을 쓰시오

```c
int x;
int *p = &x; 
```

## Int \*p 가 가리키는 위치에 25 를 대입하시오

```c
int a = 0;
int *p;
p = &a;
*p = 25;
```

```C
*(arr + i) == arr[i];
```
