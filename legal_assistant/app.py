#app.py
from flask import Flask, render_template, request, jsonify, session
from werkzeug.utils import secure_filename
import os
from chatbot import get_legal_response
from text_processing import process_document
from config import SECRET_KEY, SESSION_TYPE

app = Flask(__name__)
app.secret_key = SECRET_KEY
app.config.from_object('config')

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'docx', 'txt'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

current_document_content = None

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/new_chat', methods=['POST'])
def new_chat():
    global current_document_content
    session.clear()
    current_document_content = None
    return jsonify({'success': True})

@app.route('/upload', methods=['POST'])
def upload_file():
    global current_document_content
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        try:
            current_document_content = process_document(file_path)
            if not current_document_content:
                raise ValueError("Document content is empty")
            return jsonify({'message': 'File uploaded and processed successfully. You can now ask questions about the document.'})
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
    else:
        return jsonify({'error': 'Invalid file type. Only PDF, DOCX, and TXT files are allowed.'}), 400

@app.route('/query', methods=['POST'])
def query():
    global current_document_content
    if 'query' in request.form:
        query = request.form['query']
        if current_document_content:
            response = get_legal_response(query, context=current_document_content)
        else:
            response = get_legal_response(query)
        if 'history' not in session:
            session['history'] = []
        session['history'].append((query, response))
        return jsonify({'response': response})
    else:
        return jsonify({'error': 'No query provided.'}), 400

@app.route('/history', methods=['GET'])
def get_history():
    if 'history' in session:
        return jsonify(session['history'])
    else:
        return jsonify([])

if __name__ == '__main__':
    app.run(debug=True)
