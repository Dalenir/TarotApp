from game.models.suit_model import SuitModel, Suits


class Suit(SuitModel):

    def __init__(self, name: str):
        first_letter = name[0].lower()

        if first_letter == 'm':
            suit = Suits.major
        elif first_letter == 'w':
            suit = Suits.wands
        elif first_letter == 'c':
            suit = Suits.cups
        elif first_letter == 's':
            suit = Suits.swords
        elif first_letter == 'p':
            suit = Suits.pentacles
        else:
            raise ValueError(f"{name} is not valid suit name!")
        super().__init__(name=suit)
