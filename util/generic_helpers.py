import random
from typing import Any, Iterator


def cycle_random(l: list[Any]) -> Iterator[Any]:
    """Yields random item, won't repeat item until all others have been yielded."""
    used_items = []

    while True:
        if len(l) == len(used_items):
            used_items.clear()

        chosen_item = random.choice([i for i in l if i not in used_items])
        used_items.append(chosen_item)
        yield chosen_item
