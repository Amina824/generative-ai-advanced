from langchain_core.prompts import PromptTemplate

ptemplate= PromptTemplate(
    template="""Behave as helpful ai assistant. Explain each {input_topic} in simple words.explain as specified {input_length}. Explain in tone {input_tone}.Explain as easy as u can""",

    input_variables=['input_topic','input_length','input_tone'],
    validate_template=True )

ptemplate.save('template.json')

