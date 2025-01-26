import os
import base64
from openai import OpenAI

# Set up OpenAI API key
os.environ["OPENAI_API_KEY"] = "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"

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# def analyze_image_with_url(img_url, prompt="Analyze this image and list the main entities."):
#     """
#     Analyze a hosted image via OpenAI GPT-4 Vision API.
    
#     Args:
#         img_url (str): The URL of the hosted image.
#         prompt (str): Instruction for analyzing the image.

#     Returns:
#         str: Analysis results.
#     """
#     try:
#         response = client.chat.completions.create(
#             model="gpt-4o-mini",  # Use the appropriate Vision model
#             messages=[
#                 {
#                     "role": "user",
#                     "content": [
#                         {"type": "text", "text": prompt},
#                         {
#                             "type": "image_url",
#                             "image_url": {"url": img_url},
#                         },
#                     ],
#                 }
#             ],
#         )
#         # Access the content from the response
#         result = response.choices[0].message.content
#         return result
#     except Exception as e:
#         return f"Error analyzing image with URL: {e}"

def analyze_image_with_base64(image_path, prompt="Analyze this image and list the main entities seperated by comma and don't describe the entity only name them"):
    """
    Analyze a local image by converting it to a base64 string and sending it to the API.
    
    Args:
        image_path (str): Path to the local image file.
        prompt (str): Instruction for analyzing the image.

    Returns:
        str: Analysis results.
    """
    try:
        # Read the image and encode it as base64
        with open(image_path, "rb") as image_file:
            img_b64_str = base64.b64encode(image_file.read()).decode("utf-8")
        
        # Infer image type
        img_type = "image/jpeg" if image_path.lower().endswith((".jpg", ".jpeg")) else "image/png"

        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Use the appropriate Vision model
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {"url": f"data:{img_type};base64,{img_b64_str}"},
                        },
                    ],
                }
            ],
        )
        # Access the content from the response
        result = response.choices[0].message.content
        return result
    except Exception as e:
        return f"Error analyzing image with base64: {e}"

# Example Usage
# if __name__ == "__main__":
#     # Analyze hosted image
#     # hosted_image_url = "https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png"
#     # print("Analyzing hosted image...")
#     # print(analyze_image_with_url(hosted_image_url))

#     # Analyze local image
#     local_image_path = r"C:\Users\Suruchi\Downloads\urban_backend\images\static_map_image0.png"
#     print("\nAnalyzing local image...")
#     print(analyze_image_with_base64(local_image_path))
