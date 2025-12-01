import superquote

encoded = superquote.toSuperQuote("Hello, world !")
print(encoded)
decoded = superquote.fromSuperQuote(encoded)
print(decoded)

encoded = superquote.toSuperQuote("This\nis\nmy\npython\nlibrary !")
print(encoded)
decoded = superquote.fromSuperQuote(encoded)
print(decoded)

print(superquote.fromSuperQuote("(5)'**-'-'Hello .33. You can use this lib .33.'**-'-'"))
