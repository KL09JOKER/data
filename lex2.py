import re

patterns = {
    "NUMBER": r"^\d+(\.\d+)?$",
    "IDENTIFIER": r"^[A-Za-z_][A-Za-z0-9_]*$",
    "OPERATOR": r"^[+\-*/=<>!]+$",
    "PUNCTUATION": r"^[.,;:!?(){}[\]]$"
}

def classify_token(token):
    for token_type, pattern in patterns.items():
        if re.match(pattern, token):
            return token_type
    return "UNKNOWN"

def lexical_analyzer(text):
    tokens = re.findall(r'\w+|\d+\.\d+|[^\w\s]', text)
    result = []
    for token in tokens:
        token_type = classify_token(token)
        result.append((token, token_type))
    return result

text = "x = 100 + y * 3.5; print(x)"
tokens = lexical_analyzer(text)

print(f"{'Token':15} | Type")
print("-" * 30)
for token, token_type in tokens:
    print(f"{token:15} | {token_type}")
