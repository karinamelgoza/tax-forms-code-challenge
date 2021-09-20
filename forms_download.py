import requests
import os
from bs4 import BeautifulSoup


def download_forms(form_name, beg_year, end_year):

    URL = f"https://apps.irs.gov/app/picklist/list/priorFormPublication.html?resultsPerPage=200&sortColumn=sortOrder&indexOfFirstRow=0&criteria=formNumber&value={form_name}&isDescending=false"

    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    path = os.getcwd()
    os.mkdir(f"{path}/{form_name}")

    for year in range(beg_year, end_year+1):

        results = soup.find(
            "a", href=lambda href: href and str(year) in href, string=form_name)

        if results:

            link = results.get('href')

            with open(f"{form_name}/{form_name}-{year}.pdf", "wb") as f:
                response = requests.get(link)
                f.write(response.content)

            print(f"{form_name}-{year} downloaded")

        else:

            print("Not Available")


if __name__ == "__main__":
    download_forms('Form W-2', 2018, 2020)
