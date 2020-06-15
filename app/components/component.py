from abc import ABC, abstractmethod
from typing import Dict, Any


class Component(ABC):

    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        pass
