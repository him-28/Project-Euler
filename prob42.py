def triangle_numbers(n):
    result = [x * (x + 1) / 2 for x in xrange(1, n + 1)]
    return result


letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
values = dict(zip(letters, range(1, 27)))

result = []
with open("words.txt") as text:
    for data in text:
        data = data.split(",")
        for word in data:
            total = []
            for char in word:
                if char.isalpha():
                    total.append(values[char])
            result.append(sum(total))

count = 0
for number in result:
    if number in triangle_numbers(25):
        count += 1
print count
