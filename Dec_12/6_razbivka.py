s = open("Dec_12/24-6.txt").readline()
# s = "ACDFOACFODCOACDOFCAFOCADOF"


s = s.replace("CA", "*").replace("CO", "*").replace("DA", "*").replace("DO", "*").replace("FA", "*").replace("FO", "*")
s = s.replace("A"," ").replace("C"," ").replace("D"," ").replace("F"," ").replace("O"," ")
# print(s[:200])

a = s.split()

print(len(max(a, key=len)))

