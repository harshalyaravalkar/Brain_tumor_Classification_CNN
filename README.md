# Brain_tumor_Classification_CNN
This repo has Brain Tumor Classification project, where we leverage the power of deep learning and Convolutional Neural Networks (CNNs) to accurately diagnose brain tumors from MRI scans. This application, seamlessly deployed using Flask, offers a user-friendly interface for uploading and predicting tumor types in real-time.

## Project Structure

- `CNN project.ipynb/`: Contains the Jupyter notebook used for developing and training the CNN model.
- `code_py.py`: The main Flask application script.
- `templates/`: Directory for HTML templates.
    - `CNN_deploy.html`: HTML file for uploading images.
    - `pred.html`: HTML file for displaying predictions.
- `Brain_tumor_classification.h5`: The trained CNN model.

### Prerequisites

- Python 3.7 or higher
- TensorFlow
- Flask
- OpenCV
- PIL (Pillow)
- NumPy

  ## Project Overview

### CNN Model

The CNN model was developed using TensorFlow and trained on a dataset of brain MRI images. The model is designed to classify images into one of the following categories:

1. No Tumor
2. Pituitary Tumor
3. Meningioma Tumor
4. Glioma Tumor

The Flask application serves as a web interface for users to upload brain scan images and receive predictions from the CNN model. The application consists of two main HTML pages:

- **CNN_deploy.html**: Allows users to upload images and displays the uploaded images using JavaScript.
- **pred.html**: Displays the predicted tumor type for the uploaded images.

# Deployed Flask App
![Screenshot (1270)](https://github.com/harshalyaravalkar/Brain_tumor_Classification_CNN/assets/143155629/27f46c0a-989c-4bdf-9b6e-60c82b56d189)
![Screenshot (1271)](https://github.com/harshalyaravalkar/Brain_tumor_Classification_CNN/assets/143155629/4980ba25-feda-400b-9293-eb1aefe1ca98)
