data = {1967: ['DavidBowie'],
        1969: ['SpaceOddity'],
        1970: ['TheManWhoSoldTheWorld'],
        1971: ['HunkyDory'],
        1972: ['TheRiseAndFallOfZiggyStardustAndTheSpidersFromMars'],
        1973: ['AladdinSane', 'PinUps'],
        1974: ['DiamondDogs'],
        1975: ['YoungAmericans'],
        1976: ['StationToStation'],
        1977: ['Low', 'Heroes'],
        1979: ['Lodger'],
        1980: ['ScaryMonstersAndSuperCreeps'],
        1983: ['LetsDance'],
        1984: ['Tonight'],
        1987: ['NeverLetMeDown'],
        1993: ['BlackTieWhiteNoise'], 
        1995: ['1.Outside'],
        1997: ['Earthling'],
        1999: ['Hours'],
        2002: ['Heathen'],
        2003: ['Reality'],
        2013: ['TheNextDay'],
        2016: ['BlackStar']}

import sys
input = sys.stdin.readline
for _ in range(int(input())):
    s, f = map(int, input().split())
    if s < 1967: s = 1967
    if f > 2016: f = 2016
    result = []
    for i in range(s, f+1):
        if i in data.keys():
            for target in data[i]:
                result.append(f"{i} {target}")
    print(len(result))
    if len(result) != 0:
        print("\n".join(result))

# 데이터 제작
# import sys
# input = sys.stdin.readline
# data = {}
# for i in range(int(input())):
#     t, n = input().split()
#     if int(t) in data.keys():
#         data[int(t)].append(n)
#     else:
#         data[int(t)] = [n]
# print(data)