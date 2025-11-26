import superquote

encoded = superquote.toSuperQuote("Hello, world !")
print(encoded)
decoded = superquote.fromSuperQuote(encoded)
print(decoded)

encoded = superquote.toSuperQuote("This\nis\nmy\npython\nlibrary !")
print(encoded)
decoded = superquote.fromSuperQuote(encoded)
print(decoded)

# I use backslashes to avoid breaking the chain.
print(superquote.fromSuperQuote("(4)''**+'You can use this lib \\0033\\''**+'"))
