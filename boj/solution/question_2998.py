import sys
input = sys.stdin.readline
bin = input().rstrip()
bin2oct = {
    '000':'0',
    '001':'1',
    '010':'2',
    '011':'3',
    '100':'4',
    '101':'5',
    '110':'6',
    '111':'7',
}
while len(bin) % 3 != 0:
    bin = "0" + bin
result = ''
for i in range(0, len(bin), 3):
    result += bin2oct[bin[i:i+3]]
print(result)
