s = "1111 1 1011 1011 000  100 000 101 1011 011"
a= s.split(" ") 
n = len(a)
bin = {
    "A":"10",
    "B":"0111",
    "C":"0101",
    "D":"011",
    "E": "1",
    "F": "1101",
    "G":"001",
    "H":"1111",
    "I":"11",
    "J":"1000",
    "K":"010",
    "L":"1011",
    "M":"00",
    "N":"01",
    "O":"000",
    "P":"1001",
    "Q":"0010",
    "R":'101',
    "S":"111",
    "T":"0",
    "U":"110",
    "V":"1110",
    "W":"100",
    "X":"0110",
    "Y":"0100",
    "Z":"0011",

    " ":"",
    "  ":" "
}
def EsoremCode(a):
    for i in range(n):
        for k, v in bin.items():
            if (v == a[i]):
                print(k, end="")
        
EsoremCode(a)

# ----------------------------------------- Morse Code to Binary to Esorem Code

# mc = {
#     "A":".-",
#     "B":"-...",
#     "C":"-.-.",
#     "D":"-..",
#     "E": ".",
#     "F": "..-.",
#     "G":"--.",
#     "H":"....",
#     "I":"..",
#     "J":".---",
#     "K":"-.-",
#     "L":".-..",
#     "M":"--",
#     "N":"-.",
#     "O":"---",
#     "P":".--.",
#     "Q":"--.-",
#     "R":'.-.',
#     "S":"...",
#     "T":"-",
#     "U":"..-",
#     "V":"...-",
#     "W":".--",
#     "X":"-..-",
#     "Y":"-.--",
#     "Z":"--..",
# }

# ms = ".... . .-.. .-.. ---  .-- --- .-. .-.. -.."
# mn = len(ms)
# ns = ""
# for i in range (mn):
#     if ms[i] == ".":
#         ns += "1"
#     elif ms[i] == "-":
#         ns += "0"
#     elif ms[i] == " ":
#         ns += " "
# EsoremCode (ns.split(" "))