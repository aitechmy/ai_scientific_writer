from llm_client import LLMClient

llm = LLMClient()

output = llm.generate(
    system_prompt="You are a strict tester.",
    user_prompt="Reply only with the word SUCCESS.",
    temperature=0.0
)

print(output)
