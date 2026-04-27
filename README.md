# Social Media Content Generator

An AI-powered application that automatically generates engaging posts, captions, and hashtags for social media platforms using Generative AI models.

## 👤 Author

**GOPESH AGGARWAL**  
Roll No: 2301730158


## 📋 Description

This project leverages transformer-based AI models (specifically GPT-2) to create high-quality social media content. The application provides both a command-line interface (`content_generator.py`) and an interactive web UI (`app.py`) built with Streamlit, making it easy for users to generate content for various social media platforms.

## ✨ Features

- **AI-Powered Content Generation** - Uses GPT-2 for generating engaging social media posts
- **Post Generation** - Create original, engaging social media posts on any topic
- **Caption Generation** - Generate compelling captions for images and content
- **Hashtag Generation** - Automatically create relevant hashtags
- **Interactive Web UI** - User-friendly Streamlit interface
- **Customizable Parameters** - Control temperature, token length, and sampling parameters
- **Batch Processing** - Generate multiple variations of content

## 🛠️ Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd Socila-media
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 📦 Requirements

- `transformers` - Hugging Face transformers library for NLP models
- `langchain` - LangChain framework for language model applications
- `streamlit` - Web app framework for data science
- `huggingface_hub` - Hub API for model management
- `torch` - PyTorch deep learning framework
- `torchvision` - Computer vision utilities for PyTorch

## 🚀 Usage

### Web Interface (Recommended)

Run the Streamlit web application:

```bash
streamlit run app.py
```

The application will launch at `http://localhost:8501` in your browser. Use the intuitive interface to:
- Input topic/keywords
- Generate posts, captions, and hashtags
- Copy generated content to clipboard
- Adjust AI parameters for different content styles

### Command-Line Interface

Import and use the `content_generator.py` module directly:

```python
from content_generator import generate_post, generate_caption, generate_hashtags

# Generate a post
post = generate_post("artificial intelligence")
print(post)

# Generate a caption
caption = generate_caption("machine learning")
print(caption)

# Generate hashtags
hashtags = generate_hashtags("data science")
print(hashtags)
```

## 📝 Project Structure

```
Socila-media/
├── app.py                 # Streamlit web application
├── content_generator.py   # Core content generation module
├── requirements.txt       # Project dependencies
└── README.md             # This file
```

## ⚙️ Configuration

The AI model uses the following parameters for content generation:

- **Model**: GPT-2
- **Max Tokens**: 80 (adjustable)
- **Temperature**: 0.9 (controls randomness/creativity)
- **Top-p (Nucleus Sampling)**: 0.95
- **Repetition Penalty**: 1.2 (reduces repeated phrases)

## 📄 License

This project is developed as an educational initiative.

## 🤝 Contributing

Contributions are welcome! Feel free to fork, modify, and improve the project.

## 📧 Contact

For questions or suggestions, please reach out to the project author.

---

**Note**: This application requires an internet connection for the first run to download the GPT-2 model from Hugging Face Hub.
