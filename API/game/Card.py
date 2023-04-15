from database import Mongo
from game.Stats import Stats
from game.Suit import Suit
from game.models.card_model import CardModel, CardState
from game.models.stats_model import StatsModel
from game.models.suit_model import Suits, SuitModel


class Card(CardModel):

    @staticmethod
    async def get_card_data(card_id: int, card_state: CardState):
        card_data: dict = (
                await Mongo.cards_collection.aggregate(
                    [
                    {
                        "$match": {"_id": card_id}
                    },
                    {
                        "$project": {
                            "Name": 1,
                            "Meaning": 1,
                            "Value": '$No',
                            "Stats": {
                                "Luck": f"${'T' if card_state.up else 'R'}Luck",
                                "Good": f"${'T' if card_state.up else 'R'}Good",
                                "Order": f"${'T' if card_state.up else 'R'}Order",
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