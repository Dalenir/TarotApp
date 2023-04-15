import asyncio
import random
import secrets
from typing import Any

from game.Card import Card
from game.Field import Field
from game.models.board_model import BoardModel
from game.models.card_model import CardState


class Board(BoardModel):

    def __init__(self, fields: list[Field]):
        super().__init__(fields=fields)
        self.fields = fields

    @staticmethod
    async def game_start():

        """
        Creating and filling new board.
        :return: Board
        """

        game_range = 11

        fields = await asyncio.gather(*[Field(number=i).get_meaning() for i in range(game_range)])

        card_numbers, cards = list(), list()
        for i in range(game_range):
            x = random.randint(0, 77)
            while x in card_numbers:
                x = random.randint(0, 77)
            card_numbers.append(x)
            cards.append(Card.get_card_data(card_id=x,
                                            card_state=secrets.choice([CardState.up, CardState.reversed])))
        cards = await asyncio.gather(*cards)

        fields = await asyncio.gather(*[
            Field(number=i, card=card).get_meaning() for i, card in enumerate(cards)
        ])
        return Board(fields=fields)

    # @staticmethod
    # async def game_start_2():
    #     game_range = 11
    #
    #     card_numbers, fields = list(), list()
    #     for i in range(game_range):
    #         x = random.randint(0, 78)
    #         while x in card_numbers:
    #             x = random.randint(0, 78)
    #         card_numbers.append(x)
    #         card = await Card.get_card_data(card_id=x,
    #                                         card_state=secrets.choice([CardState.up, CardState.reversed]))
    #         fields.append(Field(number=i, card=card).get_meaning())
    #     fields = await asyncio.gather(*fields)
    #     return Board(fields=fields)
    #