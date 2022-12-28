# AI Personalised Gym Trainer

This is a project which captures your live video via webcam; on basis of 
which it detects body postures, locates the landmarks and calculates the angles 
between them and displays the same along with FPS (Frames Per Seconds).
The result of the detection will help one see how correctly one is doing 
its workouts.

## Installation
OS: Garuda Linux \
Platform: python3 
```bash
  sudo pacman -Syu  #update
  sudo pacman install python3
```
Library: OpenCv, mediapipe, Numpy
```bash
  sudo pacman -S python-pip
  python3 -m pip install opencv-python
  python3 -m pip install mediapipe
  python3 -m pip show numpy
```
## Screenshots

![App Screenshot](https://d3ftmvynp162pm.cloudfront.net/public/album_photo/9c/b2/04/bf7e25d797e2ca3ca3f6a82b7a90a59c.jpg)

## How to run it

- run it in ide of your choice (preferred on vscode)

- Once the code gets executed, it will automatically start detecting

- press `ESC` to quit the execution

## Process

### Capture original image

Live video will get captured using webcam:

```python
cap = cv2.VideoCapture(0)
```

### Posture Detector

Posture gets detected using `PoseModule.py`

class: `poseDetection`

`__intit__()` : All the self variables are declared
 and initialized to the aruments passed
  (if not passed then to a pre-denined value) 
  which will be needed to locate the landmarks and 
  illustrate that on the video captured.

`findPose()` :Takes up each frame of the captured video and gray scale it 
and processes the resultant frame. Returns the processed image. 

![App Screenshot](https://p0.piqsels.com/preview/903/501/154/grayscale-of-woman-carrying-dumbbell-thumbnail.jpg)

`findPosition()` :Takes the image(i.e. frame) and locates landmarks to each 
bodypart(specified in mediapipe). Returns list of all the landmarks' Positions.

![App Screenshot](https://editor.analyticsvidhya.com/uploads/33408human-pose-estimation-cover.jpg)

mediapipe landmarks

![App Screenshot](https://learnopencv.com/wp-content/uploads/2022/03/MediaPipe-pose-BlazePose-Topology.jpg)

`findAngle()` :takes up the imag and the elements of landmarks' list. Calculates 
the angle between the specifies points(i.e. positions given as in arguments) and 
specifies the point onto which it calculates the angle. And thus, returns the angle.

## Run Locally

Clone the project

```bash
  git clone https://github.com/TanishkaKumari/Finger-Counter
```

Go to the project directory

```bash
  cd CountFingers
```

Install dependencies

Start the server

```bash
  npm run start
```
