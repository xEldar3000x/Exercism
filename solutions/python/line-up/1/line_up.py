def line_up(name, number):
    exceptions = ("11", "12", "13")
    if str(number) in exceptions or str(number)[-2::] in exceptions:
        ending = "th"
    elif str(number)[-1] == "1":
        ending = "st"
    elif str(number)[-1] == "2":
        ending = "nd"
    elif str(number)[-1] == "3":
        ending = "rd"
    else:
        ending = "th"
    print(str(number)[-2::])
    return f"{name}, you are the {number}{ending} customer we serve today. Thank you!"
