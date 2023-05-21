
class Utils:
    @staticmethod
    def clean_html(html: str) -> list[str]:
        html = html.split("<span>")[1].split("</span>")[0]
        if "4U" in html:
            return []
        
        if "1 of " in html:
            s: list[str] = html.split("(1 of ")
            if len(s) == 1:
                return []
            
            v: list[str] = s[1].replace(")", "").split(", ")
            v.append(s[0])
            return v
        
        if " or " not in html:
            return html.split(", ")
        
        if " and " in html:
            return html.split(" and ")
        
        if "), " in html and " or " in html:
            return html.replace("(", "").split("), ")[0].split(" or ")
        
        if " or (" in html:
            return html.split(" or (")
        
        if ", " in html and " or " not in html:
            return html.split(", ")

        # the result array
        res: list[str] = []

        if ", (" in html and " or " in html:
            res.append(html.split(", (")[0])

        # example: <strong>Prerequisite(s): </strong><span>(CIS*1300 or ENGG*1410), (CIS*1910 or ENGG*1500)</span>
        # get the CIS*1300 or ENGG*1410 and CIS*1910 or ENGG*1500 all in an array
        split: list[str] = html.replace("(", "").replace(", ", "").split(")")
        
        # iterate over the split
        for i in split:
            if len(i) == 0:
                continue
            [res.append(j) for j in i.split(" or ") if len(j) > 0]
        return res

# testing
if __name__ == "__main__":
    html: str = "<strong>Prerequisite(s): </strong><span>(CIS*1300 or ENGG*1410), (CIS*1910 or ENGG*1500)</span>"
    #html = "<strong>Prerequisite(s): </strong><span>CIS*2500, STAT*2040</span>"
    print(Utils.clean_html(html))