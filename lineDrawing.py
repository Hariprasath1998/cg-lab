

def DDA(startX= -50, startY=-50, endX=200, endY=200):
    diffX = abs(endX - startX)
    diffY = abs(endY - startY)
    if diffX > diffY:
        steps = diffX
    else:
        steps = diffY
    incX = diffX / steps
    incY = diffY / steps
    vertices = []
    x, y = startX, startY
    for i in range(steps + 1):
        vertices.append((round(x),round(y)))
        x = x + incX
        y = y + incY
    return vertices


def bresenhamLine(startX= -50, startY=-50, endX=200, endY=200):
    diffX = abs(endX - startX)
    diffY = abs(endY - startY)
    P = (2 * diffY) - diffX
    vertices = [(startX, startY)]
    while(vertices[-1][0] < endX):
        if P >= 0:
            P = P +(2*diffY) - (2*diffX)
            x =vertices[-1][0] + 1
            y =vertices[-1][1] + 1
        else:
            P = P +(2*diffY) - (2*diffX)
            x =vertices[-1][0] + 1
            y =vertices[-1][1]
        vertices.append((x,y))
    
    return vertices