from openai import OpenAI

def generate_study_questions(text: str) -> str:
    client = OpenAI()
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an AI that creates study questions by summarizing text and taking out the key concepts. You will create five multiple choice questions based off the given study material"},
            {"role": "user", "content": f"Create five multiple choice questions for me based on this study material {text}"}
        ],
    )
    
    return response.choices[0].message.content