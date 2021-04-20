"""Homework 10.1."""
import asyncio
import json
from asyncio import Future
from concurrent.futures import ProcessPoolExecutor
from operator import itemgetter
from pathlib import Path
from typing import Dict, List, Tuple

import aiofiles
import aiohttp
import requests
from bs4 import BeautifulSoup


def year_growth(html: str) -> List[str]:
    """Parse annual growth.

    Args:
        html: one page companies

    Returns:
        The return value. Annual growth from 1 page companies
    """
    soup = BeautifulSoup(html, "html.parser")
    data = soup.find_all("span")
    growth = []
    for num, span in enumerate(data):
        if span.text.endswith("UTC-0400"):
            growth += [data[num + 6].text]
    return growth


def companies(html: str) -> List[str]:
    """Parse links of companies from 1 page.

    Args:
        html: one page companies

    Returns:
        The return value. links from 1 page companies
    """
    soup = BeautifulSoup(html, "html.parser")
    mn = []
    for link in soup.find_all("a"):
        k = link.get("href")
        if k.startswith("/stocks/"):
            mn.append("https://markets.businessinsider.com" + k)
    return mn[3 : len(mn) - 5]


def centrobank() -> float:
    """Parse XML data from sberbank RUB/USD course.

    Returns:
        The return value. RUB/USD course
    """
    response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
    soup = BeautifulSoup(response.content, "xml")
    data = soup.find(ID="R01235").Value.text
    coast = data.replace(",", ".")
    return float(coast)


def p_e(soup: BeautifulSoup) -> float:
    """Parse P/E ratio from personal page of company.

    Args:
        soup: parser

    Returns:
        The return value. P/E ratio
    """
    string = soup.find(class_="snapshot__header", string="P/E Ratio")
    try:
        data = string.find_parents(class_="snapshot__data-item")
    except AttributeError:
        return float("inf")
    data = data[0].text.split()[0]
    data = data.replace(",", "")
    return float(data)


def code_name_price(soup: BeautifulSoup) -> Tuple[str, str, float]:
    """Parse code, name, price shares in USD from personal page of company.

    Args:
        soup: parser

    Returns:
        The return value. Code, name, price shares in USD
    """
    data = soup.find("span", class_="price-section__category")
    code = data.span.text[2:]
    name = soup.find(class_="price-section__label").text
    data = soup.find(class_="price-section__current-value").text
    price_usd = float(data.replace(",", ""))
    return code, name.strip(), price_usd


def potential_profit(soup: BeautifulSoup) -> float:
    """Parse week_high, week_low indicators from personal page of company.

        Calculation formula: round(float(week_high) / float(week_low) * 100 - 100, 2)
    Args:
        soup: parser

    Returns:
        The return value. Potential profit in %
    """
    string = soup.find(string="52 Week Low")
    try:
        data = string.find_parent(
            class_="snapshot__data-item snapshot__data-item--small"
        )
    except AttributeError:
        return -float("inf")
    week_low = list(data)[0].strip()
    week_low = week_low.replace(",", "")
    string = soup.find(string="52 Week High")
    data = string.find_parent(
        class_="snapshot__data-item snapshot__data-item--small snapshot__data-item--right"
    )
    week_high = list(data)[0].strip()
    week_high = week_high.replace(",", "")
    return round(float(week_high) / float(week_low) * 100 - 100, 2)


async def fetch_response(url: str) -> str:
    """Fetch response function.

    Args:
        url: url

    Returns:
        The return value. Response.text
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def get_async_result(urls: List[str]) -> Future:
    """Get the result.

    Args:
        urls: urls

    Returns:
        The return value. Future object
    """
    tasks = [asyncio.create_task(fetch_response(url)) for url in urls]
    return await asyncio.gather(*tasks)


def price(cnp: Tuple[str, str, float]) -> Dict:
    """Form a resource.

    Args:
        cnp: code company, name company, price per share (usd)

    Returns:
        The return value. Dict {code, name, price}
    """
    rub_usd = centrobank()
    return {"code": cnp[0], "name": cnp[1], "price": round(cnp[2] * rub_usd, 2)}


def p_e_ratio(cnp: Tuple[str, str, float], soup: BeautifulSoup) -> Dict:
    """Form a resource.

    Args:
        cnp: code company, name company, price per share (usd)
        soup: instance of parser

    Returns:
        The return value. Dict {code, name, P/E}
    """
    return {"code": cnp[0], "name": cnp[1], "P/E": p_e(soup)}


def profit(cnp: Tuple[str, str, float], soup: BeautifulSoup) -> Dict:
    """Form a resource.

    Args:
        cnp: code company, name company, price per share (usd)
        soup: instance of parser

    Returns:
        The return value. Dict {code, name, potential profit}
    """
    return {"code": cnp[0], "name": cnp[1], "potential profit": potential_profit(soup)}


def m_growth(cnp: Tuple[str, str, float], growth: str) -> Dict:
    """Form a resource.

    Args:
        cnp: code company, name company, price per share (usd)
        growth: year growth of company

    Returns:
        The return value. Dict {code, name, growth}
    """
    return {"code": cnp[0], "name": cnp[1], "growth": growth}


TupleDict = Tuple[Dict, Dict, Dict, Dict]


def main_parser(html: str, growth: str) -> TupleDict:
    """Parse all indicators from 1 html page.

    Args:
        html: html page of company
        growth: year growth of company

    Returns:
        The return value. All indicators in special form
    """
    soup = BeautifulSoup(html, "html.parser")
    cnp = code_name_price(soup)
    return price(cnp), p_e_ratio(cnp, soup), profit(cnp, soup), m_growth(cnp, growth)


TupleListDict = Tuple[List[Dict], List[Dict], List[Dict], List[Dict]]
LD = List[Dict]


def four_sorted_list_10(lst1: LD, lst2: LD, lst3: LD, lst4: LD) -> TupleListDict:
    """Sort 4 lists of dictionaries.

    Args:
        lst1: list shares prices in rub
        lst2: list p_e ratio indicators
        lst3: list potential profit
        lst4: list annual growth

    Returns:
        The return value. 10 companies with the most expensive shares in rubles.
                          10 companies with the lowest P / E ratio.
                          10 companies that would bring the most profit if they were bought at the lowest
                                and sold at the highest in the last year.
                          10 companies that showed the highest growth in the last year
    """
    price = sorted(lst1, key=itemgetter("price"), reverse=True)
    p_e = sorted(lst2, key=itemgetter("P/E"))
    profit = sorted(lst3, key=itemgetter("potential profit"), reverse=True)
    growth = sorted(lst4, key=itemgetter("growth"), reverse=True)
    return price[:10], p_e[:10], profit[:10], growth[:10]


async def get_all_pages() -> Tuple[List[str], List[str]]:
    """Get a list of html pages of all companies and annual growth.

    Returns:
        The return value. Html pages of all companies and annual growth
    """
    urls = [
        f"https://markets.businessinsider.com/index/components/s&p_500?p={i}"
        for i in range(1, 11)
    ]
    htmls = await get_async_result(urls)
    all_html_pages = []
    growth = []
    for page_main_html in htmls:
        links = companies(page_main_html)
        growth += year_growth(page_main_html)
        pages_htmls = await get_async_result(links)
        for html in pages_htmls:
            all_html_pages += [html]
    return all_html_pages, growth


async def resources_for_write(htmls: List[str], growth: List[str]) -> TupleListDict:
    """Prepare and pass resource to write json file.

    Args:
        htmls: html pages of all companies
        growth: annual growth

    Returns:
        The return value. 10 companies with the most expensive shares in rubles.
                          10 companies with the lowest P / E ratio.
                          10 companies that would bring the most profit if they were bought at the lowest
                                and sold at the highest in the last year.
                          10 companies that showed the highest growth in the last year
    """
    with ProcessPoolExecutor(max_workers=17) as pool:
        resources = pool.map(main_parser, *(htmls, growth))
    most_price, low_p_e, most_pot_profit, most_growth = [], [], [], []
    for res in resources:
        most_price.append(res[0])
        low_p_e.append(res[1])
        most_pot_profit.append(res[2])
        most_growth.append(res[3])
    return four_sorted_list_10(most_price, low_p_e, most_pot_profit, most_growth)


async def write_json(data: LD, filename: Path) -> None:
    """Write json file.

    Args:
        data: data
        filename: Path
    """
    async with aiofiles.open(filename, mode="a") as f:
        await f.write(json.dumps(data, indent=4, sort_keys=True))


async def write_files(
    resource: TupleListDict, path1: Path, path2: Path, path3: Path, path4: Path
) -> None:
    """Write 4 files asynchronously.

    Args:
        resource: data for write
        path1: Path of 1 file
        path2: Path of 2 file
        path3: Path of 3 file
        path4: Path of 4 file
    """
    files = [
        (resource[0], Path(path1)),
        (resource[1], Path(path2)),
        (resource[2], Path(path3)),
        (resource[3], Path(path4)),
    ]
    tasks_write = [asyncio.create_task(write_json(*i)) for i in files]
    await asyncio.gather(*tasks_write)


async def main(path1: Path, path2: Path, path3: Path, path4: Path) -> None:
    """Parse information about companies in the S&P 500 index and load to 4 json files.

    Args:
        path1: Path of 1 file
        path2: Path of 2 file
        path3: Path of 3 file
        path4: Path of 4 file
    """
    results = await get_all_pages()
    htmls = results[0]
    growth = results[1]
    resource = await resources_for_write(htmls, growth)
    await write_files(resource, Path(path1), Path(path2), Path(path3), Path(path4))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        main(Path("1.json"), Path("2.json"), Path("3.json"), Path("4.json"))
    )
