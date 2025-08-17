class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Name must be a non-empty string")
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        # Silently ignore attempts to change name (immutable)
        pass
    
    def articles(self):
        return [article for article in Article.all if article.author == self]
    
    def magazines(self):
        return list({article.magazine for article in self.articles()})
    
    def add_article(self, magazine, title):
        return Article(self, magazine, title)
    
    def topic_areas(self):
        if not self.articles():
            return None
        return list({mag.category for mag in self.magazines()})


class Magazine:
    all = []
    
    def __init__(self, name, category):
        # Use setters to validate during initialization
        self.name = name  # This will call the setter
        self.category = category  # This will call the setter
        Magazine.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            # Silently ignore invalid type, keep original value
            return
        if len(value) < 2 or len(value) > 16:
            # Silently ignore invalid length, keep original value
            return
        self._name = value
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            # Silently ignore invalid category, keep original value
            return
        self._category = value
    
    def articles(self):
        return [article for article in Article.all if article.magazine == self]
    
    def contributors(self):
        return list({article.author for article in self.articles()})
    
    def article_titles(self):
        if not self.articles():
            return None
        return [article.title for article in self.articles()]
    
    def contributing_authors(self):
        authors = []
        for author in self.contributors():
            count = len([a for a in self.articles() if a.author == author])
            if count > 2:
                authors.append(author)
        return authors if authors else None
    
    @classmethod
    def top_publisher(cls):
        if not Article.all:
            return None
        return max(cls.all, key=lambda mag: len(mag.articles()))


class Article:
    all = []
    
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise Exception("Author must be an Author instance")
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be a Magazine instance")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise Exception("Title must be a string between 5 and 50 chars")
        
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        # Silently ignore attempts to change title (immutable)
        pass
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Must be an Author instance")
        self._author = value
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise Exception("Must be a Magazine instance")
        self._magazine = value