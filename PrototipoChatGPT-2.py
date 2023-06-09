import os
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

import docx2txt
import transformers
import torch

# Set CUDA device if available
if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")

# Enable CUDA if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    torch.backends.cudnn.enabled = True
    torch.backends.cudnn.benchmark = True

def ask_question(question, context):
    model = transformers.pipeline("text-generation", model="gpt2")
    inputs = {"question": question, "context": context}
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.model.to(device)
    outputs = model(**inputs)
    return outputs[0]["answer"]

# Set the maximum width of the console output
os.environ['COLUMNS'] = "10000"

# Set OpenAI API key
if not gpt_response:
    gpt_response = "I'm sorry, I couldn't generate a response at this time."
os.environ['OPENAI_API_KEY'] = ''-------------------OPENAI_API_KEY-----------------''

gpt_response = model.generate(
        input_ids=input_ids, 
        max_length=1000, 
        do_sample=True, 
        temperature=0.7,
        top_p=0.95, 
        top_k=50,
        no_repeat_ngram_size=2,
        num_return_sequences=1,
    )[0]

def translate_text(self, text, target_language):
    translate = YandexTranslate(self.api_key)
    translation = translate.translate(text, target_language)
    return translation['text'][0]

if not gpt_response:
    gpt_response = "I'm sorry, I couldn't generate a response at this time."

# Set OpenAI API key
os.environ['OPENAI_API_KEY'] = ''-------------------OPENAI_API_KEY-----------------''

chatbot = ChatBot(api_key= ''-------------------OPENAI_API_KEY-----------------'')

# Define function to read text from file
def read_text_from_file(file_path):
    if file_path.endswith('.txt'):
        # Read text file
        with open(file_path, 'r') as file:
            text = file.read()
    elif file_path.endswith('.docx'):
        # Read docx file
        text = docx2txt.process(file_path)
    else:
        # Invalid file type
        print('Error: Invalid file type')
        return None
    return text

# Define function to ask question and receive answer
def ask_question(question, context):
    model = transformers.pipeline("text-generation", model="gpt2", device=0 if not torch.cuda.is_available() else "cuda")
    return model(question)[0]["generated_text"]

# Define the main function to run the program
def main():
    # Get file path input from user
    file_path = input('Enter the file path: ')

    # Read text from file
    text = read_text_from_file(file_path)

    # Ask how to interact with the text
    interaction = input('How would you like to interact with the text? (read/respond/answer questions): ')

    if interaction == 'read':
        # Display the text and ask if user wants to continue
        print(text)
        continue_interaction = input("Do you want to continue? (y/n) ")

        while continue_interaction.lower() == 'y':
            # Ask how to interact with the text
            interaction = input('How would you like to interact with the text? (respond/answer questions): ')

            if interaction == 'respond':
                # Initialize context variable
                context = text

                while True:
                    # Ask question
                    question = input("What's your question? ")

                    # Get answer from OpenAI API
                    answer = ask_question(question, context)

                    if answer:
                        # Print answer
                        print(answer)

                        # Ask if user wants to continue
                        continue_interaction = input("Do you want to ask another question? (y/n) ")

                        if continue_interaction.lower() == 'n':
                            break

                        # Update context variable
                        context += f"\nQ: {question}\nA: {answer}\n"
                    else:
                        # Ask if user wants to try again
                        try_again = input("Do you want to try asking a different question? (y/n) ")
                        if try_again.lower() == 'n':
                            break

            elif interaction == 'answer questions':
                # Initialize context variable
                context = text

                while True:
                    # Ask question
                    question = input("What's your question? ")

                    # Get answer from OpenAI API
                    answer = ask_question(question, context)

                    if answer:
                        # Print answer
                        print(answer)

                        # Ask if user wants to continue
                        continue_interaction = input("Do you want to ask another question? (y/n) ")

                        if continue_interaction.lower() == 'n':
                            break

                        # Update context variable
                        context += f"\nQ: {question}\nA: {answer}\n"
                    else:
                        # Ask if user wants to try again
                        try_again = input("Do you want to try asking a different question? (y/n) ")
                        if try_again.lower() == 'n':
                            break

if __name__ == '__main__':
    main()
