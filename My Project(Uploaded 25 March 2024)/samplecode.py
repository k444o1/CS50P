from code import Record
record = Record(2024, "2024.csv") #Year, File name or path e.g. r"C:\Users\Olivia Ko\OneDrive\Pictures\Downloads\2024.csv"
print(record.salary(2)) #Base salary in February
print(record.salary(2, aftcpf=True)) #Salary in February after CPF deduction, shows CPF contribution
print(record.highest_month()) #Highest-earning month
print(record.mode_day(3)) #Mode working day in March