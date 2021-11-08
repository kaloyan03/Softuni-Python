text = input().split("|")
text.reverse()
print(' '.join([num for row in [i.split() for i in text] for num in row]))