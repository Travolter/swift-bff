def parse_line(line):
    print line
    parentheses_count = 0;
    angle_count = 0;
    curly_brace_count = 0;
    first_curl = False
    parsed_line = ""

    for char in line: 
        parsed_line += char

        if char == "(":
            parentheses_count += 1
        if char == ")":
            parentheses_count -= 1

        if char == "{":
            curly_brace_count += 1

        if char == "}":
            curly_brace_count -= 1
            first_curl = True

        if char == "," and parentheses_count == 0 and curly_brace_count > 0 and first_curl:
            parsed_line += "\n"

        if char == "<":
            angle_count += 1
        if char == ">":
            angle_count -= 1
            if angle_count == 0:
                parsed_line += "\n"

    return_buffer = string.split(parsed_line, "\n")
    return return_buffer

#b = vim.current.buffer
#new_buffer = []
#for line_number in range(len(b)):
#    new_buffer.extend(parse_line(b[line_number]))
#
#del b[:]
#for line in new_buffer:
#  b.append(line)
