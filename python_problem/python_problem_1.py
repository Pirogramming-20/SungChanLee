num = 0
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

num  = num_1to3
for i in range(num):
    print("playerA : ",i + 1)