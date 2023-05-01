import roman
from motor.motor_asyncio import AsyncIOMotorCollection

from game.Stats import Stats
from game.Suit import Suit
from game.models.card_model import CardModel, CardState
from game.models.suit_model import Suits


class CardMaker:
    collection: AsyncIOMotorCollection

    def __init__(self, collection: AsyncIOMotorCollection):
        self.collection = collection

    async def get_card(self, card_id: int, card_state: CardState):
        card_data: dict = (
            await self.collection.aggregate(pipeline=
            [
                {
                    "$match": {"_id": card_id}
                },
                {
                    "$project": {
                        "Name": 1,
                        "Meaning": f"${'Meaning' if card_state == CardState.up else 'Reverse'}",
                        "Value": '$No',
                        "Stats": {
                            "Luck": f"${'T' if card_state == CardState.up else 'R'}Luck",
                            "Good": f"${'T' if card_state == CardState.up else 'R'}Good",
                            "Order": f"${'T' if card_state == CardState.up else 'R'}Order",
                            "Wild": "$Wild"
                        },
                        "Suit": "$Type"
                    }
                }
            ]
            ).to_list(length=None)
        )[0]
        if card_state != CardState.up:
            print(card_data['Name'], card_data['Meaning'])
        card_stats = Stats(good=card_data['Stats']['Good'],
                           luck=card_data['Stats']['Luck'],
                           order=card_data['Stats']['Order'],
                           wild=card_data['Stats']['Wild'])

        suit = Suit(name=card_data['Suit'])
        value = card_data['Value']
        visual_value = str(value)

        if suit.name == Suits.major:
            if value > 0:
                visual_value = roman.toRoman(value)
            else:
                visual_value = ''
        else:
            if value > 10:
                match value:
                    case 11:
                        visual_value = 'Pa'
                    case 12:
                        visual_value = 'Kn'
                    case 13:
                        visual_value = 'Qu'
                    case 14:
                        visual_value = 'Ki'

        return CardModel(id=card_id,
                         name=card_data['Name'],
                         value=value,
                         visual_value=visual_value,
                         suit=suit,
                         state=card_state,
                         stats=card_stats,
                         description=card_data['Meaning']
                         )
