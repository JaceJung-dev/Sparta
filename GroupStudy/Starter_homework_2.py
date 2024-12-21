# 문제 1
# 사용자의 이름을 입력받아 "안녕하세요, [이름]님!"이라고 출력하는 함수 say_hello를 작성하세요.
def say_hello(name):
    print(f'안녕하세요, {name}님!')

# 문제 2
# 두 개의 숫자를 입력받아 큰 수를 반환하는 함수 find_larger를 작성하세요.
def find_larger(a, b):
    return max(a, b)

# 문제 3
# 리스트를 입력받아 그 리스트의 첫 번째 요소와 마지막 요소를 출력하는 함수 print_first_last를 작성하세요.
def print_first_last(list):
    print(f'첫 번째 요소: {list[0]}, 마지막 요소: {list[-1]}')
    
# 문제 4
# 숫자를 하나 입력받아 그 숫자가 짝수인지 홀수인지 출력하는 함수 even_or_odd를 작성하세요.
def even_or_odd(num):
    if num % 2 == 0:
        print("짝수")
    else:
        print("홀수")
        
# 문제 5
# 문자열을 입력받아 그 문자열을 대문자로 변환하여 반환하는 함수 to_uppercase를 작성하세요.
def to_uppercase(string):
    return string.upper()

# 문제 6
# 두 숫자를 입력받아 더한 결과를 반환하는 함수 add_numbers를 작성하세요.
def add_numbers(a, b):
    return a + b

# 문제 7
# 리스트를 입력받아 모든 요소의 합을 반환하는 함수 sum_list를 작성하세요. (내장 함수 sum을 사용하지 않고 구현해보세요.)
def sum_list(list):
    total_num = 0
    for num in list:
        total_num += num
    return total_num

# 문제 8
# 임의의 개수의 숫자를 입력받아 그 평균을 계산하는 함수 calculate_average를 작성하세요. (가변 인자를 사용하세요.)
def calculate_average(*args):
    return sum(args) / len(args)

# 문제 9
# 문자열을 입력받아 그 문자열의 길이를 반환하는 람다 함수를 작성하세요.
(lambda string : len(string))('apple')

# 문제 10
# 재귀 함수를 사용하여 팩토리얼(n!)을 계산하는 함수 factorial을 작성하세요.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    if n > 1:
        return n * factorial(n - 1)
    
# 문제 11
# 딕셔너리를 입력받아 키와 값을 바꾼 새로운 딕셔너리를 반환하는 함수 swap_dict를 작성하세요.
def swap_dict(input_dict):
    return {v : k for k, v in input_dict.items()}

# 문제 12
# 기본 매개변수를 사용하여 인사말을 출력하는 함수 greet를 작성하세요. 이름이 주어지지 않으면 "Guest"라고 인사하도록 합니다.
def greet(name = "Guest"):
    print(f"안녕하세요. {name}님")