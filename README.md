# Video processing
Processing a video sample with Python and OpenCV library. <br>

The video file is a simple letters and digits factory. They are moving from top to bottom. <br>
Among them there are some good and some defected ones. <br>
After program starts the functons are detecting and describing a type of each shape, it category (good or bad) and its' color. <br>

In the end there is displaying final raport.

## Technologies
Project is created with:
* Python 3.11
* numpy library version: 1.24.1
* OpenCV library version: 4.7.0
* scikit-image
* seaborn

## First of all install requred libraries by runing:

* for Windows:
```
pip -r install requirements.txt
```

* for Linux:
```
pip3 install -r requirements.txt
```

## Program descripction

The captured video file is Video.avi in [video_processing](/video_processing/)

In [Video_processing.py](/video_processing/Video_processing.py) first of all I declared upper and lower [limits](https://www.rapidtables.com/convert/color/rgb-to-hsv.html) for each of detected color:

```
lower_pink = np.array([150,50,50])
upper_pink = np.array([180,255,255])

lower_green = np.array([240, 80, 80])
upper_green = np.array([255, 255, 255])

lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])
```

### Program process video in this order:
- Change color [space](https://docs.opencv.org/4.x/df/d9d/tutorial_py_colorspaces.html) from RGB to GRAY scale

    - Create Region Of Intrest (ROI)
    - Take a part of image from ROI for edges detection using [Canny](https://docs.opencv.org/4.x/da/d22/tutorial_py_canny.html) filter

- Find a contours in detected shape
- After shape was detected I'm changing a color [space](https://docs.opencv.org/4.x/df/d9d/tutorial_py_colorspaces.html) again from RGB to HSV:
```
hsv = cv2.cvtColor(shape_img, cv2.COLOR_BGR2HLS)
```
- Put a mask on detected shape
- Count non-zero (no black) pixels in spicified shape
- Categorising detected shape and displaying real-time data of it

#### Additionaly I added a two user actions:
* pausing a video by pressing 'space'
* closing a program, and displaying actual final raport by presing 'q'

#### Program display following windows:
* Frame - main video file: <br>
![](static/image.png)

* ROI and edges detected in it: <br>
![](static/image-1.png)

* Detected shape and it's edges: <br>
![](static/image-2.png)

* Actual state information: <br>
![](static/image-3.png)

* Final raport after video ends or ures press 'q': <br>
![](static/image-4.png) 

<br>

# Image processing

In directory [img_processing](/img_processing/) there are two Jupyter Notebook files:
* [Img_processing](/img_processing/Img_processing.ipynb)

* [PC_camera_use](/img_processing/PC_camera_use.ipynb)

In Img_processing there are shown some functionalities of OpenCV library such as:
* converting video file to another type
* display video in Jupyter Notebook
* reading metadata od a video file
* selecting specified frames and saving them as new files
* selecting multiple frames from a video
* detecting contours of shapes in image
* show hierarhy of shapes in image

In the same directory there is also folder [Excercises](/img_processing/Excercises/) wherein there are Jupyter notebook files witch practical excersices helping in better understanding images processing.

# Directory tree:
```
Video_processing
├─ img_processing
│  ├─ Excercises
│  │  ├─ Ex_1.ipynb
│  │  ├─ Ex_2.ipynb
│  │  ├─ Ex_3.ipynb
│  │  ├─ Ex_4.ipynb
│  │  └─ images
│  │     ├─ airport.png
│  │     ├─ baboon.jpg
│  │     ├─ blob.jpg
│  │     ├─ calc.png
│  │     ├─ cube.bmp
│  │     ├─ dowels.png
│  │     ├─ kodim01.png
│  │     ├─ kodim03.png
│  │     ├─ kodim21.png
│  │     ├─ kodim23.png
│  │     ├─ lena.png
│  │     ├─ moon.png
│  │     ├─ obj.png
│  │     ├─ rice.tif
│  │     ├─ rose.png
│  │     ├─ rtg.tif
│  │     └─ tire.tif
│  ├─ frame_12_bw.png
│  ├─ frame_12_color.png
│  ├─ frame_12_contour.png
│  ├─ frame_185_bw.png
│  ├─ frame_185_color.png
│  ├─ frame_185_contour.png
│  ├─ frame_25_bw.png
│  ├─ frame_25_color.png
│  ├─ frame_25_contour.png
│  ├─ Img_processing.ipynb
│  ├─ PC_camera_use.ipynb
│  └─ Video.mp4
├─ LICENSE
├─ README.md
├─ requirements.txt
├─ static
│  ├─ image-1.png
│  ├─ image-2.png
│  ├─ image-3.png
│  ├─ image-4.png
│  └─ image.png
└─ video_processing
   ├─ Video.avi
   ├─ Video_processing.ipynb
   └─ Video_processing.py

```