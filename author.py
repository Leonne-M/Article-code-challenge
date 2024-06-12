class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if len(name) == 0:
            raise ValueError("name must not be empty")
        self._name = name
        self._articles = []
        self._magazines = []

    @property
    def name(self):
        return self._name

    def add_article(self, article):
        if article not in self._articles:
            self._articles.append(article)

    @property
    def articles(self):
        return self._articles

    def add_magazine(self, magazine):
        if magazine not in self._magazines:
            self._magazines.append(magazine)

    @property
    def magazines(self):
        return self._magazines

        
