# a = 50
# b = 60
# add = a+b
# mul = a*b
# div = a/b
# sub = a-b
#
# print("Your Answer is ",add)
# print("Your Answer is ",mul)
# print("Your Answer is ",div)
# print("Your Answer is ",add)

# a = [10,20,30,50,80,104]
# b=[]
# for i in a:
#     b.append(i)
#     b.reverse()
#
# print("copy list",b)


rows = int(input("Enter rows for print pyramid: \n"))

# k = 0
# #range(start, stop, step)
# for i in range(1, rows + 1):
#     for space in range(1, (rows - i) + 1):
#         print(end="  ")
#
#     while k != (2 * i - 1):
#         print("* ", end="")
#         k += 1
#
#     k = 0
#     print()


# # number of spaces
# k = rows - 1
#
# # outer loop to handle number of rows
# for i in range(0, rows):
#     # inner loop to handle number spaces
#     # values changing acc. to requirement
#     for j in range(0, k):
#         print(end=" ")
#
#     # decrementing k after each loop
#     k = k - 1
#
#     # inner loop to handle number of columns
#     # values changing acc. to outer loop
#     for j in range(0, i + 1):
#         #prinitng stars
#         print("* ", end="")
#
#         # ending line after each row
#     print("\r")
#


#k = rows-1

for i in range(rows, 0, -1):

    for j in range(0,rows-i):
        print(" ",end="")

    #k = k - 1

    for j in range(1, i+1):
        print(" *",end="")
    print()