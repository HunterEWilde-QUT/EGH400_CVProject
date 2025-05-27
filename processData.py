import os
import cv2

# Generate video from a series of images
def generateVideo(imageDir, videoName):
    images = [img for img in os.listdir(imageDir) if img.endswith((".jpg", ".jpeg", ".png"))]
    #print("Images:", images)

    # Set frame from the first image
    frame = cv2.imread(os.path.join(imageDir, images[0]))
    height, width, layers = frame.shape

    # Video writer to create .avi file
    destination = f"processed_data/{imageDir.split('/')[1]}/"
    video = cv2.VideoWriter(destination + videoName + ".avi",
                            cv2.VideoWriter_fourcc(*'DIVX'), 1, (width, height))

    # Appending images to video
    for image in images:
        video.write(cv2.imread(os.path.join(imageDir, image)))

    # Release the video file
    video.release()
    cv2.destroyAllWindows()
    print(f"{videoName} generated successfully!")

# Process all raw data in a directory into videos
def processDataset(datasetPath, hasList=False):
    if hasList:
        try:
            with open(datasetPath + "list.txt", 'r') as file:
                for line in file:
                    generateVideo(datasetPath + line.strip(), line.strip())
            print(f"All videos in {datasetPath} generated successfully!")
        except Exception as e:
            print(f"Error reading list.txt: {e}")
    else:
        try:
            for dirPath, _, _ in os.walk(datasetPath):
                for path in dirPath.split("\n"):
                    if any(file.lower().endswith((".jpg", ".jpeg", ".png")) for file in os.listdir(path)):
                        generateVideo(path, path.split("/")[-1].replace("\\", "_"))
            print(f"All videos in {datasetPath} generated successfully!")
        except Exception as e:
            print(f"Images not found: {e}")

processDataset("raw_data/GOT-10k/test/", True)
processDataset("raw_data/TV77/")
