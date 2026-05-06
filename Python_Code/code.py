import os
import requests

# Configuration
API_KEY = 'T9Th2By5VmomByYWGhno24yy'
INPUT_FOLDER = 'images_to_process'  # Folder with your original photos
OUTPUT_FOLDER = 'processed_images'  # Where the transparent PNGs will go

# Create output folder if it doesn't exist
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

def process_folder():
    # Loop through every file in the input folder
    for filename in os.listdir(INPUT_FOLDER):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(INPUT_FOLDER, filename)
            # Change extension to .png for the output
            output_filename = os.path.splitext(filename)[0] + ".png"
            output_path = os.path.join(OUTPUT_FOLDER, output_filename)

            print(f"Processing: {filename}...")

            response = requests.post(
                'https://api.remove.bg/v1.0/removebg',
                files={'image_file': open(input_path, 'rb')},
                data={'size': 'auto'},
                headers={'X-API-Key': API_KEY},
            )

            if response.status_code == 200:
                with open(output_path, 'wb') as out:
                    out.write(response.content)
                print(f"Done! Saved to {output_path}")
            elif response.status_code == 402:
                print("Error: You've run out of credits!")
                break # Stop the loop if you're out of credits
            else:
                print(f"Error {response.status_code} on {filename}: {response.text}")

if __name__ == "__main__":
    process_folder()