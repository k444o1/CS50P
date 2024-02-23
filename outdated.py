while True:
    try:
        list = [
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
        date = input("Date: ")
        if "," in date:
            m, d, y = date.replace(",", "").split(" ")
            if m in list:
                month = list.index(m) + 1
            if 1 <= int(d) <= 31:
                print(f"{y}-{month:02}-{int(d):02}")
        else:
            m, d, y = date.split("/")
            if 1 <= int(d) <= 31 and 1<= int(m) <= 12:
                print(f"{y}-{int(m):02}-{int(d):02}")
    except ValueError: #if format of input is invalid
        pass
    except NameError: #if month inputted is not in list
        pass
