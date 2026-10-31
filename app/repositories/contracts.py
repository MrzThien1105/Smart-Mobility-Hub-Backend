from typing import Protocol, TypeVar


EntityT = TypeVar("EntityT")


class Repository(Protocol[EntityT]):
    def get(self, **criteria) -> EntityT | None: ...

    def list(self, offset: int = 0, limit: int = 50) -> tuple[list[EntityT], int]: ...

    def add(self, entity: EntityT) -> EntityT: ...

    def delete(self, entity: EntityT) -> None: ...
