import os
import cv2

got10k_path = "raw_data/GOT-10k/test/"

# Generate video from a series of images
def generate_video(image_folder, video_name="mygeneratedvideo.avi"):
    video_name = "processed_data/" + video_name

    images = [img for img in os.listdir(image_folder) if img.endswith((".jpg", ".jpeg", ".png"))]
    print("Images:", images)

    # Set frame from the first image
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    # Video writer to create .avi file
    video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'DIVX'), 1, (width, height))

    # Appending images to video
    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    # Release the video file
    video.release()
    cv2.destroyAllWindows()
    print("Video generated successfully!")

# Calling the function to generate the video
generate_video(got10k_path + "GOT-10k_Test_000001", "GOT-10k_Test_000001.avi")
