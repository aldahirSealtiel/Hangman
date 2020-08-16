text = input()

parse_text = text.replace(",", "")
parse_text = parse_text.replace(".", "")
parse_text = parse_text.replace("!", "")
parse_text = parse_text.replace("?", "")
print(parse_text.lower())
