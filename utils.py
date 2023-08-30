# Let's start with the utility functions in utils.py

import re

def extract_code_blocks(markdown_content):
    """
    Extract code blocks from the given markdown content.
    
    Args:
        markdown_content (str): The markdown content to extract code from.
        
    Returns:
        list: A list of extracted code blocks.
    """
    # Use regex to extract code blocks demarcated by triple backticks
    code_blocks = re.findall(r'(```[\s\S]*?```)', markdown_content)
    return code_blocks

def translate_code(code, from_lang, to_lang):
    """
    Translate the code from source language to target language using OpenAI API.
    
    Args:
        code (str): The code to be translated.
        from_lang (str): The source programming language.
        to_lang (str): The target programming language.
        
    Returns:
        str: The translated code.
    """
    # Placeholder function: In reality, this will call the OpenAI API
    # For now, it will just return the same code
    # You will need to replace this with an actual API call
    
    # openai.api_key = 'YOUR_OPENAI_API_KEY'
    
    prompt = f"Translate the following {from_lang} code to {to_lang}:\n\n{code}"
    return prompt

    # response = openai.Completion.create(
    #     engine="text-davinci-002",
    #     prompt=prompt,
    #     max_tokens=500  # Adjust as needed
    # )
    # return response.choices[0].text.strip()

def replace_code_blocks(markdown_content, original_blocks, translated_blocks):
    """
    Replace the original code blocks with translated ones.
    
    Args:
        markdown_content (str): The original markdown content.
        original_blocks (list): List of original code blocks.
        translated_blocks (list): List of translated code blocks.
        
    Returns:
        str: Markdown content with code blocks replaced by translated ones.
    """
    for orig, trans in zip(original_blocks, translated_blocks):
        markdown_content = re.sub(re.escape(orig), trans, markdown_content)

    return markdown_content
