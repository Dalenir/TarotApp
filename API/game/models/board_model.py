from pydantic import BaseModel, validator

from game.models.field_model import FieldModel


class BoardModel(BaseModel):
    fields: list[FieldModel]

    @validator('fields')
    def fields_must_be_11(cls, v):
        if len(v) != 11:
            raise ValueError(f'Board must contain 11 fields! Current {len(v)}')
        return v
