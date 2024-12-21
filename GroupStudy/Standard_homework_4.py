# 숙제 - 70
# hi 함수를 호출 시 hi 출력
def hi():
    print('hi')

# 숙제 - 71
# hi 함수 호출 사 hi "여러분들의 이름"
def hi(name):
    print(f'hi {name}')

# 숙제 - 72
# 사용자가 입력한 두 개의 숫자를 받아 더해주는 함수 만드세요
def sum_x_y(x, y):
    return x + y

# 숙제 - 73
# 1000개 이상의 숫자를 받아 더해주는 함수 만드세요
def sum_infinite(*args):
    return sum(args)

# 숙제 - 74
# 리스트를 받은 뒤 그 길이를 반환하는 함수를 만드세요
def get_list_length(list):
    return len(list)

# 숙제 - 75
# 세개의 숫자를 비교하여 큰 숫자를 반환하는 함수
# 입력 -> func(50, 44444, 9)
# 출력 -> 44444
def find_max_num(a, b, c):
    return max(a, b, c)

# 숙제 - 76
# 20세 이상이면 True, 미만이면 False로 반환하는 함수
def find_adult(age):
    if age >= 20:
        return True
    else:
        return False
    
# 숙제 - 77
# 문자열의 첫 문자가 대문자인지 확인하는 함수
def check_first_letter(string):
    return string[0].isupper()

# 숙제 - 78
# 문자열에서 모음의 개수를 세어 반환하는 함수
def count_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = {vowel : string.count(vowel) for vowel in vowels if vowel in string}
    
    return result

# 숙제 - 79
# 숫자 리스트에서 짝수만 합을 계산하는 함수 
def sum_even_in_list(list):
    return sum([num for num in list if num % 2 == 0])

# 숙제 - 80
# 리스트와 특정 값을 받아 그 리스트에 그 값이 포함되어 있는지 확인하는 함수
def check_element_in_list(x, list : list) -> bool:
    return x in list

# 숙제 - 81
# 두 개의 문자열을 받아 공통으로 포함된 문자를 반환하는 함수를 만드세요
def find_common_letter(string1, string2):
    return set(string1) & set(string2)

# 숙제 - 82
# 문자열을 받아 문자를 반대로 반환하는 함수를 만드세요
def reverse_letter(string):
    return string[::-1]

# 숙제 - 83
# 삼각형의 밑변과 높이를 입력 받아 삼감형의 넓이를 계산하는 함수 만드세요
def find_triangle_area(width : float, height : float) -> float:
    return width * height / 2

# 숙제 - 84
# 리스트를 받아 중복된 요소가 있는지 확인하는 함수
def is_duplicated(list):
    if len(list) == len(set(list)):
        print("중복이 없네용")
    else:
        print("중복이 있네용")
        
# 숙제 - 85
# 두개의 리스트를 받아 공통 요소만 반환하는 함수
def get_common_elements(list1 : list, list2 : list) -> set:
    return set(list1) & set(list2)

# 숙제 - 86
# 문자열에서 숫자만 추출하는 함수
def get_number_from_input(string : str):
    num_list = []
    for char in string:
        try:
            num_list.append(int(char))
        except ValueError:
            continue
    return num_list

# 숙제 - 87
# 리스트(숫자)에서 최대값과 최솟값의 차이를 계산하는 함수
def get_max_min_difference(list):
    return max(list) - min(list)

# 숙제 - 88
# 정수를 받아 그 정수의 팩토리얼을 계산하는 재귀함수
def factorial(num):
    if num < 0:
        return "음수는 불가능해용"
    elif num == 0 or num == 1:
        return 1
    else: 
        return num * factorial(num - 1)
    
# 숙제 - 89
# 1부터 n까지의 합을 계산하는 재귀함수
def sum_one_to_num(num):
    if num == 1:
        return 1
    else:
        return num + sum_one_to_num(num - 1)
    
# 숙제 - 91
# 숫자 리스트를 받아 재귀적으로 최대 값을 찾는 함수
def find_max_num_by_recursion(list):
    if len(list) == 1:
        return list[0]
    if list[-1] > find_max_num_by_recursion(list[:-1]):
        return list[-1]
    else:
        return find_max_num_by_recursion(list[:-1])

# 숙제 - 92
# # 숫자를 입력 받아 재귀적으로 정렬하는 함수
def sorted_by_recursion(*args):
    args = list(args)
    if len(list(args)) <= 1:
        return args
            
    min_num = min(args)
    
    args.remove(min_num)
    
    return [min_num] + sorted_by_recursion(*args)