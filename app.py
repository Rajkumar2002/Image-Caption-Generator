import streamlit as st
st.set_page_config(page_title="Image Caption Generator", layout="centered")

from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
from PIL import Image
import torch
from gtts import gTTS
import tempfile
import base64

# ========== Load Model ==========
@st.cache_resource
def load_model():
    model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
    processor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
    tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
    return model, processor, tokenizer

model, feature_extractor, tokenizer = load_model()
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# ========== In-Memory User Store (For Demo) ==========
if "users" not in st.session_state:
    st.session_state.users = {}

if "registered" not in st.session_state:
    st.session_state.registered = False

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ========== Utility Functions ==========
def generate_caption(image):
    if image.mode != "RGB":
        image = image.convert(mode="RGB")
    pixel_values = feature_extractor(images=[image], return_tensors="pt").pixel_values
    pixel_values = pixel_values.to(device)

    gen_kwargs = {"max_length": 16, "num_beams": 4}
    output_ids = model.generate(pixel_values, **gen_kwargs)
    preds = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
    return preds[0].strip()

def text_to_speech(text):
    tts = gTTS(text)
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(temp_file.name)
    return temp_file.name

def get_audio_download_link(audio_path, filename="audio.mp3"):
    with open(audio_path, "rb") as f:
        audio_bytes = f.read()
    b64 = base64.b64encode(audio_bytes).decode()
    href = f'<a href="data:audio/mp3;base64,{b64}" download="{filename}">Download Audio</a>'
    return href

# ========== Streamlit UI ==========
st.title("🖼️ Image Caption Generator")

# ----- Registration First -----
# ----- Registration First -----
if not st.session_state.registered:
    st.subheader("🔐 Register First")
    reg_username = st.text_input("Choose a Username")
    reg_password = st.text_input("Choose a Password", type="password")
    if st.button("Register"):
        if reg_username in st.session_state.users:
            st.warning("Username already exists.")
        elif reg_username.strip() == "" or reg_password.strip() == "":
            st.warning("Please fill out all fields.")
        else:
            st.session_state.users[reg_username] = reg_password
            st.session_state.registered = True
            st.success("✅ Registration successful! Redirecting to login...")
            st.experimental_rerun()


# ----- Login Only After Registration -----
elif not st.session_state.logged_in:
    st.subheader("🔓 Login")
    login_username = st.text_input("Username")
    login_password = st.text_input("Password", type="password")
    if st.button("Login"):
        if login_username in st.session_state.users and st.session_state.users[login_username] == login_password:
            st.session_state.logged_in = True
            st.session_state.temp_user = login_username
            st.success("Login successful!")
        else:
            st.error("Invalid username or password")

# ----- Logout Sidebar -----
if st.session_state.logged_in:
    st.sidebar.success(f"👤 Logged in as **{st.session_state.temp_user}**")
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.registered = False
        st.experimental_rerun()

# ----- Auth Gate -----
if not st.session_state.logged_in:
    st.warning("Please register and login to continue.")
    st.stop()

# ----- Upload and Caption -----
uploaded_image = st.file_uploader("📤 Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("🧠 Generate Caption"):
        with st.spinner("Generating..."):
            caption = generate_caption(image)
            st.success("📝 Caption Generated:")
            st.write(f"**{caption}**")

            # Text to speech
            audio_path = text_to_speech(caption)
            st.audio(audio_path, format="audio/mp3")
            st.markdown(get_audio_download_link(audio_path), unsafe_allow_html=True)
