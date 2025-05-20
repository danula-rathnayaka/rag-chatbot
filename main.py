import streamlit as st
from FAQ_DB import FAQ_DB
from chains import Chain
from qa_logger import save_qa_to_txt


# Function to create the Streamlit app
def create_streamlit_app():
    st.title("🤖 FAQ RAG Chatbot")
    st.markdown("""
            Ask any question related to the knowledge base. The chatbot will retrieve relevant FAQs and answer your question using a language model.
        """)

    # Initialize FAQ and Chain objects if not already in session state
    if 'faq_obj' not in st.session_state:
        st.session_state.faq_obj = FAQ_DB()
    if 'chain' not in st.session_state:
        st.session_state.chain = Chain()

    faq_db = st.session_state.faq_obj
    chain = st.session_state.chain

    # User input for question
    question = st.text_input("Ask a question:", value="What is Agentic AI?")
    submit_button = st.button("Get Answer")

    # Process input when submit button is clicked
    if submit_button and question.strip():
        try:
            # Retrieve relevant FAQs and generate an answer
            faqs_list = faq_db.query_faqs(question)
            answer = chain.answer_question(question, faqs_list)

            save_qa_to_txt(question, answer)

            st.subheader("Chatbot Answer:")
            st.write(answer)

            st.subheader("Top Retrieved FAQs:")

            for idx, item in enumerate(faqs_list[0], 1):
                st.markdown(f"Q: {item['question']}")
                st.markdown(f"       A: {item['answer']}")
                st.markdown("---")

        except Exception as e:
            st.error(f"An error occurred: {e}")

    # Display the current FAQ knowledge base
    st.subheader("Current FAQ Knowledge Base")
    st.dataframe(faq_db.get_data())

    if st.button("Refresh Table"):
        st.session_state.faq_data = faq_db.get_data()

    # Add a new FAQ
    st.subheader("Add a New FAQ")
    with st.form("add_faq_form"):
        new_question = st.text_input("New FAQ Question")
        new_answer = st.text_input("New FAQ Answer")
        submitted = st.form_submit_button("Add FAQ")
        if submitted and new_question and new_answer:
            faq_db.add_data(new_question, new_answer)
            st.session_state.faq_data = faq_db.get_data()
            st.success("FAQ added!")


# Main function to configure Streamlit settings and run the app
if __name__ == "__main__":
    st.set_page_config(page_title="FAQ RAG Chatbot", layout="wide", page_icon="🤖")
    create_streamlit_app()
