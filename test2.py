# 虚拟环境：py36_photowall_env


import math
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import os
import time

# x = np.linspace(-2, 2, 100)
# fx = np.sqrt(2*np.abs(x)-x**2)
# gx = -2.14*np.sqrt(np.sqrt(2)-np.sqrt(np.abs(x)))
#
# fx = (fx+2.5)*7
# gx = (gx+2.5)*7
# fig = plt.figure()
# plt.axis("off")
# plt.fill_between(x, gx, fx, color="black")
# fig.savefig("t.jpg");


im = Image.open("t.jpg").convert("1")

data = ~np.array(im)
print("去除前：")
print(Image.fromarray(data))
ys, xs = np.where(data)
data = data[min(ys):max(ys) + 1, min(xs):max(xs) + 1]
print("去除后：")
print(Image.fromarray(data))

im = Image.fromarray(data).resize((60, 40), Image.ANTIALIAS)
data = np.array(im)
h, w = data.shape
print(f"共需{data.sum()}张图片，宽{w}张，高{h}张")


def create_picture_wall(data, imgs, size=50):
    h, w = data.shape
    random_imgs = iter(np.random.choice(imgs, size=data.sum()))

    new_img = Image.new('RGB', (size * w, size * h), "white")
    for y, x in zip(*np.where(data)):
        img_name = next(random_imgs)
        src_img = Image.open(f'{img_path}/{img_name}')
        src_img = src_img.resize((size, size), Image.ANTIALIAS)
        # 将图片复制到 new_image
        new_img.paste(src_img, (x * size, y * size))
    return new_img


img_path = r"D:\python-workspace\photowall\HDHeadImage"

if __name__ == '__main__':
    img = create_picture_wall(data, os.listdir(img_path))
    time = time.time()
    img.save("./images/{}-{}.jpg".format("heart", time))
    img.show()
