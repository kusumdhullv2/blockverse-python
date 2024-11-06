import cv2
import os

path = r"C:\kusum-python\classes\images"
output_video_path = r"C:\kusum-python\classes\video\video_van_images.mp4"
images = []
video_display = 1  # seconds per image

# Collect and sort image paths with valid extensions
for file in os.listdir(path):
    name, extension = os.path.splitext(file)
    if extension.lower() in ['.jpg', '.jpeg']:
        file_name = os.path.join(path, file)
        images.append(file_name)

images.sort()  # Sort images to maintain order

# Check if there are images to process
if images:
    # Read the first image to get dimensions
    frame = cv2.imread(images[0])
    if frame is None:
        raise ValueError("Could not read the first image. Check the image paths.")

    height, width, layers = frame.shape
    size = (width, height)  # Video size

    # Initialize video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for mp4 format
    video_writer = cv2.VideoWriter(output_video_path, fourcc, 1, size)

    # Add images to the video
    for image_path in images:
        img = cv2.imread(image_path)
        if img is None:
            print(f"Warning: Could not read image {image_path}, skipping.")
            continue
        
        video_writer.write(img)  # Write image to video

    # Release the video writer
    video_writer.release()

    print(f"Video successfully created at {output_video_path}")
else:
    print("No valid images found in the specified directory.")
