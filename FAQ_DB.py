import pandas as pd
import chromadb
import uuid


class FAQ_DB:
    """
    A class for managing a FAQ database using a CSV file and ChromaDB vector store.

    This class loads FAQs from a CSV file, stores them in a persistent ChromaDB vector store,
    and provides methods to query the most relevant FAQs, retrieve the entire dataset,
    and add new entries.
    """

    def __init__(self, file_path="resources/faqs.csv", collection_name="faqs", db_path="vectorstore"):
        """
        Initializes the FAQ_DB instance.

        Args:
            file_path (str): Path to the CSV file containing the FAQs.
            collection_name (str): Name of the ChromaDB collection.
            db_path (str): Path to the persistent ChromaDB storage.
        """
        self.file_path = file_path
        self.data = pd.read_csv(file_path)
        self.chroma_client = chromadb.PersistentClient(db_path)
        self.collection = self.chroma_client.get_or_create_collection(name=collection_name)
        self.load_faqs()

    def load_faqs(self):
        """
        Loads FAQs into the vector store if it is currently empty.

        This method iterates over the DataFrame and adds each question-answer pair
        to the ChromaDB collection using unique IDs.
        """

        if not self.collection.count():
            for _, row in self.data.iterrows():
                self.collection.add(
                    documents=[row["question"]],
                    metadatas=[{"question": row["question"], "answer": row["answer"]}],
                    ids=[str(uuid.uuid4())]
                )

    def query_faqs(self, question):
        """
        Queries the vector store to find the top matching FAQs for a given question.

        Args:
            question (str): The user’s query.

        Returns:
            list: A list of metadata dictionaries for the top matching FAQs.
        """
        return self.collection.query(query_texts=[question], n_results=3).get('metadatas', [])

    def get_data(self):
        """
        Retrieves the entire FAQ dataset as a DataFrame.

        Returns:
            pd.DataFrame: The full set of FAQs.
        """
        return self.data

    def add_data(self, question, answer):
        """
        Adds a new FAQ to both the CSV dataset and the vector store.

        Args:
           question (str): The new FAQ question.
           answer (str): The corresponding answer.

        This method updates both the in-memory dataset and persists the new entry
        to the CSV file and the ChromaDB collection.
        """
        # Append the new FAQ to the dataset and vector store
        new_entry = pd.DataFrame({"question": [question], "answer": [answer]})
        self.data = pd.concat([self.data, new_entry], ignore_index=True)
        self.collection.add(
            documents=[question],
            metadatas=[{"question": question, "answer": answer}],
            ids=[str(uuid.uuid4())]
        )

        # Persist updated data to CSV
        self.data.to_csv(self.file_path, index=False)
