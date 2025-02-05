# Deepseek-code-companion

 🚀 Your AI Pair Programmer with Debugging Superpowers

 DeepSeek Code Companion is an AI-powered coding assistant built with Ollama and LangChain. It provides expert assistance in Python programming, debugging, code documentation, and solution design. Whether you're a beginner or an experienced developer, DeepSeek is here to help you write better code faster.

### 🌟 Features
 🐍 Python Expert: Get expert guidance on Python programming.

 🐞 Debugging Assistant: Identify and fix bugs in your code with strategic print statements.

 📝 Code Documentation: Automatically generate clear and concise documentation for your code.

 💡 Solution Design: Receive well-structured solutions for your coding problems.

### 🛠️ Technologies Used
 Ollama: A lightweight framework for running large language models locally.

 LangChain: A framework for building applications powered by language models.

 Streamlit: A powerful tool for building interactive web applications with Python.

## 🚀 Getting Started
 Follow these steps to set up and run the DeepSeek Code Companion on your local machine.

### Prerequisites
 Python 3.9 or higher

 Ollama installed and running locally

 Streamlit installed

### Installation
Clone the Repository:

```bash
git clone https://github.com/your-username/deepseek-code-companion.git
cd deepseek-code-companion
```

#### Set Up a Virtual Environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate
```

#### Install Dependencies:

`pip install -r requirements.txt`

#### Run Ollama Locally:

Ensure Ollama is running on your machine. By default, the application connects to http://localhost:11434.

#### Run the Streamlit App:

`streamlit run app.py`

#### Access the App:
Open your browser and navigate to the URL provided in the terminal (usually http://localhost:8501).

### 🖥️ Usage
Choose a Model:

In the sidebar, select a model from the dropdown (e.g., deepseek-r1:1.5b or deepseek-r1:3b).

Ask Your Coding Questions:

Type your coding question or problem in the chat input box.

DeepSeek will provide concise and accurate solutions.

Explore Model Capabilities:

Use DeepSeek for debugging, code documentation, or solution design.

### 🎨 Customization
Styling
The app uses custom CSS for a dark theme. You can modify the styles in the st.markdown section of the code.

Models
You can add or remove models in the selected_model dropdown by editing the app.py file:
```
python
selected_model = st.selectbox(
    "Choose Model",
    ["deepseek-r1:1.5b", "deepseek-r1:3b"],  # Add or remove models here
    index=0
)
```

System Prompt
Modify the system prompt in the system_prompt variable to customize the AI's behavior:

```
python
system_prompt = SystemMessagePromptTemplate.from_template(
    "You are an expert AI coding assistant. Provide concise, correct solutions "
    "with strategic print statements for debugging. Always respond in English."
)
```

#### 🐛 Troubleshooting
Common Issues
Ollama Not Running:

Ensure Ollama is running locally and accessible at http://localhost:11434.

### Missing Variables Error:

If you encounter a KeyError related to missing variables (e.g., {r2} or {rmse}), ensure that the messages in st.session_state.message_log do not contain unescaped placeholders. Escape curly braces by doubling them (e.g., {{r2}}).

### Streamlit Issues:

If the app doesn't launch, ensure Streamlit is installed and your virtual environment is activated.

## 📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

## 🙏 Acknowledgments
Ollama for providing a lightweight framework for running LLMs.

LangChain for simplifying the integration of language models.

Streamlit for making it easy to build interactive web apps.
