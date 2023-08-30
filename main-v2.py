import argparse
import os

from utils import extract_code_blocks, translate_code, replace_code_blocks

def main():
    # Set up the argument parser
    parser = argparse.ArgumentParser(description="Translate code blocks in a markdown file.")
    parser.add_argument("file_path", help="Path to the markdown file.")
    parser.add_argument("from_lang", help="Source programming language.")
    parser.add_argument("to_lang", help="Target programming language.")
    parser.add_argument("--output", help="Path to save the translated markdown file.", default=None)
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Read the markdown content from the file
    with open(args.file_path, 'r') as f:
        markdown_content = f.read()
    
    # Extract code blocks
    code_blocks = extract_code_blocks(markdown_content)
    
    # Translate code blocks
    translated_blocks = [translate_code(block, args.from_lang, args.to_lang) for block in code_blocks]
    
    # Replace the original code blocks with translated ones
    new_markdown = replace_code_blocks(markdown_content, code_blocks, translated_blocks)
    
    # Determine the output path
    if args.output:
        output_path = args.output
    else:
        # By default, save it as "translated_<original_filename>"
        filename = os.path.basename(args.file_path)
        dirname = os.path.dirname(args.file_path)
        output_path = os.path.join(dirname, f"translated_{filename}")
    
    # Save the translated markdown content to the new file
    with open(output_path, 'w') as f:
        f.write(new_markdown)
    
    print(f"Translated markdown saved to: {output_path}")

# For now, we'll simulate the CLI call by manually setting the arguments
# args = ["sample.md", "python", "javascript", "--output", "translated_sample.md"]
args = ["cpp-cheatsheet1.md", "cpp", "csharp"]
main()
