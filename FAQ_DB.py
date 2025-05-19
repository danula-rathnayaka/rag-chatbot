import pandas as pd
import chromadb
import uuid


class FAQ_DB:
    def __init__(self, file_path="resources/faqs.csv", collection_name="faqs", db_path="vectorstore"):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)
        self.chroma_client = chromadb.PersistentClient(db_path)
        self.collection = self.chroma_client.get_or_create_collection(name=collection_name)
        self.load_faqs()

    def load_faqs(self):
        # Populate the vector store if it's empty
        if not self.collection.count():
            for _, row in self.data.iterrows():
                self.collection.add(
                    documents=[row["question"]],
                    metadatas=[{"question": row["question"], "answer": row["answer"]}],
                    ids=[str(uuid.uuid4())]
                )

    def query_faqs(self, question):
        # Retrieve the top matching FAQs based on the query
        return self.collection.query(query_texts=[question], n_results=3).get('metadatas', [])

    def get_data(self):
        # Return the full FAQ dataset
        return self.data

    def add_data(self, question, answer):
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
