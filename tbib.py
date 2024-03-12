import re

def convert_references(input_file, output_file):
    """
    Converts references in the format [n] to \bibitem{refn}.

    Args:
        input_file (str): Path to the input text file containing references.
        output_file (str): Path to the output text file with converted references.
    """

    # Define the pattern to find references like [1], [2], ..., [n]
    pattern = r'\[\d+\]'

    # Function to replace the pattern with the desired format
    def replace_func(match):
        ref_number = match.group()[1:-1]  # Extract the number from the match
        return r'\\bibitem{{ref{}}}'.format(ref_number)

    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            # Substitute all occurrences of the pattern in the line using the replace function
            converted_line = re.sub(pattern, replace_func, line)
            outfile.write(converted_line)

# Example usage
input_file_path = 'cnn_bib.txt'  # Replace with the path to your input file
output_file_path = 'tcnn_bib.txt'  # Replace with the path to your desired output file

convert_references(input_file_path, output_file_path)