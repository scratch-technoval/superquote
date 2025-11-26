# 📘 SuperQuote

SuperQuote is a small Python utility that can safely encode and decode any string — including special characters, punctuation, Unicode, and even multiline text — using a custom randomly-generated delimiter (“superquote”).

---

## 🇬🇧 English

### Features

* Encode any string, including:

  * newlines
  * tabs
  * punctuation
  * unicode
* Fully reversible
* Random superquote for each encoding
* Zero external dependencies

### Example

```python
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
print(superquote.fromSuperQuote("(7)\"''-*+\"*\"Hello\\0044\\ you can use this lib \\0033\\\"''-*+\"*\""))
```

### Output

```
(7)""+""+*""Hello\0044\ world \0033\""+""+*""
Hello, world !
(7)"*"'-***"This\0010\is\0010\my\0010\python\0010\library \0033\"*"'-***"
This
is
my
python
library !
Hello, you can use this lib !
```

### How to use it?

1. Install the library
2. Import it:

   ```python
   import superquote
   ```
3. Use it in different ways:

   1. **Variable-based usage**

      ```python
      import superquote

      encoded = superquote.toSuperQuote("Hello, world !")
      print(encoded)
      decoded = superquote.fromSuperQuote(encoded)
      print(decoded)
      ```

      You can also use newlines with `\n`:

      ```python
      import superquote

      encoded = superquote.toSuperQuote("This\nis\nmy\npython\nlibrary !")
      print(encoded)
      decoded = superquote.fromSuperQuote(encoded)
      print(decoded)
      ```

   2. **Direct string usage**

      > Be careful: the string must not break the escape sequence!

      ```python
      import superquote

      # I use backslashes to avoid breaking the chain.
      print(superquote.fromSuperQuote("(7)\"''-*+\"*\"Hello\\0044\\ you can use this lib \\0033\\\"''-*+\"*\""))
      ```

   3. **List of functions:**

      * `superquote.toSuperQuote()` – transforms a regular string into a superquote string
      * `superquote.fromSuperQuote()` – transforms a superquote string back into a normal string
      * `superquote.generate_superquote()` – generates a random delimiter

---

## 🇫🇷 Français

### Fonctionnalités

* Encode n’importe quelle chaîne, y compris :

  * les sauts de ligne
  * les tabulations
  * la ponctuation
  * l’unicode
* 100 % réversible
* Superquote aléatoire pour chaque encodage
* Aucune dépendance externe

### Exemple

```python
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
print(superquote.fromSuperQuote("(7)\"''-*+\"*\"Hello\\0044\\ you can use this lib \\0033\\\"''-*+\"*\""))
```

### Résultat

```
(7)""+""+*""Hello\0044\ world \0033\""+""+*""
Hello, world !
(7)"*"'-***"This\0010\is\0010\my\0010\python\0010\library \0033\"*"'-***"
This
is
my
python
library !
Hello, you can use this lib !
```

### Comment l'utiliser ?

1. Installer la librairie
2. L’importer : `import superquote`
3. Il ne reste plus qu’à l’utiliser de différentes manières :

   1. **Échanges par variables :**

      ```python
      import superquote

      encoded = superquote.toSuperQuote("Hello, world !")
      print(encoded)
      decoded = superquote.fromSuperQuote(encoded)
      print(decoded)
      ```

      Vous pouvez aussi mettre des sauts de ligne avec `\n` :

      ```python
      import superquote

      encoded = superquote.toSuperQuote("This\nis\nmy\npython\nlibrary !")
      print(encoded)
      decoded = superquote.fromSuperQuote(encoded)
      print(decoded)
      ```

   2. **Les chaînes**

      > Attention : il faut éviter qu’il y ait un échappement dans la chaîne !

      ```python
      import superquote

      # I use backslashes to avoid breaking the chain.
      print(superquote.fromSuperQuote("(7)\"''-*+\"*\"Hello\\0044\\ you can use this lib \\0033\\\"''-*+\"*\""))
      ```

   3. **Liste des fonctions :**

      * `superquote.toSuperQuote()` : transforme une chaîne en superquote
      * `superquote.fromSuperQuote()` : transforme une chaîne superquote en chaîne normale
      * `superquote.generate_superquote()` : génère l’entoureur aléatoire
