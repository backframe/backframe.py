def serialize(ast):
    contents = ""
    sections = ast['sections'] # list

    for s in sections:
        contents += write_block(s, 0)
        contents += "\n\n"

    return contents
    

def write_block(s, depth: int):
    template, indent = "", ""
    has_content = len(s['body']) > 0

    for _ in range(depth):
        indent += "\t"

    template += f"{indent}{s['type'].lower()} {s['name']} "
    template += "{"
    if has_content:
        template += "\n"

    # block vars
    for item in s['body']:
        if item['type'] == "ASSIGNMENT":
            name = item['name']
            token = item['body']

            _type = token._type
            value = token.value

            if _type == "CALL_EXPRESSION":
                fn_name = value['function']
                fn_arg = value['args']
                temp = f"{name} = {fn_name}({fn_arg});"

                template += f"\t{indent}{temp}\n"
            elif _type == "ARRAY": 
                elements = ",".join(value)
                temp = f"{name} = [{elements},];"
                template += f"\t{indent}{temp}\n"

            elif _type == "OBJECT":
                template += f"\t{indent}{name} = "
                template += "{\n"

                for k,v in value.items():
                    template += f"\t{indent}\t{k}: {v},\n"
                
                template += f"\t{indent}"
                template += "};\n"
            
            else:
                temp = f"{name} = {value};"
                template += f"\t{indent}{temp}\n"

        else:
            block = write_block(item , depth+1)
            template += f"\n{block}\n"

    if has_content:
        template += f"{indent}"

    template += "}"
    return template
    