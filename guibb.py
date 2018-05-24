import cv2
import argparse

def specify_bounding_box(img_path):
    rect = []
    def click_and_showBB(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            if len(rect) == 0:
                rect.append((x, y))
            elif len(rect) == 1:
                rect.append((x, y))
                _img = img.copy()
                cv2.rectangle(_img, rect[0], rect[1], (0, 255, 0), 2)
                cv2.imshow("image", _img)

        elif event == cv2.EVENT_MOUSEMOVE:
            if len(rect) == 1:
                _img = img.copy()
                cv2.rectangle(_img, rect[0], (x, y), (0, 255, 0), 2)
                cv2.imshow("image", _img)

    img = cv2.imread(img_path)
    bak = img.copy()
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", click_and_showBB)

    while True:
        cv2.imshow("image", img)
        key = cv2.waitKey()

        if key == ord('r'):
            rect = []
            img = bak.copy()
        elif key == ord('g'):
            break
    xmin = min(rect[0][0], rect[1][0])
    ymin = min(rect[0][1], rect[1][1])
    xmax = max(rect[0][0], rect[1][0])
    ymax = max(rect[0][1], rect[1][1])
    return (xmin, ymin), (xmax, ymax)

if __name__ == '__main__':
    parse = argparse.ArgumentParser()
    parse.add_argument('img', help="Path to image")
    args = parse.parse_args()
    print(specify_bounding_box(args.img))
