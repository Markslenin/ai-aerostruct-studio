from abc import ABC, abstractmethod
from typing import Any

from pydantic import BaseModel


class SkillResult(BaseModel):
    success: bool
    data: dict[str, Any] = {}
    warnings: list[str] = []
    errors: list[str] = []


class BaseSkill(ABC):
    name: str
    description: str

    @abstractmethod
    def run(self, data: dict[str, Any]) -> SkillResult:
        raise NotImplementedError
