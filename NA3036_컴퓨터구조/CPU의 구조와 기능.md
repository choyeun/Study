---
aliases:
  - CPU 의 구조와 기능
date created: 목요일, 3월 13일 2025, 2:05:52 오후
date modified: 목요일, 3월 13일 2025, 2:29:27 오후
linter-yaml-title-alias: CPU 의 구조와 기능
title: CPU 의 구조와 기능
강의 n주차: 2
과목:
  - "[[컴퓨터 구조]]"
시간: 2025-03-13T14:00:00
---

# CPU 의 구조와 기능
**[[CPU]]의 기능**
- 명령어 인출(Instruction Fetch)
  기억장치로부터 명령어를 읽어온다
- 명령어 해독(Instruction Decode)
  수행해야 할 동작을 결정하기 위하여 명령어를 해독한다
-> 위 2 기능은 모든 명령어들에 대하여 공통적으로 수행
- 데이터 인출(Data Fetch)
  명령어 실행을 위하여 데이터가 필요한 경우에는 기억장치 혹은 I/O 장치로부터 그 데이터를 읽어온다
- 데이터 처리(Data Process)
  데이터에 대한 산술적 혹은 논리적 연산을 수행
- 데이터 저장(Data Store)
  수행한 결과를 저장 
-> 명령어에 따라 필요한 경우에만 수행

## [[CPU]]의 기본 구조 
- 산술논리연산장치(Arithmetic and Logical Unit: [[ALU]])
- 레지스터 세트(Register Set)
- 제어 유니트(Control Unit)
![[../attachments/Pasted image 20250313142132.png]]
