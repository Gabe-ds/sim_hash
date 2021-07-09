from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

def color_hist(filepath):
    image = np.asarray(Image.open(filepath).convert("RGB")).reshape(-1,3)
    plt.hist(image, color=["red", "green", "blue"], histtype="step", bins=128)
    plt.show()

def comp_sin(qvec, tvec):
    return np.dot(qvec, tvec) / (np.linalg.norm(qvec) * np.linalg.norm(tvec))

def average_hash(fname, size=256):
    # 前処理
    image_data = Image.open(fname).convert('L').resize((size, size), Image.ANTIALIAS)
    pixels = np.array(image_data.getdata()).reshape((size, size))
    average = pixels.mean()
    # 値を0, 1に変換
    out_pix = 1 * (pixels > average)
    
    return out_pix

def np2hash(get_ahash):
    hash_c = []
    
    for nl in get_ahash.tolist():
        for i in nl:
            hash1 = str(i)
        hash2 = "".join(hash1)
        # 整数に変換
        i = int(hash2, 2)
        hash_c.append("%04x" % i)
        
    return "".join(hash_c)