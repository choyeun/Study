---
date created: 목요일, 3월 27일 2025, 10:15:04 오후
date modified: 목요일, 3월 27일 2025, 10:51:29 오후
title: Data Hazard
과목:
  - "[[컴퓨터 구조]]"
---

# Data Hazard

파이프라인 컴퓨터에서 [[Data Hazard]]는 명령어 간의 데이터 의존성으로 인해 발생하는 문제로, 파이프라인의 효율성을 저하시키고 잘못된 결과를 초래할 수 있다

## 발생 사례

[[RAW]] 의존성이 가장 일반적인 사례
이전 명령어의 결과를 이후 명령어가 읽어야 할 때 발생

### 예시

```assembly
ADD R1, R2, R3  # R1에 R2+R3 결과 저장
SUB R4, R1, R5  # ADD의 R1 결과를 사용
```

ADD 명령어가 R1에 값을 쓰기 전에 SUB 명령어가 R1을 읽으려고 하면, 잘못된 값이 사용된다

## 해결 방안

### 데이터 포워딩(Data Forwarding)

**원리**: 이전 명령어의 결과를 파이프라인 중간단계에서 직접 전달
**구현**:
	- 중간단계(EX) 결과를 [[ALU]] 입력으로 직접 연결
	- 중간단계(MEM) 결과 활용
**효과**: 80% 이상의 [[RAW]] Hazard 제거 가능

### 파이프라인 스톨(Pipeline Stall)

**적용 시기**: 로드 명령어 직후 데이터 사용시(Load-Use Hazard)

```assembly
LW R1, 0(R2)  # 메모리에서 R1 로드
ADD R3, R1, R4  # LW 결과 필요
```

**메커니즘**
	- PC 및 IF/ID 레지스터 갱신 중지
	- 제어 신호를 NOP로 변경

# 참고 문헌

<https://en.wikipedia.org/wiki/Hazard_(computer_architecture)>
