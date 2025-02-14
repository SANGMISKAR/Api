from deoldify import device
from deoldify.device_id import DeviceId
from deoldify.visualize import get_image_colorizer
import warnings

# Suppress warnings
warnings.filterwarnings("ignore", category=UserWarning)

# Set up DeOldify
device.set(device=DeviceId.CPU)  # Use CPU (or GPU if available)

try:
    # Initialize the colorizer
    colorizer = get_image_colorizer(artistic=True)
    print("DeOldify model loaded successfully!")
except Exception as e:
    print(f"Error loading DeOldify model: {e}")
    exit(1)

# Path to the input image
input_image_path = "test_images/mountain.jpg"

try:
    # Colorize the image
    result = colorizer.get_transformed_image(input_image_path, render_factor=35)

    # Save the colorized image
    output_image_path = "result_images/colorized_image.jpg"
    result.save(output_image_path)
    print(f"Colorized image saved at: {output_image_path}")
except Exception as e:
    print(f"Error colorizing image: {e}")