"""
Social Media Content Generator
Author: GOPESH AGGARWAL
Roll No: 2301730158

Description:
An AI-powered application that automatically generates engaging posts, 
captions, and hashtags for social media platforms using Generative AI models.
"""

from transformers import pipeline
import random

# Initialize the text generation model
# Created by: GOPESH AGGARWAL (2301730158)
print("Loading AI model... Please wait.")
generator = pipeline("text-generation", model="gpt2")
print("Model loaded successfully!")


def generate_post(topic):
    """
    Generate an engaging social media post using AI
    Author: GOPESH AGGARWAL (2301730158)
    
    Args:
        topic (str): The topic or keyword for the post
    
    Returns:
        str: Generated social media post
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
        return random.choice(templates)


def generate_caption(topic):
    """
    Generate a catchy caption using AI
    Author: GOPESH AGGARWAL (2301730158)
    
    Args:
        topic (str): The topic or keyword for the caption
    
    Returns:
        str: Generated caption
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
        return random.choice(captions)


def generate_hashtags(topic):
    """
    Generate relevant hashtags
    Author: GOPESH AGGARWAL (2301730158)
    
    Args:
        topic (str): The topic or keyword for hashtags
    
    Returns:
        str: Generated hashtags
    """
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


def main():
    """
    Main function to run the Social Media Content Generator
    Developed by: GOPESH AGGARWAL (2301730158)
    """
    print("\n" + "="*60)
    print("   SOCIAL MEDIA CONTENT GENERATOR")
    print("   Developed by: GOPESH AGGARWAL")
    print("   Roll No: 2301730158")
    print("="*60 + "\n")
    
    topic = input("Enter topic or keyword: ")
    
    print("\n🤖 Generating content... Please wait.\n")
    
    # Generate content using AI models
    post = generate_post(topic)
    caption = generate_caption(topic)
    hashtags = generate_hashtags(topic)
    
    # Display generated content
    print("\n" + "="*60)
    print("--- GENERATED CONTENT ---")
    print("="*60 + "\n")
    
    print("📝 POST:")
    print(post)
    print("\n" + "-"*60 + "\n")
    
    print("💬 CAPTION:")
    print(caption)
    print("\n" + "-"*60 + "\n")
    
    print("🏷️  HASHTAGS:")
    print(hashtags)
    print("\n" + "="*60)
    print("\n✅ Content generated successfully!")
    print("   Created by: GOPESH AGGARWAL (2301730158)")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
