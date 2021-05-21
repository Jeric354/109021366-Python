from PIL import Image, ImageDraw

newImg = Image.new('RGBA',(300, 300),"#778899")
drawObj = ImageDraw.Draw(newImg)
for i in range(100, 200, 3):
    for j in range(100, 200, 3):
        drawObj.point([i,j], fill="green")

drawObj.line([(3, 3), (296,3), (296, 296), (3, 296), (3, 3)], fill="#00ffff") 
for x in range(150, 300, 10):
   drawObj.line([(x, 0),(300, x-150)],fill="#0000ff") 
for x in range(0, 150, 10): 
    drawObj.line([(x, 0),(0, 150-x)],fill="#00ff00") 
for x in range(0, 150, 10):
    drawObj.line([(x, 300),(0, x+150)],fill="#ff0000")
for x in range(150, 300, 10):
    drawObj.line([(x,300),(300,450-x)], fill="#000000")    
 




newImg.save("testImg.png")


