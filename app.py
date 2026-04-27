"""
Social Media Content Generator - Streamlit Web Application
Author: GOPESH AGGARWAL
Roll No: 2301730158

Description:
Interactive web interface for generating social media content using AI.
This application provides an easy-to-use interface for creating posts,
captions, and hashtags automatically.
"""

import streamlit as st
from transformers import pipeline
import random

# Page configuration
st.set_page_config(
    page_title="Social Media Content Generator",
    page_icon="🚀",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 0;
    }
    .sub-header {
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .content-box {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)


@st.cache_resource
def load_model():
    """
    Load the AI model (cached for performance)
    Implemented by: GOPESH AGGARWAL (2301730158)
    """
    return pipeline("text-generation", model="gpt2")


def generate_post(topic, generator):
    """
    Generate an engaging social media post using AI
    Author: GOPESH AGGARWAL (2301730158)
    """
    import re
    
    # Better prompt for social media post generation
    prompt = f"Write an engaging social media post about {topic}. Make it exciting and professional:\n\n"
    
    try:
        # Generate with GPT-2
        result = generator(
            prompt, 
            max_new_tokens=80,
            num_return_sequences=1,
            temperature=0.9,
            top_p=0.95,
            do_sample=True,
            pad_token_id=generator.tokenizer.eos_token_id,
            repetition_penalty=1.2
        )
        
        generated_text = result[0]['generated_text']
        
        # Remove the prompt
        if prompt in generated_text:
            generated_text = generated_text.replace(prompt, "").strip()
        
        # Clean up the text
        # Remove incomplete sentences at the end
        sentences = [s.strip() for s in generated_text.split('.') if s.strip()]
        
        # Keep first 2-3 complete sentences
        if len(sentences) >= 2:
            clean_post = '. '.join(sentences[:3]) + '.'
        elif len(sentences) == 1:
            clean_post = sentences[0] + '.'
        else:
            clean_post = generated_text
        
        # Remove any URLs or website references
        clean_post = re.sub(r'http[s]?://\S+|www\.\S+', '', clean_post)
        
        # Remove any email addresses
        clean_post = re.sub(r'\S+@\S+', '', clean_post)
        
        # Remove multiple spaces
        clean_post = re.sub(r'\s+', ' ', clean_post).strip()
        
        # Add emojis for engagement
        emojis = ['✨', '🚀', '💡', '🌟', '🎯', '💫', '🔥', '⭐']
        import random
        if clean_post and len(clean_post) > 20:
            emoji = random.choice(emojis)
            clean_post = f"{emoji} {clean_post} {emoji}"
        
        # Validate output quality
        if len(clean_post) < 30 or not clean_post[0].isupper():
            raise ValueError("Low quality output")
        
        return clean_post
        
    except Exception as e:
        # Fallback to a good template if AI fails
        templates = [
            f"🌟 Discover the amazing world of {topic}! Join thousands exploring this exciting field. What makes {topic} fascinating? Let's dive in and find out together! ✨",
            f"💡 Ready to explore {topic}? This dynamic field is full of opportunities and innovation. Whether you're new or experienced, there's always something exciting to learn! 🚀",
            f"🎯 {topic} is transforming the way we think! From cutting-edge trends to timeless wisdom, join us on this incredible journey of discovery and growth! 🌟"
        ]
        import random
        return random.choice(templates)


def generate_caption(topic, generator):
    """
    Generate a catchy caption using AI
    Author: GOPESH AGGARWAL (2301730158)
    """
    import re
    
    # Better prompt for caption generation
    prompt = f"Write a short, catchy Instagram caption about {topic} in 5-10 words:\n\n"
    
    try:
        # Generate with GPT-2
        result = generator(
            prompt, 
            max_new_tokens=20,
            num_return_sequences=1,
            temperature=0.8,
            top_p=0.9,
            do_sample=True,
            pad_token_id=generator.tokenizer.eos_token_id,
            repetition_penalty=1.3
        )
        
        generated_text = result[0]['generated_text']
        
        # Remove the prompt
        if prompt in generated_text:
            generated_text = generated_text.replace(prompt, "").strip()
        
        # Take first line or sentence
        caption = generated_text.split('\n')[0].split('.')[0].strip()
        
        # Remove any URLs or unwanted content
        caption = re.sub(r'http[s]?://\S+|www\.\S+', '', caption)
        caption = re.sub(r'\S+@\S+', '', caption)
        caption = re.sub(r'\s+', ' ', caption).strip()
        
        # Add emoji if not present
        emojis = ['✨', '💫', '🌟', '🎯', '💕', '🌈', '⭐', '🚀', '💭', '🔥']
        import random
        if caption and len(caption) > 10 and len(caption) < 100:
            if not any(e in caption for e in emojis):
                emoji = random.choice(emojis)
                caption = f"{caption} {emoji}"
            return caption
        else:
            raise ValueError("Caption too short or too long")
            
    except Exception as e:
        # Fallback templates
        captions = [
            f"✨ {topic} vibes only!",
            f"Living for {topic} moments 💫",
            f"When {topic} meets passion 🌟",
            f"{topic} is my happy place 🌈",
            f"Can't get enough of {topic}! ⭐"
        ]
        import random
        return random.choice(captions)


def generate_hashtags(topic):
    """
    Generate relevant hashtags
    Author: GOPESH AGGARWAL (2301730158)
    """
    import random
    
    # Create hashtags from topic words
    words = topic.split()
    topic_tags = ["#" + word.capitalize() for word in words]
    
    # Relevant extra hashtags
    extra_tags = [
        "#Trending", "#Viral", "#Inspiration", "#MustSee", "#Amazing",
        "#Awesome", "#Love", "#InstaGood", "#Beautiful", "#Style",
        "#Life", "#Photography", "#InspirationDaily", "#Motivation",
        "#Goals", "#Success", "#Creative", "#Innovation", "#Community"
    ]
    
    # Select 4-5 extra tags randomly
    selected_extras = random.sample(extra_tags, min(5, len(extra_tags)))
    
    # Combine and return
    all_tags = topic_tags + selected_extras
    return " ".join(all_tags[:8])  # Limit to 8 tags total


# Main Application
def main():
    """
    Main Streamlit application
    Developed by: GOPESH AGGARWAL (2301730158)
    """
    
    # Header
    st.markdown('<h1 class="main-header">🚀 Social Media Content Generator</h1>', 
                unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Powered by AI | Developed by GOPESH AGGARWAL (2301730158)</p>', 
                unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.header("📋 Project Information")
        st.write("**Developer:** GOPESH AGGARWAL")
        st.write("**Roll No:** 2301730158")
        st.write("**Project:** Social Media Content Generator")
        st.divider()
        st.write("**Technologies Used:**")
        st.write("- Python")
        st.write("- Hugging Face Transformers")
        st.write("- Streamlit")
        st.write("- GPT-2 Model")
        st.divider()
        st.info("💡 Enter a topic and click 'Generate Content' to create AI-powered social media posts!")
    
    # Load model
    with st.spinner("🔄 Loading AI model..."):
        generator = load_model()
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        topic = st.text_input(
            "📝 Enter Topic or Keyword:",
            placeholder="e.g., Artificial Intelligence in Education",
            help="Enter any topic you want to create content about"
        )
    
    with col2:
        st.write("")  # Spacing
        st.write("")  # Spacing
        generate_button = st.button("✨ Generate Content", type="primary", use_container_width=True)
    
    # Generate content when button is clicked
    if generate_button:
        if topic:
            with st.spinner("🤖 AI is generating your content... Please wait."):
                try:
                    # Generate all content
                    post = generate_post(topic, generator)
                    caption = generate_caption(topic, generator)
                    hashtags = generate_hashtags(topic)
                    
                    # Display results
                    st.success("✅ Content generated successfully!")
                    
                    # Post section
                    st.markdown("### 📝 Generated Post")
                    st.markdown(f'<div class="content-box">{post}</div>', 
                              unsafe_allow_html=True)
                    
                    # Caption section
                    st.markdown("### 💬 Generated Caption")
                    st.markdown(f'<div class="content-box">{caption}</div>', 
                              unsafe_allow_html=True)
                    
                    # Hashtags section
                    st.markdown("### 🏷️ Generated Hashtags")
                    st.markdown(f'<div class="content-box">{hashtags}</div>', 
                              unsafe_allow_html=True)
                    
                    # Footer
                    st.divider()
                    st.caption("Content generated by AI | Created by GOPESH AGGARWAL (2301730158)")
                    
                except Exception as e:
                    st.error(f"❌ Error generating content: {str(e)}")
        else:
            st.warning("⚠️ Please enter a topic or keyword first!")
    
    # Instructions
    if not generate_button:
        st.markdown("---")
        st.markdown("### 📖 How to Use:")
        st.markdown("""
        1. Enter a topic or keyword in the text box above
        2. Click the **Generate Content** button
        3. Wait for the AI to generate your content
        4. Copy and use the generated post, caption, and hashtags!
        
        **Example topics:** Technology, Travel, Food, Fashion, Fitness, Business
        """)


if __name__ == "__main__":
    main()
