"""Fictional offline helper used only by the handoff demonstration."""


def is_terminal(status: str) -> bool:
    return status in {"SUCCEEDED", "FAILED"}
