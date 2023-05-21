import json

class Request:
    @staticmethod
    def headers() -> dict[str, str]:
        return {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
        }
    
    @staticmethod
    def query_payload(query: str) -> str:
        return json.dumps({
            "other": {
                "srcdb": ""
            },
            "criteria": [
                {
                    "field": "keyword",
                    "value": query
                }
            ]
        })
    
    # key example: "key:3381"
    @staticmethod
    def details_payload(key: str) -> str:
        return json.dumps({
            "group": key,
            "key": key,
            "srcdb": "2023",
            "matched": key
        })