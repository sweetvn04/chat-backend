import google.generativeai as genai

# 1. Configure your API key
genai.configure(api_key="AIzaSyDln0H0aJcSyTcoC_JwZNsbffSQDdoQDd0") # Replace with your actual key

print("Available models for chat and text generation:")
print("-" * 45)

# 2. Get the list of models
for model in genai.list_models():
    # 3. Check if the model can generate text content
    if 'generateContent' in model.supported_generation_methods:
        print(model.name)
