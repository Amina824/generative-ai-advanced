from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Optional, Annotated, Literal

load_dotenv()
model=ChatOpenAI(model='gpt-4.1')

class Review(TypedDict):
    keytheme:Annotated[list[str],"write all the key themes from the review"]
    summary:str
    sentiment:Annotated[Literal["positive",'negative'], "Tell the review is positive or negative"]
    pros:Optional[str]

structuredmodel=model.with_structured_output(Review)
result=structuredmodel.invoke("""I recently purchased the Wireless Bluetooth Headphones and have been using them daily for the past three weeks. Overall, I am very satisfied with the experience. The sound quality is clear and well-balanced, with deep bass and crisp vocals that make listening to music and watching movies enjoyable. The headphones are lightweight and comfortable enough to wear for several hours without causing discomfort.

The battery life is impressive, lasting close to 30 hours on a single charge, which means I rarely have to worry about charging them. Bluetooth connectivity is fast and stable, and pairing with my phone and laptop takes only a few seconds. The controls on the earcups are intuitive and easy to use.

The only downside is that the built-in microphone could perform better in noisy environments, as background sounds are sometimes picked up during calls. Additionally, the plastic build, while lightweight, doesn't feel as premium as some higher-end models.

Overall, these headphones provide excellent value for the price. They deliver great audio quality, long battery life, and reliable performance, making them a solid choice for students, professionals, and anyone looking for affordable wireless headphones. I would rate this product 4.7 out of 5 stars.
                       """)

print(result)

