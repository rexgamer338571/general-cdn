import sys

inputstring = """ _________
|___  |   |
| |  _| |_|
|  _|___  |
| |_   _  |
|_____|___|"""

inputstring = [sys.argv[1] if sys.argv[1] else inputstring]

def convert(multiline_str):
    lines = multiline_str.split('\n')
    
    first_line = lines[0].strip() + '|'

    processed_lines = [first_line]

    for line in lines[1:]:
        processed_lines.append(line.replace('_', ' '))
        processed_lines.append('|' + line.replace('|', ' ')[1:-1] + '|')

    second_line_length = len(lines[1])

    processed_lines[-1] = '|' + ' ' * (second_line_length - 2) + '|'

    last_line = '_' * (second_line_length - 2)
    processed_lines.append(last_line)

    return '\n'.join(processed_lines)


print(convert(inputstring))
