class URL:
    schema: str
    host: str
    path: str

    def __init__(self, url):
        if("://" not in url):
            print("Protocol missing in URL.")
            return
        
        self.schema, url = url.split("://")
        assert self.schema == "http"

        if url[-1] != "/":
            url += "/"

        self.host, url = url.split("/", 1)
        self.path = "/" + url