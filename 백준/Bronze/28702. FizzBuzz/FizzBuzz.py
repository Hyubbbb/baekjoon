import sys
input = sys.stdin.readline

w1 = input().rstrip()
w2 = input().rstrip()
w3 = input().rstrip()

if w1 not in ['Fizz', 'Buzz', 'FizzBuzz']:
    w1 = int(w1)
if w2 not in ['Fizz', 'Buzz', 'FizzBuzz']:
    w2 = int(w2)
if w3 not in ['Fizz', 'Buzz', 'FizzBuzz']:
    w3 = int(w3)

if type(w3) == int:
    result = w3+1
    if result % 15 == 0:
        print('FizzBuzz')
    elif result % 3 == 0:
        print('Fizz')
    elif result % 5 == 0:
        print('Buzz')
    else:
        print(result)
    
elif type(w2) == int:
    result = w2+2
    if result % 15 == 0:
        print('FizzBuzz')
    elif result % 3 == 0:
        print('Fizz')
    elif result % 5 == 0:
        print('Buzz')
    else:
        print(result)
elif type(w1) == int:
    result = w1+3
    if result % 15 == 0:
        print('FizzBuzz')
    elif result % 3 == 0:
        print('Fizz')
    elif result % 5 == 0:
        print('Buzz')
    else:
        print(result)