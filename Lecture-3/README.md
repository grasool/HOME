# Lecture 3



## Installation and Environment Setup

1.  Download and install [ollama](https://ollama.com/).
2.  Download and install [miniconda](https://docs.anaconda.com/free/miniconda/miniconda-install/).
3.  Download and install [vscode](https://code.visualstudio.com/).

## Setup Python Virtual Environment and Install Dependencies
1.  Oepn VScode, go to the terminal, and create a virtual environment:
   ```bash
   conda create --name llm-path-reports python=3.10
   conda activate llm-path-reports
   ```   
2. Clone this repo
   ```bash
   git clone https://github.com/grasool/HOME
   ```
3. Go to the Lecture-3 folder
4. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
5. Start ollama from VSCode terminal
   ```bash
   ollama run llama3
   ```
6. Quit ollama
   ```bash
   /bye
   ```
## Run LLM
1. Test llama3
   ```bash
   python test-langchain-ollama.py
   ```
2. Rune the main code using the command or from the editor
   ```bash
   python main-path-reports-llm.py
   ```
