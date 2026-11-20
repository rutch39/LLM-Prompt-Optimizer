from .defaults import DEFAULT_ENV

def resolve_key(env_map: dict, key: str) -> str:
    return env_map.get(key, DEFAULT_ENV.get(key, ''))
