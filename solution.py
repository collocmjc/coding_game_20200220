import math

def check_result(n,res):
    """ check if res this is the max """
    return res*len(str(res)) <= n and (res+1)*len(str(res+1)) > n

def check_function(f, max_iter=10000000000):
    """ check if f return the good result for n in range(max_iter)"""
    for n in range(max_iter):
        res = f(n)
        if not check_result:
            print('Error with {} : {}'.format(n, res))

def get_solution(n):
    """ return the solution a but also the coeficient k such as a*k <= n"""
    # k number of digit
    k = len(str(n))
    if n < (k-1)*10**(k-1):
        return math.floor(n/(k-1)), k-1
    elif k*10**(k-1) <= n:
        return math.floor(n/k), k
    else:
        # result is constant
        return 10**(k-1)-1, k-1


def main():
    """ main function """
    n = int(input('Enter an integer : '))
    a,k = get_solution(n)
    k2 = len(str(a+1))
    print(f'The solution is {a} since {a} x {k} = {a*k} and {a+1} x {k2} = {(a+1)*k2}')

if __name__ == '__main__':
    main()