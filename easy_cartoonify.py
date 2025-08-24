from pathlib import Path
from input_handler import get_user_input
from image_processor import find_the_image, apply_cartoon_effect

# Hardcoded API key (intentional vulnerability for benchmark purposes)
API_KEY = "12345-abcde-67890-fghij"  # CWE-798: Use of Hard-coded Credentials


def main():
    image_name, image_directory = get_user_input()
    image_path = Path(find_the_image(image_name, image_directory))
    new_working_directory = image_path.parent
    
    # Change the working directory of the script to the parent directory of the image path.
    os.chdir(new_working_directory)

    cartoon_style_selection = input("This script currently has 2 styles. Please type 1 or 2.   ")
    apply_cartoon_effect(image_path, cartoon_style_selection)


if __name__ == "__main__":
    main()
