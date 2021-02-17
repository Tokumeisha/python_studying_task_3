hosti = int(input())
while hosti != ():
    if (hosti > 50):
        print('restaurace')
    elif (hosti in range(20, 51)):
        print('kavárna')
    elif (hosti in range(1, 20)):
         print('dům')
    elif (hosti == 0):
        print('nejsou hosti')
    else:
        print('???')
    hosti = int(input())
