
# "r" - only read the file; 
# "w" - write in the file/modify it; 
# "a" - add new information
# "r+" - read and write

employee_file = open("employee.txt", "r") 

print(employee_file.readline()) #prints only one line
print(employee_file.readlines()) #prints all lines

for employee in employee_file.readlines():
    print(employee)

employee_file.close()

