from game.models.stats_model import StatsModel


class Stats(StatsModel):
    #TODO: change after base filled
    def __init__(self, good, luck, order, wild):
        good = good if isinstance(good, int) else 0
        luck = good if isinstance(luck, int) else 0
        order = good if isinstance(order, int) else 0
        wild = wild if isinstance(wild, bool) else True
        super().__init__(good=good, luck=luck, order=order, wild=wild)
