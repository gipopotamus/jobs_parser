from bs4 import BeautifulSoup
import json


class Parser:

    def __init__(self, source: str) -> None:
        self.source = source
        self.parsed_json_string = None

    def parse(self) -> None:
        try:
            if len(self.source) == 0 or type(self.source) == int:
                raise ValueError

            else:
                records = []
                file = open(self.source, 'r').read()
                bs_string = BeautifulSoup(file, "html.parser")
                list_of_vacancies: list = bs_string.find(class_="box-list").find_all(class_="col-md-11")
                for vacancy in list_of_vacancies:
                    title: str = vacancy.find('h3').text.strip(' ')
                    link: str = 'https://www.remotepython.com/' + vacancy.find('h3').find('a').get('href')
                    country: str = vacancy.find('h5').find_all('span')[-1].text.split(',')[-1].strip(' ')
                    year: int = int(vacancy.find('div').find('span').text.split(', ')[-1])
                    records.append({
                        'vacancy': title,
                        'link': link,
                        'country': country,
                        'year': year,
                    })

                self.parsed_json_string = json.dumps(records)

        except ValueError:
            print("Ошибка при указании пути ('path/to/file.html').")



