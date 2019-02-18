import numpy as np
import cv2 as cv
import glob

SIZE = 224

def calculate_mse(img):
    image = cv.imread(img)

    generated = image[:, SIZE*1:SIZE*2].reshape(SIZE*SIZE*3, 1)
    original = image[:, SIZE*2:].reshape(SIZE*SIZE*3, 1)

    return (np.square(generated - original)).mean()

total_mse = 0.0
count = 0.0
for img in glob.glob("summary/test/images/*.png"):
    mse = calculate_mse(img)
    print('\t%s has MSE %.3f' % (img, mse))
    total_mse += mse
    count += 1

print('Average MSE: %.5f' % (total_mse / count))
