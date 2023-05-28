import tensorflow as tf
from PIL import Image

# Load the trained model
model = tf.keras.models.load_model('TrainedModel.h5')

# Function to preprocess the captcha image
def preprocess_image(image_path):
    image = Image.open(image_path).convert('RGB')
    image = image.resize((width, height))
    image = image_to_array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image

# Function to solve the captcha using the trained model
def solve_captcha(image_path):
    image = preprocess_image(image_path)
    predicted_labels = model.predict(image)
    captcha_text = decode_captcha(predicted_labels)
    return captcha_text

# Function to decode the predicted labels to captcha text
def decode_captcha(predicted_labels):
    captcha_text = ''
    for label in predicted_labels:
        captcha_text += characters[np.argmax(label)]
    return captcha_text

# Set the characters in the captcha
characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

# Set the width and height of the captcha image
width, height = 200, 50

# Solve the captcha
captcha_text = solve_captcha('captcha.png')

# Print the solved captcha text
print(captcha_text)