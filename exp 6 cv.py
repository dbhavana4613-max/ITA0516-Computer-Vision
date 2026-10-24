import cv2
def load_image(gray=False, title=""):
    return cv2.imread("image.jpg.png", 0 if gray else 1)

def choose_video(title=""):
    return "input.mp4"

img = load_image()
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
eroded = cv2.erode(img, kernel, iterations=1)
cv2.imshow("Eroded Image", eroded)
cv2.waitKey(0)
cv2.destroyAllWindows()
