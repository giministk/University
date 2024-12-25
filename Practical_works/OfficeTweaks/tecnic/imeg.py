from PIL import Image


def compress_img(choice, images, compression):
    if int(compression) in range(1, 101):
        if int(choice) == 0:
            for i in list(images.values()):
                image_file = Image.open(i)
                image_file.save('compressed' + i, quality=int(compression))
                print(f'Изображение {i} сжато')
        else:
            if type(images) is dict:
                image = images.get(int(choice))
                image_file = Image.open(image)
                image_file.save('compressed' + image, quality=int(compression))
                print(f'Изображение {image} сжато')
            else:
                for i in images:
                    image_file = Image.open(i)
                    image_file.save('compressed' + i, quality=int(compression))
                    print(f'Изображение {i} сжато')
    else:
        print('Compression error!')