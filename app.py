import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="BERT Sentiment Analyzer",
    page_icon="🎭",
    layout="centered"
)

@st.cache_resource
def load_model():
    return pipeline(
        "sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english"
    )

classifier = load_model()

st.title("🎭 BERT Sentiment Analyzer")
st.caption("Transformer-based NLP app using DistilBERT and Hugging Face")

st.write(
    "Enter a movie review and the app will classify it as Positive or Negative with a confidence score."
)

with st.expander("ℹ️ About this project"):
    st.write(
        """
        This project uses a pre-trained DistilBERT model for sentiment analysis.
        It demonstrates Natural Language Processing, Deep Learning, Transformer models,
        Hugging Face inference pipeline, and Streamlit deployment.
        """
    )

review = st.text_area(
    "Enter a movie review:",
    placeholder="Example: The movie was amazing with great acting and story.",
    height=150
)

if st.button("Analyze Sentiment", use_container_width=True):

    if review.strip() == "":
        st.warning("Please enter a review first.")

    else:
        result = classifier(review)[0]

        label = result["label"]
        score = result["score"]

        st.subheader("Result")

        if label == "POSITIVE":
            st.success("😊 Positive Sentiment Detected")
        else:
            st.error("😠 Negative Sentiment Detected")

        st.progress(float(score))
        st.write(f"Confidence Score: **{score:.2f}**")



# import streamlit as st
# from transformers import pipeline

# st.set_page_config(
#     page_title="BERT Sentiment Analyzer",
#     layout="centered"
# )

# @st.cache_resource
# def load_model():
#     return pipeline(
#         "sentiment-analysis",
#         model="distilbert-base-uncased-finetuned-sst-2-english"
#     )

# classifier = load_model()

# st.title("🎭 BERT Sentiment Analyzer")
# st.write("Analyze whether a movie review is positive or negative using a transformer-based NLP model.")

# review = st.text_area(
#     "Enter a movie review:",
#     placeholder="Example: The movie was amazing with great acting and story..."
# )

# if st.button("Analyze Sentiment"):
#     if review.strip() == "":
#         st.warning("Please enter a review first.")
#     else:
#         result = classifier(review)[0]

#         label = result["label"]
#         score = result["score"]

#         if label == "POSITIVE":
#             st.success(f"Positive Sentiment ✅")
#         else:
#             st.error(f"Negative Sentiment ❌")

#         st.write(f"Confidence Score: {score:.2f}")