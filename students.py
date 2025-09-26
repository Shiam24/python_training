n = int(input("How many students? "))

students = {}

for i in range(n):
    name = input(f"Enter the Name of Student {i+1}: ")
    mark = int(input(f"Enter the Mark of {name}: "))
    students[name] = mark

print("Student list (name → mark):", students)
