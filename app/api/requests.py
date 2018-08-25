from collections import namedtuple
from typing import NamedTuple


class RegisterRequest(NamedTuple):
    email: str
    password: str
