from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from typing import Literal
from pydantic import BaseModel, Field

load_dotenv()
model=ChatOpenAI()

class Review(BaseModel):
    key_features: list[str] = Field(description='write all the key features in the review')
    sentiment: Literal['positive', 'negative'] = Field(description='provide the sentiment analysis off the review')
    product_name:str = Field(description='tell the name of the product')


parser=PydanticOutputParser(pydantic_object=Review)

prompt= PromptTemplate(
    template='Provide key features,sentiment and product name  of the following Review \n {review1} \n {guidelines}',
    input_variables=['review1'],
    partial_variables={'guidelines': parser.get_format_instructions()}

)

product_review= """I purchased the Apple iPhone 15 Pro (256GB, Natural Titanium) about three weeks ago, and overall, I'm extremely impressed with its performance. The A17 Pro chip makes everything incredibly fast, whether I'm gaming, editing videos, or switching between multiple apps. The 48MP camera captures stunning photos with excellent detail, especially in low-light conditions, and the portrait mode is much better than my previous phone. The Super Retina XDR display is bright, vibrant, and perfect for watching movies or browsing social media.

The new Titanium design feels premium while making the phone noticeably lighter than older Pro models. I also appreciate the USB-C charging port, which lets me use the same cable for multiple devices."""

chain =prompt | model | parser
result= chain.invoke({'review1': product_review})
print(result)