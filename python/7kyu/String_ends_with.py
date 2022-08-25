def solution(string: str, ending: str) -> bool:
    return string[-len(ending):] if len(ending) == 0 else "" == ending
