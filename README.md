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
* Zero dependencies

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
```

### Output

```
(7)"*-***+-"Hello\0044\ world \0033\"*-***+-"
Hello, world !
(7)"-+"-+-*"This\0010\is\0010\my\0010\python\0010\library \0033\"-+"-+-*"
This
is
my
python
library !
```

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
* Aucune dépendance

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
```

### Résultat

```
(7)"*-***+-"Hello\0044\ world \0033\"*-***+-"
Hello, world !
(7)"-+"-+-*"This\0010\is\0010\my\0010\python\0010\library \0033\"-+"-+-*"
This
is
my
python
library !
```
