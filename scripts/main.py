from bs4 import BeautifulSoup
import requests


def main():

    url = 'https://medium.com/comet-ml/applyingmachinelearningtoaudioanalysis-utm-source-kdnuggets11-19-e160b069e88'
    response = requests.get(url)
    r_html = response.text
    soup = BeautifulSoup(r_html, 'html5lib')

    with open('original.txt', 'w') as f:
        f.write(soup.prettify())

    soup.find(attrs={'data-test-id': 'post-sidebar'}).decompose()
    # print(type(something))

    with open('modified.txt', 'w') as f:
        f.write(soup.prettify())


if __name__ == '__main__':
    main()
