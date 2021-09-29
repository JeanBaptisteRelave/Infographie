import matplotlib.pyplot as plt

plt_axis = [0, 100, 0, 100]
plt.axis(plt_axis)
plt.axis('off')

lSize = 2
lNb = 0
lSpace = 1
lColor = "blue"
lList = []

def getLPos(lettre):
    global lSpace
    global lNb
    
    posX = plt_axis[0] + lNb * (lSize + lSpace)
    
    print(posX)
    
    for i in range(0, len(lettre["x"])):
        lettre["x"][i] = lettre["x"][i] + posX
    
    lNb += 1
    
    return lettre

T = {
     "x" : [0, lSize, lSize, 2*lSize, 2*lSize, -lSize, -lSize, 0],
     "y" : [0, 0, 3*lSize, 3*lSize, 4*lSize, 4*lSize, 3*lSize, 3*lSize],        
     "w" : [1, 1, 1, 1, 1, 1, 1, 1]
}

lList.append(getLPos(T))
lList.append(getLPos(T))

print(lList)

plt.fill(lList[0]["x"], lList[0]["y"], lColor, lList[1]["x"], lList[1]["y"], lColor)
plt.show()

