from PIL import Image
import numpy as np
import pandas as pd


# filepathで指定した画像ファイルを読み込み，その画像のrgb値の平均をNumpyのArray(行ベクトル)で返す関数
def ext_mean_rgb(filepath):
    image = np.array(Image.open(filepath).convert("RGB")).reshape(-1,3)
    
    return np.array([np.mean(image[:,0]), np.mean(image[:,1]), np.mean(image[:,2])])

# 画像のファイルパスを指定すると，画像のrgb値の平均をファイルパスとともに，`metadata.csv`に追記する関数
def metadata_rgb_write(filepath):
    rgb = ext_mean_rgb(filepath)
    
    f = open('media/data/metadata_rgb.csv', 'a+')
    f.write(filepath+','+str(rgb[0])+','+str(rgb[1])+','+str(rgb[2])+'\n')
    f.close()
    
    df = pd.read_csv('media/data/metadata_rgb.csv', header=None)
    
    return df