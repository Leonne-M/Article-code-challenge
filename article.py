from author import Author
from magazine import Magazine

class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise TypeError("author must be an instance of Author")
        if not isinstance(magazine, Magazine):
            raise TypeError("magazine must be an instance of Magazine")
        if not isinstance(title, str):
            raise TypeError("title must be a string")
        if len(title) == 0:
            raise ValueError("title must not be empty")

        self._author = author
        self._magazine = magazine
        self._title = title

        author.add_article(self)
        author.add_magazine(magazine)
        magazine.add_article(self)
        magazine.add_contributor(author)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise TypeError("title must be a string")
        if len(value) == 0:
            raise ValueError("title must not be empty")
        self._title = value

    @property
    def author(self):
        return self._author
    
    @property
    def magazine(self):
        return self._magazine

    
    
    


        