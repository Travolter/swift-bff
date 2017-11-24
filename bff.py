#! /usr/bin/python2

def parse_line(line):
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

    return parsed_line

with open('out_struct_test.ll', 'w') as the_file:
    the_file.write("")
with open('struct_test.ll') as fp:
    for line in fp:
        parsed_line = parse_line(line)
        print parsed_line
        with open('out_struct_test.ll', 'a') as the_file:
            the_file.write(parsed_line)




