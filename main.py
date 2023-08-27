import sys
import re
# import openai

def extract_code_blocks(filename, language):
    with open(filename, 'r') as file:
        contents = file.read()
        # Regular expression to find code blocks of the specified language
        pattern = re.compile(rf'```{language}\n(.*?)```', re.DOTALL)
        matches = pattern.findall(contents)
        # print_code_block(language, matches)
        return matches

def translate_code(code, from_language, to_language):
    # openai.api_key = 'YOUR_OPENAI_API_KEY'
    
    prompt = f"Translate the following {from_language} code to {to_language}:\n\n{code}"
    return prompt

    # response = openai.Completion.create(
    #     engine="text-davinci-002",
    #     prompt=prompt,
    #     max_tokens=500  # Adjust as needed
    # )
    # return response.choices[0].text.strip()

def print_code_block(language, matches):
    for match in matches:
        print(f'```{language}')
        print(match)
        print('```')
        print('')

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python script_name.py filename source_language target_language")
        sys.exit(1)
    
    filename = sys.argv[1]
    source_language = sys.argv[2]
    target_language = sys.argv[3]
    
    code_blocks = extract_code_blocks(filename, source_language)
    
    for code in code_blocks:
        translated_code = translate_code(code, source_language, target_language)
        print(translated_code)