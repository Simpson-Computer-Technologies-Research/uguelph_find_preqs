import requests, typing
from request import Request
from utils import Utils

class Courses(Request):
    @staticmethod
    def query(query: str) -> typing.Any:
        # set the api url and params
        url: str = "https://calendar.uoguelph.ca/course-search/api/"
        params: str = "?page=fose&route=search&keyword=" + query
        
        # get the headers
        headers: dict[str, str] = Courses.headers()

        # get the data
        data: str = Courses.query_payload(query)

        # send the request
        resp = requests.post(url + params, headers=headers, data=data)

        # return the response json
        if resp.status_code == 200:
            return resp.json()
        return resp.text
    
    @staticmethod
    def get_key(results: dict[typing.Any, typing.Any], query: str) -> str:
        r: list[str] = [r["key"] for r in results["results"] if r["code"] == query]
        if len(r) == 0:
            return ""
        return r[0]
    
    @staticmethod
    def details(results: dict[typing.Any, typing.Any], query: str) -> typing.Any:
        # set the api url and params
        url: str = "https://calendar.uoguelph.ca/course-search/api/"
        params: str = "?page=fose&route=details"

        # get the headers
        headers: dict[str, str] = Courses.headers()

        # get the key
        key: str = Courses.get_key(results, query)
        if len(key) == 0:
            return None

        # get the data
        data: str = Courses.details_payload(f"key:{key}")

        # send the request
        resp = requests.post(url + params, headers=headers, data=data)

        # return the response json
        if resp.status_code == 200:
            return resp.json()
        return resp.text

    @staticmethod
    def requisites(details: dict[typing.Any, typing.Any]):
        if details is None:
            return None
        
        # result dict
        res: dict = {}

        # clean the html from the details["prerequisite_s_"]
        html: str = details["prerequisite_s_"]
        if len(html) == 0:
            return None
        
        # get the codes
        codes: list[str] = Utils.clean_html(html)

        # iterate over the codes
        for code in codes:
            results: dict[typing.Any, typing.Any] = Courses.query(code)
            details = Courses.details(results, code)
            res[code] = Courses.requisites(details)

        # return the result dict
        return res