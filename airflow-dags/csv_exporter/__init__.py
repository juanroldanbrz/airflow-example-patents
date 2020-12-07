from typing import List

from model import PatentDto


def export_patents(filename: str, patents: List[PatentDto]):
    """
    Export patent DTOs to CSV files.
    :param filename: output filename.
    :param patents: list of patents to serialize.
    """

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(PatentDto.to_csv_header() + '\n')
        for patent in patents:
            file.write(patent.to_csv_entry() + '\n')
