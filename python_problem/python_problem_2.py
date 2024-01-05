##############  menu 1
def Menu1(user_state) :
    #사전에 학생 정보 저장하는 코딩 
    dict_student_state_data[user_state[0]] = [user_state[1],user_state[2]]  

##############  menu 2
def Menu2() :
    #학점 부여 하는 코딩
    #점수를 모두 string으로
    for key,values in dict_student_state_data.items():
        # 중간 기말이 학점처리 x시
        if len(dict_student_state_data[key]) == 2:
            avg_score = (values[0] + values[1]) / 2  
            if avg_score >= 90:
                dict_student_state_data[key].append('A')
            elif avg_score >= 80:
                dict_student_state_data[key].append('B')
            elif avg_score >= 70:
                dict_student_state_data[key].append('C')
            else:
                dict_student_state_data[key].append('D')
        
##############  menu 3
def Menu3() :
    #출력 코딩
    #https://pydole.tistory.com/entry/Python 참고함
    strFormat = '%-8s%-8s%-8s%-8s\n'
    strOut = '\n' +'-' * 32 + '\n'
    strOut += strFormat % ('name','mid','final','grade')
    strOut += '-' * 32 + '\n'
    for key,values in dict_student_state_data.items():
        strOut += strFormat % (key,values[0],values[1],values[2]) 
    print(strOut)

##############  menu 4
def Menu4(user_name):
    #학생 정보 삭제하는 코딩
    del(dict_student_state_data[user_name])

#학생 정보를 저장할 변수 초기화
dict_student_state_data = dict()
print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        #학생 정보 입력받기
        #예외사항 처리(데이터 입력 갯수, 이미 존재하는 이름, 입력 점수 값이 양의 정수인지)
        #예외사항이 아닌 입력인 경우 1번 함수 호출 
        try:
            user_state_input = input("Enter name mid-score final-score : ").split()
            # 예외사항 처리(데이터 입력 갯수)
            if len(user_state_input) != 3:
                raise Exception("Num of data is not 3!")
            # 예외사항 처리(이미 존재하는 이름)
            if user_state_input[0] in dict_student_state_data.keys():
                raise Exception("Already exist name!")
            # 예외사항 처리(점수 값이 양의 정수인지)
            # 정수인지
            user_state_input[1] = int(user_state_input[1])
            user_state_input[2] = int(user_state_input[2])
            if (user_state_input[1] < 0) or (user_state_input[2] < 0):
                raise ValueError
        except ValueError:
            print("Score is not positive integer!")
        except Exception as e:
            print(e)
        else:
            Menu1(user_state_input)          
    elif choice == "2" :
        #예외사항 처리(저장된 학생 정보의 유무)
        #예외사항이 아닌 경우 2번 함수 호출
        #"Grading to all students." 출력
        try:
            if not bool(dict_student_state_data):
                raise Exception("No student data!")
        except Exception as e:
            print(e)
        else:
            Menu2()
            print("Grading to all students.")

    elif choice == "3" :
        #예외사항 처리(저장된 학생 정보의 유무, 저장되어 있는 학생들의 학점이 모두 부여되어 있는지)
        #예외사항이 아닌 경우 3번 함수 호출
        try:
            if not bool(dict_student_state_data):
                raise Exception("No student data!")
            for key in dict_student_state_data:
                if len(dict_student_state_data[key]) == 2:
                    raise Exception("There is a student who didn't get grade.")
        except Exception as e:
            print(e)
        else:
            Menu3()

    elif choice == "4" :
        #예외사항 처리(저장된 학생 정보의 유무)
        #예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
        #입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
        #있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is deleted." 출력
        try:
            if not bool(dict_student_state_data):
                raise Exception("No student data!")
        except Exception as e:
            print(e)
        else:
            try:
                del_student_name = input("Enter the name to delete : ")
                if not (del_student_name in dict_student_state_data.keys()):
                    raise Exception("Not exist name!")
            except Exception as e:
                print(e)
            else:    
                Menu4(del_student_name)
                print(del_student_name,"student information is deleted.")
    elif choice == "5" :
        #프로그램 종료 메세지 출력
        #반복문 종료
        print("Exit Program!")
        break
    else :
        #"Wrong number. Choose again." 출력
        print("Wrong number. Choose again.")