from pprint import pprint
from bs4 import BeautifulSoup
import requests

class CoronaVirus:
    web_url = "https://www.worldometers.info/coronavirus/"
    
    def get_html(self, url):
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        return soup

    def get_table(self, soup):
        return soup.find('table', attrs={'id': 'main_table_countries_today'})

    # headers
    def get_headers(self, table):
        header_names = []
        for th_tag in table.find_all('thead')[0].find_all('tr'):
            header_names = [header_name.text.strip() for header_name in th_tag.find_all('th')[:15]]
        return header_names

    # body
    def get_body_info(self, table):
        countries_infos = []
        for country in table.find_all('tbody')[0].find_all('tr')[8:]:
            countries_infos.append([i.text.strip() for i in country.find_all('td')[:15]])
        return countries_infos

    def write_to_file(self):
        headers= self.get_headers(self.get_table(self.get_html(self.web_url)))
        body = self.get_body_info(self.get_table(self.get_html(self.web_url)))

        with open('myresult.txt', 'w') as file:
            file.write( f"{headers}\n" )
            print(f"{headers}\n")
            for infos in body:
                file.write(f"{infos}\n")
                print(f"{infos}\n")


if __name__ == '__main__':
    #corona_virus_obj = CoronaVirus()
    pprint(corona_virus_obj.write_to_file())
