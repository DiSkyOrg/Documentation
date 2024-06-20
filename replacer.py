# This code will take the content of all files of 'docs/docs' directory, and do the following:
# - Insert '[[[% import 'macros.html' as macros %]]]' at the beginning of each file (+ a new line after)
# - Replace every '|Since|vX|class:version|' with '[[[ macros.required_version('X') ]]]' (where X is a version number)

import os
import re

# Define the directory to be processed
dir_path = 'docs/docs'

# Define the string to be inserted at the beginning of each file
insert_string = '[[[% import \'macros.html\' as macros %]]]\n'

# Define the pattern to be replaced
pattern = re.compile(r'\|Cancellable\|(.+)\|class:version\|')

# Define the replacement string
replacement = '[[[ macros.is_cancellable(\'\g<1>\') ]]]'


# Process each file in the directory
def main():
    print(f'Processing files in directory: {dir_path} (found {len(os.listdir(dir_path))} files)')
    for filename in os.listdir(dir_path):
        # Read the content of the file
        with open(os.path.join(dir_path, filename), 'r') as file:
            content = file.read()

        # Replace the pattern with the replacement string (it could occur multiple times in the same file)
        content = pattern.sub(replacement, content)

        # Write the content back to the file
        with open(os.path.join(dir_path, filename), 'w') as file:
            file.write(content)

        print(f'Processed file: {filename}')

    print('All files processed successfully!')

if __name__ == '__main__':
    main()