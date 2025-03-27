<img src="https://capsule-render.vercel.app/api?type=transparent&height=200&section=header&text=todoList&fontSize=90&fontColor=#ffffff&fontAlignY=38"/>
<blockquote data-ke-style="style2">
<p data-ke-size="size16">오늘의 할일을 문장으로 변경하여 일기로 저장 시키는 시스템</p>
</blockquote>
<br/><br/><br/>

## 개발환경
- python : 3.13
- anaconda : 3
- mysql : 8.0.33
- Flask : 3.1.0
- LLM : skt/kogpt2-base-v2 (125M)
<br/><br/><br/>


## 패키지 설치
<blockquote data-ke-style="style2">
<p data-ke-size="size16">pip install -r requirements.txt</p>
</blockquote>
<br/><br/><br/>


## 수정내역
### 2.25
- 내보내기에 문장 요약 기능 추가
### 2.24
- 문장 만들기 기능 추가
## 2024
- 내보내기 기능 추가
- 달력 추가, 히스토리 기능 추가
- 제거기능 추가
- 시작날짜, 수정날짜, 완료날짜 추가
- 완료처리 토글버튼으로 수정
- 수정기능 추가
- 쿼리문 파일 추가
- DB연동 (Mysql) -> **pymysql 사용**
- 환경변수 파일 추가 -> **.env** ignore 설정
- 저장파일 txt 에서 json 으로 변경 (이전 파일 유무 확인 어려움으로 인한 변경) -> **ignore처리**
- json data 불러오고 값 수정하도록 변경 -> **json 파일 읽을때 예외처리**
- 완료여부 처리 오류수정
- **이전 할일중 완료처리가 된 할일 제외하고 불러오기** 로 수정
- 리스트에 할일을 추가하는 형식의 폼 생성
- 할일을 완료 처리하는 기능 추가
<br/><br/><br/>


## 추후 수정내역
- 데드라인 기능 추가
- 통계 기능 추가
