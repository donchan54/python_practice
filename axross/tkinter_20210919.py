import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
from PIL import Image, ImageFilter

root = tk.Tk()
root.title("Image Sharper")
root.geometry("600x600")

#ラベル
label = tk.Label(root, text="画像の輪郭を検出するプログラムです。")
label.grid()

#画像の読み込みとフィルタの適用
def read_file(self):
    #ファイル拡張子
    fTyp = [("jpeg-file", "*.JPG"), ("All-file", "*")]
    #フォルダパスの取得
    iDir = os.path.abspath(os.path.dirname(__file__))
    messagebox.showinfo("対象の画像","ファイルを選択してください")
    file = filedialog.askopenfilename(filetypes = fTyp, initialdir = iDir)
    
    #ファイルパスの認識
    file_name = os.path.basename(file)
    
    #フィルタの適用
    img = Image.open(file_name)
    tmp = img.filter(ImageFilter.FIND_EDGES)
    tmp.save(file_name + '_EDGES.jpg')
    
    return "break"

#ボタン
Button = tk.Button(text="画像読み込み", width=50)
Button.bind("<Button-1>", read_file)#左クリック（<Button-1>）されると，read_file関数を呼び出す
Button.grid()

root.mainloop()