import dataclasses
import functools
import typing

import flask
import flask_restx
import pandas as pd

from ..namespaces import namespace

from . import constants


@dataclasses.dataclass
class Pokemon:

    name: str
    typeOne: str
    totalStats: int
    hp: int
    attack: int
    defense: int
    attackSpecial: int
    defenseSpecial: int
    speed: int
    generation: int
    legendary: bool
    typeTwo: str = None


class Constants(constants.ResourceCommonConstants):

    FILE_REF = __file__.split('/')
    COL_MAP  = {
        'Name': 'name',
        'Type 1': 'typeOne',
        'Type 2': 'typeTwo',
        'Total': 'totalStats',
        'HP': 'hp',
        'Attack': 'attack',
        'Defense': 'defense',
        'Sp. Atk': 'attackSpecial',
        'Sp. Def': 'defenseSpecial',
        'Speed': 'speed',
        'Generation': 'generation',
        'Legendary': 'legendary'
        }
    PARAMS: dict[str, dict[str, typing.Union[str, bool]]]  = {
        'name': {
            'description': 'Name.',
            'type': 'str',
            'required': False
            },
        'typeOne': {
            'description': 'Type 1.',
            'type': 'str',
            'required': False
            },
        'typeTwo': {
            'description': 'Type 2.',
            'type': 'str',
            'required': False
            },
        'totalStats': {
            'description': 'Total stats.',
            'type': 'int',
            'required': False
            },
        'hp': {
            'description': 'HP.',
            'type': 'int',
            'required': False
            },
        'attack': {
            'description': 'Attack.',
            'type': 'int',
            'required': False
            },
        'defense': {
            'description': 'Defense.',
            'type': 'int',
            'required': False
            },
        'attackSpecial': {
            'description': 'Special Attack.',
            'type': 'int',
            'required': False
            },
        'defenseSpecial': {
            'description': 'Special Defense.',
            'type': 'int',
            'required': False
            },
        'speed': {
            'description': 'Speed.',
            'type': 'int',
            'required': False
            },
        'generation': {
            'description': 'Canon generation.',
            'type': 'int',
            'required': False
            },
        'legendary': {
            'description': 'Legendary status flag.',
            'type': 'bool',
            'required': False
            }
        }


model = namespace.model(
    'pokemon',
    {
        k: getattr(flask_restx.fields, Constants.TYPE_MAP[d['type']])(
            description=d['description'],
            required=True if k != 'typeTwo' else False
            )
        for k, d
        in Constants.PARAMS.items()
        }
    )
parser = namespace.parser()
for k, d in Constants.PARAMS.items():
    parser.add_argument(
        k,
        type=eval(d['type']),
        help=d['description'],
        required=False
        )


class PokeMeta(type):

    def __iadd__(cls, pokemon: typing.Union[dict, Pokemon]):
        if isinstance(pokemon, dict):
            pokemon = Pokemon(**pokemon)
        cls.DB.append(pokemon)

    def __getitem__(cls, params: dict) -> Pokemon:
        for pokemon in cls.DB:
            if all(getattr(pokemon, k) == v for k, v in params.items() if v):
                yield pokemon


class Pokedex(metaclass=PokeMeta):

    DB = [
        Pokemon(**record)
        for record
        in pd.read_csv(
            '/'.join(
                (
                    *Constants.FILE_REF[:Constants.FILE_REF.index('apis')],
                    'static/pokemon.csv'
                    )
                ),
            index_col=0
            ).rename(columns=Constants.COL_MAP).to_dict('records')
        ]


@namespace.route('/')
class PokemonRoutes(flask_restx.Resource):

    POKEDEX = Pokedex

    @namespace.doc('get_object', params=Constants.PARAMS)
    @namespace.expect(parser, validate=True)
    @namespace.marshal_list_with(model, code=200, description='Success.')
    def get(self) -> tuple[dict, int]:
        """Get pokemon."""
        return [
            dataclasses.asdict(pokemon)
            for pokemon
            in self.POKEDEX[parser.parse_args(flask.request)]
            ], 200

    @namespace.doc('post_object', body=model, validate=True)
    @namespace.marshal_with(model, code=201, description='Success.')
    def post(self) -> tuple[dict, int]:
        """Add pokemon."""
        self.POKEDEX += (obj := flask.request.json)
        return obj, 201
