# 🖼️ Image Caption Generator with Login

## 📌 Overview
This project is a Streamlit-based web application that allows users to **register**, **log in**, and generate **textual captions for images** using a machine learning model (`ViT-GPT2`). Additionally, it includes **text-to-speech** functionality to read the caption aloud. It's a complete ML web app with authentication, model inference, and media interaction.

---

## 🔑 Features

- 🔐 **User Authentication**  
  Users must register and log in before using the captioning feature.

- 📤 **Image Upload**  
  Upload `.jpg`, `.jpeg`, or `.png` images.

- 🤖 **Image Caption Generation**  
  Captions are generated using the `ViT-GPT2` model from Hugging Face.

- 🔊 **Text-to-Speech Conversion**  
  Captions are converted into speech using `gTTS` and can be played or downloaded as audio.

---

## ⚙️ Technologies Used

- **Python Libraries:** Streamlit, Transformers, Torch, gTTS, Pillow  
- **Model Used:** `nlpconnect/vit-gpt2-image-captioning`  
- **Frontend/UI:** Built with Streamlit for interactivity and simplicity


---

## 🚀 How to Use This Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/image-caption-generator.git
cd image-caption-generator
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```
### 3️⃣ Run the Application
```
streamlit run app.py
```
---
## 🧠 How It Works

🔍 Input: After logging in, the user uploads an image.

🧠 Prediction: The app uses a Vision Transformer (ViT) + GPT-2 model to generate a descriptive caption.

🔉 Audio: The generated caption is passed to a text-to-speech engine (gTTS), and the audio is playable/downloadable.


---
## Screenshots

![Screenshot 2025-04-20 160408](https://github.com/user-attachments/assets/73369418-0cd6-415f-90c3-6e39992aab20)
![Screenshot 2025-04-20 160434](https://github.com/user-attachments/assets/0633572a-66a4-4625-aa04-df90977c7cf7)
![Screenshot 2025-04-20 160521](https://github.com/user-attachments/assets/b17e6710-59cd-47b0-8c96-226b1bd7f77d)
![Screenshot 2025-04-20 160722](https://github.com/user-attachments/assets/c91af4fb-fd23-4d22-8163-9e55f4b29a22)

---

## 📦 Model Used
```nlpconnect/vit-gpt2-image-captioning ```
Combines a Vision Transformer (ViT) for image feature extraction and GPT-2 for language generation.

---

## Contributing

Contributions are always welcome!

 If you want to make any improvements or add new features, feel free to open an issue or submit a pull request.
 
Please adhere to this project's `code of conduct`.


## 📄 License
This project is open source and available under the MIT License.

---

## 🙌 Acknowledgements
Hugging Face for the ViT-GPT2 model

Streamlit for the interactive UI framework

Google Text-to-Speech (gTTS) for audio output


## Contact
For any questions or feedback, please reach out to rajkumarnainala08@gmail.com.




