
import streamlit as st
import pdfplumber
import pandas as pd
from PIL import Image
from google import genai
import io
import pytesseract
from pdf2image import convert_from_bytes

# =========================
# SESSION STATE INITIALIZATION
# =========================

def chatbot_app():
    if "document_text" not in st.session_state:
        st.session_state.document_text = ""

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    if "uploaded_file_name" not in st.session_state:
        st.session_state.uploaded_file_name = ""

    if "summary" not in st.session_state:
        st.session_state.summary = ""

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "page_texts" not in st.session_state:
        st.session_state.page_texts = []


    # Initialize session variables
    defaults = {
        "document_text": "",
        "chat_history": [],
        "summary": "",
        "uploaded_file_name": "",
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

    # ==========================
    # CUSTOM CSS
    # ==========================
    st.markdown("""
    <style>

    /* ===== APP BACKGROUND ===== */
    .stApp{
        background: linear-gradient(
            135deg,
            #0a0f1f,
            #111827,
            #0f172a
        );
    }

    /* ===== HIDE STREAMLIT ===== */
    #MainMenu {visibility:hidden;}
    footer {visibility:hidden;}
    header {visibility:hidden;}

    /* ===== TEXT ===== */
    h1,h2,h3,h4,h5,h6{
        color:white !important;
    }

    p, label, div{
        color:#E5E7EB;
    }

    /* ===== SUCCESS BOX ===== */
    [data-testid="stAlert"]{
        border-radius:20px;
        border:1px solid rgba(16,185,129,.4);
        background:rgba(16,185,129,.15);
    }

    /* ===== FILE UPLOADER ===== */
    [data-testid="stFileUploader"]{
        background:#111827;
        padding:20px;
        border-radius:20px;
        border:1px solid rgba(99,102,241,.25);
    }

    /* ===== METRICS ===== */
    [data-testid="stMetric"]{
        background:#111827;
        padding:20px;
        border-radius:20px;
        border:1px solid rgba(99,102,241,.25);
    }

    /* ===== CHAT MESSAGE ===== */
    .stChatMessage{
        background:#111827;
        border-radius:18px;
        padding:15px;
        border:1px solid rgba(255,255,255,.05);
        margin-bottom:12px;
    }

    /* ===== CHAT INPUT ===== */
    [data-testid="stChatInput"]{
        background:#111827;
        border-radius:20px;
        border:2px solid #6366F1;
    }

    /* ===== BUTTON ===== */
    .stButton > button{
        background:linear-gradient(
            90deg,
            #6366F1,
            #8B5CF6
        );
        color:white;
        border:none;
        border-radius:15px;
        height:50px;
        font-weight:bold;
    }

    /* ===== SIDEBAR ===== */
    [data-testid="stSidebar"]{
        background:#0f172a;
        border-right:1px solid rgba(255,255,255,.05);
    }

    /* ===== SCROLLBAR ===== */
    ::-webkit-scrollbar{
        width:8px;
    }

    ::-webkit-scrollbar-thumb{
        background:#6366F1;
        border-radius:10px;
    }

    </style>
    """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
            "",
            type=["pdf","xlsx","png","jpg","jpeg"],
            key="upload_doc"
        )
    if not st.session_state.get("started", False):
        with st.sidebar:

           st.markdown("""
        <div style="
            background:rgba(17,24,39,0.8);
            padding:20px;
            border-radius:20px;
            border:1px solid rgba(99,102,241,0.3);
        ">
        <h3 style="color:white;">📊 Insights</h3>

        <p style="color:#94A3B8;">
        • Document summary<br>
        • Key entities<br>
        • Important points<br>
        • AI confidence
        </p>

        </div>
        """, unsafe_allow_html=True)

        # =========================
        # LANDING PAGE (TOP VIEW)
        # =========================

        st.markdown("<h1 style='text-align:center;'>🤖 AI Document Assistant</h1>", unsafe_allow_html=True)

        st.markdown("<p style='text-align:center;'>Upload PDFs, Excel, Images and get AI insights instantly</p>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.info("📄 PDF Analysis")

        with col2:
            st.info("🧠 AI Insights")

        with col3:
            st.info("📊 Analytics")

    else:

        # =========================
        # INSIDE APP
        # =========================

        st.markdown("<h2 style='text-align:center;'>🤖 AI Document Assistant</h2>", unsafe_allow_html=True)

        uploaded_file = st.file_uploader("Upload your document", type=["pdf","xlsx","png","jpg","jpeg"])
    # ==========================
    # FEATURES
    # ==========================
    st.markdown("<br>", unsafe_allow_html=True)

    c1,c2,c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="card">
            <h1>📄</h1>
            <h2>Document Analysis</h2>
            <p>Extract information from documents instantly.</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="card">
            <h1>🧠</h1>
            <h2>AI Insights</h2>
            <p>Generate summaries and key findings automatically.</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="card">
            <h1>📊</h1>
            <h2>Analytics</h2>
            <p>View document statistics and metrics.</p>
        </div>
        """, unsafe_allow_html=True)

    # ==========================
    # SAMPLE METRICS
    # ==========================
    st.markdown("<br>", unsafe_allow_html=True)

    m1,m2,m3,m4 = st.columns(4)

    with m1:
        st.markdown("""
        <div class="metric-box">
        <div class="metric-number">12</div>
        <div class="metric-label">Pages</div>
        </div>
        """, unsafe_allow_html=True)

    with m2:
        st.markdown("""
        <div class="metric-box">
        <div class="metric-number">2.8K</div>
        <div class="metric-label">Words</div>
        </div>
        """, unsafe_allow_html=True)

    with m3:
        st.markdown("""
        <div class="metric-box">
        <div class="metric-number">18K</div>
        <div class="metric-label">Characters</div>
        </div>
        """, unsafe_allow_html=True)

    with m4:
        st.markdown("""
        <div class="metric-box">
        <div class="metric-number">92%</div>
        <div class="metric-label">Confidence</div>
        </div>
        """, unsafe_allow_html=True)

    # ==========================
    # START BUTTON
    # ==========================
    st.markdown("<br><br>", unsafe_allow_html=True)

    if st.button("🚀 Start Assistant", use_container_width=True):
     st.session_state.started = True
     st.rerun()
    st.success("Open your chatbot page here")
    st.markdown("""
    <h1 style='text-align:center;
    color:white;
    font-size:55px;
    font-weight:800;'>

    🤖 AI Document Assistant

    </h1>

    <p style='text-align:center;
    font-size:20px;
    color:#94A3B8;'>

    Upload PDFs, Excel files and Images.
    Get AI-powered insights instantly.

    </p>
    """, unsafe_allow_html=True)
        
    # =========================
    # GEMINI CLIENT
    # =========================
    client = genai.Client(
        api_key=" "
    )
        # =========================
    # GEMINI RESPONSE FUNCTION
    # =========================

    def generate_response(question, document_text):

        prompt = f"""
    You are an AI Document Assistant.

    Document Content:
    {document_text}

    User Question:
    {question}

    Answer clearly and accurately.
    """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text
    # =========================
    # FILE UPLOAD
    # =========================
    text = ""
    columns_text = ""
    file_type = None



    if uploaded_file:

        file_type = uploaded_file.name.split(".")[-1].lower()

        # =========================
        # PDF
        # =========================

        if file_type == "pdf":

            text = ""
            total_pages = 0
            page_texts = []

            try:

                pdf_bytes = uploaded_file.getvalue()

                with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:

                    total_pages = len(pdf.pages)

                    for page_num, page in enumerate(pdf.pages):

                        page_text = page.extract_text()

                        if page_text:
                            page_texts.append(
                                {
                                    "page": page_num + 1,
                                    "text": page_text
                                }
                            )

                            text += page_text + "\n"

                        tables = page.extract_tables()

                        for table in tables:

                            try:
                                df_table = pd.DataFrame(table)

                                text += "\n===== TABLE DATA =====\n"
                                text += df_table.to_csv(index=False)

                                for row in table:
                                    text += " | ".join(
                                        [str(x) for x in row if x]
                                    )
                                    text += "\n"

                            except:
                                pass

                # OCR Extraction
                try:

                    images = convert_from_bytes(
                        pdf_bytes,
                        poppler_path=r"poppler-26.02.0\Library\bin"
                    )

                    for img in images:

                        ocr_text = pytesseract.image_to_string(img)

                        if ocr_text.strip():
                            text += "\n===== OCR TEXT =====\n"
                            text += ocr_text

                except Exception as ocr_error:
                    st.warning(f"OCR Error: {ocr_error}")

                st.success("📄 PDF Loaded Successfully")
                st.markdown("### 📊 Document Metrics")

                col1, col2, col3 = st.columns(3)

                with col1:
                  st.metric("📄 Pages", total_pages)

                with col2:
                  st.metric("📝 Words", len(text.split()))

                with col3:
                 st.metric("🔤 Characters", len(text))
                st.session_state.document_text = text
                st.session_state.page_texts = page_texts
                doc_type = generate_response(
                "Identify document type only.",
                text[:10000]
    )

                st.sidebar.success(f"Detected: {doc_type}")

            except Exception as e:
                st.error(f"PDF Error: {e}")

        # =========================
        # EXCEL
        # =========================

        elif file_type == "xlsx":

            df = pd.read_excel(uploaded_file)

            df = df.fillna("")
            df = df.astype(str)

            text = df.to_csv(index=False)

            columns_text = ", ".join(df.columns)

            st.success("Excel Loaded Successfully")
            st.write("Rows:", len(df))
            st.write("Columns:", len(df.columns))

            st.dataframe(df.head(1000))

            st.session_state.document_text = text
            doc_type = generate_response(
        "Identify document type only.",
        text[:10000]
    )

            st.sidebar.success(f"Detected: {doc_type}")

        # =========================
        # IMAGE
        # =========================

        elif file_type in ["png", "jpg", "jpeg"]:

            image = Image.open(uploaded_file)

            st.image(image)

            if st.button("Analyze Image"):

                with st.spinner("Analyzing Image..."):

                    response = client.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=[
                            """
    Analyze this image.

    Provide:
    1. Summary
    2. Important Information
    3. Key Text
    4. Purpose
    """,
                            image
                        ]
                    )

                    st.write(response.text)

    # =========================
    # CHATGPT STYLE DOCUMENT ASSISTANT
    # =========================

    if st.session_state.document_text:

        st.success("✅ Document Loaded Successfully")

        if len(st.session_state.messages) == 0:
         st.session_state.messages.append(
            {
                "role": "assistant",
                "content": """
    🚀 Welcome to AI Document Assistant

    📄 Document loaded successfully.

    ✨ I can help you:

    • Summarize document
    • Extract key points
    • Find dates
    • Find amounts
    • Extract entities
    • Analyze invoices
    • Check security risks

    💬 Ask me anything about your document.
    """
            }
        )

        # =========================
        # CHAT HISTORY
        # =========================
        if len(st.session_state.messages) == 0:

         st.info("""
    👋 Welcome to AI Document Assistant

    You can ask:

    • Summarize document

    • Extract key points

    • Analyze invoice

    • Extract entities

    • Classify document

    • Check security risks

    • Ask any question from document
    """)

        for msg in st.session_state.messages:

         with st.chat_message(msg["role"]):

            st.markdown(f"""
            <div style="
                background:#111827;
                padding:15px;
                border-radius:15px;
                border:1px solid rgba(255,255,255,0.05);
                color:white;
            ">
            {msg["content"]}
            </div>
            """, unsafe_allow_html=True)

        # =========================
        # CHAT INPUT
        # =========================

        question = st.chat_input(
            "Ask anything about your document..."
        )

        if question:

            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": question
                }
            )

            with st.chat_message("user"):
                st.write(question)

            with st.spinner("Analyzing document..."):

                relevant_text = ""
                question_words = question.lower().split()

                if st.session_state.page_texts:

                    for page in st.session_state.page_texts:

                        score = 0

                        page_text = page["text"].lower()

                        for word in question_words:

                            if word in page_text:
                                score += 1

                        if score > 0:

                            relevant_text += (
                                f"\n\n===== PAGE {page['page']} =====\n"
                                + page["text"]
                            )

                if relevant_text.strip() == "":
                    relevant_text = st.session_state.document_text[:100000]

                question_lower = question.lower()

                # =========================
                # SUMMARY
                # =========================

                if (
                    "summary" in question_lower
                    or "summarize" in question_lower
                ):

                    prompt = f"""
    Summarize this document clearly.

    DOCUMENT:

    {st.session_state.document_text[:100000]}
    """

                # =========================
                # KEY POINTS
                # =========================

                elif "key point" in question_lower:

                    prompt = f"""
    Extract all important key points.

    DOCUMENT:

    {st.session_state.document_text[:100000]}
    """

                # =========================
                # INVOICE ANALYSIS
                # =========================

                elif (
                    "invoice" in question_lower
                    or "bill" in question_lower
                ):

                    prompt = f"""
    Analyze this invoice.

    Extract:

    1. Invoice Number
    2. Invoice Date
    3. Vendor Name
    4. Customer Name
    5. GST Number
    6. Tax Amount
    7. Total Amount
    8. Due Date
    9. Products or Services
    10. Payment Terms

    DOCUMENT:

    {st.session_state.document_text[:100000]}
    """

                # =========================
                # ENTITY EXTRACTION
                # =========================

                elif (
                    "entity" in question_lower
                    or "entities" in question_lower
                ):

                    prompt = f"""
    Extract:

    - Person Names
    - Organizations
    - Email IDs
    - Phone Numbers
    - Dates
    - Addresses
    - Employee IDs
    - Invoice Numbers
    - GST Numbers
    - Financial Amounts
    - Important Keywords

    DOCUMENT:

    {st.session_state.document_text[:100000]}
    """

                # =========================
                # DOCUMENT CLASSIFICATION
                # =========================

                elif (
                    "classify" in question_lower
                    or "classification" in question_lower
                    or "document type" in question_lower
                ):

                    prompt = f"""
    Identify:

    1. Document Type
    2. Purpose
    3. Category
    4. Confidence Percentage

    DOCUMENT:

    {st.session_state.document_text[:100000]}
    """

                # =========================
                # CYBER SECURITY
                # =========================

                elif (
                    "security" in question_lower
                    or "cyber" in question_lower
                    or "risk" in question_lower
                ):

                    prompt = f"""
    Analyze this document for:

    - Sensitive Information
    - Security Risks
    - Compliance Issues
    - Data Exposure
    - Recommendations

    DOCUMENT:

    {st.session_state.document_text[:100000]}
    """

                # =========================
                # DATES
                # =========================

                elif "date" in question_lower:

                    prompt = f"""
    Extract all dates with context.

    DOCUMENT:

    {st.session_state.document_text[:100000]}
    """

                # =========================
                # AMOUNTS
                # =========================

                elif (
                    "amount" in question_lower
                    or "price" in question_lower
                    or "cost" in question_lower
                ):

                    prompt = f"""
    Extract all financial amounts with context.

    DOCUMENT:

    {st.session_state.document_text[:100000]}
    """

                # =========================
                # GENERAL DOCUMENT CHAT
                # =========================

                else:

                    prompt = f"""
    You are an intelligent AI Document Assistant.

    Rules:

    1. Use ONLY document content.
    2. Do NOT guess.
    3. Search tables carefully.
    4. Search OCR text carefully.
    5. Mention page number if available.
    6. Give exact values.
    7. If information is missing say:
    "Information not found in document."

    DOCUMENT:

    {relevant_text}

    QUESTION:

    {question}
    """

                try:

                    response = client.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=prompt
                    )

                    answer = response.text

                except Exception as e:

                    answer = f"Error: {e}"

                with st.chat_message("assistant"):
                    st.write(answer)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer
                    }
                )
if __name__ == "__main__":
    chatbot_app()