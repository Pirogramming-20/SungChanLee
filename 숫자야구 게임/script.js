// 게임 시작 변수
let randomNumber123 = [];  // 맞출 숫자
let numLife = 9;    // 남은 시도 횟수
const resultBox = document.querySelector(".result-display");// 결과 창
const resultImg = document.getElementById('game-result-img');//결과 이미지 
const submitButton =document.querySelector(".submit-button");// 확인 버튼 
const input = document.getElementsByClassName("input-field");
// 게임 초기화
function game_init(){
    // 시도 가능 횟수를 설정합니다.
    numLife = 9;
    // 중복되지 않는 3개의 랜덤한 숫자를 설정합니다.
    randomNumber123 = [];
    let allNumber = [0,1,2,3,4,5,6,7,8,9];  // 0~9의 배열
    //0~9의 배열에서 3개 뽑기
    for(let i = 0; i < 3; i++){
        const idx = Math.floor(Math.random() * allNumber.length); 
        randomNumber123.push(allNumber[idx]);
        allNumber.splice(idx, 1);
    }
    console.log(randomNumber123);   // 정답
    //html의 input과 결과창의 내용을 비웁니다.
    for(let j = 0; j < 3; j++){
        input[j].value = '';
    }
    resultBox.replaceChildren();
    resultImg.src = '';
    // 버튼 입력 가능
    submitButton.disabled = false;
}
game_init();  // 게임 초기화
// 게임 진행 변수 
const inputNumbers = [];

// 확인하기 버튼 클릭시 게임 진행
function check_numbers(){
    //1.입력되지 않은 input 이 있다면 숫자를 확인하지 않고 input 창만 비웁니다.
    // 입력 받은 input 배열(inputNumbers)에 넣고 확인하기
    for(let i = 0; i < 3; i++){
        inputNumbers[i] = input[i].value;
        // 하나라도 비면
        if(inputNumbers[i] === ''){
            console.log("입력 오류")
            // input 창 비우기
            for(let j = 0; j < 3; j++){
                input[j].value = '';
            }
            return;
        }
    }
    // 문제 없어도 input 창 비우기
    for(let j = 0; j < 3; j++){
        input[j].value = '';
    }

    //2.숫자 3개가 입력되었다면 결과를 확인합니다.
    let strike = 0;
    let ball = 0;
    let out = 0;
    //입력된 숫자들과 정답을 비교하여 결과를 생성하는 로직 만들기
    for(let i = 0; i < 3; i++){
        if(randomNumber123[i] == inputNumbers[i]){
            strike += 1;
        }
        else if(randomNumber123.includes(Number(inputNumbers[i]))){
            ball +=1;
        }
        else{
            out += 1;
        }
    }
    
    //3. 결과 출력
    const checkResult = document.createElement("div");
    checkResult.className = "check-result";
    // left
    const checkResultLeft = document.createElement("div");
    checkResultLeft.className = "left";
    //input 받은 거 html에 출력
    for(let i = 0; i < 3; i++){
        checkResultLeft.innerHTML += inputNumbers[i] + ' ';
    } 
    checkResult.appendChild(checkResultLeft);
    // 출력 형식 
    checkResult.innerHTML +=":"
    // right
    const checkResultRight = document.createElement("div");
    checkResultRight.className = "right";

    if(out == 3){ // out만 존재 시
        const checkResultOut = document.createElement("div");
        checkResultOut.className = "out num-result";
        checkResultOut.innerHTML = 'O';
        checkResultRight.appendChild(checkResultOut);
    }
    else{ // out 아닐 시
        //strike
        checkResultRight.innerHTML = strike + ' ';
        
        const checkResultStrike = document.createElement("div");
        checkResultStrike.className = "strike num-result";
        checkResultStrike.innerHTML = 'S';
        checkResultRight.appendChild(checkResultStrike);
        //Ball
        checkResultRight.innerHTML += ' ' +ball + ' ';
        
        const checkResultBall = document.createElement("div");
        checkResultBall.className = "ball num-result";
        checkResultBall.innerHTML = 'B';
        checkResultRight.appendChild(checkResultBall);      
    }
    checkResult.appendChild(checkResultRight);

    resultBox.appendChild(checkResult);

    //4. 게임 종료
    if(strike == 3){ // 승리
        submitButton.disabled = true;
        console.log("게임 승리")
        resultImg.src = 'success.png';
    }
    // 확인하기 누를 때마다 life--
    numLife --;

    if(numLife <= 0){ // 패배
        submitButton.disabled = true;
        console.log("게임 오버")
        resultImg.src = 'fail.png';
    }
} 