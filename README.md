Genuine eReceipt Identification using NLP Techniques
By Ghulam Murtaza

Date: 07/25/2023

Introduction
This repository provides a solution to identify genuine eReceipts from a collection of emails received by customers, crucial for accurate rewards points processing. We combine preprocessing, filtering, Named Entity Recognition (NER), and specific information extraction techniques to accurately extract key information from eReceipts.

Table of Contents
Approach
Evaluation
Model Selection and Suitability
Addressing Potential Challenges
Installation
Usage
Approach
Preprocessing: Leveraging BeautifulSoup for parsing HTML and XML documents.
Filtering: Employing regular expressions to filter out non-eReceipt emails.
Named Entity Recognition (NER): Utilizing the spaCy NER model (en_core_web_sm).
Specific Information Extraction: Extracting information like receipt date, subtotal, total, order ID, and product details using regex.
LayoutLM Token Classification: Using the LayoutLM model for token classification.
Evaluation
Data Quality: Check accuracy by comparing the extracted information with the expected results.
Performance Metrics: Use metrics such as accuracy, precision, recall, and F1-score.
LayoutLM Token Classification: Assess accuracy of product details extraction.
Manual Inspection: Helps in identifying specific cases or patterns that the models might miss.
Model Selection and Suitability
spaCy NER Model (en_core_web_sm): Efficient for identifying store names from eReceipts.
LayoutLM Model: Highly suitable for extracting structured information like product details.
Addressing Potential Challenges
Enhancing entity recognition accuracy.
Handling the variability in eReceipt formats.
Addressing ambiguous textual context.
Overcoming limited data availability.
Reducing false positives and negatives.
Installation
Download necessary libraries:
bash
Copy code
pip install -U spacy
python -m spacy download en_core_web_trf
pip install transformers
Clone this repository:
bash
Copy code
git clone <repository_url>
Usage
Load spaCy NER Model.
Initialize LayoutLM Model and Tokenizer.
Use the provided functions to extract information:
extract_key_information_from_html(html_content)
extract_key_information_from_file(file_path)
Example:

python
Copy code
file_path = "/path/to/eReceipt.html"
info = extract_key_information_from_file(file_path)
print(info)
