class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not (2 <= len(name) <= 15):
            raise ValueError("name must be between 2 and 15 characters")
        self._name = name
        
        if not isinstance(category, str):
            raise TypeError("category must be a string")
        if len(category) == 0:
            raise ValueError("category must not be empty")
        self._category = category
        
        self._articles = []
        self._contributors = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be a string")
        if not (2 <= len(value) <= 15):
            raise ValueError("name must be between 2 and 15 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise TypeError("category must be a string")
        if len(value) == 0:
            raise ValueError("category must not be empty")
        self._category = value

    def add_article(self, article):
        if article not in self._articles:
            self._articles.append(article)

    def add_contributor(self, author):
        if author not in self._contributors:
            self._contributors.append(author)

    @property
    def articles(self):
        return self._articles

    @property
    def contributors(self):
        return self._contributors

        


         
        