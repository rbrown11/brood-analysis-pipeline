import glob
import PySimpleGUI as sg
from PIL import Image, ImageTk
import os
import cv2
import numpy as np
import tkinter as tk
import pandas as pd

from threading import Thread


def parse_folder(path):
    images = glob.glob(f'{path}/*.jpg') + glob.glob(f'{path}/*.png')
    return images


def load_image(path, window):
    try:
        image = Image.open(path)
        image.thumbnail((1440, 810))
        photo_img = ImageTk.PhotoImage(image)
        window["image"].update(data=photo_img)
    except:
        print(f"Unable to open {path}!")


def main():
    elements = [
        [sg.Image(key="image")],
        [
            sg.Text("Image File"),
            sg.Input(size=(25, 1), enable_events=True, key="file"),
            sg.FolderBrowse(),
        ],
        [
            sg.Button("Prev"),
            sg.Button("Next"),
            sg.Button('Brood area'),
            sg.Button('export results')

        ]
    ]
    window = sg.Window("Image Viewer", elements, size=(1600, 1000))
    images = []
    location = 0
    resultsTable = pd.DataFrame(
        columns=['file_name', 'top_left_x', 'top_left_y', 'width', 'height'])
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "file":
            images = parse_folder(values["file"])
            if images:
                load_image(images[0], window)
        if event == "Next" and images:
            if location == len(images) - 1:
                location = 0
            else:
                location += 1
            load_image(images[location], window)
        if event == "Prev" and images:
            if location == 0:
                location = len(images) - 1
            else:
                location -= 1
            load_image(images[location], window)

        if event == "Brood area":
            fromCenter = False
            im = cv2.imread(images[location])
            file_name = os.path.basename(images[location])
            r = cv2.selectROI(im, fromCenter)
#            print(r)
            currentResults = pd.DataFrame({'file_name': file_name, 'top_left_x': [r[0]],
                                           'top_left_y': [r[1]], 'width': [r[2]], 'height': [r[3]]})
#            print(currentResults)
#            print(resultsTable)
            resultsTable = pd.concat(
                [currentResults, resultsTable.loc[:]]).reset_index(drop=True)
            print(resultsTable)

            cv2.waitKey(2500)

        if event == "export results":

            resultsTable.to_csv('brood_regions.csv', sep=",", index=False)

    window.close()


if __name__ == "__main__":
    main()
