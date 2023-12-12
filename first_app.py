from openai_key import API_KEY
from openai import OpenAI

client=OpenAI(api_key=API_KEY)
def main():
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]
    )
   
    for choice in completion.choices:
        print(choice.message)
        print('---'*30)
    return None

if __name__=="__main__":
    main()