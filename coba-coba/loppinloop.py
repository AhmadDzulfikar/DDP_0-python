## ------------ 1 ------------
# for i in range(2):
#     for j in range(3):
#         print(i, j)

# i = 0
# while i < 2:
#     j = 0
#     while j < 3:
#         print(i, j)
#         j += 1
#     i += 1

## ------------ 2 ------------
# for i in range(2):
#     for j in range(i, 3):
#         print(i, j)

i = 0
while i < 2:
    j = i
    while j < 3:
        print(i, j)
        j += 1
    i += 1

## ------------ 3 ------------
for i in range(1,5):
    for j in range(1,5):
        if i + j == 4:
            print(i, j)

# i = 1
# while i < 4:
#     j = 3
#     while j > 0:
#         if i + j == 4:
#             print(i,j)
#             j -= 1
#         i += 1