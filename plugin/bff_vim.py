import vim
import string

def should_parse(line):
    if not line:
        return False

    if not line[0] == "@":
        return False

    return True

def parse_line(line):
    if not should_parse(line):
        return [line]

    return_buffer = []
    line_partition = line.split("=")
    return_buffer.extend(line_partition[0])

    parentheses_count = 0;
    angle_bracket_count = 0;
    curly_bracket_count = 0;
    square_bracket_count = 0;
    first_curl = False
    parsed_line = ""

    for char in line: 
        parsed_line += char

        if char == "(":
            parentheses_count += 1
        if char == ")":
            parentheses_count -= 1

        if char == "[":
            square_bracket_count += 1
        if char == "]":
            square_bracket_count -= 1
            if curly_bracket_count == 0:
                parsed_line += '\n'

        if char == "{":
            curly_bracket_count += 1

        if char == "}":
            curly_bracket_count -= 1
            first_curl = True

        if char == "," and parentheses_count == 0 and curly_bracket_count > 0 and first_curl:
            parsed_line += "\n"

        if char == "<":
            angle_bracket_count += 1
        if char == ">":
            angle_bracket_count -= 1
            if angle_bracket_count == 0:
                parsed_line += "\n"

    return_buffer = parsed_line.split("\n")
    return return_buffer

def format_vim():
    b = vim.current.buffer
    r = vim.current.range

    new_buffer = []
    original_length = len(b)
    for line_number in range(original_length):
        new_buffer.extend(parse_line(b[line_number]))
    
    del b[:]
    for line in new_buffer:
      b.append(line)
    del b[0]

def format_file():
    print "Format file"
# TODO: Allow file input
#    try:
#        with open('out_struct_test.ll', 'w') as the_file:
#            the_file.write("")
#        with open('struct_test.ll') as fp:
#            for line in fp:
#                parsed_line = parse_line(line)
#                print parsed_line
#                with open('out_struct_test.ll', 'a') as the_file:
#                    the_file.write(parsed_line)
#    except:


def format():
    try: 
        import vim
        format_vim()
        return
    except ImportError, e:
        pass #not using as a vim plugin
    format_file()
