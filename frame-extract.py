import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

def extract_frames(video):
    cap = cv2.VideoCapture(video)
    folder_name = video.split('/')[-1].split('.')[0] # create a folder with same name as video file
    try:
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
    except OSError:
        print ('Folder {} already exists'.format(folder_name))

    currentFrame = 0
    video_frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    print('Total frames to be written: {}'.format(video_frame_count))
    success, frame = cap.read()
    while success:
    # Capture frame-by-frame
        name = '/pfs/out/{}/frame{}{}'.format(folder_name, str(currentFrame), '.jpg')
        print ('Creating...' + name)
        cv2.imwrite(name, frame)
        success, frame = cap.read()
        currentFrame += 1

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # walk /pfs/videos and call extract_frames on every file found
    for dirpath, dirs, files in os.walk("/pfs/videos"):
        for file in files:
            extract_frames(os.path.join(dirpath, file))
