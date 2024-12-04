<img src="https://capsule-render.vercel.app/api?type=transparent&height=200&section=header&text=todoList&fontSize=90&fontColor=#ffffff&fontAlignY=38"/>
<blockquote data-ke-style="style2">
<p data-ke-size="size16">오늘의 할일을 문장으로 변경하여 일기로 저장 시키는 시스템</p>
</blockquote>
<br/><br/><br/>

## 개발환경
- python : 3.13
- anaconda : 3
<br/><br/><br/>


## 수정내역
### 12.04
- 저장파일 txt 에서 json 으로 변경 (이전 파일 유무 확인 어려움으로 인한 변경) -> **ignore처리**
- json data 불러오고 값 수정하도록 변경 -> **json 파일 읽을때 예외처리**
- 완료여부 처리 오류수정
- **이전 할일중 완료처리가 된 할일 제외하고 불러오기** 로 수정
### 11.30
- ~~이전 파일 유뮤 확인해서 이전 할일중 완료처리가 안된 할일 불러오기~~
### 11.29
- 리스트에 할일을 추가하는 형식의 폼 생성
- 할일을 완료 처리하는 기능 추가
- ~~파일관리를 위해 날짜별로 생성하는 부분 수정~~
<br/><br/><br/>


## 추후 수정내역
- DB 연동
- 텍스트 분석해서 문자으로 변환 하는 기능 추가
- 완료된 날짜별로 txt 문서파일로 저장 (히스토리)
