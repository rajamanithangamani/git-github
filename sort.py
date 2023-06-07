#sorting for tuples and lists
students=(("siva","C",47),
          ("caviya","D",42),
          ("tarun","A",12),
          ("joshi","B",16))


age = lambda ages:ages[2]
#for tuple
sorted_students=sorted(students,key=age)

#this is for list
#students.sort(key=age,reverse=True)
for i in sorted_students:
    print(i)
