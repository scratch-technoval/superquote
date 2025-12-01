import random
import re

ALPHA_NUMS = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
QUOTE_CHARS = "\'-+*"

def generate_superquote(length: int = None) -> str:
    if length is None:
        length = random.randint(4, 10)
    return ''.join(random.choice(QUOTE_CHARS) for _ in range(length))

def toSuperQuote(quote: str, superquote: str = None) -> str:
    if superquote is None:
        superquote = generate_superquote()
    length = len(superquote)
    encoded_parts = []
    for c in quote:
        if c in ALPHA_NUMS:
            encoded_parts.append(c)
        else:
            encoded_parts.append(f'.{ord(c):d}.')
    encoded_content = ''.join(encoded_parts)
    return f"({length})'{superquote}'{encoded_content}'{superquote}'"

def fromSuperQuote(encoded: str) -> str:
    m = re.match(r"^\((\d+)\)'", encoded)
    if not m:
        raise ValueError("Format de superquote invalide")
    length = int(m.group(1))
    start = m.end()
    if len(encoded) < start + length + 1:
        raise ValueError("Format de superquote invalide")
    superquote = encoded[start:start+length]
    after = start + length
    if encoded[after] != "'":
        raise ValueError("Format de superquote invalide")

    pattern = re.compile(
        rf"^\({length}\)'{re.escape(superquote)}'(.*)'{re.escape(superquote)}'$",
        re.DOTALL
    )
    m2 = pattern.match(encoded)
    if not m2:
        raise ValueError("Bloc encodé invalide")
    content = m2.group(1)

    def replace_match(match):
        code = match.group(1)
        return chr(int(code))

    return re.sub(r'\.([0-9]+)\.', replace_match, content)
