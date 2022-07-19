import sys
crypto = {
    "D":"A",
    "E":"B",
    "F":"C",
    "G":"D",
    "H":"E",
    "I":"F",
    "J":"G",
    "K":"H",
    "L":"I",
    "M":"J",
    "N":"K",
    "O":"L",
    "P":"M",
    "Q":"N",
    "R":"O",
    "S":"P",
    "T":"Q",
    "U":"R",
    "V":"S",
    "W":"T",
    "X":"U",
    "Y":"V",
    "Z":"W",
    "A":"X",
    "B":"Y",
    "C":"Z",
}
result = ''
for s in sys.stdin.readline().rstrip():
    result += crypto[s]
print(result)