# URL Phishing Detection Application

This project provides a web application for detecting phishing URLs based on machine learning models. The application evaluates the provided URL on several factors and predicts whether it is legitimate or a phishing URL. Below, you'll find details on the project setup, structure, and usage.

---

## Prerequisites

### Installation Requirements

Make sure you have the following installed before proceeding:

- Python 3.8 or higher
- Flask
- Required Python libraries (see [requirements.txt](#dependencies))

### Required Files and Folders

1. **Dataset:** Used for training the model.
2. **Static folder:** Contains images and other static files needed for the application.
3. **Template folder:** Contains the HTML files (e.g., `html2.html`) used for rendering web pages.
4. **requirements.txt:** Contains a list of all necessary Python packages to run the application.
5. **Trained Model:** Pre-trained machine learning model `CAT96.pkl` included for phishing detection.

---

## Project Structure

The project structure includes the following key directories and files:

```
URL-Phishing-Detector/
|-- static/
|   |-- pics/
|       |-- img.jpg
|
|-- templates/
|   |-- html2.html
|
|-- CAT96.pkl
|-- requirements.txt
|-- AI_phishing_detection.py
```

### Key Files

1. **`app.py`:** Main Flask application file. Defines the routes, implements the phishing detection logic, and serves the web interface.
2. **`CAT96.pkl`:** Pre-trained model used to classify URLs as phishing or legitimate.
3. **`requirements.txt`:** Includes Python libraries required to run the application.
4. **Static Assets:**
   - **static/pics/img.jpg:** Placeholder image displayed on the web interface.
5. **`templates/html2.html`:** HTML template to provide the user interface for input and result display.

---

## Features

- Unshortens shortened URLs.
- Extracts key attributes of the provided URL, including special characters, path length, external resource references, etc.
- Makes predictions using a pre-trained model.
- Displays the prediction result (Legitimate or Phishing) on the web interface.

---

## Setup Instructions

1. Clone the repository or download the project files.

   ```bash
   git clone https://github.com/praveency046/Phishing-Detection-Using-AI-ML.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Phishing-Detection-Using-AI-ML
   ```

3. Install the required dependencies:

   ```bash
   pip3 install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python3 AI_phishing_detection.py
   ```

5. Open your browser and navigate to:

   ```
   http://127.0.0.1:5000/
   ```

---

## Usage Instructions

1. Open the application in your web browser using the provided URL (`http://127.0.0.1:5000/`).
2. Enter a URL into the input field on the web interface.
3. Submit the URL for analysis.
4. View the result, which will indicate whether the URL is legitimate or a phishing attempt.

---

## Dependencies

The necessary Python packages are listed in the `requirements.txt` file. Install them as follows:

```bash
pip3 install -r requirements.txt
```

Sample `requirements.txt`:

```
Flask==2.3.2
joblib
beautifulsoup4
requests
whois
```

---

## Contact

For any questions or issues regarding the application, please reach out to me.

---
