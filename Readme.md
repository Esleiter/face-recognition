# Face Recognition

## Overview

This Python script utilizes the `face_recognition` library along with OpenCV (`cv2`) to create a simple face recognition system. The system captures live video from a webcam, detects faces, and compares them with known faces stored in a specified directory. If a match is found, it displays the name of the recognized person on the video feed.

## Prerequisites

Make sure you have the following libraries installed before running the script:

- `face_recognition`
- `opencv-python`

You can install them using the following:

```bash
pip install face_recognition opencv-python
```

## Directory Structure

Ensure that you have a directory containing face images for recognition. In this example, the directory is set to "./data/faces/". The images in this directory should be in JPG or PNG format.

## Usage

1. Clone the repository or download the script.
2. Install the required libraries mentioned in the "Prerequisites" section.
3. Place your face images in the specified directory (default is "./data/faces/").
4. Run the script.

```bash
python main.py
```

5. The script will access the webcam, detect faces, compare them with known faces, and display the result on the video feed.

## Controls

- Press 'q' to quit the application.

## Script Explanation

1. **Loading Known Faces:**

   - The script loads face images from the specified directory.
   - It extracts face encodings using the `face_recognition` library.

2. **Live Video Capture:**

   - The script captures live video from the default webcam (or specified camera index).

3. **Face Detection and Recognition:**

   - Face locations and encodings are obtained from each frame.
   - The script compares the detected face encodings with the known face encodings.
   - If a match is found, it displays the name of the recognized person on the video feed.

4. **Display and User Interaction:**
   - The script displays the video feed with rectangles around detected faces and the corresponding names.
   - Press 'q' to exit the application.

## Notes

- Make sure to have a well-lit environment for better face recognition.
- The script uses the default camera (camera index 0). If you have multiple cameras, you may need to adjust the `cv2.VideoCapture()` parameter.

Feel free to modify the script to suit your specific use case or integrate it into a larger project.
