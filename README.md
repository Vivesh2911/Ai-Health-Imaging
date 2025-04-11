
# Healthcare Imaging AI

This project is a basic AI-based application for detecting pneumonia in X-ray images. The model is built using PyTorch, and the application uses Flask for the web interface. The system can classify images and give predictions about pneumonia based on trained models.

## Folder Structure

```
healthcare-imaging-ai/
├── model/
│   └── pneumonia_model.pth         # Trained PyTorch model for pneumonia detection
├── test_images/
│   └── sample1.jpeg                # Sample X-ray image for testing
├── app.py                          # Main Python script (Flask app)
├── requirements.txt                # List of dependencies
└── README.md                       # Project info
```

## Features

- **Pneumonia Detection**: The AI model detects whether an X-ray image shows signs of pneumonia.
- **User Upload**: Users can upload their own X-ray images for analysis.
- **Basic Web Interface**: The app provides a simple web interface for uploading images and receiving predictions.
- **Prediction Output**: The app provides a prediction of whether the X-ray shows pneumonia or not.

## Requirements

Before running the application, ensure you have all the required dependencies installed. You can install them using `pip`:

1. **Python 3.x** (ensure Python 3.7+ is installed)
2. **PyTorch** (for deep learning model)
3. **Flask** (for web application)
4. **Other Dependencies** (listed in `requirements.txt`)

### To Install Dependencies:

1. **Clone the repository** or create a project folder.
2. **Create a virtual environment** (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Mac/Linux
   venv\Scripts\activate     # For Windows
   ```

3. **Install dependencies** from the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

### Install PyTorch

To install PyTorch, follow the instructions from the official site:  
[PyTorch Installation Guide](https://pytorch.org/get-started/locally/)

### Install Flask

To install Flask:

```bash
pip install Flask
```

## Running the Application

Once you've installed all dependencies, you can run the Flask application:

1. **Navigate to the project directory**:

   ```bash
   cd /path/to/healthcare-imaging-ai
   ```

2. **Run the application**:

   ```bash
   python app.py
   ```

This will start the Flask server. By default, it will be hosted at `http://127.0.0.1:5000/`.

## How to Use

1. **Upload Image**: Go to the web interface (usually at `http://127.0.0.1:5000/`), and you'll be prompted to upload an X-ray image.
2. **Get Prediction**: Once the image is uploaded, the AI model will predict if the image shows pneumonia.

## Project Details

### Model

- The model used for pneumonia detection is a pre-trained model saved as `pneumonia_model.pth` in the `model/` directory.
- You can find detailed instructions for training the model and using other datasets in the comments of the code.

### Sample Image

The `test_images/` folder contains a sample X-ray image (`sample1.jpeg`) for testing purposes.

## Conclusion

This is a basic prototype of an AI system for healthcare imaging. The goal is to use machine learning for detecting conditions like pneumonia from X-ray images. You can extend this project by adding more features like multi-condition detection, real-time webcam analysis, or expanding the dataset for better accuracy.

## License

This project is licensed under the MIT License.

