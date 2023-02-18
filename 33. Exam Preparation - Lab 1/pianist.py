pieces = int(input())

for x in range(initial_pieces):
    piece,composer,key = input().split('|')

command = input()

while True:
    if command == "Stop":
        break
     
