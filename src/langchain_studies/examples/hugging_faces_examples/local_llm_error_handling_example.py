def safe_model_call(llm, prompt, max_retries=2):
    """Safely call a local model with retry logic and graceful
    failure"""
    retries = 0
    while retries <= max_retries:
        try:
            return llm.invoke(prompt)
        except RuntimeError as e:
            # Common error with local models when running out of VRAM
            if "CUDA out of memory" in str(e):
                print(f"GPU memory error, waiting and retrying ({retries+1}/{max_retries+1})")
                time.sleep(2)  # Give system time to free resources
                retries += 1
            else:
                print(f"Runtime error: {e}")
                return "An error occurred while processing your request."
        except Exception as e:
            print(f"Unexpected error calling model: {e}")
            return "An error occurred while processing your request."
    # If we exhausted retries
    return "Model is currently experiencing high load. Please try again later."

# Use the safety wrapper in your LCEL chain
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline


llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(
        max_new_tokens=512,
        do_sample=False,
        repetition_penalty=1.03,
    ),
)
chat_model = ChatHuggingFace(llm=llm)

prompt = PromptTemplate.from_template("Explain {concept} in simple terms")
safe_llm = RunnableLambda(lambda x: safe_model_call(chat_model, x))
safe_chain = prompt | safe_llm

response = safe_chain.invoke({"concept": "robotics"})
print(response)
