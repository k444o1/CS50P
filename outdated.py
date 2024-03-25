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
        if "," in date: #"September 8, 1636" format
            m, d, y = date.replace(",", "").split(" ")
            if m in list:
                month = list.index(m) + 1
            if 1 <= int(d) <= 31:
                print(f"{y}-{month:02}-{int(d):02}")
                break
        else: #"9/8/1636" format
            m, d, y = date.split("/")
            if 1 <= int(d) <= 31 and 1<= int(m) <= 12:
                print(f"{y}-{int(m):02}-{int(d):02}")
                break
    except ValueError: #if format of input is invalid
        pass
    except NameError: #if month inputted is not in list, month becomes undefined
        pass