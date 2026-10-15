# Daily analysis 2026-10-15

## Coverage

| source | sport | rows | events | passes | window_rows | first | last |
|---|---|---|---|---|---|---|---|
| polymarket_bbo | bundesliga | 90 | 1 | 15 | 0 | 10-15 06:34 | 10-15 10:22 |
| polymarket_bbo | cs2 | 5,287 | 99 | 332 | 765 | 10-14 19:27 | 10-15 10:17 |
| polymarket_bbo | laliga | 72 | 1 | 12 | 0 | 10-15 07:34 | 10-15 10:22 |
| polymarket_bbo | ligue1 | 78 | 1 | 13 | 0 | 10-15 06:55 | 10-15 10:22 |
| polymarket_bbo | lol | 234 | 3 | 104 | 39 | 10-14 19:27 | 10-15 10:11 |
| polymarket_bbo | mlb | 3,222 | 4 | 129 | 882 | 10-14 19:27 | 10-15 10:22 |
| polymarket_bbo | nba | 2,212 | 9 | 192 | 1,257 | 10-14 19:27 | 10-15 10:22 |
| polymarket_bbo | nfl | 462 | 1 | 66 | 0 | 10-14 19:27 | 10-15 10:22 |
| polymarket_bbo | nhl | 8,262 | 13 | 171 | 1,125 | 10-14 19:27 | 10-15 10:22 |
| polymarket_bbo | seriea | 78 | 1 | 13 | 0 | 10-15 06:55 | 10-15 10:22 |
| pinnacle | mlb | 242 | 3 | 35 |  | 10-14 21:29 | 10-15 10:00 |
| pinnacle | nba | 2,256 | 12 | 47 |  | 10-14 21:29 | 10-15 10:00 |
| pinnacle | nfl | 1,176 | 14 | 21 |  | 10-14 21:29 | 10-15 10:00 |
| pinnacle | nhl | 2,150 | 13 | 43 |  | 10-14 21:29 | 10-15 10:00 |
| polymarket_history | cs2 | 53 | 45 | 34,768 |  | NaT | NaT |
| polymarket_history | lol | 1 | 0 | 776 |  | NaT | NaT |
| polymarket_history | mlb | 33 | 33 | 35,673 |  | NaT | NaT |
| polymarket_history | nba | 117 | 117 | 121,689 |  | NaT | NaT |
| polymarket_history | nhl | 52 | 52 | 56,212 |  | NaT | NaT |
| news_mlb | mlb | 23 |  |  |  | NaT | NaT |
| news_nhl | nhl | 22 |  |  |  | NaT | NaT |
| news_nhl_schedule | nhl | 28 |  |  |  | NaT | NaT |

Odds API quota at last pass: used 222.0, remaining 19778.0 (59 Pinnacle passes recorded).

## Event matching (Polymarket US vs Pinnacle)

133 Polymarket events, 42 Pinnacle events, 17 matched (4 by full name, 13 by nickname).

Unmatched Polymarket events (116): bundesliga Eintracht Frankfurt vs. 1. FC Koln; cs2  Phantom Academy vs. ZOTIX; cs2 FURIA vs. BetBoom Team; cs2 Pandaric eSports vs. BIG Academy; cs2 WBT vs. Esport Academy Copenhagen; cs2 ENCE vs. BOJONG; cs2 Heroic vs. Envy; cs2 MIBR vs. BC.Game Esports; cs2 WBT vs. ENCE; cs2 Esport Academy Copenhagen vs. BOJONG; cs2 WBT vs. BOJONG; cs2 Saint Sinners vs. maybe; cs2 Esport Academy Copenhagen vs. ENCE; cs2 Damajuana vs. Alianza Lima Esports; cs2 Joga de terno vs. A NATA

## Polymarket mid vs Pinnacle fair, main winner contracts

mid_minus_fair > 0 means Polymarket prices the team higher than Pinnacle's de-vigged price. taker_edge_at_ask = fair − ask − fee: what a taker would expect if Pinnacle were exactly right.

| sport | bucket | n | mean_diff | mean_abs_diff | within_1c | within_2c | mean_spread | median_bid_shares | taker_edge_mean | taker_edge_pos_share |
|---|---|---|---|---|---|---|---|---|---|---|
| mlb | 0-15 min | 7 | 0.022 | 0.027 | 43% | 57% | 0.005 | 700,000 | -0.039 | 0% |
| mlb | 15-60 min | 8 | -0.002 | 0.002 | 100% | 100% | 0.005 | 4,200,000 | -0.017 | 0% |
| mlb | 1-3 h | 9 | -0.001 | 0.002 | 100% | 100% | 0.005 | 4,400,000 | -0.018 | 0% |
| mlb | 3-12 h | 7 | 0.001 | 0.003 | 100% | 100% | 0.005 | 1,500,000 | -0.021 | 0% |
| mlb | 12 h+ | 29 | 0.015 | 0.015 | 10% | 100% | 0.005 | 900,000 | -0.034 | 0% |
| nhl | 0-15 min | 23 | -0.008 | 0.027 | 48% | 70% | 0.010 | 76,000 | -0.013 | 13% |
| nhl | 15-60 min | 17 | 0.002 | 0.004 | 100% | 100% | 0.010 | 590,000 | -0.024 | 0% |
| nhl | 1-3 h | 24 | 0.001 | 0.010 | 88% | 88% | 0.010 | 670,000 | -0.023 | 12% |
| nhl | 3-12 h | 1 | -0.007 | 0.007 | 100% | 100% | 0.010 | 540,000 | -0.016 | 0% |
| nhl | 12 h+ | 473 | 0.003 | 0.006 | 77% | 100% | 0.010 | 140,000 | -0.025 | 0% |

Largest gaps seen:

| sport | team | pin_ts | minutes_to_start | fair | pm_mid | pm_spread | mid_minus_fair | taker_edge_at_ask |
|---|---|---|---|---|---|---|---|---|
| nhl | Canadiens | 10-14 23:56 | -32 | 0.640 | 0.495 | 0.010 | -0.145 | 0.122 |
| nhl | Canadiens | 10-15 00:01 | -32 | 0.640 | 0.495 | 0.010 | -0.145 | 0.122 |
| mlb | Milwaukee Brewers | 10-15 01:57 | -118 | 0.135 | 0.247 | 0.005 | 0.113 | -0.128 |
| nhl | Canadiens | 10-15 02:26 | -170 | 0.105 | 0.020 | 0.020 | -0.085 | 0.073 |
| nhl | Stars | 10-15 01:07 | -37 | 0.406 | 0.445 | 0.010 | 0.039 | -0.061 |
| nhl | Canadiens | 10-15 01:07 | -97 | 0.272 | 0.305 | 0.010 | 0.033 | -0.053 |
| mlb | Milwaukee Brewers | 10-15 02:26 | -147 | 0.842 | 0.873 | 0.005 | 0.031 | -0.041 |
| nhl | Stars | 10-15 03:29 | -171 | 0.465 | 0.495 | 0.010 | 0.030 | -0.052 |
| nhl | Stars | 10-14 22:04 | 141 | 0.444 | 0.415 | 0.010 | -0.029 | 0.007 |
| nhl | Stars | 10-14 22:09 | 141 | 0.444 | 0.415 | 0.010 | -0.029 | 0.007 |
| nhl | Stars | 10-14 22:14 | 130 | 0.444 | 0.415 | 0.010 | -0.029 | 0.007 |
| mlb | Milwaukee Brewers | 10-15 01:07 | -67 | 0.499 | 0.528 | 0.005 | 0.029 | -0.049 |

## Test (b): calibration of last pre-game mids (settled games)

| sport | n | mean_mid | win_rate |
|---|---|---|---|
| cs2 | 17 | 0.557 | 0.647 |
| mlb | 1 | 0.383 | 1.000 |
| nba | 7 | 0.442 | 0.429 |
| nhl | 2 | 0.445 | 0.500 |

27 settled main winner contracts so far; calibration is reported from 30 per sport.

## Test (a): news events and price reaction

6 news events recorded; 5 joined to a Polymarket contract with a price path.

| sport | kind | n |
|---|---|---|
| nhl | goalie_confirmed | 5 |
| nhl | goalie_likely | 1 |

Most recent joined events:

| sport | kind | team | detail | news_ts | minutes_to_start | contract_is_news_team | mid_before | move_plus5 | move_plus15 | move_plus30 | pin_fair_before | pin_fair_after | minutes_to_within_1c |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| nhl | goalie_confirmed | Colorado Avalanche | Scott Wedgewood | 10-15 00:07 | 23 | False | 0.405 | 0.000 | 0.000 | 0.000 | 0.406 | 0.406 | 0.624 |
| nhl | goalie_confirmed | Washington Capitals | Charlie Lindgren | 10-14 21:01 | 148 | False | 0.485 | 0.000 | 0.000 | 0.000 |  | 0.480 | 0.343 |
| nhl | goalie_confirmed | Dallas Stars | Casey DeSmith | 10-14 11:46 | 764 | True |  |  |  |  |  | 0.442 | 90.768 |
| nhl | goalie_likely | Colorado Avalanche | Scott Wedgewood | 10-14 11:43 | 767 | False |  |  |  |  |  | 0.442 | 93.552 |
| nhl | goalie_confirmed | Montreal Canadiens | Jakub Dobes | 10-13 14:08 | 2,001 | True |  |  |  |  |  | 0.480 | 1607.097 |

Generated by method/analysis/report.py from the data branch.
