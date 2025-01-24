from openai import OpenAI

with open('keys.txt', 'r') as file:
        KEY = file.read()

def generate_study_questions(text: str) -> str:
    client = OpenAI(api_key=KEY)
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "tutor",
             "content": """You are an AI that creates study questions by summarizing text and taking out the key concepts. 
                You will create between five and eight multiple choice questions based off the given study material. 
                I want you to only give me output with the following base format {
                "questions": [
                    {
                    "id": 1,
                    "question": "What is the main idea of slide 3?",
                    "options": [
                        "Option A",
                        "Option B",
                        "Option C",
                        "Option D"
                    ],
                    "answer": "Option B",
                    "explanation": "Slide 3 focuses on..."
                    },
                    {
                    "id": 2,
                    "question": "Describe the key concept introduced on slide 5.",
                    "options": [],
                    "answer": "Open-ended",
                    "explanation": null
                    }
                ],
                "metadata": {
                    "source": "input.pdf",
                    "generated_on": "todays date in the following format: YYYY-MM-DD",
                    "total_questions": "Add the number of Questions as a integer. Example: 5",
                    "best_score": "N/A",
                    "attempts": 0
                }
                }"""},
            {"role": "user", "content": f"Create between five and eight multiple choice questions for me based on this study material {text}"}
        ],
    )
    
    return response.choices[0].message.content