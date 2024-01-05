// 어려운데?
// 10ms단위 증가 ㅇㅈ?
// gettime으로 현재 시간 계속 받고 10ms 마다 숫자 증가 하면 되지않을까? ==> 개에바
// setTimeout()으로 10ms마다 더하기
// setInterval 함수가 있네......

// 타이머 기능
let stopwatch_time_10ms = 0;
let flag_timer = false; // 시작 여부
// 타이머
function time_10ms_inf(callback){
    if(flag_timer == false){ // 재귀 종료
        return;
    }
    setTimeout(()=>{
        if(flag_timer == true) // 바로 멈추지 않고 스택남은 하나가 더 실행
            stopwatch_time_10ms++; // 10ms마다 증가
        console.log(stopwatch_time_10ms);
        callback(stopwatch_time_10ms); //display(time_10ms)
        time_10ms_inf(callback) // 무한 재귀
    },10)
}

// 타이머 2
// const time_10ms_inf_2 = function(){
//     setInterval(()=>{
//         stopwatch_time_10ms++;
//         console.log(stopwatch_time_10ms);
//     },10)
// }

// 시간 표시 기능
const display_time = document.querySelector(".stopwatch-display"); // 시간 표시 창
const record_time = document.querySelector(".stopwatch-record"); // 시간 기록 창

function display(time_10ms){
    let ms = ('0' + time_10ms % 100).slice(-2);
    let s =  ('0' + parseInt(time_10ms / 100)).slice(-2);
    if(time_10ms / 100 >= 100){
        s = (parseInt(time_10ms / 100));
    }
    let strOutTime = s + ' : '+ ms;
    display_time.innerHTML = strOutTime;
}

function record(time_10ms){
    let ms = ('0' + time_10ms % 100).slice(-2);
    let s =  ('0' + parseInt(time_10ms / 100)).slice(-2);
    if(time_10ms / 100 >= 100){
        s = (parseInt(time_10ms / 100));
    }
    let strOutTime = s + ' : '+ ms;
    //귀찮으니 헤더 복사 하고 클래스만 바꾸기
    const record_div = record_time.children[0].cloneNode(true);
    record_div.className = "record-div";
    //체크박스 클래스 바꾸기
    record_div.children[0].children[0].className="check-box"
    //체크박스 이벤트 리스너 등록
    record_div.addEventListener("click",toggle_all) 
    //span내용바꾸고
    record_div.children[1].innerHTML = strOutTime;
    //형식 맞추게 휴지통대신 빈공간으로
    const div_format = document.createElement("div");
    div_format.className = "div-format"
    record_div.replaceChild(div_format, record_div.children[2]); 
    //추가
    record_time.appendChild(record_div)
}

// 버튼들
const button_started = document.getElementById("start"); // 시작 버튼
const button_stop = document.getElementById("stop"); // 스탑 버튼
const button_reset = document.getElementById("reset"); // 시작 버튼

// 시작
button_started.addEventListener("click", function() {
    console.log(button_started)
    if (flag_timer == true){ // 이미 실행중
        console.log("이미 실행중");
        return;
    }
    else{
        flag_timer = true;
        console.log(display);
        time_10ms_inf(display)
    }
})

// 멈춤
button_stop.addEventListener("click", function() {
    flag_timer = false;
    //문제 : stop시 원하는 것 보다 하나더 증가 --> 왜?
    // record 시점 문제?
    //--> 콜백 프로미스 해봤는데 해결 x
    // 원인 = 스택에 재귀가 하나더 남음 ==> 예외처리
    record(stopwatch_time_10ms);
})

// 리셋
button_reset.addEventListener("click", function() {
    stopwatch_time_10ms = 0;
    flag_timer = false;
    display_time.innerHTML = "00 : 00"
})

// 체크박스
const button_del = document.getElementById("del"); //삭제 버튼
const button_all = document.querySelector(".all-check")
const button_check = document.getElementsByClassName("check-box")
let list_record;

// 전체 선택
button_all.addEventListener("click", function(){
    list_record = document.getElementsByClassName("record-div")
    if(button_all.checked){
        for(let i = 0; i < list_record.length; i++){
            list_record[i].children[0].children[0].checked = true;
        }
    }
    else{
        for(let i = 0; i < list_record.length; i++){
            list_record[i].children[0].children[0].checked = false;
        }
    }
})

// 체크박스가 만들어 질때 이벤트 리스너에 등록됨
const toggle_all = function(){
    list_record = document.getElementsByClassName("record-div")
    let all = true;
    for(let i = 0; i < list_record.length; i++){
        if(list_record[i].children[0].children[0].checked == false){
            all = false;
        }
    }
    if(all == true){
        button_all.checked = true;
    }
    else{
        button_all.checked = false;
    }
}

// 지우기
button_del.addEventListener("click", function() {
    list_record = document.getElementsByClassName("record-div")
    // 아래부터 삭제해야 순서가 안꼬임
    for(let i = list_record.length - 1; i >= 0; i--){
        if(list_record[i].children[0].children[0].checked){
            list_record[i].remove();
        }
    }
})
