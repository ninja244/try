# def Tabl():
#     tabl = ""
#     for x in range (1,11):
#         for y in range (1, x+1):
#             tabl +=f"{x}*{y}\t"
#         tabl += "\n"
#         return tabl
# print(Tabl())
for i in range(1, 10):
        for j in range(1,10):
            print("{}*{}={}\t".format(j, i, j*i), end="")
        print()