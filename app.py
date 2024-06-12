from magazine import Magazine
from author import Author
from article import Article

a1 = Author("Bryan")
print(vars(a1))

mag = Magazine("The Beginning", "Genesis")
print(vars(mag))

art = Article(a1, mag, "You Suck")
print(vars(art))

print(vars(a1))

for article in a1.articles:
    print(vars(article))

print(vars(mag))

for article in mag.articles:
    print(vars(article))


