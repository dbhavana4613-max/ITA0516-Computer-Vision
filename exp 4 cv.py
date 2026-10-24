import cv2
def load_image(gray=False, title=""):
    return cv2.imread("image.jpg.png", 0 if gray else 1)

def choose_video(title=""):
    return "input.mp4"

img = load_image(gray=True)
equalized = cv2.equalizeHist(img)
cv2.imshow("Original", img)
cv2.imshow("Equalized", equalized)
cv2.waitKey(0)
cv2.destroyAllWindows()
