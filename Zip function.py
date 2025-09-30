s1=[100,200,300,400]
s2=[1,2,3,4]
s3=zip(s2,s1)
print(list(s3))

for x,y in zip(s1,s2[::-1]):
    print(x,y)
