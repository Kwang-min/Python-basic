class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def say_hello(self, to_name):
        print("안녕 " + to_name + "내 이름은" + self.name)
        
    def introduce(self):
        print("안녕 내 이름은  " + self.name + "이고 나이는 " + str(self.age) + "살이야" )

p = Person("광민",20)
p.say_hello("민우야")
p.introduce()

#여기서부터는 상속에 대한 내용

class Police(Person):
    def arrest(self, to_arrest):
        print("넌 체포됐다" + to_arrest)
class Programmer(Person):
    def program(self, to_program):
        print("다음엔 뭘 만들지 아 이걸 만들어야겠다" + to_program)
        
min = Person("min",20)
minwoo = Police("minwoo", 20)
hun = Programmer("hun",21)

min.introduce()
minwoo.introduce()
hun.introduce()

minwoo.arrest("도둑놈")
hun.program("크롤러")

