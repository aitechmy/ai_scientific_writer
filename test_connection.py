from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"
)

response = client.chat.completions.create(
    model="local-model",
    messages=[
        {"role": "system", "content": "You are a test system."},
        {"role": "user", "content": "Reply with: CONNECTION_OK"}
    ],
    temperature=0.3
)

print(response.choices[0].message.content)
