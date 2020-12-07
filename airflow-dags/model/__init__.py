class PatentDto:
    """
    Encapsulate patents information.
    """

    def __init__(self, patent_id: str, patent_nr: str, patent_title: str, patent_date: str, keyword: str):
        self.patent_id = patent_id
        self.patent_nr = patent_nr
        self.patent_title = patent_title
        self.patent_date = patent_date
        self.keyword = keyword

    @staticmethod
    def to_csv_header() -> str:
        return 'patent_id,patent_nr,patent_title,keyword,patent_date'

    def to_csv_entry(self) -> str:
        return f'{self.patent_id},{self.patent_nr},"{self.patent_title}","{self.keyword}",{self.patent_date}'
