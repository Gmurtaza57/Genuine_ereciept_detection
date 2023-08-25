  Receipt Analyzer
Receipt Analyzer is a Flask web application that uses a machine learning model from Hugging Face's pipeline to extract and answer questions from uploaded receipts.

Features:
File Input: Users can upload both images and PDFs of receipts.
Predefined Questions: The tool automatically extracts and answers common questions such as:
Name of the person
Name of the company
Subtotal
Total
Address
Order ID
Custom Questions: Users can input custom questions about the receipt, which the model will then attempt to answer.
Technologies Used:
Flask: Python-based micro web framework used for web application.
Hugging Face's Transformers: Used to deploy the LayoutLM v2 model for document-based question answering.
pdf2image: For converting PDFs into image format.
PIL (Python Imaging Library): For handling image files.
Setup and Usage:
Installation:

bash
Copy code
pip install Flask transformers pdf2image Pillow
Running the app:

bash
Copy code
FLASK_APP=app.py FLASK_DEBUG=1 flask run --host=0.0.0.0 --port=8080
Usage:

Navigate to the given URL (e.g., http://127.0.0.1:8080 or your deployed link).
Upload an image or PDF of a receipt.
View the predefined answers or input a custom question for the uploaded receipt.
Demo:
For a live demo, navigate to http://13.58.131.137:8080/.

Note:
Ensure you have the necessary resources and setup for deploying and running a model-intensive web application.

Contributions:
Feel free to fork this repository and make improvements or adaptations.

License:
This project is open-source 

Remember to replace placeholders (e.g., "http://13.58.131.137:8080/") with actual links or information pertinent to your application. Adjust sections as necessary to better suit the details and structure of your project.
