from download import Downloader
from parse import Parser
from data import Data


def process(url, web_page_path=None, data_path=None):
    downloader = Downloader(url)
    downloader.get_html()
    downloader.save(web_page_path)
    new_parser = Parser(web_page_path)
    new_parser.parse()
    new_data = Data(new_parser.parsed_json_string)
    convert_json = new_data.get_data()
    some_logic = new_data.vacancies(convert_json)
    with open(data_path, 'w') as f:
        f.write("".join(some_logic))
    return some_logic


print(process('https://www.remotepython.com/jobs/', 'download.html', 'new.txt'))
