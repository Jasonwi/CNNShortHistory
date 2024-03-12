import re

def convert_references(input_file, output_file):
    """
    Converts references in a LaTeX file from the format [n] to \ref{n}.

    Args:
        input_file (str): Path to the input .tex file containing references.
        output_file (str): Path to the output .tex file with converted references.
    """

    # Define the pattern to find references like [1], [2], ..., [n]
    pattern = r'\[(\d+)\]'

    # Define the replacement format
    replacement = r'\\cite{ref\1}'

    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            # Substitute all occurrences of the pattern in the line using the replacement format
            converted_line = re.sub(pattern, replacement, line)
            outfile.write(converted_line)

# Specify the path to your input and output .tex files
input_file_path = 'b.tex'
output_file_path = 'c.tex'

# Convert the references in the input file and write to the output file
convert_references(input_file_path, output_file_path)