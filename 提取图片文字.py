import pathlib
import xlwings as xw
import pandas as pd
import easyocr
import os

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
    return df[[1]]

#获取指定文件夹的所有文件名
def filedir(path):

    f_list = os.listdir(path)

    return f_list


if __name__ == '__main__':

    path_f = r'./data'
    files = filedir(path_f)

    df = read_text(r'./data/' + files[0])
    print(df[8,1])
    # with xw.App() as app:
    #     books = app.books.add()
    #     for file in files:
    #         df = read_text(file)



