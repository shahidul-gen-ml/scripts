from PIL import Image

# load video
vid = Image.open(
    '/home/shahidul/Desktop/scripts/video/REC_CS_S2996_U4_20230105_1672893018366.mp4'
)

# cut the video to the desired time and save as new video
start_time = 2.143
end_time = 3.642

start_frame = int(start_time * vid.info['fps'])
end_frame = int(end_time * vid.info['fps'])

vid.seek(start_frame)
vid.save(
    '/home/shahidul/Desktop/scripts/video/REC_CS_S2996_U4_20230105_1672893018366a_cut.mp4',
    save_all=True,
    append_images=[vid.seek(i) for i in range(start_frame, end_frame)])


