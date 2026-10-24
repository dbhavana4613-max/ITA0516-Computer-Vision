import cv2
def load_image(gray=False, title=""):
    return cv2.imread("image.jpg.png", 0 if gray else 1)

def choose_video(title=""):
    return "input.mp4"

import matplotlib.pyplot as plt
img = load_image()
colors = ("b", "g", "r")
for i, color in enumerate(colors):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=color)
plt.title("Color Histogram")
plt.xlabel("Pixel intensity")
plt.ylabel("Number of pixels")
plt.show()
