# Simple example of use

import superquote

encoded = superquote.toSuperQuote("Hello, world !")
print(encoded)
decoded = superquote.fromSuperQuote(encoded)
print(decoded)

encoded = superquote.toSuperQuote("This\nis\nmy\npython\nlibrary !")
print(encoded)
decoded = superquote.fromSuperQuote(encoded)
print(decoded)
