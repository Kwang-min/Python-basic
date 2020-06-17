for i in range(3):
    print("영희야 뭐해 ?")
    print("철수야 나는 그냥 있어")

i = 0
while i < 3:
    print("영희야 뭐해 ?")
    print("철수야 나는 컴퓨터 해 ")
    i = i + 1
    
i = 0
while True:
    print("영희야 뭐해?")
    print("무한루프 돌리고 있어")
    
    i = i + 1
    if i > 2:
        break
        
for i in range(100):
    print("영희야 뭐해?")
    print("포 루프 돌리고 있어")
    if i > 2:
        break
        
for i in range(3):
    print("영희야 뭐해?")
    print("포 루프 돌리고 있어")
    
    if i == 1:
        continue
    
    print("철수야 영희야 안녕")