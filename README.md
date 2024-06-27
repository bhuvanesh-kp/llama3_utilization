# llama3_utilization

Task-1:
utilization of llama3 and testing its working by downloading the model from hugging face transformer library,
Asking few questions and checking its work progress

Task-2:
Here I have used langchain to use Chat Groq to use multiple models ,I have used LLama3-70B and used to as a summarizer to evaluate resume for a job description.
I have a job decription and linkedin and tested it.
remark : The model is good but I feel like its max token limit is less even compared to GPT 3.5 turbo, even with 70B parameters and there is many things to imporove,
I have tested it and it have a lot space to improve

Task-3:
RetrivalQA has been performed from a wikepedia article on LLM(Large Language Model) , the task has been performed using "microsoft/Phi-3-mini-4k-instruct" from huggingface.
The model was too big to work under GPU requirements so Quantization has been performed to reduce the weights of parameter to easily be load into GPU.
The produre for quantization is here: https://huggingface.co/docs/transformers/main/en/quantization/bitsandbytes?bnb=8-bit#offloading
