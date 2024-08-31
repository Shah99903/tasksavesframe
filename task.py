import cv2
import os

video_path = r'C:\Users\Jagdamb\Desktop\python\traffic_signs.mp4'
saved_dir = r'C:\Users\Jagdamb\Desktop\python\output'

if not os.path.exists(saved_dir):
    os.makedirs(saved_dir)
    
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print('Error: Could not open video.')
    exit()
    
frame_count = 0
    
while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    
    frame_filename = os.path.join(saved_dir, f'frame_{frame_count:02d}.jpg')
    cv2.imwrite(frame_filename, frame)
    
    print(f'Saved {frame_filename}')
    
    frame_count += 1
    
cap.release()
print("Frames saved to directory.")
