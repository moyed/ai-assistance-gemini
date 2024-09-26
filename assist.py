# Import the necessary function from helper_functions.py
from helper_functions import get_llm_response

# Define the Assistant class
class Assistant:
    def __init__(self):
        # Any initialization code (if needed) goes here
        pass
  
    def run(self):
        # Main method to run the assistant
        while True:
            user_input = input("Ask your question: ")
            if user_input.lower() == "exit":
                print("Goodbye!")
                break
            
            # Get response from the LLM
            response = get_llm_response(user_input)
            print(f"User: {user_input}")
            print(f"Assistant >>: {response}")