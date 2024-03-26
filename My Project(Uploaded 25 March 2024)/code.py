import csv
import datetime
from statistics import multimode

class Record:
    def __init__(self, year, file_name):
        self.year = year
        self.file_name = file_name

    def salary(self, month, aftcpf = False):
        list = []
        with open(self.file_name) as file:
            reader = csv.DictReader(file)
            for row in reader:
                if int(row["month"]) == month:
                    list.append((float(row["to"]) - float(row["from"]) - float(row["break"])) * 10.5)
            salary = sum(list)
            if aftcpf:
                if 50 < salary <= 500:
                    return f"{salary:.2f}, CPF contribution: {(salary * 17/100):.2f}"
                elif 500 < salary <= 750:
                    return f"{(salary * 99.4/100):.2f}, CPF contribution: {(salary * 17.6/100):.2f}"
                elif salary > 750:
                    return f"{(salary * 80/100):.2f}, CPF contribution: {(salary * 37/100):.2f}"
                else:
                    return f"{salary:.2f}, CPF contribution: NIL"
            else:
                return f"{salary:.2f}"

    def highest_month(self):
        list = []
        calendar = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"]
        for i in range(1, 4): #data is only available for January to March
            list.append(float(Record.salary(self, i)))
        return f"{calendar[list.index(max(list))]}, Base: {max(list):.2f}"


    def lowest_month(self):
        list = []
        calendar = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"]
        for i in range(1, 4): #data is only available for January to March
            list.append(float(Record.salary(self, i)))
        return f"{calendar[list.index(min(list))]}, Base: {min(list):.2f}"


    def mode_day(self, month):
        list = []
        with open(self.file_name) as file:
            reader = csv.DictReader(file)
            for row in reader:
                if int(row["month"]) == month:
                    day = datetime.datetime(self.year, int(row["month"]), int(row["day"])).strftime("%A")
                    list.append(day)
            return multimode(list)
