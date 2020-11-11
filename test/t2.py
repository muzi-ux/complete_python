# def fibonacci(i):
#     if i == 2 or i == 1:
#         return 1
#     return fibonacci(i - 2) + fibonacci(i - 1)
#
#
# print(fibonacci(20))


lis = []
for i in range(25):
    lis.append(50 + i + 1)

print(lis)
print(len(lis))
print(sum(lis))
