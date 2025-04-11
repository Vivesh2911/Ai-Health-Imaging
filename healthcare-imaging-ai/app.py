import random
import os
from PIL import Image
import matplotlib.pyplot as plt
from datetime import datetime

history_log = "prediction_history.txt"
output_dir = "output_images"

# Ensure output_images/ exists
os.makedirs(output_dir, exist_ok=True)

def load_image(image_path):
    try:
        image = Image.open(image_path).convert("RGB")
        return image
    except Exception as e:
        print(f"❌ Error loading {image_path}: {e}")
        return None

def predict(image):
    # Random mock prediction
    return "Pneumonia" if random.random() > 0.5 else "Normal"

def save_prediction(image, result, image_path):
    base_name = os.path.basename(image_path)
    output_name = f"{result}_{base_name}"
    output_path = os.path.join(output_dir, output_name)
    image.save(output_path)
    print(f"📸 Saved predicted image as: {output_path}")

def log_history(image_path, prediction):
    with open(history_log, "a") as f:
        f.write(f"{datetime.now()} - {image_path} -> {prediction}\n")

def show_result(image, prediction):
    plt.imshow(image)
    plt.title(f"Prediction: {prediction}")
    plt.axis("off")
    plt.show()

def run_prediction_on_image(image_path):
    image = load_image(image_path)
    if image:
        result = predict(image)
        print(f"✅ Prediction for {image_path}: {result}")
        show_result(image, result)
        save_prediction(image, result, image_path)
        log_history(image_path, result)
    else:
        print(f"⚠️ Skipping {image_path}")

if __name__ == "__main__":
    print("🩺 Healthcare Imaging AI - CLI")
    choice = input("➡️ Enter image file path or folder: ").strip()

    if os.path.isdir(choice):
        for filename in os.listdir(choice):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                run_prediction_on_image(os.path.join(choice, filename))
    elif os.path.isfile(choice):
        run_prediction_on_image(choice)
    else:
        print("❌ Invalid file or folder path.")
