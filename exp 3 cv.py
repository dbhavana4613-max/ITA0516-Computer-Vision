import cv2
def load_image(gray=False, title=""):
    return cv2.imread("image.jpg.png", 0 if gray else 1)

def choose_video(title=""):
    return "input.mp4"

img = load_image()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 200)
cv2.imshow("Canny Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
