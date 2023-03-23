import os
import docx2txt
import transformers
import torch

# Set the maximum width of the console output
os.environ['COLUMNS'] = "10000"

# Set OpenAI API key
os.environ['OPENAI_API_KEY'] = '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'

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