// 추가 버튼
function onAddTodoList(){
    const todoInput = $('#todoInput');
    const todoText = todoInput.val().trim();
    if (todoText !== '') {
        const listItem = document.createElement('li');
        listItem.textContent = todoText;
        // update API
        apiFunc("updated", {"text" : todoText})
        .then(response => {
            if(response.state == 'SUCCESS'){
                todoInput.val(''); // 입력 필드 초기화
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

// 수정 버튼
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

// 저장 버튼
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

// 제거 버튼
function onRemoveTodoList(item) {
    let li = $(item).closest('.todo-item');
    li.remove();

    // delete API
    apiFunc("deleted", {"id" : li.attr('id').replace('todo-','')});
}

// 문장 만들기 버튼
function onCreateSentence(){
    apiFunc("sentence", {})
    .then(response => {
        openModal(response.result);
    })
    .catch(error => console.error(error));
}

// 내보내기 버튼
function onExportTodoList(){
    const sel = $('.select');
    if(sel.length > 0){
        let date = sel.data('date');
        console.log('date', date);

        apiFunc("export", {"date" : date.replaceAll('-','')})
        .then(response => {
            alert(response.message);
        })
        .catch(error => console.error(error));
    }
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
                if (data.state === 'SUCCESS') {
                    resolve(data);
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

$(function(){
    const calendarEl = document.getElementById("calendar");
    const dateTodoListEl = $('#dateTodoList');

    const calendar = new FullCalendar.Calendar(calendarEl, {
        headerToolbar: {
            left:'prev',
            center:'title',
            right:'next'
        },
        height: 300,
        initialView: "dayGridMonth",
        locale: "ko",
        dayMaxEvents: true,
        dayCellContent: function (info) {
            // 날짜의 "일" 부분 숫자로 표시
            return { html: info.date.getDate() };
        },
        dateClick: function (info) {
            $('.select').removeClass('select');
            $(info.dayEl).addClass('select');

            const selectedDate = info.dateStr.replaceAll('-','');
            // history API
            apiFunc("history", {"date" : selectedDate})
            .then(response => {
                if(response.state == 'SUCCESS'){
                    $('#selectedDate').text(info.dateStr);
                    let todoList = response?.list;

                    dateTodoListEl.empty();
                    if (todoList?.length > 0) {
                        todoList.forEach(todo => {
                            let html = `<li class="todo-item">`;
                            html += `<span class="todo-text">${todo.TEXT}</span>`;
                            html += `</li>`;
                            dateTodoListEl.append(html);
                        });
                    } else {
                        dateTodoListEl.append('<li class="todo-item"><span class="todo-text">완료된 일이 없습니다.</span></li>');
                    }
                }
            })
            .catch(error => console.error(error));
        },
        viewDidMount: function(info) {
            // 어제 날짜 구하기
            const yesterday = new Date();
            yesterday.setDate(yesterday.getDate() - 1);

            // 어제 날짜를 'YYYY-MM-DD' 형식으로 변환
            const year = yesterday.getFullYear();
            const month = String(yesterday.getMonth() + 1).padStart(2, '0');
            const day = String(yesterday.getDate()).padStart(2, '0');
            const yesterdayDateString = `${year}-${month}-${day}`;
            const specificDateElement = $(`.fc-day[data-date="${yesterdayDateString}"]`);
            
            specificDateElement?.addClass('select');
        },
    });

    calendar.render();
});

// 모달 열기
function openModal(text) {
    $('#modalOverlay').addClass('active');
    $('#modalOverlay').find('.modal-content').text(text);
}

// 모달 닫기
function closeModal() {
    $('#modalOverlay').removeClass('active');
}