import sys

ladder = int(sys.argv[1])

for i in range(ladder):
    print(' '*(ladder-(i+1))+'#'*(i+1))
