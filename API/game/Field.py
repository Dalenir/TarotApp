from game.models.field_model import FieldModel


class Field(FieldModel):

    async def get_meaning(self):
        self.description = 'Description from database (not atm)'
        return self