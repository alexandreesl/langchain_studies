from pathlib import Path

from langgraph.graph import StateGraph, START, END
from IPython.display import Image, display

from langchain_studies.examples.langchain_examples.langchain_state import JobApplicationState


def analyze_job_description(state):
   print("...Analyzing a provided job description ...")
   return {"is_suitable": len(state["job_description"]) > 100}
def generate_application(state):
   print("...generating application...")
   return {"application": "some_fake_application"}

builder = StateGraph(JobApplicationState)
builder.add_node("analyze_job_description", analyze_job_description)
builder.add_node("generate_application", generate_application)
builder.add_edge(START, "analyze_job_description")
builder.add_edge("analyze_job_description", "generate_application")
builder.add_edge("generate_application", END)
graph = builder.compile()

_graph_png_path = Path(__file__).resolve().parent / "first_graph.png"
_png_bytes = graph.get_graph().draw_mermaid_png(output_file_path=str(_graph_png_path))
print(f"Saved graph diagram to {_graph_png_path}")

res = graph.invoke({"job_description":"fake_jd"})

print(res)