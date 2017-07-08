from PIL import Image
from PIL import ImageEnhance
image = Image.open("test_pic.jpg")
image = ImageEnhance.Sharpness(image).enhance(5)# 图像增强
image = ImageEnhance.Contrast(image).enhance(1.3) #对比度增强
imgry = image.convert('L')  # 转化为灰度图
def get_binary_pic():
    threshold = 80
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    return table
table = get_binary_pic()
out = imgry.point(table, '1')
out.show()
