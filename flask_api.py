from flask import Flask, request, jsonify
from entities import Campaign, Advertiser
from ad_exchange import AdExchange

app = Flask(__name__)

# Setup dummy advertiser
nike = Advertiser(
    "adv001", "Nike Inc.", 1000,
    [Campaign("c001", "RunMax", ["sports", "shoes"], 500, 1.5)]
)
ad_exchange = AdExchange("AdTechX API", [nike])

class BidRequest:
    def __init__(self, req_id, keywords):
        self.id = req_id
        self.keywords = set(keywords)

@app.route('/bid', methods=['POST'])
def bid():
    data = request.json
    req_id = data.get("id", 1)
    keywords = data.get("keywords", [])
    bid_req = BidRequest(req_id, keywords)
    result = ad_exchange.run_auction(bid_req)
    if result:
        return jsonify({"winner": result["winner"].name, "price": result["price"]})
    else:
        return jsonify({"winner": None}), 204

if __name__ == "__main__":
    app.run(debug=True)