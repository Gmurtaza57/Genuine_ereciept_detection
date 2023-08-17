Genuine eReceipts Identification using NLP Techniques
Author
Ghulam Murtaza

Date
07/25/2023

Overview
A comprehensive solution to identify genuine eReceipts from a collection of emails. Combines preprocessing, filtering, Named Entity Recognition (NER), and information extraction techniques for accurate key information extraction from eReceipts.

Table of Contents
Introduction
Approach
Evaluation
Model Selection and Suitability
Potential Challenges
Results
Installation and Usage
Introduction
Crucial for rewards points processing, this solution aids in accurately extracting information from eReceipts. It demonstrates a deep understanding of NLP models and their real-world application.

Approach
Preprocessing: Removes unnecessary HTML tags, extracts plain text using BeautifulSoup.
Filtering: Regular expressions identify and exclude non-eReceipt content.
NER with spaCy: Identifies general entities like store names in the text.
Specific Information Extraction: Regular expressions extract structured information.
LayoutLM Token Classification: Transformer-based LayoutLM model extracts structured product details.
Evaluation
Data Quality: Examine eReceipt samples, comparing extracted information with expected results.
Performance Metrics: Metrics like accuracy, precision, recall, and F1-score for spaCy and LayoutLM models.
Manual Inspection: Identify specific patterns or cases models might miss.
Model Selection and Suitability
spaCy NER Model (en_core_web_sm): Efficient for identifying store names from eReceipts text.
LayoutLM Model: Ideal for extracting structured information like product details.
Addressing Potential Challenges
SpaCy NER Limitations: Consider training a custom entity recognition model.
eReceipt Formats Variability: Refine regular expressions to handle common variations.
Ambiguous Textual Context: Use post-processing steps or leverage other relevant information.
Limited Data Availability: Fine-tune LayoutLM with transfer learning on document-based datasets.
False Positives/Negatives: Implement a human expert review feedback loop.
Results
Sample results can be viewed by running the code provided for dummy_order.html.

Installation and Usage
python
Copy code
# Downloading Libraries
!pip install -U spacy
!pip install transformers

# Code provided in the provided document should be placed in a Python environment.
# Follow the provided steps to extract key information from eReceipt HTML files.
To view this README in the best format, it is suggested to visualize it on a platform that supports Markdown, such as GitHub.# Genuine_ereciept_detection
