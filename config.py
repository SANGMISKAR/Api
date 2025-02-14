import os

# Access environment variables
model_path = os.getenv("MODEL_PATH", "models/ColorizeArtistic_gen.pth")  # Path to DeOldify model
allowed_extensions = os.getenv("ALLOWED_EXTENSIONS", "jpg,png")  # Allowed file extensions
debug_mode = os.getenv("DEBUG", "True").lower() == "true"  # Debug mode (True/False)

# Optional: Print the values for debugging
print(f"Model Path: {model_path}")
print(f"Allowed Extensions: {allowed_extensions}")
print(f"Debug Mode: {debug_mode}")
