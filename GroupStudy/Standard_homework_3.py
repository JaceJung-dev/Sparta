# 숙제 - 40
# 빈 딕셔너리에 키: name, 값, 본인 이름을 추가하고 출력
def homework_40():
    id_dict = {}
    id_dict['name'] = 'Jace'

# 숙제 - 41
# {'name': 'won', 'age': 1000} 에서 키 age의 값을 출력
def homework_41():
    ex_dict = {'name': 'won', 'age': 1000}
    print(ex_dict['age'])

# 숙제 - 42
# {'apple': 111, 'banana': 222, 'cherry': 333} 에서 모든 키 출력
def homework_42():
    ex_dict = {'apple': 111, 'banana': 222, 'cherry': 333}
    print(ex_dict.keys())

def homework_42_2():
    ex_dict = {'apple': 111, 'banana': 222, 'cherry': 333}
    for key in ex_dict:
        print(key)

# 숙제 - 43
# {'apple': 111, 'banana': 222, 'cherry': 'babo'} 에서 모든 값 출력
def homework_43():
    ex_dict = {'apple': 111, 'banana': 222, 'cherry': 'babo'}
    print(ex_dict.values())

def homework_43_2():
    ex_dict = {'apple': 111, 'banana': 222, 'cherry': 'babo'}
    for value in ex_dict.values():
        print(value)

# 숙제 - 44
# {'apple': 111, 'banana': 222, 'cherry': 'babo'} 에서 값이 babo가 있다면 babo 출력
def homework_44():
    ex_dict = {'apple': 111, 'banana': 222, 'cherry': 'babo'}
    if 'babo' in ex_dict.values():
        print('babo')

def homework_44_2():
    ex_dict = {'apple': 111, 'banana': 222, 'cherry': 'babo'}
    for value in ex_dict.values():
        if value == 'babo':
            print(value)            

# 숙제 - 45
# {'apple': 111, 'banana': 222, 'cherry': 'babo'} 에서 apple 삭제 후 출력
def homework_45():
    ex_dict = {'apple': 111, 'banana': 222, 'cherry': 333}
    del ex_dict['apple']
    print(ex_dict)

def homework_45_2():
    ex_dict = {'apple': 111, 'banana': 222, 'cherry': 333}

    value = ex_dict.pop('apple', 'No value')
    print(ex_dict)

# 숙제 - 46
# # 숙제 - 46
# {'apple': 111, 'banana': 222, 'cherry': 'babo'} 에서 banana의 값을 babooo로 수정
def homework_46():
    ex_dict = {'apple': 111, 'banana': 222, 'cherry': 'babo'}
    ex_dict['banana'] = 'babooo'

    print(ex_dict)

# 숙제 - 47
# {'a': 1, 'b': 2}와 {'c': 3, 'd': 4}를 합치시오
def homework_47():
    a_dict, b_dict =  {'a': 1, 'b': 2}, {'c': 3, 'd': 4}

    merged_dict = a_dict | b_dict
    return merged_dict

def homework_47_2():
    a_dict, b_dict =  {'a': 1, 'b': 2}, {'c': 3, 'd': 4}

    a_dict.update(b_dict)
    return a_dict

# 숙제 - 48
# {'apple': 111, 'banana': 222, 'cherry': 'babo'}에서 모든 키와 모든 값을 순회하여 출력
def homework_48():
    ex_dict = {'apple': 111, 'banana': 222, 'cherry': 'babo'}
    for key in ex_dict:
        print(f'key값 {key}, value값: {ex_dict[key]}')

def homework_48_2():
    ex_dict = {'apple': 111, 'banana': 222, 'cherry': 'babo'}
    for key, value in ex_dict.items():
        print(f'key값 {key}, value값: {value}')

# 숙제 - 49
# {'apple': 111, 'banana': 222, 'cherry': 'babo'} 키 'cherry'의 '값'을 출력 하시오
# 없을 경우 None이라고 출력
def homework_49():
    ex_dict = {'apple': 111, 'banana': 222, 'cherry': 'babo'}

    if 'cherry' in ex_dict:
        print(ex_dict['cherry'])
    else:
        print('None')

def homework_49_2():
    ex_dict = {'apple': 111, 'banana': 222, 'cherry': 'babo'}

    try:
        print(ex_dict['cherry'])
    except:
        print('None')


def homework_49_3():
    ex_dict = {'apple': 111, 'banana': 222, 'cherry': 'babo'}

    value = ex_dict.get('cherry', None)
    print(value)

# 숙제 - 50
# {'apple': 111, 'banana': 222, 'cherry': 'babo'} 의 길이 출력
def homework_50():
    ex_dict = {'apple': 111, 'banana': 222, 'cherry': 'babo'}

    print(len(ex_dict))

# 숙제 - 51
# {'apple': 111, 'banana': '222', 'cherry': True} 값의 자료형 출력
def homework_51():
    ex_dict = {'apple': 111, 'banana': 222, 'cherry': 'babo'}

    for key, value in ex_dict.items():
        print(f'key타입: {type(key)}, value타입: {type(value)}')

# 숙제 - 52
# {'apple': 111, 'banana': '222', 'cherry': 333} 에 값을 합산하라
# hint 형변환
def homework_52():
    ex_dict = {'apple': 111, 'banana': '222', 'cherry': 333}
    dict_list = [int(value) for value in ex_dict.values()]
    return sum(dict_list)

# 숙제 - 53
# 문자열 "abcd abcd babo'에서 각 문자에 개수를 딕셔너리에 저장 후 출력
# 출력 시 -> {'a': 3, 'b': 4, 'c': 2, 'd': 2, ' ': 2, 'o': 1}
def homework_53():
    text = "abcd abcd babo"
    frequency_dict = {char : text.count(char) for char in text}

    print(frequency_dict)

# 숙제 - 54
# {'apple': 111, 'banana': 222, 'cherry': 'babo'}에서 키와 값을 각각 리스트로 변환 후 출력
def homework_54():
    ex_dict = {'apple': 111, 'banana': 222, 'cherry': 'babo'}

    key_list = [key for key in ex_dict.keys()]   # .items() 가능
    value_list = [value for value in ex_dict.values()]

    print(key_list)
    print(value_list)

# 숙제 - 55
# {'apple': 111, 'banana': 222, 'cherry': 'babo'} 에서 값 babo에 해당하는 키를 출력
def homework_55():
    ex_dict = {'apple': 111, 'banana': 222, 'cherry': 'babo'}

    for key, value in ex_dict.items():
        if value == 'babo':
            print(key)

# 숙제 - 56
# 중첩 딕셔너리를 만드시오
def homework_56():
    nested_dict = {
        'student_1' : {'name' : 'Kim', 'age' : 20, 'gender' : 'female'},
        'student_2' : {'name' : 'John', 'age' : 25, 'gender' : 'male'},
        'student_3' : {'name' : 'Jace', 'age' : 21, 'gender' : 'male'},
        'student_4' : {'name' : 'Alice', 'age' : 28, 'gender' : 'female'},
    }

    print(nested_dict)

# 숙제 - 57
# 딕셔너리와 리스트의 차이점에 대해
# 메모리? 더 많이 씀.

# 숙제 - 58
# 딕셔너리에 get 메소드 사용 용도와 사용하는 이유에 대해

# 숙제 - 59
# [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]에서 중복 값 제거
def homework_59():
    ex_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    set_list = set(ex_list)
    return list(set_list)

# 숙제 - 60
# {1, 2, 3}에 4를 추가 후 출력
def homework_60():
    set_data = {1, 2, 3}
    set_data.add(4)   # .update([4,5,6,7])

    print(set_data)

# 숙제 - 61
# {1, 2, 3, 4} 4 제거 후 출력
def homework_61():
    set_data = {1, 2, 3, 4}
    set_data.remove(4)   # .discard

    print(set_data)

# 숙제 - 62
# {1, 2, 3} 2가 있는지 확인
def homework_62():
    set_data = {1, 2, 3}
    
    return 2 in set_data

# 숙제 - 63
# 빈 집합 생성 후 타입 출력
def homework_63():
    new_set = {}

    print(type(new_set))

# 숙제 - 64
# {1, 2, 3, 4}와, {3, 4, 5, 6}의 합집합 출력
def homework_64():
    a_set, b_set = {1, 2, 3, 4}, {3, 4, 5, 6}
    union_set = a_set | b_set
    print(union_set)

# 숙제 - 65
# {1, 2, 3, 4}와, {3, 4, 5, 6}의 교집합 출력
def homework_65():
    a_set, b_set = {1, 2, 3, 4}, {3, 4, 5, 6}
    intersection_set = a_set & b_set
    print(intersection_set)

# 숙제 - 66
# {1, 2, 3, 4}와, {3, 4, 5, 6}의 차집합 출력
def homework_66():
    a_set, b_set = {1, 2, 3, 4}, {3, 4, 5, 6}

    a_difference_set = a_set - b_set
    b_difference_set = b_set - a_set

    print(f'a 차집합 b: {a_difference_set}')
    print(f'b 차집합 a: {b_difference_set}')

# 숙제 - 67
# # {1, 2, 3, 4}에 {3, 4, 5, 6}의 추가 후 출력
def homework_67():
    a_set, b_set = {1, 2, 3, 4}, {3, 4, 5, 6}

    a_set.update(b_set)
    union_set = a_set | b_set

    print(a_set)
    print(union_set)

# 숙제 - 68
# {1, 2, 3, 4} 모든 요소 제거
def homework_68():
    set_data = {1, 2, 3, 4}

    set_data.clear()
    return set_data

# 숙제 - 69
# {1, 2, 3}과 {2, 3, 4} 교집합 구한 결과와 {3, 4, 5} 합집합 결과 
def homework_69():
    a_set, b_set, c_set = {1, 2, 3}, {2, 3, 4}, {3, 4, 5}
    result = (a_set & b_set) | c_set
    return result
