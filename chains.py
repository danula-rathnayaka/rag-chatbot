from langchain_core.prompts import PromptTemplate
from langchain_ollama.llms import OllamaLLM
from typing import List


class Chain:
    def __init__(self):
        # Initialize the LLM with the specified model and temperature
        self.llm = OllamaLLM(
            model="llama3.2:latest",
            temperature=0
        )

    def answer_question(self, question: str, faqs: List[str]):
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
        return res
