URL Phishing Detection Application
This project provides a web application for detecting phishing URLs based on machine learning models. The application evaluates the provided URL on several factors and predicts whether it is legitimate or a phishing URL. Below, you'll find details on the project setup, structure, and usage.

Prerequisites
Installation Requirements
Make sure you have the following installed before proceeding:

Python 3.8 or higher
Flask
Required Python libraries (see requirements.txt)
Required Files and Folders
Dataset: Used for training the model.
Static folder: Contains images and other static files needed for the application.
Template folder: Contains the HTML files (e.g., html2.html) used for rendering web pages.
requirements.txt: Contains a list of all necessary Python packages to run the application.
Trained Model: Pre-trained machine learning model CAT96.pkl included for phishing detection.
Project Structure
The project structure includes the following key directories and files:

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
Key Files
app.py: Main Flask application file. Defines the routes, implements the phishing detection logic, and serves the web interface.
CAT96.pkl: Pre-trained model used to classify URLs as phishing or legitimate.
requirements.txt: Includes Python libraries required to run the application.
Static Assets:
static/pics/img.jpg: Placeholder image displayed on the web interface.
templates/html2.html: HTML template to provide the user interface for input and result display.
Features
Unshortens shortened URLs.
Extracts key attributes of the provided URL, including special characters, path length, external resource references, etc.
Makes predictions using a pre-trained model.
Displays the prediction result (Legitimate or Phishing) on the web interface.
Setup Instructions
Clone the repository or download the project files.

git clone https://github.com/praveency046/Phishing-Detection-Using-AI-ML.git
Navigate to the project directory:

cd Phishing-Detection-Using-AI-ML
Install the required dependencies:

pip3 install -r requirements.txt
Run the application:

python3 AI_phishing_detection.py
Open your browser and navigate to:

http://127.0.0.1:5000/
Usage Instructions
Open the application in your web browser using the provided URL (http://127.0.0.1:5000/).
Enter a URL into the input field on the web interface.
Submit the URL for analysis.
View the result, which will indicate whether the URL is legitimate or a phishing attempt.
Dependencies
The necessary Python packages are listed in the requirements.txt file. Install them as follows:

pip3 install -r requirements.txt
Sample requirements.txt:

Flask==2.3.2
joblib
beautifulsoup4
requests
whois
Contact
For any questions or issues regarding the application, please reach out to me.

