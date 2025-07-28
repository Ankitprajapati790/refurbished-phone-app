# utils.py

condition_map = {
    "Like New": {
        "X": "New",
        "Y": "3 Stars (Excellent)",
        "Z": "New"
    },
    "Good": {
        "X": "Good",
        "Y": "2 Stars (Good)",
        "Z": "As New"
    },
    "Fair": {
        "X": "Scrap",
        "Y": "1 Star (Usable)",
        "Z": "Good"
    }
}

def get_platform_data(phone):
    price = phone['base_price']
    condition = phone['condition']
    platforms = []

    platforms.append({
        "platform": "X",
        "condition": condition_map[condition]["X"],
        "price": round(price * 1.10, 2),  # 10% fee
        "fee": "10%"
    })
    platforms.append({
        "platform": "Y",
        "condition": condition_map[condition]["Y"],
        "price": round(price * 1.08 + 2, 2),  # 8% + $2
        "fee": "8% + $2"
    })
    platforms.append({
        "platform": "Z",
        "condition": condition_map[condition]["Z"],
        "price": round(price * 1.12, 2),  # 12% fee
        "fee": "12%"
    })
    return platforms

def check_profitability(platform_data):
    base_price = platform_data["price"]
    cost = base_price / 1.1 if platform_data["platform"] == "X" else \
           (base_price - 2) / 1.08 if platform_data["platform"] == "Y" else \
           base_price / 1.12
    return base_price - cost > 0
