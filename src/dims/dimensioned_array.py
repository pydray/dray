# SPDX-License-Identifier: BSD-3-Clause
# Copyright (c) 2024 Pydray contributors (https://github.com/pydray)
from collections.abc import Hashable
from dataclasses import dataclass
from typing import Protocol


class ArrayImplementation(Protocol):
    """Array of values following the Python array API standard."""


class UnitImplementation(Protocol):
    pass


@dataclass
class DimensionedArray:
    """
    General idea:
    - __getitem__ accepts dict with dims labels. Only 1-D allows for omitting index.
    - Probably we need to support duplicate dims
    - dims should be readonly?
    - unit must avoid assigning from slices? Do we need readonly flags?
    """

    values: ArrayImplementation
    dims: tuple[Hashable, ...]
    unit: UnitImplementation | None

    @property
    def shape(self) -> tuple[int, ...]:
        return self.values.shape

    # TODO
    # - not mutable dict
    # - not dict, since duplicates need to be supported
    @property
    def sizes(self) -> dict[Hashable, int]:
        return dict(zip(self.dims, self.shape, strict=True))