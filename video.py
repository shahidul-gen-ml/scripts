# cv2 play video
import cv2

cap = cv2.VideoCapture(
    '/home/shahidul/Desktop/scripts/video/REC_CS_S2996_U4_20230105_1672893018366.mp4'
)

# cut the video to the desired time and save as new video

start_time = 2.143
end_time = 3.642
fps = cap.get(cv2.CAP_PROP_FPS)

start_frame = int(start_time * fps)
end_frame = int(end_time * fps)

cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(
    '/home/shahidul/Desktop/scripts/video/REC_CS_S2996_U4_20230105_1672893018366_cut.mp4',
    fourcc, fps, (int(cap.get(
        cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

for i in range(start_frame, end_frame):
    ret, frame = cap.read()
    if ret == True:
        out.write(frame)
    else:
        break

cap.release()
out.release()

cv2.destroyAllWindows()
