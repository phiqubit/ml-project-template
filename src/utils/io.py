"""Simple JSON I/O helpers."""
from pathlib import Path
import json
from typing import Any

def read_json(path: str | Path) -> Any:
    """Read and parse JSON from file."""
    return json.loads(Path(path).read_text())

def write_json(path: str | Path, obj: Any) -> None:
    """Write object as JSON to file, creating parents if needed."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj))

