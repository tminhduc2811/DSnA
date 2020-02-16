"""
    Greatest common devisor (GCD) is the maximum number that a & b can evenly devide
"""

def find_GCD(a, b):
    while b:
        a, b = b, a%b
    return a
"""
    Least common multiple (LCM) is the minimum number that can evenly devide a & b
"""
def find_LCM(a, b):
    return a * (b/find_GCD(a, b))

def gcd(array):
    result = array[0]
    for i in range(1, len(array)):
        result = find_GCD(result, array[i])
    return result

def lcm(array):
    result = array[0]
    for i in range(1, len(array)):
        result = find_LCM(result, array[i])
    return result

if __name__=='__main__':
    arr = [4, 2, 6, 8, 16]
    print('GCD in the array is ', gcd(arr))
    print('LCM in the array is ', lcm(arr))
