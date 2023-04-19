import json


class Data:
    def __init__(self, json_data):
        self.json_data = json_data

    def get_data(self):
        try:
            data = json.loads(self.json_data)
            return data
        except json.decoder.JSONDecodeError:
            print('неверный формат данных')

    def vacancies(self, data):
        countries = set([i['country'] for i in data])
        answer = {'statistics': []}
        a = '\n'
        for country in countries:
            stat = {}
            stat['country'] = country
            stat['vacancies'] = '\n'.join([i['link'] for i in data if i['country'] == country])
            stat['vacancies_count'] = len(stat['vacancies'].split('\n'))
            stat['is_demanded'] = True if stat['vacancies_count'] >= 2 else False
            answer['statistics'].append(stat)
        answer['statistics'].sort(key=lambda x: x['vacancies_count'], reverse=True)
        ans = []
        for i in answer['statistics']:
            ans.append((f"{i['country']} has {i['vacancies_count']} vacancies:\n"
                  f"{i['vacancies']}.\n"
                  f"Python programmers are {'demended' if i['is_demanded'] == True else 'not demended'} in this country.\n\n"))
        return ans
