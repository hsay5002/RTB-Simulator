# RTB AdTech Simulator 🎯

A Python-based Real-Time Bidding (RTB) simulation to understand how programmatic advertising auctions work behind the scenes. This project models a simplified AdTech ecosystem with Advertisers, Campaigns, Publishers, and an Ad Exchange.

## Features

✅ Simulates second-price auctions (industry standard)  
✅ Models multiple advertisers and campaigns  
✅ Tracks advertiser and campaign budgets  
✅ Outputs realistic auction logs and budget consumption  
✅ Easy to extend for geotargeting, CTR, eCPM logic, and pacing

## Project Structure

```
RTB-AdTech-Simulator/
│
├── entities.py        # Advertiser and Campaign class definitions
├── ad_exchange.py     # Auction logic for second-price auctions
├── simulator.py       # Simulation engine that runs bid requests and prints results
└── README.md          # Project overview and instructions
```

## Getting Started

### 1. Requirements

- Python 3.x

### 2. Run the Simulation

```bash
python simulator.py
```

You’ll see 10 randomized auctions printed in your terminal.

### 3. Sample Output

```
[AdTechX Exchange] Auction - BidRequest ID: 101, Keywords: ['sports', 'fitness']
  > Bid from Nike Inc. (Campaign: 'RunMax Shoes') - $1.50
  > Bid from Amazon Ads (Campaign: 'FitSpace') - $1.30
  Winner: Nike Inc. ($1.30) [Second-highest: $1.30]
  ✔️ Charged Nike Inc. Remaining: $4998.70
```

## Extension Ideas

- Add CTR (Click-Through Rate) to compute eCPM = max_bid × CTR  
- Introduce geolocation and device targeting  
- Support both first-price and second-price modes  
- Add pacing and frequency capping

## License

MIT License

---

Built for educational purposes in understanding the core mechanics of AdTech RTB systems.