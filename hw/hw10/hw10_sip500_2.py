"""Homework 10.1."""
import asyncio
import json
from asyncio import Future
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


async def result(urls: List[str]) -> Future:
    """Get the result.

    Args:
        urls: urls

    Returns:
        The return value. Future object
    """
    tasks = [asyncio.create_task(fetch_response(url)) for url in urls]
    return await asyncio.gather(*tasks)


async def pages(
    urls: List[str], growth: Dict[str, str], rub_usd: float
) -> Tuple[List[Dict], List[Dict], List[Dict], List[Dict]]:
    """Treat the parsing results and return data to generate json.

    Args:
        urls: urls
        growth: link on the page of company/annual growth
        growth: rub per 1 usd

    Returns:
        The return value. 10 companies with the most expensive shares in rubles.
                          10 companies with the lowest P / E ratio.
                          10 companies that would bring the most profit if they were bought at the lowest
                                and sold at the highest in the last year.
                          10 companies that showed the highest growth in the last year

    """
    pages_htmls = await result(urls)
    most_exp = []
    most_p_e = []
    most_pot_profit = []
    most_growth = []
    for num, html in enumerate(pages_htmls):
        soup = BeautifulSoup(html, "html.parser")
        cnp = code_name_price(soup)
        comp = {"code": cnp[0], "name": cnp[1]}
        comp["price"] = round(cnp[2] * rub_usd, 2)
        most_exp.append(comp)
        comp = {"code": cnp[0], "name": cnp[1]}
        comp["P/E"] = p_e(soup)
        most_p_e.append(comp)
        comp = {"code": cnp[0], "name": cnp[1]}
        comp["potential profit"] = potential_profit(soup)
        most_pot_profit.append(comp)
        comp = {"code": cnp[0], "name": cnp[1]}
        comp["growth"] = growth[urls[num]]
        most_growth.append(comp)
    most_exp = sorted(most_exp, key=itemgetter("price"), reverse=True)
    most_p_e = sorted(most_p_e, key=itemgetter("P/E"))
    most_pot_profit = sorted(
        most_pot_profit, key=itemgetter("potential profit"), reverse=True
    )
    most_growth = sorted(most_growth, key=itemgetter("growth"), reverse=True)
    return most_exp[:10], most_p_e[:10], most_pot_profit[:10], most_growth[:10]


async def write_json(data: List[Dict], filename: Path) -> None:
    """Write json file.

    Args:
        data: data
        filename: Path
    """
    async with aiofiles.open(filename, mode="a") as f:
        await f.write(json.dumps(data))


async def write_files(
    res: Tuple[List[Dict], List[Dict], List[Dict], List[Dict]],
    path1: Path,
    path2: Path,
    path3: Path,
    path4: Path,
) -> None:
    """Write 4 files asynchronously.

    Args:
        res: data
        path1: Path of 1 file
        path2: Path of 2 file
        path3: Path of 3 file
        path4: Path of 4 file
    """
    files = [
        (res[0], Path(path1)),
        (res[1], Path(path2)),
        (res[2], Path(path3)),
        (res[3], Path(path4)),
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
    rub_usd = centrobank()
    urls = [
        f"https://markets.businessinsider.com/index/components/s&p_500?p={i}"
        for i in range(1, 11)
    ]
    htmls = await result(urls)
    all_urls = []
    growth = {}
    for page_htmls in htmls:
        links = companies(page_htmls)
        y_gr = year_growth(page_htmls)
        all_urls += links
        growth.update({link: growth for link, growth in zip(links, y_gr)})
    res = await pages(all_urls, growth, rub_usd)
    await write_files(res, Path(path1), Path(path2), Path(path3), Path(path4))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        main(Path("1.json"), Path("2.json"), Path("3.json"), Path("4.json"))
    )
