---
date created: 월요일, 6월 17일 2024, 3:55:59 오전
date modified: 목요일, 3월 13일 2025, 12:57:12 오전
title: Switch 문에서 주의할 점
과목:
  - "[[프로그래밍 입문]]"
---

# Switch 문에서 주의할 점

```c
switch(number)
{
    case x:    // 변수는 사용할 수 없다.
        printf("x와 일치합니다. ");
        break;

    case (x+2):    // 변수가 들어간 수식은 사용할 수 없다.
        printf("수식과 일치합니다. ");
        break;

    case 0.001:    // 실수는 사용할 수 없다.
        printf("실수");
        break;

    case “001”:    // 문자열은 사용할 수 없다.
        printf("문자열");
        break;
}

```
