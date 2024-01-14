#it can also be numbers and other variables (not only strings)
month_conversion = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May", 
    "Jun": "June",
    "Jul": "July",
    "Aug": "August", 
    "Sep": "September",
    "Oct": "October", 
    "Nov": "November",
    "Dec": "December",
}

#access a specific key or a value in two different ways
print(month_conversion["Nov"]) 
print(month_conversion.get("Liv"))