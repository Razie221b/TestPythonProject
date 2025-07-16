import logging

log = logging.getLogger()


def is_not_null(value: str) -> bool:
    return value is not None and value.strip().lower() != 'null' and value.strip() != ""
