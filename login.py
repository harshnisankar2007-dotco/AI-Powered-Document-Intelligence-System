import streamlit as st
import text

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

st.set_page_config(
    page_title="AI Document Assistant",
    page_icon="🤖",
    layout="wide"
)

# =====================================
# CUSTOM CSS
# =====================================
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg,#0f172a,#1e293b,#0f172a);
}

.main-title{
    text-align:center;
    color:white;
    font-size:52px;
    font-weight:bold;
}

.sub-title{
    text-align:center;
    color:#cbd5e1;
    font-size:20px;
    margin-bottom:30px;
}

.feature-box{
    background:#1e293b;
    padding:20px;
    border-radius:15px;
    text-align:center;
    color:white;
    border:1px solid #334155;
}

.stTextInput input{
    border-radius:12px;
}

.stButton button{
    width:100%;
    background:#10a37f;
    color:white;
    border:none;
    border-radius:12px;
    height:50px;
    font-size:18px;
    font-weight:bold;
}

.stButton button:hover{
    background:#0d8b6b;
    color:white;
}

.metric-card{
    background:#1e293b;
    padding:20px;
    border-radius:15px;
    text-align:center;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# LOGIN PAGE
# =====================================
if not st.session_state.logged_in:

    st.markdown(
        "<div class='main-title'>🤖 AI DOCUMENT ASSISTANT</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='sub-title'>Upload Documents • Analyze Content • Chat with AI</div>",
        unsafe_allow_html=True
    )

    col_img1, col_img2, col_img3 = st.columns([1,2,1])

    with col_img2:
        st.image(
            "https://cdn-icons-png.flaticon.com/512/4712/4712109.png",
            width=180
        )

    st.write("")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class='feature-box'>
        📄<br><br>
        <b>PDF Analysis</b><br>
        Extract and understand documents instantly
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class='feature-box'>
        🤖<br><br>
        <b>AI Chat</b><br>
        Ask questions from uploaded files
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class='feature-box'>
        ⚡<br><br>
        <b>Instant Answers</b><br>
        Get responses within seconds
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        st.markdown("### 🔐 Login")

        email = st.text_input(
            "📧 Email Address",
            placeholder="Enter Email"
        )

        password = st.text_input(
            "🔒 Password",
            type="password",
            placeholder="Enter Password"
        )

        remember = st.checkbox("Remember Me")

        if st.button("🚀 Login"):

            if email.strip() and password.strip():

                st.session_state.logged_in = True
                st.success("Login Successful")
                st.rerun()

            else:
                st.error("Please enter Email and Password")

# =====================================
# DASHBOARD AFTER LOGIN
# =====================================


else:

    with st.sidebar:
        st.success("✅ Logged In")

        if st.button("🚪 Logout"):
            st.session_state.logged_in = False
            st.rerun()

    text.chatbot_app()