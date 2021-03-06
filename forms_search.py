import requests
import json
from bs4 import BeautifulSoup


def search_irs_forms(search):

    results_info = []

    for search_term in search:
        URL = f"https://apps.irs.gov/app/picklist/list/priorFormPublication.html?resultsPerPage=200&sortColumn=sortOrder&indexOfFirstRow=0&criteria=formNumber&value={search_term}&isDescending=false"

        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")

        results = soup.find_all("a", string=search_term)
        forms = [form_link.parent.parent for form_link in results]
        years = []

        if results:

            for form in forms:

                year = int(
                    form.find("td", class_="EndCellSpacer").text.strip())
                years.append(year)

                info = {
                    "form_number": form.find("a", string=search_term).text.strip(),
                    "form_title": form.find("td", class_="MiddleCellSpacer").text.strip(),
                    "min_year": min(years),
                    "max_year": max(years)
                }
        else:

            info = {
                search_term: "Not Found"
            }

        results_info.append(info)

    return json.dumps(results_info, indent=2)


# if __name__ == "__main__":
#     print(search_irs_forms(["Form W-2", "Form 1095-C", "Form W-2 P"]))
