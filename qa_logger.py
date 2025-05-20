import os


def save_qa_to_txt(question, answer, folder="outputs/", filename="qa_log.txt"):
    """
    Appends a question and its corresponding answer to a text file.
    Creates the output directory if it does not exist.

    Args:
        question (str): The user's question.
        answer (str): The chatbot's answer.
        folder (str): Directory to save the log file.
        filename (str): Name of the log file.
    """
    # Ensure the output directory exists
    os.makedirs(folder, exist_ok=True)
    file_path = os.path.join(folder, filename)

    # Append the Q&A to the text file
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(f"Question: {question}\n")
        f.write(f"Chatbot: {answer}\n\n")
