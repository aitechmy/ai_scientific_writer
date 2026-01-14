from openai import OpenAI

class LLMClient:
    def __init__(self):
        self.client = OpenAI(
            base_url="http://localhost:1234/v1",
            api_key="lm-studio"
        )

    def generate(self, system_prompt, user_prompt, temperature=0.2):
        response = self.client.chat.completions.create(
            model="local-model",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=temperature,
        )
        return response.choices[0].message.content.strip()
