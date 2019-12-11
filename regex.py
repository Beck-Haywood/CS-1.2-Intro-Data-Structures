import re
with open('corpus_simpsons.txt', 'r') as file:
        words = file.read()

result = re.match(r".*", words)
print(result)
print(result.group(0))

#Homer:(.*$)