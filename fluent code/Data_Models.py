import collections
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA') 
    suits = 'spades diamonds clubs hearts'.split()
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
        for rank in self.ranks]
    def __len__(self):
        return len(self._cards)
    def __getitem__(self, position): return self._cards[position]
# print ("hello")
# ranks = [str(n) for n in range(2, 11)] + list('JQKA') 
# print(ranks)
# suits = 'spades diamonds clubs hearts'.split()
# h = [[suit,rank] for suit in suits for rank in ranks ]
# print(len(h))

const  = FrenchDeck()
const.__len__()
print(len(const))