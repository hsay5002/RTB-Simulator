import pytest
from entities import Campaign, Advertiser
from ad_exchange import AdExchange

class BidRequest:
    def __init__(self, request_id, keywords):
        self.id = request_id
        self.keywords = set(keywords)

def test_auction_with_single_bidder():
    campaign = Campaign("c1", "Shoes", ["shoes"], 100, 1.0)
    advertiser = Advertiser("a1", "TestAd", 500, [campaign])
    exchange = AdExchange("TestExchange", [advertiser])
    req = BidRequest(1, ["shoes"])
    result = exchange.run_auction(req)
    assert result["winner"].name == "TestAd"
    assert result["price"] == 0.01

def test_no_bid():
    campaign = Campaign("c2", "Books", ["books"], 0, 1.0)
    advertiser = Advertiser("a2", "EmptyAd", 0, [campaign])
    exchange = AdExchange("TestExchange", [advertiser])
    req = BidRequest(2, ["sports"])
    result = exchange.run_auction(req)
    assert result is None