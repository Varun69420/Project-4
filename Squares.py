print("Enter the marks obtained in 4 subjects:")
math = int(input("Maths:"))
eng= int(input("English:"))
sci = int(input("Science:"))
fre = int(input("French:"))
sum = math+eng+sci+fre
print("sum of all 4 subjects is:",sum)
perc = (sum/400)
print(end="Percentage of Total of 4 subjects=")
print(perc)