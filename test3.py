# 虚拟环境：py36_photowall_env


from PIL import Image
import requests
import numpy as np
from io import BytesIO
import os
import time


def get_mask_data(im, size=50):
    width, height = im.size
    if width > height:
        height = height * size // width
        width = size
    else:
        width = width * size // height
        height = size
    im = im.resize((width, height), Image.ANTIALIAS)
    return np.array(im) > 0


def create_picture_wall(data, img_path, size=50):
    h, w = data.shape
    imgs = os.listdir(img_path)
    random_imgs = iter(np.random.choice(imgs, size=data.sum()))
    new_img = Image.new('RGB', (size * w, size * h), "white")
    for y, x in zip(*np.where(data)):
        img_name = next(random_imgs)
        src_img = Image.open(f'{img_path}/{img_name}')
        src_img = src_img.resize((size, size), Image.ANTIALIAS)
        new_img.paste(src_img, (x * size, y * size))
    return new_img


def download_img(url):
    r = requests.get(url)
    return Image.open(BytesIO(r.content))


url = "https://staticc.ywordle.com/static/2020-11-03/f18f814d52768eb29111c0be52b14ca2_preview.png"

if __name__ == '__main__':
    im = download_img(url)
    data = get_mask_data(im)
    img = create_picture_wall(data, r"D:\python-workspace\photowall\HDHeadImage")
    time = time.time()
    img.save("./images/{}-{}.jpg".format("cloud", time))
    img.show()
