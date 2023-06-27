import os
import cv2
import numpy as np
import concurrent.futures
import tensorflow as tf

# Define the folder path where the images are stored
folder_path = "/Users/stuartfinley/Downloads/ImageFolder2/"

# Define the data augmentation pipeline
data_augmentation = tf.keras.Sequential([
    tf.keras.layers.experimental.preprocessing.RandomFlip("horizontal_and_vertical"),
    tf.keras.layers.experimental.preprocessing.RandomRotation(0.2)])

def process_file(file_path):
    """
    Process a single image file.
    """
    if file_path.endswith(".jpg"):
        # Using openCV to open and process the images
        image = cv2.imread(file_path)
        # Apply the data augmentation pipeline to the image
        augmented_image = data_augmentation(np.array([image]))

        # Convert the augmented image to a NumPy array
        augmented_image = np.asarray(augmented_image * 255.0, dtype=np.uint8)
        # Save the augmented image to disk
        cv2.imwrite(file_path[:-4] + "_augmented.jpg", augmented_image)
# Loop through all the files in the main images folder and each of the sub folders
with concurrent.futures.ThreadPoolExecutor() as executor:
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # Submit a new task to the executor for each file found
            executor.submit(process_file, os.path.join(root, file))