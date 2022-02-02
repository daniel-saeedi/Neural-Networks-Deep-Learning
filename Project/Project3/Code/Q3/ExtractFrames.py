import cv2
vidcap = cv2.VideoCapture('DragonBall.mkv')
success,image = vidcap.read()
count = 0
frame_count = 0
while success:
    if count%200 == 0:
        if frame_count <= 90:
            cv2.imwrite("frames/train/frame%d.jpg" % frame_count, image)     # save frame as JPEG file
        else:
            cv2.imwrite("frames/test/frame%d.jpg" % frame_count, image)     # save frame as JPEG file
        frame_count += 1
    success,image = vidcap.read()
    count += 1

    if frame_count >= 121:
        break