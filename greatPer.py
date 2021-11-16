# rows = int(input("Kindly enter digit for print Pyramid: "))

# k = rows +1
#
# for i in range(rows):
#     for j in range(k):
#         print(end=" ")
#
#     k = k-1
#     for j in range(i+1):
#         print("* ",end="")
#
#     print()
#
# for i in range(rows, 0, -1):
#     for j in range(0, rows - i):
#         print(end=" ")
#     for j in range(1, i+1):
#         print(" *",end="")
#     print()
#
#
#multiplicant = int(input("Kindly enter digit for print Pyramid: "))
# multiplier = int(input("Please enter digit for print Table: "))
#
# for i in range (1 , 11):
#      a = multiplier * i
#
#      print(multiplier, "x", i, "=", a)

#Marks = int(input("Please enter digit for print Table: "))
#
# with open("sample.txt", 'r') as my_file:
#     content = my_file.read()    # read() returns the content of file
#     #print("Reading file: ")
#     print(content)


f = open("sample.txt", "w")
#a = ["Hamza","CSE",24]
#multiplier = int(input("Please enter digit for print Table: "))
f = open("sample.txt", "w")
multiplier = 3
table= []
for i in range (1 , 11):
     z = multiplier, "x", i, "=", multiplier * i
     table.append(z)

f.write(str(table))
f.close()

f = open("sample.txt", "r")
f.read()