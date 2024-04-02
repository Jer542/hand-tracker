# Hand Tracker

This Python script uses the `cvzone` library to detect and process hands in a video stream. 

## Dependencies

- cvzone
- OpenCV

You can install these packages using pip:

```bash
pip install cvzone opencv-python
```

## How it works

The script first imports the necessary modules and defines a function `process_hand` that takes a hand object and a detector object as arguments. It extracts various properties of the hand such as landmark list (`lmList`), bounding box (`bbox`), center point (`center`), hand type (`type`), and the state of the fingers (whether they are up or down). It then prints the state of the fingers.

The `main` function starts by initializing a video capture object with the default camera (camera index 0). If the video capture fails to open, it prints an error message and returns.

A `HandDetector` object is then created with a detection confidence of 0.8 and a maximum of 2 hands to be detected.

In an infinite loop, the script reads frames from the video capture, detects hands in the frame, and processes each detected hand using the `process_hand` function. If no frame can be read (which usually means the end of the video stream), it prints an error message and breaks the loop.

Finally, the processed image is displayed in a window named "Image". The `cv.waitKey(1)` call ensures that the script doesn't end abruptly and allows the window to be closed properly.

## Running the script

You can run the script using Python 3:

```bash
python handtracker.py
```

Please note that this script uses the webcam of your machine for video capture.
