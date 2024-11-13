from openai import OpenAI
import os

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o-mini"

def generate_study_guide(text: str) -> str:
    client = OpenAI(
        base_url=endpoint,
        api_key=token
    )
    
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are an AI that creates study guides by summarizing text into clear, concise notes, with explanations of key ideas and concepts."},
            {"role": "user", "content": f"Summarize the following text as if creating a study guide. Include the main points and any relevant examples or explanations for better understanding: {text}"}
        ],
        temperature=1.0,
        top_p=1.0,
        max_tokens=1000,
        model="gpt-4o-mini"
    )
    
    return response.choices[0].message.content