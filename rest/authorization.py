class TokenNumbres:
    @staticmethod
    def token():
        with open("token.txt", "r") as file:
            content = file.read()
        return content

