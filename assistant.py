# assistant.py
import google.generative_ai as genai

class SmartAssistant:
     def __init__(self, api_key):
        """
        Initialize the assistant with the API key and configure the LLM model.
        """
        self.api_key = api_key
        genai.configure(api_key=self.api_key)

    def process_request(self, request):
        """
        Use the Google Gemini LLM to generate a response for the given user input.
        """
        try:
            response = genai.generate_text(
                model="gemini-1.5-flash",  # Ensure you have access to this model
                prompt=request,
                max_output_tokens=1024
            )
            return response.candidates[0]['output']  # Extracting generated text
        except Exception as e:
            return f"Error: {str(e)}"

    def query_llm(self, user_input):
        """
        Queries the LLM model with user input and returns a response.
        """
        try:
            response = requests.post(f"{self.base_url}/generate", 
                                     json={"input": user_input, "model": self.model},
                                     headers={"Authorization": f"Bearer {self.api_key}"})
            response.raise_for_status()
            return response.json()["output"]
        except requests.exceptions.RequestException as e:
            return f"Error: {str(e)}"

    def log_query(self, user_input, response):
        """
        Logs the user input and LLM response to a text file.
        """
        with open("queries.txt", "a") as file:
            file.write(f"User: {user_input}\nAssistant: {response}\n\n")
    
    def run(self):
        """
        Runs the assistant in a loop, continuously taking user input and responding.
        """
        print("Welcome to Smart Personal Assistant!")
        while True:
            user_input = input("Ask your question: ")
            if user_input.lower() == "exit":
                print("Goodbye!")
                break
            
            response = self.process_request(user_input)
            print(f"Assistant: {response}")
            self.log_query(user_input, response)