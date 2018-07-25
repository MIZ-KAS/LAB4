score = float(input("Enter score: "))
pay = 50
if (score > 90):
    sum = pay + (score * 0.03)
else:
    sum = pay + (score * 0.01)
print sum