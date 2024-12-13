// 리스트에 추가하는 함수
function onAddTodoList(){
    const todoInput = document.getElementById('todoInput');
    const todoList = document.getElementById('todoList');
    const todoText = todoInput.value.trim();
    if (todoText !== '') {
        const listItem = document.createElement('li');
        listItem.textContent = todoText;
        // update API
        apiFunc("updated", {"text" : todoText})
        .then(result => {
            console.log('result',result)
            if(result == 'success'){
                todoInput.value = ''; // 입력 필드 초기화
                $('#todoList').load('/ #todoList'); // relaod
            }
        })
        .catch(error => console.error(error));
    }
}

// 완료 처리 토글 함수
function toggleCompletion(item) {
    let li = $(item).closest('.todo-item');
    let json_data = {"id" : li.attr('id').replace('todo-','')}
    // update API
    apiFunc("updated", json_data);
}

// 수정 버튼 함수
function btnEditMode(item) {
    let li = $(item).closest('.todo-item');
    let todoText = li.find('.todo-text');
    let editInput = li.find('.edit-input');
    let saveButton = li.find('.save-button');
    let removeButton = li.find('.remove-button');
    let toggleSwitch = li.find('.toggle-switch');

    // 토글 수정 모드
    $(item).hide();
    todoText.hide();
    toggleSwitch.hide();
    editInput.show();
    saveButton.show();
    removeButton.show();
}

// 저장 버튼 함수
function onSaveTodoList(item) {
    let li = $(item).closest('.todo-item');
    let editInput = li.find('.edit-input');
    let todoText = li.find('.todo-text');
    let editButton = li.find('.edit-button');
    let removeButton = li.find('.remove-button');
    let toggleSwitch = li.find('.toggle-switch');

    // Update the UI with new text
    todoText.text(editInput.val());
    $(item).hide();
    editInput.hide();
    removeButton.hide();
    todoText.show();
    editButton.show();
    toggleSwitch.show();
    
    // update API
    apiFunc("updated", {"id" : li.attr('id').replace('todo-','') ,"text" : editInput.val()});
}

// 제거 버튼 함수
function onRemoveTodoList(item) {
    let li = $(item).closest('.todo-item');
    li.remove();

    // delete API
    apiFunc("deleted", {"id" : li.attr('id').replace('todo-','')});
}

// 문장 만들기 버튼
function onCreateSentence(){
    // create sentence API
    apiFunc("sentence", {});
}

function apiFunc(url, json_data) {
    return new Promise((resolve, reject) => {
        $.ajax({
            url: "http://127.0.0.1:5000/" + url,
            type: "POST",
            dataType: "json",
            contentType: "application/json",
            data: JSON.stringify(json_data),
            success: function (data) {
                if (data['state'] === 'SUCCESS') {
                    resolve('success');
                } else {
                    resolve('fail');
                }
            },
            error: function (request, status, error) {
                console.log('error : ',error);
            }
        });
    });
}