import requests


class Downloader:

    def __init__(self, url: str, params: dict = {}, method: str = "GET") -> None:
        self.url = url
        self.params = params
        self.method = method
        self.html = None

    def get_html(self) -> str:
        try:

            if self.method == "GET":
                response = requests.get(self.url, params=self.params)
                self.html = response

            elif self.method == "POST":
                response = requests.post(self.url, params=self.params)
                self.html = response

            else:
                print("Некорректный метод (GET | POST)")
                return ""

            return self.html.text

        except requests.exceptions.ConnectionError:
            print("Удаленный хост закрыл подключение без ответа. Попробуйте позже...")
            return ""

        except requests.exceptions.InvalidURL:
            print("Введен некорректный URL (https://...).")
            return ""

        except TypeError:
            print("Отсутсвует URL (https://...).")
            return ""

    def save(self, filepath: str) -> None:
        try:
            if type(self.html.content) == bytes:

                if type(filepath) == int:
                    raise ValueError

                else:
                    file = open(filepath, "w", encoding="utf-8")
                    file.write(self.html.text)
                    file.close()

        except FileNotFoundError:
            print(
                "Ошибка записи файла. Задайте корректный путь к директории и название файла ('path/to/download.html')")

        except AttributeError:
            print("Ошибка создания файла. Задайте ссылку в методе get_html (Downloader.get_html(url)).")

        except ValueError:
            print("Ошибка записи файла. Возможно, кодировка.")


