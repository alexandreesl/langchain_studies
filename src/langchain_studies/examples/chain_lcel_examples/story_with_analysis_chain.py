from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
# Initialize the model
llm = GoogleGenerativeAI(model="gemini-flash-latest")
# First chain generates a story
story_prompt = PromptTemplate.from_template("Write a short story about {topic}")
story_chain = story_prompt | llm | StrOutputParser()
# Second chain analyzes the story
analysis_prompt = PromptTemplate.from_template(
    "Analyze the following story's mood:\n{story}"
)
analysis_chain = analysis_prompt | llm | StrOutputParser()

# Combine chains
story_with_analysis = story_chain | analysis_chain
# Run the combined chain
story_analysis = story_with_analysis.invoke({"topic": "a rainy day"})
print("\nAnalysis:", story_analysis)

print('============================')
# Using RunnablePassthrough.assign to preserve data
enhanced_chain = RunnablePassthrough.assign(
    story=story_chain  # Add 'story' key with generated content
).assign(
    analysis=analysis_chain  # Add 'analysis' key with analysis of the story
)

result = enhanced_chain.invoke({"topic": "a rainy day"})
print(result.keys()) 
print(result['story'])
print('========================')
print(result['analysis'])