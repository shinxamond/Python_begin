#첫 번째 : O(n)

def prime_checker(number):
    prime = True
    for i in range(2, number):
        if number%i==0:
            prime = False

    if (prime):
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


# 두 번째 : O(n^(1/2)) = O(√n)
# 
# import math
# 
# def prime_checker(number):
#     prime = True
#     for i in range(2, int(math.sqrt(number))+1): # n의 제곱근을 정수화 시켜준 후 + 1
#         if number % i == 0:
#             prime=False
#            
#     if (prime):
#         print("소수")
#     else:
#         print("소수아님")


#세 번째 : 에라토스테네스의 체 O(nlog(logn))
#
# import math
#
# def prime_checker(number):
#     arr = [True] * (number + 1)
#     arr[0] = False
#     arr[1] = False
#
#     for i in range(2, int(math.sqrt(number)+1)):
#         if arr[i] == True:
#             j = 2
#
#             while (i * j) <= number:
#                 arr[i*j] = False
#                 j += 1
#
#     return arr
#
# arr = prime_checker(50)
#
# for i in range(len(arr)):
#     if arr[i] == True:
#         print(i, end=' ')

n = int(input("Check this number: "))
prime_checker(number=n)