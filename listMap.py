

mapX = 0
mapY = 0
positionBox = []
positionDoor = []
positionRock = []
positionPerson = []

def change_map(i):
    with open(str(i) + ".txt", "r") as ins:
        array = []
        for line in ins:
            array.append(line)
    global mapX, mapY, positionBox, positionDoor, positionRock, positionPerson
    mapY = len(array)

    mapX = 0
    for i in range(mapY):
        l = len(array[i])
        mapX = max(mapX, l)

    mapX = mapX - 1

    # print(mapX, mapY)
    positionDoor = []
    positionBox = []
    positionRock = []

    for i in range(mapY):
        l = len(array[i])
        for j in range(l - 1):
            if array[i][j] == ".":
                pD = [mapY - i, j]
                positionDoor.append(pD)

            if array[i][j] == "$":
                pB = [mapY - i, j]
                positionBox.append(pB)

            if array[i][j] == "#":
                pR = [mapY - i, j]
                positionRock.append(pR)

            if array[i][j] == "@":
                positionPerson = [mapY - i, j]


                # print(positionDoor)
# print(positionBox)
# print(positionRock)
# print(positionPerson)


    # for j in range(len(array[i])):
    #     if