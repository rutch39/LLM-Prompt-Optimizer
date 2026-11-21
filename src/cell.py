def clip_cell(text: str, width: int = 32) -> str:
    s = str(text or '').strip()
    if len(s) <= width:
        return s
    return s[:max(1, width - 3)] + '...'
