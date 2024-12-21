# 문제 1
# 주어진 문자열에서 각 문자의 출현 빈도를 계산하는 딕셔너리 컴프리헨션을 작성하세요.
# text = "hello world"
def prac_1():
    text = "hello world"
    frequency_dict = {char : text.count(char) for char in text}

    return frequency_dict

# 문제 2
# 1부터 100까지의 숫자 중 3의 배수이면서 5의 배수인 숫자만을 포함하는 리스트를 리스트 컴프리헨션으로 생성하세요.
def prac_2():
    multi_list = [num for num in range(1, 101) if num % 3 == 0 and num % 5 == 0]
    return multi_list

# 문제 3
# 두 개의 리스트가 주어졌을 때, 이를 딕셔너리로 결합하는 딕셔너리 컴프리헨션을 작성하세요.
# keys = ['a', 'b', 'c'] / values = [1, 2, 3]
# def prac_3():
    keys = ['a', 'b', 'c']
    values = [1, 2, 3]
    combine_dict = {keys[i]: values[i] for i in range(len(keys))}
    return combine_dict
def prac_3_2():
    keys = ['a', 'b', 'c']
    values = [1, 2, 3]
    conbine_dict = {key : values[i] for i, key in enumerate(keys)}
    return conbine_dict
def prac_3_3():
    keys = ['a', 'b', 'c']
    values = [1, 2, 3]
    conbine_dict = {k : v for k, v in zip(keys, values)}
    return conbine_dict

# 문제 4
# 주어진 리스트에서 중복을 제거하고 고유한 요소만을 포함하는 새로운 리스트를 생성하세요. (힌트: set 사용)
# original_list = [1, 2, 2, 3, 4, 4, 5]
def prac_4():
    original_list = [1, 2, 2, 3, 4, 4, 5]
    return list(set(original_list))

# 문제 5
# 2차원 리스트를 생성하는 리스트 컴프리헨션을 작성하세요. (예: 5x5 행렬)
def prac_5():
    matrix_list = [[ j for j in range(5)] for i in range(5)]
    return matrix_list

def prac_5_2():
    import random
    random_matrix = [[random.randint(1, 100) for _ in range(5)] for _ in range(5)]
    return random_matrix

# 문제 6
# 주어진 문자열 리스트에서 길이가 5 이상인 문자열만 대문자로 변환하여 새로운 리스트를 만드세요
# string_list = ['apple', 'banana', 'pear', 'grape', 'kiwi']
def prac_6():
    string_list = ['apple', 'banana', 'pear', 'grape', 'kiwi']
    select_list = [string for string in string_list if len(string) >= 5]
    return select_list

# 문제 7
# 두 개의 집합 A와 B가 주어졌을 때, 두 집합의 대칭 차집합을 구하세요.
# set_a = {1, 2, 3, 4, 5} / set_b = {4, 5, 6, 7, 8}
# symmetric_diff = set_a.symmetric_difference(set_b)
# symmetric_diff_alt = set_a ^ set_b  # XOR(^) 연산자 사용
def prac_7():
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}
    sym_diff_set = (set_a | set_b) - (set_a & set_b)
    return sym_diff_set

# 문제 8
# 1부터 10까지의 숫자에 대해 각 숫자의 제곱을 값으로 갖는 딕셔너리를 생성하세요.
def prac_8():
    power_dict = {num : num ** 2 for num in range(1,11)}
    return power_dict

# 문제 9
# 주어진 리스트에서 짝수만 선택하여 그 제곱값을 가진 새로운 리스트를 생성하세요.
# given_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def prac_9():
    given_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    new_list = [i ** 2 for i in given_list if i % 2 == 0]
    return new_list

# 문제 10
# 여러 개의 리스트가 주어졌을 때, 이들을 하나의 리스트로 평탄화하는 함수를 작성하세요.
# lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
def prac_10():
    lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    flatten_list = [column for row in lists for column in row]
    return flatten_list

print(prac_10())