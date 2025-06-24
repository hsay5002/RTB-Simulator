import random
from entities import Campaign, Advertiser
from ad_exchange import AdExchange

class BidRequest:
    def __init__(self, request_id, keywords):
        self.id = request_id
        self.keywords = set(keywords)

# Define campaigns and advertisers (AdTech simulation)
nike = Advertiser(
    advertiser_id="adv001",
    name="Nike Inc.",
    budget=5000,
    campaigns=[
        Campaign("c001", "RunMax Shoes", ["running", "shoes", "sports"], 1000, 1.50),
        Campaign("c002", "Pro Apparel", ["apparel", "clothing", "sportswear"], 800, 1.20)
    ]
)

amazon = Advertiser(
    advertiser_id="adv002",
    name="Amazon Ads",
    budget=10000,
    campaigns=[
        Campaign("c003", "BookZone", ["books", "reading"], 500, 0.80),
        Campaign("c004", "Tech Bazaar", ["electronics", "tech", "deals"], 1500, 1.75),
        Campaign("c005", "FitSpace", ["sports", "fitness"], 700, 1.30)
    ]
)

booking = Advertiser(
    advertiser_id="adv003",
    name="Booking Holdings",
    budget=8000,
    campaigns=[
        Campaign("c006", "StayFinder", ["hotel", "travel", "vacation"], 2000, 2.00),
        Campaign("c007", "SkySaver Flights", ["flights", "airline", "travel"], 2500, 2.25)
    ]
)

ad_exchange = AdExchange("AdTechX Exchange", [nike, amazon, booking])

# Simulated user requests from publishers
bid_requests = [
    BidRequest(1, ["sports", "running"]),
    BidRequest(2, ["travel", "flights", "vacation"]),
    BidRequest(3, ["fashion", "clothing"]),
    BidRequest(4, ["tech", "deals"]),
    BidRequest(5, ["books", "reading"]),
    BidRequest(6, ["sports", "fitness", "shoes"]),
    BidRequest(7, ["vacation", "hotel"]),
    BidRequest(8, ["news", "politics"]),
]

print("==== AdTech RTB Simulation ====")
for i in range(10):
    request = random.choice(bid_requests)
    request.id = i + 100
    ad_exchange.run_auction(request)

print("\n==== Final Budget States ====")
for advertiser in [nike, amazon, booking]:
    print(f"{advertiser.name}: ${advertiser.budget:.2f}")
    for c in advertiser.campaigns:
        print(f"  - {c.name}: ${c.budget:.2f}")