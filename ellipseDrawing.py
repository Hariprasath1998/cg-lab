def ellipseDrawing(xRadius=30, yRadius=45, xOrigin=0, yOrigin=0):
    Vertices = []
    x = 0
    y = yRadius
    
    d1 = ((yRadius * yRadius) - (xRadius * xRadius * yRadius) +
                    (0.25 * xRadius * xRadius))
    dx = 2 * yRadius * yRadius * x
    dy = 2 * xRadius * xRadius * y

    while (dx < dy):
        Vertices.append((x + xOrigin, y + yOrigin))
        Vertices.append((-x + xOrigin, y + yOrigin))
        Vertices.append((x + xOrigin, -y + yOrigin))
        Vertices.append((-x + xOrigin, -y + yOrigin))

        if (d1 < 0):
            x += 1
            dx = dx + (2 * yRadius * yRadius)
            d1 = d1 + dx + (yRadius * yRadius)
            
        else:
            x += 1
            y -= 1
            dx = dx + (2 * yRadius * yRadius)
            dy = dy - (2 * xRadius * xRadius)
            d1 = d1 + dx - dy + (yRadius * yRadius)

    d2 = (((yRadius * yRadius) * ((x + 0.5) * (x + 0.5))) +
        ((xRadius * xRadius) * ((y - 1) * (y - 1))) -
        (xRadius * xRadius * yRadius * yRadius))

    while (y >= 0):
        Vertices.append((x + xOrigin, y + yOrigin))
        Vertices.append((-x + xOrigin, y + yOrigin))
        Vertices.append((x + xOrigin, -y + yOrigin))
        Vertices.append((-x + xOrigin, -y + yOrigin))

        if (d2 > 0):
            y -= 1
            dy = dy - (2 * xRadius * xRadius)
            d2 = d2 + (xRadius * xRadius) - dy

        else:
            y -= 1
            x += 1
            dx = dx + (2 * yRadius * yRadius)
            dy = dy - (2 * xRadius * xRadius)
            d2 = d2 + dx - dy + (xRadius * xRadius)

    return Vertices