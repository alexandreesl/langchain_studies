import json
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI

# 1. Define desired output structure (Pydantic model)
class ProductReview(BaseModel):
    """Information extracted from a product review."""
    gift: bool = Field(description="Was the item purchased as a gift? True if yes, False if not.")
    delivery_days: int = Field(description="How many days did it take to arrive? -1 if not found.")
    price_value: str = Field(description="Sentence about the value or price.")

# 2. Instantiate parser with Pydantic schema
parser = JsonOutputParser(pydantic_object=ProductReview)

# 3. Inject format instructions into prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "Extract info: {format_instructions}"),
    ("human", "{text}")
])

# 4. Chain: Prompt -> Model -> Parser
model = ChatOpenAI(model="gpt-4o-mini", temperature=0.0)
chain = prompt | model | parser

# 5. Invoke
customer_review = "Arrived in 2 days. It's pricey, but worth it. Mom loved it!"
output = chain.invoke({
    "text": customer_review,
    "format_instructions": parser.get_format_instructions()
})

print(json.dumps(output, indent=2))
