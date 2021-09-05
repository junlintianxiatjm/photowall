# 虚拟环境：py36_photowall_env


from PIL import Image, ImageFont, ImageDraw, ImageChops
import numpy as np
import os
import time

img_path = r"D:\python-workspace\photowall\HDHeadImage"


def create_text_img(text, size=30, fontname="msyhbd.ttc"):
    # 获取字体对象
    font = ImageFont.truetype(fontname, size)
    width = len(text) * size

    # 左上角对齐绘制文字
    im = Image.new(mode='RGBA', size=(width, size))
    draw = ImageDraw.Draw(im=im)
    w, h = draw.textsize(text, font)
    o1, o2 = font.getoffset(text)
    draw.text(xy=(-o1, -o2), text=text,
              fill="black", font=font)

    # 裁切文字多余空白
    bg = Image.new(mode='RGBA', size=im.size)
    bbox = ImageChops.difference(im, bg).getbbox()
    im = im.crop(bbox)
    text_img = Image.new(mode='L', size=im.size, color=255)
    text_img.paste(im, mask=im)
    return text_img


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


if __name__ == '__main__':
    print('PyCharm')
    im = create_text_img("西安欢迎您")
    img = create_picture_wall(np.array(im) != 255, os.listdir(img_path))
    time = time.time()
    img.save("./images/{}-{}.jpg".format("西安欢迎您", time))
    img.show()
