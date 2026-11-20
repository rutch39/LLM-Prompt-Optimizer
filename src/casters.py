def as_bool(val: str, default: bool = False) -> bool:
    if val is None:
        return default
    return str(val).strip().lower() in {'1', 'true', 'yes', 'on'}

def as_int(val: str, default: int = 0) -> int:
    try:
        return int(str(val).strip())
    except (TypeError, ValueError):
        return default
