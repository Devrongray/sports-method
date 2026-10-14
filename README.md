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

1. Push this folder to a GitHub repository. On the first push, two workflows
   run by themselves and commit their results to `analysis/`: **Test (c)**
   (Pinnacle closing reliability, no key needed) and **Discover** (the live
   Polymarket US league list and a check of every configured slug and
   market type). The 30-minute snapshot loop and the daily history pull
   start on their schedules.
2. Add the repository secret `ODDS_API_KEY` (The Odds API). Without it the
   Polymarket side still runs; the Pinnacle side is skipped.
3. League slugs in `config/sports.yaml` were confirmed against the live list
   on 14 Oct 2026; `analysis/discovery/summary.md` is refreshed daily and
   shows any slug that stops matching.

## Market classes

Polymarket US names market types by sport (`BASKETBALL_TEAM_FULL_GAME_WINNER`,
`HOCKEY_TEAM_FIRST_PERIOD_TOTAL`, `FOOTBALL_GAME_FIRST_HALF_TOTAL`,
`BASEBALL_TEAM_INNING3_TOTAL`, `ESPORTS_MATCH_WINNER`,
`ESPORTS_MAP_TOTAL_ROUNDS_1`, ...). `polymarket_us.classify` maps each to a
class (`WINNER`, `TOTAL`, `SPREAD`, `TEAM_TOTAL`) and a segment
(`FULL_GAME`, `FIRST_HALF`, `FIRST_PERIOD`, `INNING3`, `MAP_1`, `SERIES`,
...). Every market of every upcoming event is written to the `markets_*`
file each pass (all alternate lines, with an `is_main` flag for the line
closest to even). BBO calls, order books and price histories go to main
lines of the configured classes only.

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

## Data notes

- `data/polymarket/2026-10-14/*_20261014T192700Z.*`: first live pass. Its
  `is_main` flags on totals/spread ladders are unreliable (the picker then
  compared the two side prices, which are the bid and ask of one contract,
  rather than the contract mid). All lines are in the markets file, so the
  main line can be recomputed; BBO rows exist only for the lines it picked.
