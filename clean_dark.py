import cv2
import os
import numpy as np

# Threshold for what is considered dark
BRIGHTNESS_THRESHOLD = 10

def is_image_dark(image_path):
    # Load image using OpenCV
    image = cv2.imread(image_path)
    if image is None:
        return False  # Skip if the image can't be loaded

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Calculate the average brightness
    average_brightness = np.mean(gray)

    # Return True if the brightness is below the threshold
    return average_brightness < BRIGHTNESS_THRESHOLD

def process_images_folder(folder_path):
    dark_images = []
    
    # Loop through all files in the folder
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path) and file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            if is_image_dark(file_path):
                os.remove(file_path)  # Delete dark image
                dark_images.append(file_name)
    
    return dark_images

def process_videos_folder(folder_path):
    dark_videos = []
    
    # Loop through all files in the folder
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path) and file_name.lower().endswith(('.mp4', '.avi', '.mkv', '.mov')):
            if is_video_dark(file_path):
                os.remove(file_path)  # Delete dark video
                dark_videos.append(file_name)
    
    return dark_videos

def is_video_dark(video_path):
    # Open video using OpenCV
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        return False
    
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    dark_frames_count = 0
    frame_threshold = 0.5  # Proportion of dark frames to consider video dark

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Check brightness
        average_brightness = np.mean(gray)
        if average_brightness < BRIGHTNESS_THRESHOLD:
            dark_frames_count += 1

    cap.release()

    # Check if the proportion of dark frames exceeds the threshold
    return (dark_frames_count / total_frames) > frame_threshold

if __name__ == "__main__":
    # Paths to the folders
    images_folder = "/home/masamba/csvdata/images"
    videos_folder = "/home/masamba/csvdata/vids"
    
    dark_images = process_images_folder(images_folder)
    dark_videos = process_videos_folder(videos_folder)
    
    print("Deleted Dark Images:")
    print(f"Removed {len(dark_images)} images")