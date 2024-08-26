#Remainder division
prompt = ("Enter number of students: ")
secondprompt = ("Enter number of apples: ")

students = input(prompt)
apples = input(secondprompt)

numofapples = (float(apples) / float(students))
remainder = (float(apples) // float(students))

print(numofapples)
print(remainder)