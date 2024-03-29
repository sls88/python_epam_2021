"""Homework 10.1."""
import asyncio
import json
from asyncio import Future
from concurrent.futures import ProcessPoolExecutor
from dataclasses import dataclass
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


@dataclass
class StockStat:
    """Save 4 lists of dictionaries stock statistic.

    Args:
        price: list shares prices in rub
        p_e: list p_e ratio indicators
        profit: list potential profit
        growth: list annual growth
    """

    price: List[Dict]
    p_e: List[Dict]
    profit: List[Dict]
    growth: List[Dict]


def four_sorted_list_10(stock_stat_obj: StockStat) -> StockStat:
    """Get 4 lists of stock statistic from dataclass, sort and write 10 pos. from every list back.

        10 companies with the most expensive shares in rubles.
        10 companies with the lowest P / E ratio.
        10 companies that would bring the most profit if they were bought at the lowest
                and sold at the highest in the last year.
        10 companies that showed the highest growth in the last year
    Args:
        stock_stat_obj: dataclass object

    Returns:
        The return value. Modified dataclass object
    """
    stock_stat_obj.price = sorted(
        stock_stat_obj.price, key=itemgetter("price"), reverse=True
    )[:10]
    stock_stat_obj.p_e = sorted(stock_stat_obj.p_e, key=itemgetter("P/E"))[:10]
    stock_stat_obj.profit = sorted(
        stock_stat_obj.profit, key=itemgetter("potential profit"), reverse=True
    )[:10]
    stock_stat_obj.growth = sorted(
        stock_stat_obj.growth, key=itemgetter("growth"), reverse=True
    )[:10]
    return stock_stat_obj


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


async def resources_for_write(htmls: List[str], growth: List[str]) -> StockStat:
    """Prepare and pass resource to write json file.

        10 companies with the most expensive shares in rubles.
        10 companies with the lowest P / E ratio.
        10 companies that would bring the most profit if they were bought at the lowest
             and sold at the highest in the last year.
        10 companies that showed the highest growth in the last year
    Args:
        htmls: html pages of all companies
        growth: annual growth

    Returns:
        The return value. Dataclass object
    """
    with ProcessPoolExecutor(max_workers=17) as pool:
        resources = pool.map(main_parser, *(htmls, growth))
    stock_stat_obj = StockStat([], [], [], [])
    for res in resources:
        stock_stat_obj.price.append(res[0])
        stock_stat_obj.p_e.append(res[1])
        stock_stat_obj.profit.append(res[2])
        stock_stat_obj.growth.append(res[3])
    return four_sorted_list_10(stock_stat_obj)


async def write_json(data: List[Dict], filename: Path) -> None:
    """Write json file.

    Args:
        data: data
        filename: Path
    """
    async with aiofiles.open(filename, mode="a") as f:
        await f.write(json.dumps(data, indent=4, sort_keys=True))


async def write_files(resource: StockStat, *paths: Path) -> None:
    """Write 4 files asynchronously.

    Args:
        resource: data for write from dataclass object
        *paths: 4 Paths to save files
    """
    resource = (resource.price, resource.p_e, resource.profit, resource.growth)
    files = [*zip(resource, paths)]
    tasks_write = [asyncio.create_task(write_json(*i)) for i in files]
    await asyncio.gather(*tasks_write)


async def main(*paths: Path) -> None:
    """Parse information about companies in the S&P 500 index and load to 4 json files.

    Args:
        *paths: 4 Paths to save files
    """
    results = await get_all_pages()
    htmls = results[0]
    growth = results[1]
    resource = await resources_for_write(htmls, growth)
    paths = [Path(path) for path in paths]
    await write_files(resource, *paths)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    paths = ("price.json", "p_e.json", "profit.json", "growth.json")
    paths = tuple(Path(el) for el in paths)
    loop.run_until_complete(main(*paths))
