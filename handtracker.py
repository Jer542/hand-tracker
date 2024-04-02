from cvzone.HandTrackingModule import HandDetector
import cv2 as cv

def process_hand(hand, detector):
    lmList = hand["lmList"]
    bbox = hand["bbox"] 
    centerPoint = hand['center']
    handType = hand["type"]  
    fingers = detector.fingersUp(hand)
    print(fingers)

def main():
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Error opening video capture")
        return

    detector = HandDetector(detectionCon=0.8, maxHands=2)
    while True:
        success, img = cap.read()
        if not success:
            print("Failed to read frame")
            break

        hands, img = detector.findHands(img)
        if hands:
            process_hand(hands[0], detector)
            if len(hands) == 2:
                process_hand(hands[1], detector)

        cv.imshow("Image", img)
        cv.waitKey(1)

if __name__ == "__main__":
    main()