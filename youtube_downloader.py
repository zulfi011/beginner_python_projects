import tkinter as tk
from pytube import YouTube
from tkinter import filedialog

def video_downloader(url, path):
    try:
        yt = YouTube(url)
        print("Making things ready")
        stream = yt.streams.filter(progressive=True, file_extension="mp4")
        high_res = stream.get_highest_resolution()
        print("downloading!!!")
        high_res.download(output_path=path)
        print("downloaded successfully!!!")
    except Exception as e:
        print('error',e)

def file_dict():
    dic = filedialog.askdirectory()
    if dic:
        print(f'file saved at {dic}')
    return dic

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    url = input('input the url: ')
    save_address = file_dict()
    if save_address:
        video_downloader(url, save_address)
    else:
        print('not a valid address')