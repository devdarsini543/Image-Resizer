import os
from PIL import Image

# === Configuration ===
input_folder = "images"        # Folder containing the original images
output_folder = "resized"      # Folder to save resized images
new_size = (800, 600)          # Width x Height in pixels
output_format = "JPEG"         # Format to save (e.g., JPEG, PNG)

# Create output folder if not exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Process each image in the folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        img_path = os.path.join(input_folder, filename)
        try:
            with Image.open(img_path) as img:
                # Maintain aspect ratio
                img.thumbnail(new_size)

                # Save the image
                output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.{output_format.lower()}")
                img.save(output_path, output_format)
                print(f"Resized & saved: {output_path}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")

print("✅ All images have been resized and saved!")
