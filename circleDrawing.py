def circleDrawing(xOrigin=0, yOrigin=0, r=50):
    Vertices = []
    x = r
    y = 0
	
    Vertices.append((x + xOrigin,y + yOrigin))
    
    if (r > 0) :
        Vertices.append((x + xOrigin,-y + yOrigin))
        Vertices.append((y + xOrigin,x + yOrigin))
        Vertices.append((-y + xOrigin,x + yOrigin))

    P = 1 - r

    while x > y:

        y += 1
        
        if P <= 0:
            P = P + 2 * y + 1
        
        else:		
            x -= 1
            P = P + 2 * y - 2 * x + 1
        
        if (x < y):
            break
                
        Vertices.append((x + xOrigin,y + yOrigin))
        
        Vertices.append((-x + xOrigin,y + yOrigin))
        
        Vertices.append((x + xOrigin,-y + yOrigin))
        
        Vertices.append((-x + xOrigin,-y + yOrigin))
        
        if x != y:
            Vertices.append((y + xOrigin,x + yOrigin))
            
            Vertices.append((-y + xOrigin,x + yOrigin))
            
            Vertices.append((y + xOrigin,-x + yOrigin))
            
            Vertices.append((-y + xOrigin,-x + yOrigin))


    return Vertices
							
