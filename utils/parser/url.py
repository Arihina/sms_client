class UrlParser:
    """
    A class for parsing strings with URL.
    """

    @staticmethod
    def parse(url: str) -> tuple[str, int, str]:
        """
        Selects the URL string.

        :param url: The URL string.
        :return: The tuple from host, port, URI of URL.
        """
        try:
            if url.startswith("http://"):
                url = url[7:]

            url_parts = url.split("/", 1)
            host_port, uri = url_parts[0], "/" + url_parts[1]
            host, port = host_port.split(":")
            port = int(port)

            return host, port, uri
        except ValueError as e:
            raise ValueError(f"Value error in URL: {e}")
        except Exception as e:
            raise Exception(f"Unexpected error occurred: {e}")
