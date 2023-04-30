items = ["hallo", "welt", "wie", "geht", "es", "dir"]

sorted_l = sorted(items, key=len)

result = [item for item in sorted_l]

print(result)
# Output
# ['es', 'dir', 'wie', 'geht', 'welt', 'hallo']


numbers = "928349"

sorted_l = sorted(numbers, key=int)

result = [item for item in sorted_l]

print(result)
# Output
# ['2', '3', '4', '8', '9', '9']
