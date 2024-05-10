a = int(input())
if a>=1 and a<=1000:
    if a % 2 == 0:
        print(f'{a} is even')
    else: print(f'{a} is odd')
else: print('retry')