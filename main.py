import os
from PIL import Image

def scale_images_in_folder(folder_path, scale_factor=1/3, output_folder=None):
    """
    Scales all images in the specified folder by the given scale factor.

    :param folder_path: Path to the folder containing images.
    :param scale_factor: Factor by which to scale the images (default is 1/3).
    :param output_folder: Path to the output folder for scaled images. If None, overwrites the originals.
    """
    # Create output folder if specified and doesn't exist
    if output_folder and not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        # Skip hidden files (those starting with a dot)
        if filename.startswith('.'):
            #print(f"Skipping hidden file: {filename}")
            continue

        file_path = os.path.join(folder_path, filename)

        try:
            with Image.open(file_path) as img:
                # Get current image size
                original_size = img.size  # (width, height)
                
                # Compute new dimensions
                new_size = (int(original_size[0] * scale_factor), int(original_size[1] * scale_factor))
                
                # Resize image using LANCZOS filter (which is the replacement for ANTIALIAS)
                scaled_img = img.resize(new_size, Image.Resampling.LANCZOS)
                
                # Save scaled image
                if output_folder:
                    output_path = os.path.join(output_folder, filename)
                    scaled_img.save(output_path)
                else:
                    scaled_img.save(file_path)  # Overwrite the original image

                print(f"Scaled {filename} to {new_size}")
        
        except Exception as e:
            print(f"Error processing {filename}: {e}")

# Example usage:
folder_path = "/home/potechius/Projects/VSCode/gaussian-splatting/datasets/EAH5/images"  # Replace with your folder path
output_folder = "/home/potechius/Projects/VSCode/gaussian-splatting/datasets/EAH5/images2"  # Optional: specify if you want to save scaled images elsewhere
scale_images_in_folder(folder_path, output_folder=output_folder)