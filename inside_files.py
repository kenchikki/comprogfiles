linenum = int(input())
output = {'line': 0, 's': 0, 'c': 0, 'u': 0, 'o': 0}
with open('tweets2.txt', 'r') as file_obj:
    lines = file_obj.readlines()
    if 1 <= linenum <= len(lines):
        line = lines[linenum - 1].strip()
        words = line.split()
        counts = {'line': linenum, 's': 0, 'c': 0, 'u': 0}
        wordfreq = {}
        for word in words:
            word = word.strip(",.?!-\"\'()")
            if len(word) <= 3:
                counts['s'] += 1
            elif len(word) > 3:
                counts['c'] += 1

            if word in wordfreq:
                wordfreq[word] += 1
            else:
                wordfreq[word] = 1

        for word, freq in wordfreq.items():
            if freq == 1:
                counts['u'] += 1

        output.update(counts)
        output['o'] = len(words)

print(output)



