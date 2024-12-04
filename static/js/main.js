// 리스트에 추가하는 함수
function onAddTodoList(){
    const todoInput = document.getElementById('todo');
    const todoList = document.getElementById('todoList');
    const todoText = todoInput.value.trim();
    if (todoText !== '') {
        const listItem = document.createElement('li');
        listItem.textContent = todoText;
        addList(todoText, 'saved');
        todoList.appendChild(listItem);
        todoInput.value = ''; // 입력 필드 초기화
    }
}

// 리스트에 추가하는 api
function addList(messageText) {
    item = {"text" : messageText}
    $.ajax({
        url: "http://127.0.0.1:5000/updated",
        type: "POST",
        dataType: "json",
        contentType: "application/json",
        data: JSON.stringify(item),
        success: function (data) {
            state = data['state'];

            if (state === 'SUCCESS') {
                return 'success';
            } else {
                return 'fail';
            }
        },
        error: function (request, status, error) {
            console.log('error : ',error);
        }
    });
}

// 완료 처리 토글 함수
function toggleCompletion(item) {
    // 클릭한 항목에 'completed' 클래스 추가/제거
    item.classList.toggle('completed');
    json_data = {"id" : item.id ,"text" : item.innerText}

    $.ajax({
        url: "http://127.0.0.1:5000/updated",
        type: "POST",
        dataType: "json",
        contentType: "application/json",
        data: JSON.stringify(json_data),
        success: function (data) {
            state = data['state'];

            if (state === 'SUCCESS') {
                return 'success';
            } else {
                return 'fail';
            }
        },
        error: function (request, status, error) {
            console.log('error : ',error);
        }
    });
}