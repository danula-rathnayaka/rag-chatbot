import pandas as pd
import os


def save_qa_to_csv(question, answer, folder="outputs/", filename="qa_log.csv"):
    # Create a DataFrame with the current question and answer
    new_entry = pd.DataFrame({"Question": [question], "Answer": [answer]})

    # Create output folder if not exists
    os.makedirs(folder, exist_ok=True)

    # Check if the file already exists
    if os.path.exists(folder + filename):
        # Read existing data and append the new entry
        existing_data = pd.read_csv(folder + filename)
        updated_data = pd.concat([existing_data, new_entry], ignore_index=True)
    else:
        # If file doesn't exist, start with the new entry
        updated_data = new_entry

    # Save the updated data to CSV
    updated_data.to_csv(folder + filename, index=False)
