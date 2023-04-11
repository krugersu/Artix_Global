import requests


class ServerRestApi:

    def __init__(self, host="192.168.0.238", port=38056, user="",
                 password="", rest=""):
        self.restHeader = {'Content-Type': 'application/json'}
        self.user = user
        self.password = password
        self.restRoot = "/ACC"
        self.host = f"http://{host}:{str(port)}{self.restRoot}"
        self.session = requests.Session()

    def _sendmsg(self, url, msg="", method="get", head=None):
        if head is None:
            head = {"Content-Type": "application/json"}
        send = getattr(self.session, method)
        if method == "get":
            resp = send(url, headers=head, timeout=30, auth=(self.user, self.password))
        else:
            resp = send(url, msg, headers=head, timeout=30)
        return resp

    def sendmsg(self, url, msg="", method="get", head=None):
        return self._sendmsg(self.host + url, msg, method, head)

    def get_accounts(self):
        resp = self.sendmsg("/rest/v1/accounts")
        if resp.status_code == 200:
            return resp.json()
        else:
            return []


if __name__ == "__main__":
    rest = ServerRestApi("192.168.0.238", user="LM_DEFAULT_TERMINAL")
    print(rest.get_accounts())
