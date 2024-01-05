num = 0
while(True):
    # playerA
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
            break
    for i in range(num + 1, num+num_1to3 + 1):
        print("playerA :",i)
        if i == 31:
            # 6단계에서 해버렸어요..... 근데 승자가 반대라 수정할게요
            print("playerB win!")
            break
    num += num_1to3
    # playerB
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
            break
    for i in range(num + 1 , num+num_1to3 + 1):
        print("playerB :",i )
        if i == 31:
            # 6단계에서 해버렸어요..... 근데 승자가 반대라 수정할게요
            print("playerA win!")
            break
    num += num_1to3
