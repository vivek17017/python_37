
"""
#Q1
def first(n):
    if n==1:
        print(1)
    else:
        first(n-1)
        print(n,end=' ')
first(19)


#Q2
def first(n):
    if n>1:
        print(n)
        first(n-1)
    else:
        print(1)
first(19)


#Q2
def first(n):
    if n==1:
        print(1)
    else:
        print(n,end=' ')
        first(n-1)
first(19)


#Q3
def first(n):
    if n==1:
        print(1)
    else:
        first(n-1)
        print(2*n-1,end=' ')
first(19)



#Q3
def first(n):
    if n==1:
        print(1)
    else:
        print(2*n-1,end=' ')
        first(n-1)
first(19)


#Q3
def first(n):
    if n==1:
        print("MySirG")
    else:
        first(n-1)
        print("Mysirg",end=' ')
first(5)

"""
def extraNumbersFromText(text):
    num=[]
    for word in text.split(' '):
        for x in word.split(','):
            if type(eval(x))==int or type(eval(x))==float:
                num.append(float(x))
    return num
print(extraNumbersFromText("i want to add 4,4,45 to get 456"))



