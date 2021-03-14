from time import sleep
values = []


def setup():
    # fullScreen()
    size(500,400)
    global values
    values = [i for i in range(width+1)]
    for i in range(len(values)):
        values[i] = random(height)
        # noise(i/100.0)*height
        
i = 0
j = 0

def draw():
    background(0)
    global values,i,j
    if i < len(values)-1:
        # for j in range(len(values)):
        #     while values[j-1] > values[j] and j > 0:    
        #         values[j-1], values[j] = values[j], values[j-1]
        for j in range(len(values)-1):
            if values[j] > values[j+1]:
                values[j], values[j+1] = values[j+1], values[j]
        i += 1
        print(j,i)
    if i >= len(values)-1:
        noLoop()
        print("break")
        # print(values)        
    for x in range(len(values)):
        stroke(255)
        line(x, height, x, height-values[x])
   
