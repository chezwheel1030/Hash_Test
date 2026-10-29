from hash import Hash
from find import Find

Hash.size = input("Paste Hash: ")
print(Hash.size)

class Memory:
    mem = len(Hash.size)
    print(mem)

if Find.finding(32) or Find.finding(16):
    class Source: 
        source = input("Paste source code: ")