## 쿼리문 파일

# todo 등록
INSERT_TODO = "INSERT TODOS INTO(TEXT, DATE, STATUS)VALUES(%s, %s, 'N')"

# todo list 조회
SELECT_TODO_LIST = "SELECT ID, TEXT, DATE, STATUS FROM TODOS WHERE DATE >= %s OR STATUS <> 'C'"

# todo 수정
UPDATE_TODO = "UPDATE TODOS SET status = CASE WHEN STATUS = 'C' THEN 'N' ELSE 'C' END WHERE ID = %s"
