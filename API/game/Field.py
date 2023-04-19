from game.models.field_model import FieldModel


class Field(FieldModel):

    # TODO: Ofc redo, but not now, i'm in hurry to bed
    async def get_meaning(self):
        match self.number:
            case 0:
                self.description = 'You'
            case 1:
                self.description = 'Atmosphere'
            case 2:
                self.description = 'Advice / Obstacle'
            case 3:
                self.description = 'Сonsciousness / Best of you'
            case 4:
                self.description = 'Subconsciousness / Your roots'
            case 5:
                self.description = 'The close past'
            case 6:
                self.description = 'The close future'
            case 7:
                self.description = 'Your attitude'
            case 8:
                self.description = 'Your home'
            case 9:
                self.description = 'Hopes and Fears'
            case 10:
                self.description = 'Outcome'
        return self