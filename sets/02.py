sets = {"dog","cat","hen"}

sets.add(input("enter a word: "))
sets.update([input("enter the second word:  ")])
print(len(sets))
sets.remove("dog")

sets.discard("cat")

print(sets)

sets2 = {"lion","tiger","cheater"}

sets2.add(input("enter an animal: "))
sets2.update([input("enter the second animal:  ")])
print(len(sets2))
sets2.remove("lion")

sets2.discard("tiger")

print(sets2)


sets3 = sets.union(sets2)
print(sets3)