x=[1,5,6,4,1,2,3,6]
y=[1,1,5]

def check(a,b):
    for i in a:
        for j in b:
            if(len(b)>=0 and j == i):
                b.pop(0)
            else:
                break
    return b

if len(check(x,y))==0:
    print("Its a match")
else: print("Its gone")
    
check(x,y)