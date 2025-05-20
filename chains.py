from langchain_core.prompts import PromptTemplate
from langchain_ollama.llms import OllamaLLM
from typing import List


class Chain:
    """
    A simple question-answering chain using an LLM and a list of FAQs.

    The chain is designed to answer a user-provided question using a predefined
    list of frequently asked questions (FAQs). If the answer cannot be inferred
    from the FAQs, the system responds appropriately.
    """

    def __init__(self):
        """
        Initializes the Chain with a specific LLM model (`llama3.2:latest`)
        and sets the temperature to 0 for deterministic output.
        """
        self.llm = OllamaLLM(
            model="llama3.2:latest",
            temperature=0
        )

    def answer_question(self, question: str, faqs: List[str]):
        """
        Answers a given question using a list of FAQs.

        Args:
            question (str): The user's question.
            faqs (List[str]): A list of frequently asked questions (and answers).

        Returns:
            str: The AI-generated answer based on the FAQs. If no relevant
                 answer is found, a fallback message is returned.
        """

        # Format the FAQs as a bullet-pointed string
        faqs_text = "\n".join(f"- {faq}" for faq in faqs)

        # Create the prompt template with placeholders for question and FAQs
        prompt_extract = PromptTemplate.from_template(
            """
            You are an AI assistant. Use the provided FAQs to answer the user's question. 
            If the answer is not in the FAQs, say "I don't know."

            Question: {question}
            FAQs:
            {faqs}
            """
        )

        # Combine the prompt with the language model
        chain_extract = prompt_extract | self.llm

        # Execute the chain with the user's input
        res = chain_extract.invoke(input={"question": question, "faqs": faqs_text})

        if "don't know" in res.lower() or "not in the faqs" in res.lower():
            res = "I couldn't find a relevant answer. Please rephrase your question."

        return res
