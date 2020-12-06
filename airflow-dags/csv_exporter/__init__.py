from typing import List

from model import PatentDto


def export_patterns(filename: str, patents: List[PatentDto]):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(PatentDto.to_csv_header() + '\n')
        for patent in patents:
            file.write(patent.to_csv_entry() + '\n')
