from dataclasses import dataclass, field


@dataclass
class Entity:

    type: str
    value: str
    confidence: float = 1.0


@dataclass
class Intent:

    action: str | None = None

    target: str | None = None

    entities: list[Entity] = field(default_factory=list)

    modifiers: list[str] = field(default_factory=list)

    confidence: float = 0.0

    original_text: str = ""

    cleaned_text: str = ""

    tokens: list[str] = field(default_factory=list)