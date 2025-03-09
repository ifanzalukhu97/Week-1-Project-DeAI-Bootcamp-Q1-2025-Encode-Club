from openai import OpenAI

client = OpenAI()

messages = [
    {
        "role": "system",
        "content": "You are an experienced Korean chef with decades of experience in traditional and modern Korean cuisine.\n\n"
                   "You help people by suggesting dishes based on ingredients, providing detailed recipes, and offering "
                   "constructive critiques to improve cooking.\n\n"
                   "You're knowledgeable about Korean cooking techniques, flavor combinations, and cultural context of dishes.\n\n"
                   "You always provide clear, detailed responses with a warm, encouraging tone while maintaining "
                   "authenticity in your Korean culinary expertise.",
    }
]
messages.append(
    {
        "role": "system",
        "content": "You can respond to three types of requests:\n\n"
                   "1) Suggest dishes based on ingredients the user provides\n\n"
                   "2) Provide detailed recipes for specific Korean dishes\n\n"
                   "3) Offer constructive critiques and improvement suggestions for recipes the user shares.\n\n"
                   "Always maintain your Korean chef persona and provide culturally authentic information.",
    }
)

print("안녕하세요! I'm your Korean Chef Assistant. I can help you with:")
print("1. Suggesting Korean dishes based on ingredients you have")
print("2. Providing detailed recipes for Korean dishes")
print("3. Offering critiques and improvements for your recipes")
print("\nWhat would you like help with today?")

model = "gpt-4o-mini"

while True:
    user_input = input("\nYou: ")
    
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("\nChef: 안녕히 가세요! (Goodbye!) Happy cooking!")
        break
    
    messages.append({"role": "user", "content": user_input})
    
    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )
    
    print("\nChef: ", end="")
    collected_messages = []
    for chunk in stream:
        chunk_message = chunk.choices[0].delta.content or ""
        print(chunk_message, end="")
        collected_messages.append(chunk_message)
    
    messages.append({"role": "assistant", "content": "".join(collected_messages)})