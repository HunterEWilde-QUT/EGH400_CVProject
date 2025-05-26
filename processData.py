import os
import cv2

got10k_path = "raw_data/GOT-10k/test/"

# Generate video from a series of images
def generate_video(image_folder, video_name):
    images = [img for img in os.listdir(image_folder) if img.endswith((".jpg", ".jpeg", ".png"))]
    #print("Images:", images)

    # Set frame from the first image
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    # Video writer to create .avi file
    video = cv2.VideoWriter(f"processed_data/{video_name}.avi",
                            cv2.VideoWriter_fourcc(*'DIVX'), 1, (width, height))

    # Appending images to video
    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    # Release the video file
    video.release()
    cv2.destroyAllWindows()
    print(f"{video_name} generated successfully!")

# Process all raw data into videos
def process_data(raw_data_path):
    try:
        with open(raw_data_path + "list.txt", 'r') as file:
            for line in file:
                generate_video(raw_data_path + line.strip(), line.strip())
        print(f"All videos in {raw_data_path} generated successfully!")
    except Exception as e:
        print(f"Error reading list.txt: {e}")

process_data(got10k_path)
