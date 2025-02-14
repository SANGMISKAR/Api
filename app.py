from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from deoldify import device
from deoldify.device_id import DeviceId
from deoldify.visualize import get_image_colorizer
import os
import warnings

# Suppress warnings
warnings.filterwarnings("ignore", category=UserWarning)

# Set up DeOldify
device.set(device=DeviceId.CPU)  # Use CPU (or GPU if available)
colorizer = get_image_colorizer(artistic=True)

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Ensure the result_images folder exists
os.makedirs("result_images", exist_ok=True)

# Root route
@app.route('/')
def home():
    return "DeOldify Flask API is running!"

# Optional: Serve favicon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico')

# Colorize image route
@app.route('/colorize', methods=['POST'])
def colorize_image():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Save the uploaded file temporarily
    input_image_path = "temp_image.jpg"
    file.save(input_image_path)

    try:
        # Colorize the image
        result = colorizer.get_transformed_image(input_image_path, render_factor=35)

        # Save the colorized image
        output_image_path = "result_images/colorized_image.jpg"
        result.save(output_image_path)

        # Return the path to the colorized image
        return jsonify({"result_path": output_image_path})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Enable debug mode for development
    app.run(host='0.0.0.0', port=5000, debug=True)