class AdExchange:
    def __init__(self, ad_network_name, advertisers):
        self.ad_network_name = ad_network_name
        self.advertisers = advertisers

    def run_auction(self, bid_request):
        print(f"\n[{self.ad_network_name}] Auction - BidRequest ID: {bid_request.id}, Keywords: {list(bid_request.keywords)}")
        bids = []

        for advertiser in self.advertisers:
            campaign = advertiser.get_relevant_campaign(bid_request.keywords)
            if campaign:
                bid_amount = campaign.max_bid
                bids.append({
                    "advertiser": advertiser,
                    "campaign": campaign,
                    "bid_amount": bid_amount
                })
                print(f"  > Bid from {advertiser.name} (Campaign: '{campaign.name}') - ${bid_amount:.2f}")

        if not bids:
            print("  No valid bids received.")
            return None

        bids.sort(key=lambda x: x['bid_amount'], reverse=True)

        if len(bids) == 1:
            winner = bids[0]
            winning_price = 0.01
            print(f"  One bid. Winner: {winner['advertiser'].name} (${winning_price:.2f})")
        else:
            winner = bids[0]
            second_highest = bids[1]['bid_amount']
            winning_price = second_highest
            print(f"  Winner: {winner['advertiser'].name} (${winning_price:.2f}) [Second-highest: ${second_highest:.2f}]")

        if winner['campaign'].budget < winning_price or winner['advertiser'].budget < winning_price:
            print(f"  Budget exceeded. {winner['advertiser'].name} can't pay ${winning_price:.2f}.")
            return None

        winner['advertiser'].reduce_budget(winning_price)
        winner['campaign'].reduce_budget(winning_price)

        print(f"  ✔️ Charged {winner['advertiser'].name}. Remaining: ${winner['advertiser'].budget:.2f}")

        return {"winner": winner['advertiser'], "price": winning_price}