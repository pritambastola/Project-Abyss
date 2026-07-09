from dataclasses import dataclass, field


@dataclass
class Intent:

    action: str | None = None

    target: str | None = None

    value: str | None = None

    modifiers: list[str] = field(default_factory=list)

    confidence: float = 0.0

    original_text: str = ""

    normalized_text: str = ""