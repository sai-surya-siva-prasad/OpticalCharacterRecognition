import os
from google.cloud import vision
import io

# Set up authentication
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\Users\surya\OneDrive\Desktop\xxx\xxx.json'

# Initialize Vision API client
client = vision.ImageAnnotatorClient()

def detect_text(path):
    """Detects text in the file."""
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    # Language hints for better accuracy (optional)
    # Add 'te' for Telugu, you can add more language codes if needed
    image_context = vision.ImageContext(language_hints=['te', 'en'])

    response = client.text_detection(image=image, image_context=image_context)
    texts = response.text_annotations

    print('Texts:')
    for text in texts:
        print(f'\n"{text.description}"')
        vertices = [f'({vertex.x},{vertex.y})' for vertex in text.bounding_poly.vertices]
        print('bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

# Usage
if __name__ == "__main__":
    file_path = r"C:\Users\surya\xxx\xxxx.jpg" # Update this path
    detect_text(file_path)
