import streamlit as st
from transformers import pipeline

# Load the sentiment analysis pipeline
sent_pipeline = pipeline("sentiment-analysis")

# Define the Streamlit app
def main():
    st.title("Sentiment Analysis with Streamlit")

    # Input from user
    text = st.text_area("Enter English text for sentiment analysis:")

    if st.button("Analyze"):
        if text:
            # Analyze sentiment
            result = sent_pipeline(text)
            sentiment = result[0]['label']
            score = result[0]['score']

            # Display results
            st.write(f"Sentiment: {sentiment}")
            st.write(f"Confidence Score: {score:.2f}")
        else:
            st.warning("Please enter some text.")

if __name__ == "__main__":
    main()
