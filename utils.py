import skimage
import skimage.io
import skimage.transform
import numpy as np

synset = [l.strip() for l in open('synset.txt').readlines()]


def load_image(path):
    # load image
    img = skimage.io.imread(path)
    img = img / 255.0
    assert (0 <= img).all() and (img <= 1.0).all()

    # we crop image from center
    short_edge = min(img.shape[:2])
    yy = int((img.shape[0] - short_edge) / 2)
    xx = int((img.shape[1] - short_edge) / 2)
    crop_img = img[yy: yy + short_edge, xx: xx + short_edge]

    # resize to 224, 224
    resized_img = skimage.transform.resize(crop_img, (224, 224))
    return resized_img


# returns the top1 string
def print_prob(prob):
    pred = np.argsort(prob)[::-1]
    top5 = [synset[pred[i]] for i in range(5)]
    print("Top5: ", top5)

