# 1.напечатать сторку в одну линию - C:\WINDOWS\System32\drivers\etc\nst
# print("C:\WINDOWS\System32\drivers\etc\\nst")
# print(r"C:\WINDOWS\System32\drivers\etc\nst")



#2. Сортировка:
#  a = [4, 3, -10, 1, 7, 12]
# a=[4, -10, 12, 3, 1, 7]

a = [4, 3, -10, 1, 7, 12]
a.sort(key=lambda x: x%2)
print(a)