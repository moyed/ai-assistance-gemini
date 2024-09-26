# 💬 AI Assistant in Python 🌟

Welcome to AI Assistant, an intelligent Python application built to answer your questions in natural language. This project is an excellent starting point for beginners who want to explore AI development, prompt engineering using gemini LLM.

## 🚀 What is this Application?

This AI Assistant uses a Large Language Model (LLM) to generate responses based on user input. It provides a simple interaction where you can ask questions, and it returns answers. The application is a great hands-on introduction to the world of AI and Natural Language Processing (NLP).

## 🎯 Main Features

 1. 🧠 Real-time AI Responses – Enter a question, and the assistant will give you a meaningful answer using LLM technology.
 2. 📝 Query Logging – All interactions are logged in a text file for future reference.
 3. 💻 Simple Setup – Easy to install and run in any environment, including Jupyter Notebooks.
 4. 🔄 Class-Based Design – The logic is structured using Object-Oriented Programming (OOP) for clean and reusable code.
 5. 🛠️ Expandable – Add more functionality as you grow as a developer.

## 🏗️ How to Run the Application

1. Clone the Repository

`git clone https://github.com/yourusername/ai-assistant-python.git
cd ai-assistant-python`

2. Install Dependencies

`pip install -r requirements.txt`

3. Set Up Environment Variables
The app requires a few environment variables to run correctly. Make sure to create a .env file in your project root, like this:

.env file

```
GEMINI_API_KEY=your-api-key
LOG_FILE=queries.txt
```

 Note: Get your API key from OpenAI (or any other LLM service you’re using) and replace your-api-key with your actual key.
4. Run the Application

In a Jupyter Notebook:

```
from assistant import Assistant

assistant = Assistant()
assistant.run()
```

On the command line:

`python assist.py``

## 🌱 Beginner Friendly!

If you’re new to Python or AI, don’t worry! This project is designed with beginners in mind. Here’s why:

 • Simple and Clear Code – The project focuses on readability and ease of understanding.
 • Step-by-Step Setup – Follow the instructions, and you’ll be up and running in no time.
 • OOP Concepts – Learn the basics of class-based programming in Python by looking at how the Assistant class is structured.

## 🛠️ Customizing the Assistant

Feel free to customize the assistant! You can add more features or connect it to different language models. Here are a few ideas to extend this project:

 • 🔍 Add More Functionality – Incorporate more advanced commands for your assistant.
 • 📊 Analytics – Track the most frequently asked questions by adding more logging details.
 • 🌐 Web Integration – Hook the assistant into a web application using Flask or FastAPI.

## 💡 Why This Project?

This project is a great showcase of how you can start small and build something useful. As a beginner, it helps you:

 • 🌍 Understand basic AI concepts.
 • 🖥️ Practice Python and OOP.
 • 📂 Work with environment variables.
 • 📜 Log and analyze user interactions.

## 🎉 Contributing

We love contributions! If you have an idea for improving the assistant, feel free to submit a pull request.

## 👏 Special Thanks

A big thanks to all the contributors and open-source projects that made this assistant possible. You’re welcome to join our journey!

