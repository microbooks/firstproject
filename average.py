#total = 0
#count = 0
#while (True):
#    inp = input('Enter a number: ')
#    if inp == 'done':
#        break
#    try:
#        value = float(inp)
#    except:
#        print('Invalid input')
#        continue
#    total = total + value
#    count = count + 1
#
#average = total / count
#print('Average:', average)



total=0
count=0
largest=0
smallest=0
s=[]
while(True):
    inp=input("Input a number")
    if inp=="Done":
        break
    try:
        value=float(inp)
    except:
        print('input value')
        continue
    total =total +value
    if largest == 0:
        largest=value
    if smallest==0:
        smallest = value
    if value<smallest:
        smallest=value
    if value>largest:
        largest=value
    count +=1
    s.append(value)
if count==0:
    print("No numbers to Average")
else:
    average=total/count
    print("Numbers entered:", s.sort(), "\nTotal numbers=", count, s[0], s[len(s)-1])
    print('Average', average, "\nLargest = ", largest, "\nSmallest = ", smallest)