from abc import ABC, abstractstaticmethod


class Importer(ABC):
    @abstractstaticmethod
    def import_data(path: str) -> str:
        pass
