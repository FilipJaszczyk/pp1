import re

regex = r"MAT|GEO|HIS|INF|AST"

test_str = ("MAT Matematyka 45\n"
            "GEO Geografia 210\n"
            "HIS Historia 28\n"
            "INF Informatyka 196\n"
            "AST Astronomia 9")

matches = re.finditer(regex, test_str, re.MULTILINE)
print('Kody przedmiotów : ')
for matchNum, match in enumerate(matches, start=1):

    print("Match {matchNum} was found at {start}-{end}: {match}".format(
        matchNum=matchNum, start=match.start(), end=match.end(), match=match.group()))

    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        print("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=groupNum,
        start=match.start(groupNum), end=match.end(groupNum), group=match.group(groupNum)))
regex = r"Matematyka|Geografia|Historia|Informatyka|Astronomia"
matches = re.finditer(regex, test_str, re.MULTILINE)
print('Nazwy Przedmiotów')
for matchNum, match in enumerate(matches, start=1):

    print("Match {matchNum} was found at {start}-{end}: {match}".format(
        matchNum=matchNum, start=match.start(), end=match.end(), match=match.group()))

    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1

        print("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=groupNum,
        start=match.start(groupNum), end=match.end(groupNum), group=match.group(groupNum)))
regex = r"45|210|28|196|9"
matches = re.finditer(regex, test_str, re.MULTILINE)
print('Liczba uczestników: ')
for matchNum, match in enumerate(matches, start=1):

    print("Match {matchNum} was found at {start}-{end}: {match}".format(
        matchNum=matchNum, start=match.start(), end=match.end(), match=match.group()))

    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1

        print("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=groupNum,
        start=match.start(groupNum), end=match.end(groupNum), group=match.group(groupNum)))
        