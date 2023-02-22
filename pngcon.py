import os
from moviepy.editor import ImageSequenceClip
import glob

input_dir = r'G:\My Drive\AI\StableDiffusion\2023-02\See You Again'
output_path = 'output.mp4'

try:
    # Create a list of png files in the input directory
    png_files = glob.glob(os.path.join(input_dir, '*.png'))

    # Sort the png files in ascending order
    png_files.sort()

    # Create a video clip object
    clip = ImageSequenceClip(png_files, fps=30)

    # Write the video clip to the output file
    clip.write_videofile(output_path, codec='libx264', audio=False)

except Exception as e:
    print(f"An error occurred: {e}")
