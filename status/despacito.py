import discord

class Despacito(discord.Game):
    __slots__ = ['name', 'type', 'url']

    def __init__(self):
        self.name = "Despacito"
        self.url = "https://www.youtube.com/watch?v=kJQP7kiw5Fk"
        self.type = 1

    def __str__(self):
        return self.name

    def _iterator(self):
        for attr in self.__slots__:
            value = getattr(self, attr, None)
            if value is not None:
                yield (attr, value)

    def __iter__(self):
        return self._iterator()

    def __eq__(self, other):
        return isinstance(other, Game) and other.name == self.name

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.name)
