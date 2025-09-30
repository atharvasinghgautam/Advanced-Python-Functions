numbers1=[1,2,3,4]
numbers2=[1,2,3,4]

result=map(lambda x,y: x+y,numbers1,numbers2)
print("The addition of two lists is: ")
print(list(result))

def sq(n):
    return n*n
square=map(sq,numbers1)
print("The square of numbers are: ")
print(list(square))