---
date created: 20250530T234121
date modified: 20250530T234405
---
# SATA 규격 조사 보고서

## 개요

Serial ATA(SATA)는 컴퓨터 버스 인터페이스로서 호스트 버스 어댑터와 하드 디스크 드라이브(HDD), 광학 드라이브(ODD), 솔리드 스테이트 드라이브(SSD) 등의 대용량 저장 장치를 연결하는 표준 규격이다. SATA는 기존의 Parallel ATA(PATA) 표준을 대체하여 PC 저장 장치의 사실상 표준이 되었다.

## SATA 규격의 역사

### 초기 개발 및 표준화

SATA 규격은 2000년 2월 APT Technologies, Dell, Intel, Maxtor, Seagate의 공동 노력으로 최초 발표되었다. 이후 Serial ATA International Organization(SATA-IO)이 2004년 9월에 설립되어 SATA 규격의 소유권을 관리하고 개방형 산업 표준으로 유지하고 있다.

### 주요 버전별 발전사

#### SATA 1.0 (2003년)

- 전송 속도: 1.5 Gbit/s (150 MB/s)
- 8b/10b 인코딩 사용으로 실제 데이터 전송률은 120 MB/s

#### SATA 2.0 (2004년 4월)

- 전송 속도: 3.0 Gbit/s (300 MB/s)
- 실제 데이터 전송률: 240 MB/s
- Native Command Queuing(NCQ) 도입
- SATA 1.5 Gbit/s와 하위 호환성 유지

#### SATA 3.0 (2009년 5월)

- 전송 속도: 6.0 Gbit/s (600 MB/s)
- 실제 데이터 전송률: 480 MB/s (8b/10b 인코딩 고려)
- SATA 2.0 대비 2배 성능 향상
- SAS 6 Gbit/s와의 지속적인 호환성
- Isochronous NCQ 스트리밍 명령
- 향상된 전력 관리 기능
- 1.8인치 저장 장치용 소형 LIF 커넥터
- 슬림라인 SATA 커넥터용 7mm 광학 드라이브 프로파일

## 최신 SATA 규격 동향

### SATA 3.1 (2011년 7월)

- mSATA 표준 도입: 모바일 컴퓨팅 장치용 SSD를 위한 PCI Express Mini Card 형태의 커넥터
- Zero-power 광학 디스크 드라이브: 유휴 상태에서 전력을 소비하지 않는 SATA 광학 드라이브
- 1미터까지의 거리 지원 지속

### SATA 3.2 (2013년 8월)

- **SATA Express 규격**: SATA와 PCI Express 버스를 결합한 인터페이스
    - PCI Express 사용으로 1969 MB/s의 이론적 처리량 달성
- **M.2 표준**: SATA Express 인터페이스의 소형 폼 팩터 구현
- **microSSD**: 소형화된 임베디드 SATA 저장 장치용 BGA 전기 인터페이스
- **USM Slim**: Universal Storage Module 두께를 14.5mm에서 9mm로 감소
- **DevSleep**: InstantGo 등 저전력 모드에서 향상된 전력 관리

### SATA 3.3 (2016년 2월)

- **Shingled Magnetic Recording(SMR) 지원**: 하드 디스크 드라이브 용량을 25% 이상 증가
- **Zoned ATA Command Set(ZAC)** 선택적 기능
- **Power Disable 기능**: SATA 드라이브의 원격 전력 순환 가능
- **Rebuild Assist 기능**: 데이터 센터 유지보수 지원을 위한 재구축 프로세스 가속화
- **Transmitter Emphasis 규격**: 전기적으로 까다로운 환경에서 호스트와 장치 간 상호 운용성 및 신뢰성 향상

### SATA 3.4 (2018년 6월)

SATA 3.4 규격은 장치 상태 모니터링 및 하우스키핑 작업 실행에 중점을 두면서도 전체 성능에 미치는 영향을 최소화하는 것을 목표로 개발되었다.

주요 기능:

- **Durable/Ordered Write Notification**: 선택된 중요 캐시 데이터를 미디어에 기록하여 정상 작업에 미치는 영향을 최소화
- **Device Temperature Monitoring**: SFF-8609 표준을 활용한 OOB(Out-of-Band) 통신으로 정상 작업을 방해하지 않고 SATA 장치 온도 및 기타 조건의 능동적 모니터링
- **Device Sleep Signal Timing**: 제조업체 구현 간 호환성 향상을 위한 추가 정의

### SATA 3.5 (2020년 7월) - 최신 규격

SATA 3.5 규격은 성능 향상과 다른 산업 I/O 표준과의 통합 증진에 중점을 두고 개발되었다.

**주요 새 기능:**

1. **Device Transmit Emphasis for Gen 3 PHY**
    
    - SATA를 다른 I/O 측정 솔루션의 특성과 정렬
    - SATA-IO 회원들의 테스트 및 통합 지원
2. **Defined Ordered NCQ Commands**
    
    - 호스트가 대기열 명령 간의 처리 관계를 지정할 수 있게 함
    - 큐에서 명령이 처리되는 순서 설정
3. **Command Duration Limit Features**
    
    - 호스트가 서비스 품질 카테고리를 정의하여 지연 시간 감소
    - 명령 속성에 대한 더 세밀한 제어 제공
    - Open Compute Project(OCP)에서 설정한 "Fast Fail" 요구사항과 정렬
    - INCITS T13 기술 위원회 표준에 명시된 요구사항 준수
4. **기타 개선사항**
    
    - 최신 T13 표준 업데이트 통합
    - 이전 SATA 3.4 규격의 다양한 수정 및 명확화

## SATA의 기술적 특징

### 핫 플러그 지원

SATA 규격은 핫 플러그 기능을 의무적으로 요구한다. 이는 전원이 켜진 상태에서 장치를 백플레인 커넥터에 삽입하거나 제거할 수 있음을 의미한다. 삽입 후 장치는 초기화되어 정상적으로 작동한다.

### 호환성

- **하위 호환성**: 모든 SATA 버전은 이전 버전과 하위 호환성을 유지
- **SAS 호환성**: SATA 장치는 SAS 도메인에 직접 연결 가능
- **운영체제 지원**: 최신 Windows, macOS, Linux, FreeBSD, Solaris 등에서 AHCI 지원

### 전력 관리

SATA 3.0부터 향상된 전력 관리 기능이 도입되어 모바일 및 항상 켜져 있는 장치의 전력 효율성이 크게 개선되었다.

## 현재 시장 동향

### SATA vs NVMe

현재 스토리지 시장에서는 NVMe(Non-Volatile Memory Express) 인터페이스가 고성능 SSD의 주류로 자리잡고 있다. 그러나 SATA는 여전히 다음과 같은 영역에서 중요한 역할을 하고 있다:

- 대용량 기계식 하드 드라이브
- 비용 효율적인 SSD 솔루션
- 엔터프라이즈 및 클라우드 환경
- 레거시 시스템 지원

### 시장 전망

2023년 SATA 커넥터 시장 규모는 1,065억 달러로 평가되었으며, 2032년까지 2,100억 달러에 달할 것으로 예상되어 연평균 성장률(CAGR) 7.0%를 기록할 전망이다.

## SATA-IO 조직

Serial ATA International Organization(SATA-IO)은 2004년 9월에 설립된 국제 기구로, SATA 규격을 개방형 산업 표준으로 소유하고 관리한다. 조직의 주요 역할은:

- SATA 규격의 품질, 무결성, 보급 유지
- 산업 발전에 따른 규격 정의 및 구현
- 기술 홍보 및 마케팅
- 향후 인터페이스 기능 및 규격 개발

## 결론

SATA 규격은 2000년 최초 발표 이후 25년간 지속적으로 발전해왔다. 최신 SATA 3.5 규격은 성능 향상과 다른 I/O 표준과의 통합성을 개선하여 여전히 관련성을 유지하고 있다. NVMe와 같은 새로운 인터페이스의 등장에도 불구하고, SATA는 특정 용도와 시장에서 여전히 중요한 역할을 담당하고 있으며, 앞으로도 스토리지 생태계의 핵심 구성 요소로 남을 것으로 예상된다.

---

## 참고 문헌

1. Serial ATA International Organization (SATA-IO). (2020). "SATA-IO Increases Interoperability Features with Revision 3.5 Specification." _Business Wire_.  https://www.businesswire.com/news/home/20200715005295/en/
    
2. SATA-IO. (2024). "Home | SATA-IO." Official Website.  https://sata-io.org/
    
3. Wikipedia Contributors. (2025). "SATA." _Wikipedia_.  https://en.wikipedia.org/wiki/SATA
    
4. SATA-IO. (2020). "SATA-IO Increases Interoperability Features with Revision 3.5 Specification." _TechPowerUp_.  https://www.techpowerup.com/269946/sata-io-increases-interoperability-features-with-revision-3-5-specification
    
5. Bit-tech.net. (2018). "SATA-IO announces SATA 3.4 release."  https://bit-tech.net/news/tech/storage/sata-io-announces-sata-34-release/1/
    
6. SATA-IO. (2016). "SATA-IO Expands Supported Features in Revision 3.3 Specification." _Business Wire_.  https://www.businesswire.com/news/home/20160216005077/en/
    
7. Market Research Forecast. (2025). "SATA Connector Market 2025-2033 Trends: Unveiling Growth Opportunities and Competitor Dynamics."  https://www.marketresearchforecast.com/reports/sata-connector-market-5378
    
8. Wikipedia (2024). "SATA Express."   https://en.wikipedia.org/wiki/SATA_Express
    
9. SATA-IO. (2024). "Specification Errata, Technical Proposals, and Design Guidelines."  https://sata-io.org/developers/errata-design-guidelines
    