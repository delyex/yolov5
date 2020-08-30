# 图片转视频
import cv2
import os

im_dir = './inference/output'
vid_dir = 'output.mp4'

fps = 30
img_size = (960, 540)
# img_size = (640, 480)
fourcc = cv2.VideoWriter_fourcc(*'X264')
videoWriter = cv2.VideoWriter(vid_dir, fourcc, fps, img_size)
img_list = sorted(os.listdir(im_dir))
num = len(img_list)
# num = 1000
for i in range(num):
    # im_name = os.path.join(im_dir, str(i).zfill(6)+'.jpg')
    im_name = im_dir+'/'+img_list[i]
    frame = cv2.imread(im_name)
    videoWriter.write(frame)
    if i % 100 == 0:
        print(im_name, i, num)

videoWriter.release()
print('finish')
