def floodFill(image, sr, sc, color): 
    def flood_rec(image,sr,sc,color,cy,cx):
        
        if not 0 <= cy < len(image) or not 0 <= cx < len(image[0]):
            return image
        if sr - cy == 0 and sc - cx == 0:
            if image[cy][cx] != color:
                image[cy][cx] = color
        if (sr - cy) + (sc - cx) < 4 and (sr - cy > 0 or sc - cx > 0):
            if image[cy][cx] != color:
                image[cy][cx] = color
        flood_rec(image,sr,sc,color,cy+1,cx)
        flood_rec(image,sr,sc,color,cy,cx+1)
        return image
    return flood_rec(image,sr,sc,color,0,0)

print(floodFill(image = [[0,0,0],[0,0,0]], sr = 1, sc = 1, color = 2)) #[[2,2,2],[2,2,0],[2,0,1]]