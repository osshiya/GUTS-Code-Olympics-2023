import re

hourlib = {
    "0" : "zero",
    "1" : "zero one",
    "2" : "zero two",
    "3" : "zero three",
    "4" : "zero four",
    "5" : "zero five",
    "6" : "zero six",
    "7" : "zero seven",
    "8" : "zero eight",
    "9" : "zero nine",
    "10" : "ten",
    "11" : "eleven",
    "12" : "twelve",
    "13" : "thirteen",
    "14" : "fourteen",
    "15" : "fifteen",
    "16" : "sixteen",
    "17" : "seventeen",
    "18" : "eighteen",
    "19" : "nineteen",
    "20" : "twenty",
    "21" : "twenty-one",
    "22" : "twenty-two",
    "23" : "twenty-three",
}

tenminlib = {
    "0" : "zero",
    "1" : "ten",
    "2" : "twenty",
    "3" : "thirty",
    "4" : "fourty",
    "5" : "fifty"
}

minlib= {
    "0" : "",
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
    "9" : "nine"
}

# time = input()

s = "6:00PM"

s = re.split('(\d+)', s)
print(s)

ans = ""

if s[-1] == "AM":
    if s[1] in hourlib:
        ans += hourlib.get(s[1]) + " "
elif s[-1] == "PM":
    hour = int(s[1])
    hour += 12
    if str(hour) in hourlib:
        ans += hourlib.get(str(hour)) + " "

if len(s) > 3:
    if s[3] == "00":
        ans += "hundred hours"
    else:
        min = [*s[3]]
        if min[0] in tenminlib:
            ans += tenminlib.get(str(min[0])) + " "
            if min[1] in minlib:
                ans += minlib.get(str(min[1])) + " "
            else:
                ans += " hundred hours"

print(ans)
# elif s[3] == "PM":
#     s[1] += 12