from PIL import Image
import numpy as np

start = 1
stop = 8

for index in range(start, stop+1):
    img_fname = r'G:\내 드라이브\Python_Project\Raspberry_Pico\ys_cartoon\ys_cartoon_0%d.jpg' % index
    img = Image.open(img_fname)
    #img.show()
    #print(img.size)

    (w, h) = img.size
    denominator_w = int(w / 128 * 100) / 100
    denominator_h = int(h / 64 * 100) / 100

    if denominator_w <= denominator_h:
        (new_w, new_h) = (w / denominator_h, h / denominator_h)
        print(new_w, new_h)
    else:
        (new_w, new_h) = (w / denominator_w, h / denominator_w)
        print(new_w, new_h)

    new_w, new_h = int(new_w), int(new_h)
    img_resized = img.resize((new_w, new_h))
    print(img_resized.size)
    #img_resized.show()

    img_black = img_resized.convert('1')
    img_black.show()
    #img_black.save('black.jpg')

    #img_array = np.array(img_resized)
    img_array = np.array(img_black)
    #img_array = np.sum(img_array, axis=2)
    #threshold = int(img_array.min())
    #one = img_array <= (threshold+200)
    #zero = img_array > (threshold+200)
    #img_array[zero] = 0
    #img_array[one] = 1
    #img_array = img_array + 1
    #img_array[img_array == 2] = 0
    row, col = img_array.shape

    w_default = 128
    h_default = 64

    if w_default > col:
        w_left = int((w_default - col)/2)
        w_right = w_default - col - w_left
        img_redundancy_left = np.zeros((h_default, w_left))
        img_redundancy_right = np.zeros((h_default, w_right))
        img_reshaped = np.concatenate((img_redundancy_left, img_array, img_redundancy_right), axis=1)
    else:
        h_upper = int((h_default - row) / 2)
        h_lower = h_default - h_upper - row
        img_redundancy_upper = np.zeros((h_upper, w_default))
        img_redundancy_lower = np.zeros((h_lower, w_default))
        img_reshaped = np.concatenate((img_redundancy_upper, img_array, img_redundancy_lower), axis=0)

    print(img_reshaped.shape)
    txt_fname = r'G:\내 드라이브\Python_Project\Raspberry_Pico\ys_cartoon\ys_cartoon_0%d.txt' % index
    np.savetxt(txt_fname, img_reshaped, fmt='%d')
