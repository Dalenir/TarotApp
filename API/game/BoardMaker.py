import asyncio
import random
import secrets

from database.MongoDB.basic_mongo import Mongo
from game.CardMaker import CardMaker
from game.FieldsMaker import FieldsMaker
from game.models.board_model import BoardModel
from game.models.card_model import CardState
from game.models.field_model import FieldModel


# Really can be function. I don't want to give it dependency injection.

class BoardMaker:

    @staticmethod
    async def game_start():

        """
        Creating and filling up new board.
        :return: Board
        """
        card_collection = Mongo().cards_collection
        game_range = 11

        card_numbers, cards = list(), list()
        for i in range(game_range):
            x = random.randint(0, 77)
            while x in card_numbers:
                x = random.randint(0, 77)
            card_numbers.append(x)
            cards.append(CardMaker(card_collection).get_card(card_id=x,
                                                             card_state=secrets.choice(
                                                                 [CardState.up, CardState.reversed])))
        cards = await asyncio.gather(*cards)

        field_maker = FieldsMaker()
        fields: list[FieldModel] = await asyncio.gather(*[
            field_maker.get_field(field_number=i, card=card) for i, card in enumerate(cards)
        ])
        print(len(fields))
        return BoardModel(fields=fields)
