f = open("students.txt","r")
count = 0
#in is 250
#out is 500
totalTuition = 0.00

student = f.readline().strip("\n")



while student != "":
    count = count +1
    status = f.readline().strip("\n")
    credits = float(f.readline().strip("\n"))
    if status == "I":
        tuition = credits * 250
    else:
        tuition = credits*500
    totalTuition = totalTuition + tuition
    print()
    print(f"Name: {student}")
    print(f"credits taken: {credits}")
    print(f"tuition owed: ${tuition:,.2f}")
    student = f.readline().strip("\n")
    pass
print()
print(f"total tuition: ${totalTuition}")
print(f"number of students: {count}")