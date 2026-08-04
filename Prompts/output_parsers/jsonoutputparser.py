from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()
model=ChatOpenAI()
parser=JsonOutputParser()

prompt=PromptTemplate(
    template='write the name and key features of the product in the following review \n {review1} \n {instructions}',
    input_variables=['review1'],
    partial_variables={'instructions': parser.get_format_instructions()}
)

product_review= """I purchased the Apple iPhone 15 Pro (256GB, Natural Titanium) about three weeks ago, and overall, I'm extremely impressed with its performance. The A17 Pro chip makes everything incredibly fast, whether I'm gaming, editing videos, or switching between multiple apps. The 48MP camera captures stunning photos with excellent detail, especially in low-light conditions, and the portrait mode is much better than my previous phone. The Super Retina XDR display is bright, vibrant, and perfect for watching movies or browsing social media.

The new Titanium design feels premium while making the phone noticeably lighter than older Pro models. I also appreciate the USB-C charging port, which lets me use the same cable for multiple devices."""

chain =prompt | model | parser
result= chain.invoke({'review1': product_review})
print(result)
