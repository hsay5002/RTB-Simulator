class Campaign:
    def __init__(self, campaign_id, name, target_keywords, budget, max_bid):
        self.campaign_id = campaign_id
        self.name = name
        self.target_keywords = set(target_keywords)
        self.budget = budget
        self.max_bid = max_bid

    def __repr__(self):
        return f"Campaign(id={self.campaign_id}, name='{self.name}', budget=${self.budget:.2f})"

    def reduce_budget(self, amount):
        self.budget -= amount


class Advertiser:
    def __init__(self, advertiser_id, name, budget, campaigns):
        self.advertiser_id = advertiser_id
        self.name = name
        self.budget = budget
        self.campaigns = campaigns

    def __repr__(self):
        return f"Advertiser(id={self.advertiser_id}, name='{self.name}', budget=${self.budget:.2f})"

    def get_relevant_campaign(self, keywords):
        best_campaign = None
        highest_bid = -1

        for campaign in self.campaigns:
            if campaign.target_keywords.intersection(keywords):
                if campaign.budget > 0 and self.budget > 0 and campaign.max_bid > highest_bid:
                    highest_bid = campaign.max_bid
                    best_campaign = campaign

        return best_campaign

    def reduce_budget(self, amount):
        self.budget -= amount