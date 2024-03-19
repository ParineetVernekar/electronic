import os
import pygame
from pygame.locals import *
from time import sleep

usb_path = '/media/pi/your_usb_drive'  # Update with your USB drive path
image_folder = 'images'  # Folder containing images on the USB

def display_slideshow():
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN))
    pygame.mouse.set_visible(False)

    image_files = [f for f in os.listdir(os.path.join(usb_path, image_folder)) if f.endswith(('.jpg', '.png', '.jpeg'))]
    
    print(image_files)
    
    while True:  # Loop indefinitely
        for image_file in image_files:
            image_path = os.path.join(usb_path, image_folder, image_file)
            
            #add here
					  img = pygame.image.load(image_path)
            original_width, original_height = img.get_size()
            
            # Calculate scaled dimensions
            screen_width = screen.get_width()
            screen_height = screen.get_height()
            aspect_ratio = original_width / original_height
            if screen_width / screen_height < aspect_ratio:
                scaled_width = screen_width
                scaled_height = int(screen_width / aspect_ratio)
            else:
                scaled_width = int(screen_height * aspect_ratio)
                scaled_height = screen_height
                
            # Scale image
            img = pygame.transform.scale(img, (scaled_width, scaled_height))
            
            # Calculate position to center image
            x = (screen_width - scaled_width) // 2
            y = (screen_height - scaled_height) // 2
            
            # Display image
            screen.blit(img, (x, y))
            pygame.display.flip()

            sleep(5)  # Adjust duration per image (in seconds)

if __name__ == "__main__":
    display_slideshow()
