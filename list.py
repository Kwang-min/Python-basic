x = list() # 빈 리스트 만들기 
y = [] # 빈 리스트 만들기 

a = [1,2,3]
b = ["hello","hi"]
c = [1,2,"hello"]

print(a)
print(b)
print(c)

print(a + b)
print(a[0])

a[2] = 10

print(a)

num_elements = len(a)
print(num_elements)

x = [4,2,5,1]

y = sorted(x)
print(y)
z = sum(y)
print(z)

for n in y:
    print(n)
    
u = y.index(5)# .index()는 위치를 알 수 있음
print(u)
print(4 in y)# 있는지 없는지만 확인하고 싶을 때

if 1 in y:
    print("1은 y 안에 있어요")
