x = dict()
y = {}

a = {
    "name" : "광민",
    "age" : 20,
}

print(a)
print(a["name"])
print(a["age"])

b = {
    1:"kwangmin",
    0: "hello",
    "age": 20,
}
# 딕셔너리의 key 값은 불변하는 것들을 사용할 수 있음. 리스트는 값을 바꿀 수 있기 때문에 
# 딕셔너리의 key 값으로 사용할 수 없음

print(b[1])
print(b[0])
print(b["age"])

print("age" in b)

print(b.keys())
print(b.values())

for key in b:
    print("key : " + str(key))
    print("value : " + str(b[key]))
    
b[1] = "광민"
print(b)

b["school"] = "한빛"

print(b)
