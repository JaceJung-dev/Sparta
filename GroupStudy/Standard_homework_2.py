#숙제1
#Hello World를 5번 출력
def homework_1():
    print("Hello World")
    print("Hello World")
    print("Hello World")
    print("Hello World")
    print("Hello World")
    

#숙제2
#1부터 44까지 짝수만 출력
def homework_2():
    for i in range(45):
        if i % 2 == 0:
            print(i)

# homework_2()

#숙제3
#1부터 44까지 짝수는 * 4, 홀수 그냥 출력
def homework_3():
    for i in range(45):
        if i % 2 == 0:
            print(i * 4)
        else:
            print(i)


#숙제4
#Hello World 4번 출력
def homework_4():
    for i in range(4):
        print('Hello World')

#숙제5
#numbers = [1, 2, 3, 4, 5]
#순회를 돌아 numbers 요소 출력
def homework_5():
    numbers = [1, 2, 3, 4, 5]
    for num in numbers:
        print(num)

#숙제6
#1부터 4까지 합 계산
def homework_6():
    result = 0
    for i in range(5):
        result += i
    return result

#숙제7
#사용자가 입력한 숫자의 구구단을 출력 (input)
#예시)
#입력값 : 3
def homework_7():
    input_num = int(input("숫자를 넣어주세요:"))
    for i in range(1, 10):
        print(f'{input_num} * {i} =', input_num * i)

#숙제8
#피보나치 수열에서 14개만 출력
#a, b = 1, 1
def homework_8():
    a, b = 1, 1
    num = 0
    print(a)
    print(b)
    for i in range(12):
        num = a + b
        print(num)
        a, b = b, num
    
#숙제9
#numbers = [11, 22, 33, 44, 55]
#target = 44 
def homework_9():
    numbers = [11, 22, 33, 44, 55]
    target = int(input('숫자를 넣어주세요:'))
    for num in numbers:
        if num == target:
            print("찾았습니다.")
        else: 
            print(False)

#숙제10
#1부터 100까지 3과 7의 배수만 출력
def homework_10():
    for i in range(1, 101):
        if i % 3 == 0 or i % 7 == 0:
            print(i)

#숙제11
#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#홀수만 새로운 리스트에 추가
def homework_11():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    new_list = []
    for number in numbers:
        if number % 2 == 1:
            new_list.append(number)

    return new_list

#숙제12
#사용자가 입력한 숫자를 받아, 팩토리얼 계산
def homework_12():
    input_num = int(input("숫자를 넣어주세요:"))
    result = 1
    for num in range(1, input_num + 1):
        result *= num

    return result

#숙제13
#아래 리스트에서 최솟값과 최댓값 찾기
#numbers = [44, 12, 35, 96, 46, 87, 2, 63]
def homework_13():
    numbers = [44, 12, 35, 96, 46, 87, 2, 63]
    print('최대값:', max(numbers), '최소값:', min(numbers))

#숙제14 (슬랙에선 12이라고 적힘)
#아래 리스트의 요소를 뒤에서부터 출력
#numbers = [44, 12, 35, 96, 46, 87, 2, 63]
def homework_14():
    numbers = [44, 12, 35, 96, 46, 87, 2, 63]
    print(numbers[::-1])

#숙제15
#회문(palindrome)일 경우 회문입니다 출력, 아닐 경우 아님 출력
#회문 예: 토마토, 구로구, ....등등
#hint: 인덱싱?????
def homework_15():
    string = input('글자를 입력해주세묘:')
    if string == string[::-1]:
        print("회문입니다.")
    else:
        print('회문이 아닙니다.')

#숙제16
#사용자의 입력을 숫자를 입력 받아, 0, 양수, 음수 판별
def homework_16():
    input_num = float(input("숫자를 입력해주세요:"))
    if input_num > 0:
        print('양수입니다.')
    elif input_num == 0:
        print('0 입니다.')
    else:
        print('음수입니다.')

#숙제17
#사용자에게 3개의 숫자를 받고, 그 중 가장 큰 수 출력
def homework_17():
    num1 = float(input('첫번쨰 숫자를 적어주세요:'))
    num2 = float(input('두번쨰 숫자를 적어주세요:'))
    num3 = float(input('세번째 숫자를 적어주세요:'))

    print(max(num1, num2, num3))

#숙제18
#사용자에게 요일을 받고, 그 요일이 주말이면 주말입니다로 출력
def homework_18():
    day = input('요일을 적어주세요:')
    if day in ['토요일', '일요일']:
        print('주말입니다.')
    else:
        pass

#숙제19 (슬랙에서 17이라고 적힘)
#0부터 100사이의 점수를 받아 학점 출력
#90이상 A / #80이상 B / #70이상 C / #60이상 D / #60미만 F
def homework_19():
    score = int(input("점수를 입력해주세요:"))
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("F")

#숙제20 
#숙제19와 동일 but 조건 추가
#만약에 100초과의 점수를 받을 경우, 바보라고 출력
def homework_20():
    score = int(input("점수를 입력해주세요:"))
    if score > 100:
        print("바보")
    elif score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("F")

#숙제21 (슬랙에선 19이라고 적힘)
#숙제20와 동일 but 조건 추가
#만약에 100초과의 점수를 받을 경우 바보라고 출력, 0미만일 경우 멍청이라고 출력

def homework_21():
    score = int(input("점수를 입력해주세요:"))
    if score > 100:
        print("바보")
    elif score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    elif score >= 0:
        print("F")
    else:
        print("멍청이")

#숙제22 (슬랙에선 20이라고 적힘)
#id = admin
#password = 1234
#로그인 성공 시, 로그인 성공 출력
#로그인 실패 시, 로그인 실패 출력
def homework_22():
    login_id, login_password = 'admin', '1234'
    input_id = input("ID를 입력해주세요:")
    input_password = input("Password를 입력해주세요:")

    if input_id == login_id and input_password == login_password:
        print("로그인 성공")
    else:
        print("로그인 실패")

#숙제23
#사용자에게 3개의 숫자를 받아, 오름차순 정렬하여 출력
def homework_23():
    num1 = float(input('첫번쨰 숫자를 적어주세요:'))
    num2 = float(input('두번쨰 숫자를 적어주세요:'))
    num3 = float(input('세번째 숫자를 적어주세요:'))

    numbers = [num1, num2, num3]
    numbers.sort()

    for num in numbers:
        print(num)


#숙제24
#숙제21과 동일 but 조건 추가
#5개의 숫자를 받은 뒤 그 평균을 구하고, 그에 따른 등급 출력

def homework_24():
    score_list = []
    for i in range(1, 6):
        score_list.append(int(input(f"{i}번쨰 점수를 입력해주세요:")))
    
    score = sum(score_list) / len(score_list)

    def grade():
        if score > 100:
            return "바보"
        elif score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        elif score >= 0:
            return "F"
        else:
            return "멍청이"
        
    print(f"평균: {score}, 둥급:", grade())

# 숙제 - 25
# number = [1, 4, 4, 4, 4, 4, 4]에 중복 제거 해주세요
def homework_25():
    numbers = [1, 4, 4, 4, 4, 4, 4]
    remove_dup_numbers = list(set(numbers))
    print(remove_dup_numbers)

# 숙제 - 26
# number = [1, 4, 4, 4, 4, 4, 4, 5]에서 5 제거 후 출력해주세요 
def homework_26():
    number = [1, 4, 4, 4, 4, 4, 4, 5]
    number.remove(5)

    print(number)

# 숙제 - 27
# number = [1, 2, 3, 4, 5]에서 3 제거 후 나머지 요소의 평균 값 구해주세요
def homework_27():
    numbers = [1, 2, 3, 4, 5]
    numbers.remove(3)
    print(sum(numbers) / len(numbers))

# 숙제 - 28
# number = [1, 2, 3, 4, 5]에서 뒤의 3개만 출력해주세요 후 귀차나 슬슬
def homework_28():
    number = [1, 2, 3, 4, 5]

    print(number[-3:])

# 숙제 - 29
# number = [1, 4, 4, 4, 4, 4, 4. 5]에서 중복된 요소의 개수 출력
def homework_29():
    number = [1, 4, 4, 4, 4, 4, 4, 5]
    set_number = set(number)

    for num in set_number:
        count_num = number.count(num)
        if count_num > 1:
            print(f'{num}이란 요소가 {count_num}개 있습니다.')

# 숙제 - 30
# number = [1, 4, 4, 4, 4, 4, 4. 5]에서 요소 4의 위치(인덱스)를 출력하세요
def homework_30():
    number = [1, 4, 4, 4, 4, 4, 4, 5]
    for idx, num in enumerate(number):
        if num == 4:
            print(idx)

# 숙제 - 31
# list_1 = [1, 2, 3]
# list_2 = [4, 5, 6]
# 위의 두개의 리스트를 하나로 합쳐주세요
def homework_31():
    list_1 = [1, 2, 3]
    list_2 = [4, 5, 6]
    merged_list = list_1 + list_2
    # merged_list = list_1.extend(list_2)
    return merged_list

# 숙제 - 32
# number = [[1, 2], [3, 4], [5, 6]]의 모든 요소를 더해주세여
def homework_32():
    number = [[1, 2], [3, 4], [5, 6]]
    sum_num = 0
    for in_list in number:
        for num in in_list:
            sum_num += num
    return sum_num

def homework_32_2():
    number = [[1, 2], [3, 4], [5, 6]]
    flatten_num = [column for row in number for column in row]
    return sum(flatten_num)

# 숙제 - 33
# a = 11
# b = 22
# 위의 변수를 선언 후 a의 값을 22, b의 값을 11로 교환  
def homework_33():
    a, b = 11, 22
    a, b = 22, 11
    print(a, b)

# 숙제 - 34
# 값 3, 6, 9를 a, b, c 변수들에게 각각 할당해라
def homework_34():
    a, b, c = 3, 6, 9
    print(a, b, c)

# 숙제 - 35
# (44, 33, 22, 11)의 튜플을 리스트로 변환 후 출력
def homework_35():
    tup = (44, 33 , 22, 11)
    print(list(tup))

# 숙제 - 36
# 리스트 [11, 22, 33, 44]에 11의 값을 110으로 변경
# 튜플 (11, 22, 33, 44)에 11의 값을 110 변경 시도 
#def homework_36():
    a_list = [11, 22, 33, 44]
    b_tup = (11, 22, 33, 44)

    a_list[0] = 110
    b_tup[0] = 110

# 숙제 - 37
# 리스트 [44, 33, 22, 11]을 튜플로 변환하고, 55를 추가 시도해보아라.
# 안 된다면 그 이유는? 튜플은 불변 자료형이라 요소를 변경 할 수 없당.

# 숙제 - 38
# 리스트 튜플 차이점은?
# 함수 호출 시 인자를 전달 할 때 함수에서 데이터를 수정하고 싶지 않을 때, 어떤 자료형을 쓰면 되나요? 튜플이죵

# 숙제 - 39
# 리스트, 튜플 중 메모리를 적게 쓰는 것은 무엇이고 그 이유는? 튜플 (정적배열)  cf) 리스트 (정적배열)