# HOME
Hands-on Machine Learning lectures/lab series
[Link on the Moffitt Website](https://www.moffitt.org/research-science/divisions-and-departments/quantitative-science/machine-learning/news-and-events/hands-on-machine-learning/)

The Hands-On Machine lEarning lecture/lab series offers a practical introduction to artificial intelligence and machine learning. Attendees will gain valuable skills in harnessing AI to improve healthcare through lectures, hands-on labs, and real-world projects.

The course starts with a grounding in core concepts and methods like regression, classification, and neural networks. Techniques for processing medical data and training models to analyze images, text notes, genetic data, and more will be covered, as well as guidance and examples tailored to medicine. An emphasis is placed on rigorously testing models to ensure they are fair, accurate, and safe for patients. Exciting lectures on state-of-the-art Foundation Models explore how AI breakthroughs like ChatGPT can be applied to tasks like providing patient education or extracting insights from the medical literature.

The curriculum underscores best practices for developing and deploying reliable, transparent, and ethical medical AI systems. Upon completing this course, the attendees will have the know-how to implement AI solutions that enhance diagnoses, personalize treatments, streamline workflows, and ultimately get the proper care to patients.


### Lecture 1 - An Introduction to Machine Learning Using LLMs as an Example - Part I
[Video](https://moffitt.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=945c0f41-9c93-43f9-9c0d-b10e015f68f8)
[Code](https://github.com/grasool/HOME/tree/main/Lecture-1)

### Lecture 2 - An Introduction to Machine Learning Using LLMs as an Example – Part II
[Video](https://moffitt.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=65a27a26-520e-4fef-a6d8-b12a015a83b8)
[Code](https://github.com/grasool/HOME/tree/main/Lecture-2)

## Here are the core takeaways

* Gain practical skills in Python programming, data wrangling, and implementing machine learning pipelines for medical data.
* Understand how to apply regression, classification, neural networks, CNNs, RNNs, and other core ML techniques to medical use cases.
* Learn best practices for training, evaluating, and testing models rigorously, focusing on performance metrics relevant to medical practice.
* Appreciate the expanding capabilities and limitations of state-of-the-art foundation models and large language models.
* Develop expertise in applying AI to tasks like analyzing medical images and scans, extracting information from clinical text, conversational agents, prediction models, and more.
* Gain hands-on experience by undertaking an end-to-end ML project from data processing to model deployment.
* Appreciate the importance of responsibly developing interpretable models and integrating AI in clinical workflows.
* Become fluent in data ethics, model bias, regulatory requirements, and other considerations when applying AI in medical settings.
* Build foundational skills to participate in multidisciplinary teams advancing research and applied AI solutions in healthcare.
* The core emphasis would be gaining conceptual and practical AI literacy to translate machine learning responsibly into improved patient outcomes.

## Link to recordings
https://www.moffitt.org/research-science/divisions-and-departments/quantitative-science/machine-learning/news-and-events/hands-on-machine-learning/

## Setup environment
Please use the following steps to set up things on your laptop/computer.

1.  Download and install ollama https://ollama.com/
2.  Download and install LM Studio https://lmstudio.ai/.
3.  Download and install VS Code https://code.visualstudio.com/
4.  Download and install miniconda https://docs.conda.io/projects/miniconda/en/latest/index.html
5.  Make a virtual environment: https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
6.  Activate environment
7.  Install LangChain https://python.langchain.com/docs/get_started/installation
8.  Install other dependencies



## Setup ollama - with Docker
Source: [https://hub.docker.com/r/ollama/ollama]
### Without GPU 
```
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
docker exec -it ollama ollama run llama2
```

### With GPU
```
docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
docker exec -it ollama ollama run llama2

```
