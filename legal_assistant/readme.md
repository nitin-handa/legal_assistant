# AI Legal Chatbot

This is a Flask-based AI Legal Chatbot that uses the Gemini API to provide legal information and guidance. The chatbot can process uploaded documents (PDF, DOCX, TXT) and answer questions based on the document content or general legal queries.

## Features

- Document upload and processing (PDF, DOCX, TXT)
- AI-powered legal responses using Gemini API
- Chat history management
- Simple web interface

## Installation

1. Clone the repository:
   ```
   git clone https://https://github.com/nitin-handa/legal_assistant.git
   cd legal_assistant
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up your Gemini API key:
   - Create a `.env` file in the project root
   - Add your API key: `GEMINI_API_KEY=your_api_key_here`

## Usage

1. Run the Flask application:
   ```
   python app.py
   ```

2. Open a web browser and go to `http://localhost:5000`

3. Upload a document or start asking legal questions

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).
