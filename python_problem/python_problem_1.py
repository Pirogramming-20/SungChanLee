num = 0
def brGame():
    while(True):
        num_1to3 = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")
        try:
            num_1to3 = int(num_1to3)
            if num_1to3 != 1 and num_1to3 != 2 and num_1to3 != 3:
                raise Exception("1,2,3 중 하나를 입력하세요")
        except ValueError:
            print("정수를 입력하세요")
        except Exception as e:
            print(e)
        else:
            return num_1to3 
        
while(True):
    # playerA
    num_input = brGame()
    for i in range(num + 1, num + num_input + 1):
        print("playerA :",i)
        if i == 31:
            print("playerB win!")
            break
    num += num_input
    # playerB
    num_input = brGame()
    for i in range(num + 1 , num + num_input + 1):
        print("playerB :",i )
        if i == 31:
            print("playerA win!")
            break
    num += num_input
