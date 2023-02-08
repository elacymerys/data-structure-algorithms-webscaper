class Topic:
    def __init__(self, title):
        self._title = title

    @property
    def title(self):
        return self._title

    def __repr__(self):
        return self.title


class Task:
    def __init__(self, _id, title, link):
        self._id = _id
        self._title = title
        self._link = link

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def link(self):
        return self._link

    def __repr__(self):
        return {'id': self.id, 'title': self.title, 'link': self.link}.__repr__()
