import httpx
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class BelvoAPIClient:
    def __init__(self, base_url, username, password):
        self.base_url = base_url
        self.client = httpx.Client(auth=(username, password), base_url=base_url)

    def get_institutions(self) -> dict:
        response = self.client.get("links").json()
        institutions = {data["institution"] for data in response["results"]}
        response = self.client.get("institutions", params={"name__in": ",".join(institutions)})

        return response.json()

    def get_accounts(self, institution: str) -> dict:
        response = self.client.get("accounts", params={"institution": institution})
        return response.json()

    def get_transactions(self, link: str, account: str) -> dict:
        response = self.client.get(
            "transactions", params={"link": link, "account": account, "page_size": 100}
        )
        data = response.json()
        transactions = data["results"]

        while data["next"] is not None:
            response = self.client.get(data["next"])
            data = response.json()
            transactions += data["results"]

        balance = sum(
            transaction["amount"] if transaction["type"] == "INFLOW" else -transaction["amount"]
            for transaction in transactions
        )

        return {"balance": balance, "results": transactions}
