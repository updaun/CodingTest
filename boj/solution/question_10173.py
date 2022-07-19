import sys
input = sys.stdin.readline
while True:
    sentence = input().rstrip()
    if sentence == 'EOI':
        break
    if 'nemo' in sentence.lower():
        print("Found")
    else:
        print("Missing")