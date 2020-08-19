with open('my_text.txt') as file:
    line = file.readlines()
content = ''
for line in lines:
    content += line

print(content)
