import random
class Tutor:
    '''
    Tutor 클래스는 Sparta에서 일하시는 튜터님들의 속성과 매서드입니다.
    
    class arguments
        1. answer_count : int : 튜터님들이 받은 질문의 수
        2. tutor_count : int : 현재 계신 튜터님들의 수
        3. students : list : 학생 리스트
    '''
    answer_count = 0
    tutor_count = 0
    students = []
    
    # 생성자 매서드
    def __init__(self, name : str, feature : str, salary : float):
        '''
        Tutor 인스턴스를 초기화하고 생성합니다.
        Tutor 인스턴스가 생성될 때, 전체 Sparta 내에 있는 튜터의 수(tutor_count)를 증가해줍니다.
        
        parameters
            1. name : str : 튜터님의 이름
            2. feature : str : 튜터님의 개성
            3. salary : float : 튜터님의 월급
        '''
        self.name = name
        self.feature = feature
        self.salary = salary
        
        Tutor.tutor_count += 1
    
    # __str__ 매서드    
    def __str__(self)딩
        return f'name >>> {self.name}, feature >>>> {self.feature}, salary >>>> {self.salary}'
    
    # 연산자 오버라이딩
    def __add__(self, other):
        '''
        self.salary + other.salary
        '''
        return self.salary + other.salary
    
    def __truediv__(self, other):
        '''
        a / b : a튜터님이 업무를 b튜터님에게 토스합니다.
        '''
        return f'{self.name}튜터님의 업무를 {other.name}튜터팀에게 나눠줍니다'
    
    # 인스턴스 매서드
    def roulette(self):
        '''
        Sparta는 새로운 급여시스템을 도입해서 한달에 한번씩 룰렛을 돌려 월급 협상을 진행합니다.
        '''
        lucky_number = random.randint(1,4)
        if lucky_number % 3 == 0:
            self.salary *= 2
            print(f"축하드립니다! 월급이 200%로 인상되었습니다. :D, 현재 월급 : {self.salary}")
        elif lucky_number % 3 == 1:
            print(f"안심하세요! 월급에는 변동이 없습니다. :|, 현재 월급 : {self.salary}")
        else:
            self.salary *= 0.5
            print(f'아쉽네요! 월급이 50%로 감소되었습니다. :O, 현재 월급 : {self.salary}')
    
    # 클래스 매서드
    @classmethod
    def check_tutor_count(cls):
        '''
        현재 Sparta 내에 있는 튜터님들의 수를 반환합니다.
        '''
        return f"현재 {cls.tutor_count}명의 튜터님이 있습니다."
    
    @classmethod
    def ask(cls):
        '''
        Sparta 튜터님꼐 질문하는 매서드입니다.
        Sparta 내에 있는 튜터들이 받은 총 질문의 개수가 하나씩 증가합니다.
        '''
        cls.answer_count += 1
        return f"튜터님이 질문에 친절하게 답을 해주셨습니다. 튜터님들이 총 {cls.answer_count} 개의 질문을 해결해주셨습니다."

    @classmethod
    def did_hustle(cls):
        '''
        Sparta 튜터님들이 한달동안 받은 질문의 개수로 hustle하셨는지 확인합니다.
        '''
        if cls.answer_count >= 3:
            return f'튜터님들이 이번 달에도 정말 열심히 일하셨습니다.'
        else:
            return f'이번 달에는 학생들이 질문이 별로 없었나보네요.'
            
    @classmethod
    def add_student(cls, student):
        '''
        튜터님들이 담당하고 있는 학생들의 리스트에 새로운 학생을 추가하는 매서드입니다.
        '''
        cls.students.append(student)
        return f'{student}가 새로 들어왔습니다. 현재 학생 리스트는 {cls.students} 입니다.'
    
    # 스태틱매서드
    @staticmethod
    def did_student_hustle(question_number):
        '''
        학생들이 한달동안 질문한 숫자를 받아 열심히 했는지 알려줍니다.
        '''
        if question_number >= 10:
            return f'튜터님 방에 상주하시는 분이네요.'
        elif question_number > 3:
            return f'열심히 공부하고 질문도 많은 휼륭한 학생이네요.'
        else:
            return f'헤치치 않아요. 질문하러 가세요.'
    
t1 = Tutor('Lim', '가세요. 혼자있고 싶으니까요.', 15000000)
t2 = Tutor('Min', '총을 쏴요', 10000000)

print(t1)
# name >>> Lim, feature >>>> 가세요. 혼자있고 싶으니까요., salary >>>> 15000000
print(t2)
# name >>> Min, feature >>>> 총을 쏴요, salary >>>> 10000000
print(t1 + t2)
# 25000000
print(t1 / t2)
# Lim튜터님의 업무를 Min튜터팀에게 나눠줍니다
t1.roulette()
# 축하드립니다! 월급이 200%로 인상되었습니다. :D, 현재 월급 : 30000000
print(t1.check_tutor_count())
# 현재 2명의 튜터님이 있습니다.
print(t1.ask())
# 튜터님이 질문에 친절하게 답을 해주셨습니다. 튜터님들이 총 1 개의 질문을 해결해주셨습니다.
print(t2.ask())
# 튜터님이 질문에 친절하게 답을 해주셨습니다. 튜터님들이 총 2 개의 질문을 해결해주셨습니다.
print(t1.did_hustle())
# 이번 달에는 학생들이 질문이 별로 없었나보네요.
print(t1.add_student('Jace'))
# Jace가 새로 들어왔습니다. 현재 학생 리스트는 ['Jace'] 입니다.
print(t1.add_student('Jade'))
# Jade가 새로 들어왔습니다. 현재 학생 리스트는 ['Jace', 'Jade'] 입니다.
print(t1.did_student_hustle(6))
# 열심히 공부하고 질문도 많은 휼륭한 학생이네요.