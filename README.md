# eduChatBot

교육용 AI 챗봇 - Anthropic Claude API와 Google Sheets를 활용한 대화형 학습 도구

## 📝 개요

eduChatBot은 교육 환경에서 학생들이 AI와 대화하며 학습할 수 있도록 설계된 Streamlit 기반 웹 애플리케이션입니다. 모든 대화 내용은 Google Sheets에 자동으로 기록되어 교사가 학생들의 학습 과정을 모니터링하고 평가할 수 있습니다.

## ✨ 주요 기능

- **AI 대화**: Anthropic Claude API를 활용한 실시간 AI 대화
- **대화 기록**: Google Sheets에 자동으로 대화 내용 저장
- **학생별 워크시트**: 각 학생(대화명)별로 개별 워크시트 생성
- **평가 시스템**: 대화 종료 시 AI 기반 종합 평가 및 평어 생성
- **서비스 제어**: 관리자가 서비스 on/off 제어 가능
- **스트리밍 응답**: 실시간 스트리밍으로 AI 응답 표시
- **비용 절감**: Prompt Caching을 활용하여 토큰 비용 최대 90% 절감

## 🚀 시작하기

### 필수 요구사항

- Python 3.8 이상
- Anthropic API 키
- Google Cloud 프로젝트 및 서비스 계정
- Google Sheets API 활성화

### 설치

1. 저장소 클론
```bash
git clone <repository-url>
cd debate
```

2. 필요한 패키지 설치
```bash
pip install -r requirements.txt
```

### 설정

#### 1. Google Cloud 설정

1. [Google Cloud Console](https://console.cloud.google.com/)에서 프로젝트 생성
2. Google Sheets API 활성화
3. 서비스 계정 생성 및 JSON 키 다운로드
4. 서비스 계정에 Google Sheets 편집 권한 부여

#### 2. Google Sheets 준비

관리 시트(설정 정보가 들어가는 시트)를 만들고 "정보" 워크시트에 다음 정보 입력:

| 항목 | 설명 | 예시 |
|------|------|------|
| 수업할 시트 URL | 학생 대화 기록이 저장될 시트 URL | https://docs.google.com/spreadsheets/d/... |
| 서비스 여부 | on/off | on |
| 생성형 AI | 사용할 AI | anthropic |
| API KEY | Anthropic API 키 | sk-ant-... |
| model | 모델명 | claude-3-5-sonnet-20241022 |
| max_tokens | 최대 토큰 수 | 4096 |
| temperature | 온도 설정 | 0.7 |
| select | 선택 옵션 | (옵션) |
| system | 시스템 프롬프트 | 당신은 교육용 AI입니다... |
| a_p | 종합 평가 프롬프트 | 학생의 대화 내용을 바탕으로... |
| e_p | 평어 프롬프트 | 간단한 평어를 작성해주세요... |
| stream | 스트리밍 사용 여부 | true |

수업 시트에는 다음 워크시트 필요:
- **템플릿**: 새 학생 워크시트 생성 시 복사할 템플릿
- **수업요약**: 모든 학생 워크시트 링크 및 평가가 저장되는 곳

#### 3. Streamlit Secrets 설정

`.streamlit/secrets.toml` 파일 생성:

```toml
# Google Service Account 정보
type = "service_account"
project_id = "your-project-id"
private_key_id = "your-private-key-id"
private_key = "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n"
client_email = "your-service-account@your-project.iam.gserviceaccount.com"
client_id = "123456789"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "https://www.googleapis.com/robot/v1/metadata/x509/..."
universe_domain = "googleapis.com"

# 관리 시트 URL (설정 정보가 있는 시트)
sheet_url = "https://docs.google.com/spreadsheets/d/YOUR_MANAGEMENT_SHEET_ID/edit"
```

## 💻 실행

```bash
streamlit run app.py
```

브라우저에서 자동으로 열리지 않으면 `http://localhost:8501` 접속

## 📖 사용 방법

1. **대화명 입력**: 사이드바에서 대화명(닉네임) 입력
2. **대화 시작**: 채팅 입력창에 메시지 입력
3. **대화 진행**: AI와 자유롭게 대화
4. **대화 종료**: "대화 종료" 버튼 클릭 시 자동으로 평가 생성

## 📁 프로젝트 구조

```
debate/
├── app.py              # 메인 애플리케이션
├── config.py           # 설정 파일 (현재 미사용)
├── requirements.txt    # 패키지 의존성
├── utils/
│   └── gs.py          # Google Sheets 유틸리티
└── README.md          # 이 문서
```

## 🔧 주요 함수

### app.py
- `main()`: 메인 애플리케이션 로직
- `initialize()`: API 및 Google Sheets 초기화
- `execute_prompt()`: AI 프롬프트 실행
- `message_processing()`: 스트리밍 응답 처리
- `end_conversation()`: 대화 종료 및 평가 생성

### utils/gs.py
- `get_authorize()`: Google Sheets 인증
- `get_setup_info()`: 설정 정보 가져오기
- `get_worksheet()`: 학생별 워크시트 가져오기/생성
- `add_content()`: 대화 내용 Google Sheets에 추가

## ⚠️ 주의사항

1. **API 키 보안**: `.streamlit/secrets.toml` 파일은 절대 git에 커밋하지 마세요
2. **서비스 계정 권한**: Google Sheets에 서비스 계정 이메일을 편집자로 추가해야 합니다
3. **비용**: Anthropic API 사용에 따른 비용이 발생할 수 있습니다

## 💰 비용 절감: Prompt Caching

이 프로젝트는 **Anthropic의 Prompt Caching** 기능을 활용하여 토큰 비용을 대폭 절감합니다.

### 작동 원리
- **시스템 프롬프트 캐싱**: 매 요청마다 반복되는 시스템 프롬프트를 캐싱
- **대화 히스토리 캐싱**: 오래된 대화 내용을 캐싱 (최근 2개 메시지 제외)
- **캐싱된 토큰**: 90% 할인된 가격으로 사용
- **캐시 유지 시간**: 5분

### 비용 절감 효과
- **짧은 대화 (3턴 미만)**: 약 10-30% 절감
- **중간 대화 (3-10턴)**: 약 40-60% 절감
- **긴 대화 (10턴 이상)**: 약 70-90% 절감

대화가 길어질수록 캐싱 효과가 커지므로, 학생들이 장시간 대화할수록 비용 절감 효과가 극대화됩니다!

### 요구사항
- `anthropic` 패키지 버전 0.16.0 이상 필요
- Claude 3.5 Sonnet (2024-10-22) 이상 모델 권장

## 🐛 문제 해결

### "Sheet not found" 에러
- Google Sheets URL이 올바른지 확인
- 서비스 계정에 시트 접근 권한이 있는지 확인

### "API Connection Error"
- 인터넷 연결 확인
- Anthropic API 키가 유효한지 확인

### "Rate Limit Error"
- API 사용량 한도 초과 - 잠시 후 재시도

## 📄 라이선스

이 프로젝트는 교육 목적으로 제작되었습니다.

## 🤝 기여

버그 리포트나 개선 제안은 이슈로 등록해 주세요.