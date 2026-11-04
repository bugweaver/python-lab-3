class CatalogError(Exception):
    "Base exception"


# TODO: Неверная сущность


class DuplicatedIdError(CatalogError):
    def __init__(self) -> None:
        super().__init__("Element with this id is already in the list")


class ObjectIsNotFoundError(CatalogError):
    def __init__(self) -> None:
        super().__init__("Element is not found")


class VersionIsNotSupportedError(CatalogError):
    def __init__(self) -> None:
        super().__init__("Version is not supported")


class CorruptedFileError(CatalogError):
    def __init__(self) -> None:
        super().__init__("File is corrupted")
