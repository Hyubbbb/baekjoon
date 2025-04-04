n = int(input())

def sugar(n):
    n1, remainder1 = divmod(n, 5)
    n2, _ = divmod(n, 3)
    
    if remainder1 == 0: # 5kg으로 다 해결될 때
        return(n1)
    else:
        # 완탐
        for i in range(n1+1, n2+1):
            for j in range(i, -1, -1):
                # print(f'j: {j}')
                if 5*j + 3*(i-j) == n:
                    return(i)
        return(-1)

print(sugar(n))