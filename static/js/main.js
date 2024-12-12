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
    let item = {"text" : messageText}
    // update API
    apiUpdate(item);
}

// 완료 처리 토글 함수
function toggleCompletion(item) {
    let li = $(item).closest('.todo-item');
    let json_data = {"id" : li.attr('id').replace('todo-','')}
    // update API
    apiUpdate(json_data);
}

// 수정 버튼 함수
function btnEditMode(item) {
    let li = $(item).closest('.todo-item');
    let todoText = li.find('.todo-text');
    let editInput = li.find('.edit-input');
    let saveButton = li.find('.save-button');
    let removeButton = li.find('.remove-button');

    // 토글 수정 모드
    $(item).hide();
    todoText.hide();
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

    let json_data = {"id" : li.attr('id').replace('todo-','') ,"text" : editInput.val()}

    // Update the UI with new text
    todoText.text(editInput.val());
    $(item).hide();
    editInput.hide();
    removeButton.hide();
    todoText.show();
    editButton.show();
    
    // update API
    apiUpdate(json_data);
}

function onRemoveTodoList(id) {
    // Logic to remove the to-do item
    var item = document.getElementById(id);
    item.remove();

    // Optionally, send a request to the server to remove the item
    // Example with AJAX:
    $.ajax({
        url: '/remove-todo', // Your server endpoint for removing the item
        type: 'POST',
        data: { id: id },
        success: function(response) {
            // Handle server response if needed
        }
    });
}

// update API
function apiUpdate(json_data) {
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