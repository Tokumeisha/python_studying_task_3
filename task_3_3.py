line = input()
while line != ():
    if len(line) > 10:
        print(line + '!!!')
    else:
        line = list(line)
        print(line[1])
    line = input()
        
