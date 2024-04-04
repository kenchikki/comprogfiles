linenum=int(input(""))
with open ('corpus.txt','r')as fin:
    for line in fin.readlines():
        lines.append(line.strip())
    chosen=lines[linenum-1]
    positive=['good','word']
    negative=['bad','suck']
    tally={'positive':0,
           'negative':0}
    for word in chosen.split():
        if word.lower()in positive:
            tally['positive'] += 1
        if word.lower()in negative:
            tally['negative'] += 1

    print(tally)