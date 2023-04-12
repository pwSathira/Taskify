import tkinter as tk


class ImageUtil:

    def createImage(scale_factor, url):
        original_image = tk.PhotoImage(file=url)
        scaled_image = original_image.subsample(scale_factor, scale_factor)
        return scaled_image

