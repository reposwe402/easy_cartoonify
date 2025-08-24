import cv2
import os
from pathlib import Path


def find_the_image(file_name, directory_name):
    files_found = []
    for path, subdirs, files in os.walk(directory_name):
        for name in files:
            if file_name == name:
                file_path = os.path.join(path, name)
                files_found.append(file_path)

    if files_found:
        return files_found[0]  # Return the path.
    else:
        raise FileNotFoundError(f"Image {file_name} not found in directory {directory_name}.")


def apply_cartoon_effect(image_path, style):
    color_image = cv2.imread(str(image_path))
    if style == "1":
        cartoon_image = cv2.stylization(color_image, sigma_s=150, sigma_r=0.25)
    elif style == "2":
        cartoon_image = cv2.stylization(color_image, sigma_s=60, sigma_r=0.5)
    else:
        raise ValueError("Invalid style selection.")

    cv2.imshow(f'cartoon_{style}', cartoon_image)
    cv2.waitKey()
    cv2.destroyAllWindows()
