import cv2
import numpy as np

# Read video file
cap = cv2.VideoCapture('OKNO_4.avi')

# declare var's
shape_detected = False
previous_x, previous_y = 0,0
counter = 0
good_8 = 0
bad_8 = 0
good_u = 0
bad_u = 0
area = 0
type = ''

# Specified boundries for colors pink, green and blue
lower_pink = np.array([150,50,50])
upper_pink = np.array([180,255,255])

lower_green = np.array([240, 80, 80])
upper_green = np.array([255, 255, 255])

lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])

# Areas of detected shapes - taken by experimental probes
marg = 1.0
upper_8 = 1099.5 
lower_8 = 1086.5
upper_8g = 830.0 + marg
lower_8g = 820.0 - marg
upper_8d = 1086.5
lower_8d = 1083.0

upper_u = 630.0 + marg
lower_u = 590.0 - marg
upper_ul = 1120.0 + marg
lower_ul = 1100.0 - marg
upper_up = 1065.0 + marg
lower_up = 1020.0 - marg    

while True:
    
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # change color space BGR -> GRAY
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Window size 
    height, width = gray.shape[:2]

    # ROI size
    roi_width = int(width)
    roi_height = int(height / 2)

    # Placing ROI in window
    roi_x = int((width - roi_width) / 2)
    roi_y = int((height - roi_height)/2)
    
    # Take img part from ROI
    roi = cv2.getRectSubPix(gray, (roi_width, roi_height), (roi_x + roi_width / 2, roi_y + roi_height / 1000))

    # Edge deteciot using Canny filter
    edges = cv2.Canny(roi, 50, 50)

    # Finding contours
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:

        # Calculating params for each detected contour
        area = cv2.contourArea(cnt)
        perimeter = cv2.arcLength(cnt, True)

        if area < 3000 and area > 400:
            # Fcn that return position upper left corner and sizes of detected contour
            (x, y, w, h) = cv2.boundingRect(cnt)
            
            # Check if next detected shape is in antother positon than previous one
            # Avoid repeated detection of the same shape
            if abs(previous_x - x) == 0 and abs(previous_y - y) != 0:
                shape_detected = False  
                continue

            previous_x, previous_y = x, y

            # Drawing rectange around detected shape - None by dafault,
            # can be changed for exaple green (0, 255, 0)
            contour = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 0), 0) 
        
            width, height = 200, 260

            # Display detected shape in new window
            shape_img = cv2.resize(frame[y:y+h, x:x+w], (width, height))

            # change color space BGR -> HSV
            hsv = cv2.cvtColor(shape_img, cv2.COLOR_BGR2HLS)

            pink_mask = cv2.inRange(hsv, lower_pink, upper_pink)
            green_mask = cv2.inRange(hsv, lower_green, upper_green)
            blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)

            # Countiing non zero (not black) pixels in mask
            pink_area = cv2.countNonZero(pink_mask)
            green_area = cv2.countNonZero(green_mask)
            blue_area = cv2.countNonZero(blue_mask)

            # Setting a color
            color = "pink" if pink_area > green_area and pink_area > blue_area else "celadon" if green_area == blue_area and blue_area == pink_area else "blue"

            # Which shape is displaying
            if (area >= lower_8 and area <= upper_8) or (area == 1084.5 and (perimeter < 149.0 and perimeter > 148.0)) or (area == 1086.0 and color == 'blue'):
                type = 'eight'
            elif (area >= lower_8g and area <= upper_8g) or (area >= lower_8d and area <= upper_8d) or (area == 1086.5 and color == 'blue') or (area == 1086.0 and color == 'pink'):
                type = 'bad eight' 
            elif area >= lower_u and area <= upper_u:
                type = 'u letter'
            elif (area >= lower_ul and area <= upper_ul) or (area >= lower_up and area <= upper_up):
                type = 'bad u letter'
            
            # Displaying edges of detected shape
            edges2 = cv2.Canny(shape_img, 50, 150)
            cv2.imshow("Edges", edges2)

            # New window for actual state
            cv2.namedWindow("Actual state", cv2.WINDOW_NORMAL)
            cv2.resizeWindow("Actual state", 700, 50)

            # New window for txt informations
            stan = np.zeros((50, 700, 3), dtype=np.uint8)

            if not shape_detected:                                                                                                      #         DORZUCIC ZLICZANIE KOLOROW
                counter += 1
                # Prints in console
                #print('Detected shape no. ' + str(counter) + " in color " + color + '. It is ' + type +'.')

                if type == 'eight':
                    good_8 += 1
                elif type == 'bad eight':
                    bad_8 += 1
                elif type == 'u letter':
                    good_u += 1
                elif type == 'bad u letter':
                    bad_u += 1

                shape_detected = True
            
            # Displaying new shape in resizing window
            cv2.imshow("Detected Shape", shape_img)

            # Display information about actual shape
            cv2.putText(stan, 'Detected shape no. ' + str(counter) + " in color " + color + '. It is ' + type +'.', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
            cv2.imshow("Actual state", stan)

    # Display .avi, edges and ROI vids
    cv2.imshow('Frame', frame)
    cv2.imshow('Edges in ROI', edges)
    cv2.imshow('ROI', roi)

    # Pausing video by clicking 'space', closing by clicking 'q'
    if cv2.waitKey(1) & 0xFF == ord(' '):      
            while True:
                key2 = cv2.waitKey(1)
                if key2 == ord(' '):      
                    break                       

    elif cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

# End raport
#print('Detected ' + str(counter) + ' shapes. \n' + 'Among them was: \n' + str(good_8) + ' good 8s,\n' + str(bad_8) + ' bad 8s,\n' + str(good_u) + ' good Us,\n' + str(bad_u) + ' bad Us.')

# New window for raport
cv2.namedWindow("Raport", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Raport", 300, 200)

end_img = np.zeros((200, 300, 3), dtype=np.uint8)

# Put text in window
cv2.putText(end_img, 'Detected ' + str(counter) + ' shapes.', (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
cv2.putText(end_img, 'Among them was: ', (30, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
cv2.putText(end_img, str(good_8) + ' good 8s,', (30, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
cv2.putText(end_img, str(bad_8) + ' bad 8s,', (30, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
cv2.putText(end_img, str(good_u) + ' good Us,', (30, 130), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
cv2.putText(end_img, str(bad_u) + ' bad Us.', (30, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

cap.release()
cv2.destroyAllWindows()

# Display end raport
cv2.imshow("Raport", end_img)

if cv2.waitKey(1) & 0xFF == ord('q') or cv2.waitKey(0):
    cv2.destroyAllWindows()

    