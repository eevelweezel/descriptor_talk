class Immutable:

    __slots__ = ('_name', '_desc')          # Replace the instance dictionary

    def __init__(self, name, description):
        self._desc = description            # Store to private attribute
        self._name = name                   # Store to private attribute

    @property                               # Read-only descriptor
    def desc(self):
        return self._desc

    @property
    def name(self):                         # Read-only descriptor
        return self._name


doom = Immutable('Doom Weasel', 'Weasel of Doom')

print(dir(doom.desc))

doom.desc = 'Calm & docile'

