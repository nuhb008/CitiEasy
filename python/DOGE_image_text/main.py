import streamlit as st
from helpers.image_utils import encode_image_to_base64
from helpers.api_utils import extract_text_from_image, summarize_text, generate_insights

# Initialize session state variables
if "extracted_text" not in st.session_state:
    st.session_state.extracted_text = ""
if "summary" not in st.session_state:
    st.session_state.summary = ""
if "insights" not in st.session_state:
    st.session_state.insights = ""

st.title("Image-to-Insights Workflow with Grok Vision")

# File uploader
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    # Display the uploaded image
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    # Save the image to a temporary location
    with open("temp_image.jpg", "wb") as f:
        f.write(uploaded_file.read())

    # Encode image to Base64
    st.info("Encoding image...")
    image_base64 = encode_image_to_base64("temp_image.jpg")
    st.success("Image encoded successfully!")

    # Call API to extract text
    st.info("Extracting text from the image...")
    st.session_state.extracted_text = extract_text_from_image(image_base64)
    st.success("Text extracted successfully!")

# Display the extracted text
if st.session_state.extracted_text:
    st.subheader("Extracted Text:")
    st.text_area("Extracted Text", st.session_state.extracted_text, height=200)

    # Summarize the extracted text
    if st.button("Summarize Text"):
        st.info("Summarizing text...")
        st.session_state.summary = summarize_text(st.session_state.extracted_text)
        st.success("Text summarized successfully!")

# Display the summary
if st.session_state.summary:
    st.subheader("Summary:")
    st.text_area("Summary", st.session_state.summary, height=150)

    # Generate insights from the summary
    if st.button("Generate Insights"):
        st.info("Generating actionable insights...")
        st.session_state.insights = generate_insights(st.session_state.summary)
        st.success("Insights generated successfully!")

# Display the insights
if st.session_state.insights:
    st.subheader("Actionable Insights:")
    st.text_area("Insights", st.session_state.insights, height=150)