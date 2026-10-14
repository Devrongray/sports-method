# Sports Prediction Method — data pipeline (v0.1)

Code for the data phase of *Sports Prediction Method v1*: record Polymarket US
and Pinnacle prices, grade bets by closing-line value (CLV), and run the
pre-registered 90-day tests. Nothing here places a bet.

## What it does

| Piece | Purpose | Test it serves |
|---|---|---|
| `method/polymarket_us.py` | Public, keyless client for the Polymarket US gateway: leagues, events, markets, BBO, order book, minute-level price history, settlement | (a) lag, (b) calibration, (d) maker/taker |
| `method/odds_api.py` | The Odds API v4 client, filtered to Pinnacle, quota-aware | sharp reference price for every test |
| `method/snapshot.py` | `pass`: record BBO (and books near start) for upcoming games plus Pinnacle odds. `history`: after games, pull each market's full 24h price path and settlement | (a), (b), (d) |
| `method/devig.py` | Multiplicative, additive, power and Shin de-vigging | fair prices |
| `method/metrics.py` | Log loss, Brier, calibration slope/intercept, Murphy decomposition, CLV, sample-size arithmetic | scorecard |
| `method/fees.py` | Polymarket US taker fee `0.0695·p(1−p)`, break-even, edge after costs, fractional Kelly | execution |
| `method/pinnacle_reliability.py` | Test (c): Pinnacle closing-price calibration by season (2019–2026) and de-vig comparison on football-data.co.uk | (c) |
| `.github/workflows/` | Snapshot loop every 30 min, daily history pull, test (c) on demand | automation |

## Why GitHub Actions

Claude's workspace cannot reach polymarket.us, the-odds-api.com or
football-data.co.uk (its network is limited to package registries and
GitHub). A GitHub Actions runner can. The workflows record data to a `data`
branch so the repo stays the single durable home for code and data.

## Setup (one time)

1. Create a GitHub repository and push this folder.
2. Add the repository secret `ODDS_API_KEY` (The Odds API). Without it the
   Polymarket side still runs; the Pinnacle side is skipped.
3. Run the **Test (c)** workflow once by hand (Actions → Pinnacle reliability →
   Run workflow). It needs no key.
4. Check `config/sports.yaml`: the Polymarket league slugs are best guesses.
   The first snapshot run prints the real slugs from `/v2/leagues`; fix any
   that differ.

## Running locally

```
pip install -r requirements.txt
pytest                                    # math checks, no network
python -m method.snapshot leagues         # print Polymarket US league slugs
python -m method.snapshot pass --out data # one snapshot pass
python -m method.snapshot history --out data --hours 24
python -m method.pinnacle_reliability --out analysis/test_c
```

## Costs and limits

- Polymarket US public API: no key; 20 requests/second/IP on price history.
- The Odds API: each call to `/v4/sports/{sport}/odds` costs 1 credit per
  market per region. With `h2h,totals` in region `eu` that is 2 credits per
  sport per poll. Default cadence (30 min, 5 min inside the last 90 minutes
  before a game) runs about 6–10k credits/month for five sports; the free
  tier (500/month) covers only a trial, so budget for a paid tier.
- Esports: The Odds API does not carry CS2/LoL. Pinnacle esports odds need a
  second feed (OddsPapi has a free Pinnacle esports endpoint); `odds_api.py`
  leaves a hook for it.

## Data layout (`data` branch)

```
data/polymarket/YYYY-MM-DD/markets_<ts>.ndjson.gz   # event + market metadata per pass
data/polymarket/YYYY-MM-DD/bbo_<ts>.ndjson.gz       # one row per market per pass
data/polymarket/YYYY-MM-DD/book_<ts>.ndjson.gz      # order books inside the pre-start window
data/polymarket_history/YYYY-MM-DD/<market_slug>.json.gz  # minute-level price path + settlement
data/pinnacle/YYYY-MM-DD/odds_<ts>.ndjson.gz        # one row per outcome per pass
analysis/test_c/                                     # test (c) outputs
```

Every row carries `ts` (UTC, when we recorded it) and the venue's own
timestamp where the API gives one (`transactTime`, `last_update`,
`lastPriceSample.ts`). Timestamp alignment is the main data-quality risk in
the lag test, so both are kept.

## Not yet built

- News timestamps for the lag test (NBA official injury reports, MLB lineups
  via MLB StatsAPI, NHL goalie confirmations). Next addition.
- Pinnacle esports feed.
- The order-placement layer (Phase 2, needs your go and an API key).
