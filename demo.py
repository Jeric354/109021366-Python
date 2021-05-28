import sys
from PIL import Image, ImageFilter
#等比縮放
def resizeImg(imgName):                                               
    try:
        img = Image.open(imgName)
        print("Current size (width, height)", img.size)
        newWidth = int(input("new width: "))
        ratio = float(newWidth) / img.size[0]
        newHeight = int(img.size[1] * ratio)
        resizeImg = img.resize( (newWidth, newHeight), Image.BILINEAR)
        print("new image size: ", resizeImg.size)
        dotIndex = imgName.index(".")
        newImgName = imgName[:dotIndex] + "_resized" + imgName[dotIndex:]
        resizeImg.save(newImgName)
        print("Resizeed img is saved as", newImgName, "\n")
    except FileNotFoundError as fnfe:
        print(fnfe)
#圖片選轉
def rotateImg(imgName):
    try:
        img = Image.open(imgName)
        print("選轉: ")
        print("1. 左右翻轉")
        print("2. 上下翻轉")
        print("3. 翻轉90")
        print("4. 翻轉180")
        print("5. 翻轉270")
        print("6. other")
        op1 = input("進行的操作: ")
        if op1 == "1":
            newIm = img.transpose(Image.FLIP_LEFT_RIGHT)
            str1 = "_flip_LR "
        elif op1 == "2":
            newIm = img.transpose(Image.FLIP_TOP_BOTTOM)
            str1 = "_flip_TB "
        elif op1 == "3":
            newIm = img.transpose(Image.ROTATE_90)
            str1 = "_rotate_90 "
        elif op1 == "4":
            newIm = img.transpose(Image.ROTATE_180)
            str1 = "_rotate_180"
        elif op1 == "5":
            newIm = img.transpose(Image.ROTATE_270)
            str1 = "_rotate_270 "
        elif op1 == "6":
            rotDegree = float(input("Rotate degree: "))
            newIm = img.rotate(rotDegree)
            str1 = "_rotate_" + str(rotDegree) 
        dotIndex = imgName.index(".")
        newImgName = imgName[:dotIndex] + str1 + imgName[dotIndex:]
        newIm.save(newImgName)
        print("Rotated image is saved as", newImgName,"\n")
    except FileNotFoundError as fnfe:
        print(fnfe)
#產生縮圖
def genThumbnail(imgName):
    try:
        img = Image.open(imgName)
        print("Current size (width, height)", img.size)
        newWidth, newHeight = map(int, input("輸入縮圖尺寸: ").split())
        img.thumbnail((newWidth, newHeight))
        dotIndex = imgName.index(".")
        newImgName = imgName[:dotIndex] + "_thumbnail" + imgName[dotIndex:]
        img.save(newImgName)
        print("Thumbnail image is saved as ", newImgName, "\n")
    except FileNotFoundError as fnfe:
        print(fnfe)    

#濾鏡
def applyFilter(imgName):
    try:
        im = Image.open(imgName)
        print("濾鏡選擇: ")
        print("1. 模糊(BLUR)")
        print("2. 輪廓(CONTOUR)")
        print("3. 細節增強(DETAIL)")
        print("4. 邊緣增強(EDGE_ENHANCE)")
        print("5. 深度邊緣增強(EDGE_ENHANCE_MORE)")
        print("6. 浮雕效果(EMROSS)")
        print("7. 邊緣訊息(FIND_EDGES)")
        print("8. 平滑效果(SMOOTH)")
        print("9. 深度平滑效果(SMOOTH_MORE)")
        print("A. 銳利化效果(SHARPEN)")
        op1 = input("選擇套用濾鏡: ")
        if op1 == "1":
            newImg = im.filter(ImageFilter.BLUR)
            str1 = "_BLUR "
        elif op1 == "2":
            newImg = im.filter(ImageFilter.CONTOUR)
            str1 = "_CONTOUR "
        elif op1 == "3":
            newImg = im.filter(ImageFilter.DETAIL)
            str1 = "_DETALL "
        elif op1 == "4":
            newImg = im.filter(ImageFilter.EDGE_ENHANCE)
            str1 = "_EDGE_ENHANCE"
        elif op1 == "5":
            newImg = im.filter(ImageFilter.EDGE_ENHANCE_MORE)
            str1 = "_EDGE_ENHANCE_MORE "
        elif op1 == "6":
            newImg = im.filter(ImageFilter.EMBOSS)
            str1 = "_EMBOSS"
        elif op1 == "7":
            newImg = im.filter(ImageFilter.FIND_EDGES)
            str1 = "_FIND_EDGES"
        elif op1 == "8":
            newImg = im.filter(ImageFilter.SMOOTH)
            str1 = "_SMOOTH"
        elif op1 == "9":
            newImg = im.filter(ImageFilter.SMOOTH_MORE)
            str1 = "_SMOOTH_MORE "
        elif op1 == "A":
            newImg = im.filter(ImageFilter.SHARPEN)
            str1 = "_SHARPEN"
        dotIndex = imgName.index(".")
        newImgName = imgName[:dotIndex] + str1 + imgName[dotIndex:]
        newImg.save(newImgName)    
        print("Filtered image is saved as ", newImgName, "\n")
    except FileNotFoundError as fnfe:
        print(fnfe)
          

def showMenu():
    print("======================")
    print("1: 等比例縮放")
    print("2: 圖片旋轉")
    print("3: 產生縮圖")
    print("4: 套用濾鏡")
    print("0: 結束")

#利用while迴圈，讓使用者比較好辨識
if __name__ == "__main__":
    if len(sys.argv) > 1:
        while True:
            showMenu()
            op = input("選擇功能: ")
            if op == "1":
                resizeImg(sys.argv[1])
            elif op =="2":
                rotateImg(sys.argv[1])
            elif op =="3":
                genThumbnail(sys.argv[1])
            elif op =="4":
                applyFilter(sys.argv[1])
            elif op == "0":
                print("bye")
                break    
    else:
        print("argument error")    
