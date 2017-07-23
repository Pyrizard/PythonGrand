'''
Python based code developed by 👾 Pyrizard
Powered by SoloLearn 🌟
.............................................................................
Kindly upvote 👍 if u find this useful and drop a comment for any query 🙋 '''

from itertools import count

print("===========")
numbers = ['i', 'love', 'sololearn']
for num in numbers:
    print(num)

print("===========")
reverse = ['learning', 'of', 'fond', 'am', 'i']
for rev in reverse[::-1]:
    print(rev)

print("===========")
squares = [1, 2, 3, 4, 5, 6, 7, 8]
for sq in squares:
    print(sq ** 2)

print("===========")
for i in "Python":
    print(i)

print("===========")
for i in count(0):
    print(i)
    if i >= 5:
        break

print("===========")
for z in range(75, 80):
    print(z)

print("===========")
for k in range(-5, 5, 1):
    print(k)

print("===========")
g = 0
while g <= 10:
    print(g)
    g += 1