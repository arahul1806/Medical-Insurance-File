def subs(a,b):
    # a = 10
    # b = 30
    sub = a - b
    print(f'Addition of {a} and {b} is {sub}')
    return f'Addition of {a} and {b} is {sub}'

def divi(p,q):
    # p = 45
    # q = 15
    div = p // q
    print(f'Division of {p} and {q} is {div}')
    return f'Division of {p} and {q} is {div}'

print('Value of __name__ is :',__name__)

if __name__ == '__main__':
    subs(22,18)
    divi(50,10)