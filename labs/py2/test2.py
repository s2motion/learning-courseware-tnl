items = ["1", "7", "10", "2", "-1", "-20"]

print(max(items))
print(max(items, key=int))
print(max(items, key=abs(str)))

