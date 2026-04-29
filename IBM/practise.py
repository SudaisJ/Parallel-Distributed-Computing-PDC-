# numbers = list(map(int, input().split()))
# print(max(numbers))

# num = int(input())
# if num > 1:
#     for i in range (2,num):
#         if num % i == 0:
#             print ("not prime")
#         else:
#             print ("prime")

# number = list(map(int, input().split()))
# largest =max(number)
# number.remove(largest)
# second_largest = max(number)
# print(second_largest)

# n = int(input())
# a,b = 0,1
# for i in range(n):
#     print(a,end ="")
#     a,b = b, a+b

# s1 = input().replace("","").lower()
# s2 = input().replace("","").lower()
# if sorted(s1) == sorted(s2):
#     print("Anagrams")
# else:
#     print("Not Anagrams")

n = int(input())
arr = list(map(int, input().split()))

expected_sum = n* (n+1) //2
actual_sum = sum(arr)
print(expected_sum - actual_sum)