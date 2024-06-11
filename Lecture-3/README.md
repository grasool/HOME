# Lecture 3



## Installation and Environment Setup

1.  Download and install ollama.
2.  Dowonload and install miniconda.
3.  Download and install vscode.

## Setup Python Virtual Environment and Install Dependencies
1.  Oepn VScode, go to the terminal and create a virtual environment in a
   ```bash
conda create --name llm-path-reports python=3.10
conda activate llm-path-reports
```   
2. Clone repo
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
7. Test llama3
   ```bash
   python test-langchain-ollama.py
   ```
8. Rune the main code using command or from the editor  
