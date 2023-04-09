import cv2

def show_hal():
    import cv2
    # read image 
    image = cv2.imread('hal.png')
    # show the image, provide window name first
    cv2.imshow('HAL 9000', image)
    # add wait key. window waits until user presses a key
    cv2.waitKey(0)

if __name__ == "__main__":
    show_hal()
