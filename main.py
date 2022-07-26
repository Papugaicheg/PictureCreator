import math
import os
import time

from PIL import Image


def check_avg_color(path):
    img = Image.open(path)
    check_img = Image.new('RGB', (250, 250), img.resize((1, 1)).getpixel((0, 0)))
    print(img.resize((1, 1)).getpixel((0, 0)))
    check_img.show()


def get_list_of_files(string):
    list_of_files = []
    for root, dirs, files in os.walk(string):
        for file in files:
            list_of_files.append(file)
    return list_of_files


def get_dict():
    photos = dict()
    for file in get_list_of_files('images/changed'):
        r, g, b = map(int, (file.replace('.jpg', '').replace('(', '').replace(')', '').replace(' ', '').split(',')))
        photos.setdefault(file, tuple((r, g, b)))

    return photos


def get_pixels():
    for file in get_list_of_files('images/changed'):
        print(f'images/changed/{file}')
        img = Image.open(f'images/changed/{file}')

        img = Image.new('RGB', (250, 250), avg_color(img))
        img.save(f'D:/PictureCreator/image/pixels/{avg_color(img)}.jpg')


def reformat_files():
    for file in get_list_of_files('images'):
        print(f'images/{file}')
        img = Image.open(f'images/{file}')
        w, h = img.size
        new = Image.new('RGB', (w, h))
        new.paste(img, (0, 0))
        new.save(f'D:/PictureCreator/images/changed/{avg_color(img)[0], avg_color(img)[1], avg_color(img)[2]}.jpg',
                 'JPEG')


def color_distance(e1, e2):
    r = abs(e1[0] - e2[0])
    g = abs(e1[1] - e2[1])
    b = abs(e1[2] - e2[2])
    return math.sqrt(r ** 2 + g ** 2 + b ** 2)


def create_collage(w, h):
    timer = time.time()
    img = Image.open('image/2.jpg')
    cord = (0, 0, 512, 512)
    img = img.crop(cord)
    img = img.resize((w, h))
    width, height = img.size
    new_img = Image.new('RGB', (w * 100, h * 100), 'black')
    dict_with_items = get_dict().items()

    for i in range(height):
        timerr = time.time()
        print('i = ', i, '   | Complete:', round(((i + 1) / w) * 100), '% | ', time.time() - timer, 'sec.')
        for j in range(width):
            minimal_dist = 999
            key = ''
            color = tuple(img.getpixel((i, j)))
            for keys, value in dict_with_items:
                dist = color_distance(color, value)
                if dist < 5:
                    key = keys
                    break
                if minimal_dist > dist:
                    minimal_dist = dist
                    key = keys

            img_put = Image.open(f'D:/PictureCreator/images/changed/{key}')
            new_img.paste(img_put.resize((100, 100)), (i * 100, j * 100))
        print('Время выполнения для ', i, '-той строки: ', time.time()-timerr)
    new_img.save('images/new.png')
    print(time.time() - timer)


def avg_color(img_get):
    return img_get.resize((1, 1)).getpixel((0, 0))


create_collage(60, 128, 128, 50)


