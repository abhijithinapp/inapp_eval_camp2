for i in range(2000,2501):
    if i%5 ==0 and i%8 ==0:
        print(i)

num = int(input('Enter the number: '))
for i in range(10):
    print(i+1,'*',num,'=', (i+1)*num)
