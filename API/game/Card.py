from typing import Any

from database.Mongo import Mongo
from game.Stats import Stats
from game.Suit import Suit
from game.models.card_model import CardModel, CardState


class Card(CardModel):
    database: Any = Mongo

    def __init__(self, **data: Any):
        super().__init__(**data)

    @classmethod
    async def get_card_data(cls, card_id: int, card_state: CardState):
        db = cls.database()
        card_data: dict = (
                await db.cards_collection.aggregate(pipeline=
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

        card_stats = Stats(good=card_data['Stats']['Good'],
                                luck=card_data['Stats']['Luck'],
                                order=card_data['Stats']['Order'],
                                wild=card_data['Stats']['Wild'])

        return Card(id=card_id,
                    name=card_data['Name'],
                    value=card_data['Value'],
                    suit=Suit(name=card_data['Suit']),
                    state=card_state,
                    stats=card_stats,
                    description=card_data['Meaning']
                    )