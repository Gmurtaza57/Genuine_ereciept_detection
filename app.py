import os
from pdf2image import convert_from_path
from flask import Flask, request, jsonify, render_template
from transformers import pipeline
from PIL import Image

app = Flask(__name__)

# Create a question answering pipeline for document question answering
qa_pipeline = pipeline("document-question-answering", model="magorshunov/layoutlm-invoices")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify(error="No file provided"), 400

        uploaded_file = request.files['file']

        if uploaded_file.filename == '':
            return jsonify(error="No selected file"), 400

        # Convert PDF to images
        if uploaded_file.filename.endswith(".pdf"):
            temp_path = "temp_uploaded.pdf"
            uploaded_file.save(temp_path)
            images = convert_from_path(temp_path)
            os.remove(temp_path)
        else:
            images = [Image.open(uploaded_file)]

        # Predefined questions
        predefined_questions = [
            "What is the name of the person?",
            "What is the name of the company?",
            "What is the subtotal?",
            "What is the total?",
            "What is the address?",
            "what is order id"
        ]

        responses = {}

        # Get answers for predefined questions
        for q in predefined_questions:
            collected_answers = []
            for image in images:
                answers_for_q = qa_pipeline(question=q, image=image)
                if answers_for_q:
                    collected_answers.extend([ans['answer'] for ans in answers_for_q])
            unique_answers = list(set(collected_answers))
            responses[q] = ", ".join(unique_answers)

        # Handle custom question
        custom_question = request.form.get('custom_question', None)
        if custom_question:
            collected_custom_answers = []
            for image in images:
                custom_answer = qa_pipeline(question=custom_question, image=image)
                if custom_answer:
                    collected_custom_answers.extend([ans['answer'] for ans in custom_answer])
            unique_custom_answers = list(set(collected_custom_answers))
            responses["custom_question"] = ", ".join(unique_custom_answers)

        return jsonify(responses)

    else:
        return render_template('index.html')

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

