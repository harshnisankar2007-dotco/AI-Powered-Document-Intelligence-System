### AI Document Assistant – Generative AI Powered Document Intelligence System

Built with Streamlit, Google Gemini AI, OCR, PDF Processing, and Conversational AI

### 🤖 AI Document Assistant

AI-powered Document Intelligence System built using Streamlit and Google Gemini AI for intelligent analysis of PDFs, Excel files, and Images. The application supports OCR extraction, document summarization, entity extraction, invoice analysis, security risk detection, and conversational question answering.

### 🚀 Features

* 🔐 User Login System

* 📄 PDF Text Extraction using pdfplumber

* 📷 OCR Support for scanned PDFs using Tesseract OCR

* 📊 Excel File Analysis with pandas

* 🖼️ Image Content Analysis using Gemini Vision

* 🧠 AI-Powered Chat Interface

* 📑 Document Summarization

* 📌 Key Point Extraction

* 🏷️ Entity Extraction (Names, Emails, Dates, GST, Amounts, etc.)

* 🧾 Invoice Analysis

* 🛡️ Security & Compliance Risk Detection

* 🔍 Page-wise Intelligent Search

* ⚡ Real-time AI Responses

### 🛠️ Technology Stack

| Category         | Technologies            |
| ---------------- | ----------------------- |
| Frontend         | Streamlit               |
| AI Model         | Google Gemini 2.5 Flash |
| PDF Processing   | pdfplumber              |
| OCR              | pytesseract             |
| Image Conversion | pdf2image               |
| Data Analysis    | pandas                  |
| Image Handling   | Pillow (PIL)            |
| Language         | Python                  |

### 📂 Project Structure

cpcl-genai-document-chatbot/

│

├── login.py # Login and authentication page

├── text.py # Main AI Document Assistant logic

├── requirements.txt # Project dependencies

├── README.md

│

├── images/ # Screenshots

├── docs/ # Project report / presentation

└── sample_files/ # Sample PDFs or Excel files

### ⚙️ Installation

1. Clone the repository

git clone [https://github.com/your-username/cpcl-genai-document-chatbot.git](https://github.com/your-username/cpcl-genai-document-chatbot.git)

cd cpcl-genai-document-chatbot

2. Install dependencies

pip install -r requirements.txt

3. Configure Gemini API Key

Replace the API key in text.py:

client = genai.Client(

api_key="YOUR_API_KEY"

)

4. Run the application

streamlit run login.py

### 📸 Screenshots

* 🏠 Login Page

* 📄 PDF Upload Interface

* 💬 AI Chat Interface

* 📊 Document Analytics Dashboard

* 🖼️ Image Analysis Results

### 🧠 Example Queries

* "Summarize this document"

* "Extract all key points"

* "Analyze this invoice"

* "List all dates mentioned"

* "Extract GST numbers"

* "Find security risks in the document"

* "What is the total amount?"

* "Identify the document type"

### 📈 Future Enhancements

* 🔎 Vector database integration (FAISS / ChromaDB)

* 📚 Multi-document search

* 🌐 Cloud deployment

* 🔐 Database-backed authentication

* 📤 Export chat history

* 📱 Mobile-responsive UI improvements

* 🗂️ Support for Word and PowerPoint files

### 🎯 Key Learning Outcomes

* Generative AI Integration

* Document Intelligence

* OCR Processing

* Prompt Engineering

* Streamlit Application Development

* AI-based Information Retrieval

* Data Extraction & Analytics

### 👩‍💻 Author

Harshni Sankar

B.E. Electronics and Communication Engineering (ECE)

CPCL Internship Project

AI & Embedded Systems Enthusiast

### 📜 License

This project is licensed under the MIT License.

⭐ If you found this project useful, consider giving it a star on GitHub!
