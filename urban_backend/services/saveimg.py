from datetime import datetime
import os
import requests
from PIL import Image
from io import BytesIO

from image_detect import analyze_image_with_base64

# Mapbox access token (replace this with your actual token)
access_token = 'pk.eyJ1IjoiaW1wLXVuaXF1ZTc1MDciLCJhIjoiY20yZnFnZWRqMGMxNTJscTJrdnMyNnB3cCJ9.nDPkD12D6xzkvSy2KZ0Fgg'
def saveimg(lng, lat):
    

    # Construct the URL for fetching the static image
    static_map_url = f"https://api.mapbox.com/styles/v1/mapbox/satellite-streets-v11/static/{lng},{lat},15,0/600x400?access_token={access_token}&attribution=false&logo=false&marker={lng},{lat};"

    # Make a GET request to download the image
    response = requests.get(static_map_url)
    
    
    # Check if the request was successful
    if response.status_code == 200:
    # Ensure the 'images' folder exists
        images_folder = "images"
        if not os.path.exists(images_folder):
            os.makedirs(images_folder)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        # Save the image in the 'images' folder
        image_path = os.path.join(images_folder, f"static_map_image{timestamp}.png")
        img = Image.open(BytesIO(response.content))
        img.save(image_path)
        data= analyze_image_with_base64(image_path)
        return {"message": "image saved successfully", "main entity":data}
    # # Initialize the Mask R-CNN predictor
    #     predictor = setup_mask_rcnn()
        
    #     # Process the image
    #     img_rgb, outputs = process_image(predictor, image_path)
        
    #     # Visualize the results
    #     visualize_results(img_rgb, outputs)
    
        # print(f"Image saved successfully in '{image_path}'")
        # return "Image saved successfully"
    
    else:
        print(f"Failed to retrieve image. HTTP Status code: {response.status_code}")
        return response.status_code