# /code/shared/gumroad_api.py

class GumroadAPI:
    def __init__(self):
        self.published = []

    def publish(self, product_data):
        # Fake publish logic for now
        product = {
            "title": product_data.get("title", "Untitled Product"),
            "description": product_data.get("description", ""),
            "price": product_data.get("price", 0)
        }
        self.published.append(product)
        return f"[GUMROAD MOCK] Launched '{product['title']}' at ${product['price']}"
