from llm_client import LLMClient

class Agent:
    def __init__(self, prompt_path):
        self.llm = LLMClient()
        with open(prompt_path, "r", encoding="utf-8") as f:
            self.system_prompt = f.read()

    def run(self, input_text, temperature=0.2):
        return self.llm.generate(
            system_prompt=self.system_prompt,
            user_prompt=input_text,
            temperature=temperature
        )
