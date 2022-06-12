def serialize(ast):
    contents = ""
    sections = ast['sections'] # list

    for s in sections:
        contents += write_block(s, 0)
        contents += "\n\n"

    return contents
    

def write_block(s, depth: int):
    tmpl, ident = "", ""
    has_content = len(s['body']) > 0

    for _ in range(depth):
        ident += "\t"

    tmpl += f"{ident}{s['type'].lower()} {s['name']} "
    tmpl += "{"
    if has_content:
        tmpl += "\n"

    # block vars
    for item in s['body']:
        if item['type'] == "ASSIGNMENT":
            name = item['name']
            value: str = item['value']

            if value.__contains__("|"):
                v = value.replace("|", ",")
                temp = f"{name} = [{v},];"
                tmpl += f"\t{ident}{temp}\n"
            else:
                temp = f"{name} = {value};"
                tmpl += f"\t{ident}{temp}\n"

        else:
            block = write_block(item , depth+1)
            tmpl += f"\n{block}\n"

    if has_content:
        tmpl += f"{ident}"

    tmpl += "}"
    return tmpl
    