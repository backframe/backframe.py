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
            value: str = item['value']

            if value.__contains__("|"):
                # tis array
                v = value.replace("|", ",")
                temp = f"{name} = [{v},];"
                template += f"\t{indent}{temp}\n"
            elif value.__contains__(";"):
                # tis an object
                template += f"\t{indent}{name} = "
                template += "{\n"

                fields = value.split(";")
                for f in fields:
                    pair = f.split("->")
                    k = pair[0]
                    v = pair[1]

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
    