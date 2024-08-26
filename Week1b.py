import cv2 as cv
vid = cv.VideoCapture('Asgard.mp4')
if (vid.isOpened() == False):
    print("Error opening the video file")
else:
    fps = vid.get(5)
    print('Frames per second : ', fps,'FPS')
    frame_count = vid.get(7)
    print('Frame count : ', frame_count)
while(vid.isOpened()):
    ret, frame = vid.read()
    if ret:
        frame=cv.resize(frame,(500,300))
        cv.imshow('Frame',frame)
        key = cv.waitKey(20)
        if key == ord('q'):
            break
    else:
        break
vid.release()
cv.waitKey(20)
cv.destroyAllWindows()