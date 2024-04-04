letter=input()
with open ('words.txt','r') as file_obj:
    lines=[]
    for line in file_obj.readlines():
        lines.append(line.strip())
    count+=0

    for line in lines:
        if len(line)>20:
            for char in line:
                if char==letter:
                    count+=1
    output={letter:count}
    print(output)