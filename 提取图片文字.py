import pathlib
import xlwings as xw
import pandas as pd
import easyocr

#显示所有列
pd.set_option('display.max_rows', None)
#显示所有列
pd.set_option('display.max_columns', None)

#封装ocr函数
def read_text(path):
    #实例化Reader对象
    ocr = easyocr.Reader(['ch_sim', 'en'], gpu=True)
    #调用reader的readtext方法提取图片文字信息
    text = ocr.readtext(path)
    #将提取到的图片信息格式
    df = pd.DataFrame(text)
    return df[[1, 2]]

if __name__ == '__main__':

    df = read_text(r'./data/MVIMG_20230512_152630.JPG')
    print(df)