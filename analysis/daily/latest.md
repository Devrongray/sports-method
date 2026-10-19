# Daily analysis 2026-10-19

## Coverage

| source | sport | rows | events | passes | window_rows | first | last |
|---|---|---|---|---|---|---|---|
| polymarket_bbo | bundesliga | 20,562 | 9 | 639 | 4,644 | 10-15 06:34 | 10-18 17:21 |
| polymarket_bbo | cs2 | 71,796 | 300 | 2,698 | 16,192 | 10-14 19:27 | 10-19 09:55 |
| polymarket_bbo | epl | 24,239 | 10 | 637 | 4,140 | 10-15 23:32 | 10-19 09:51 |
| polymarket_bbo | laliga | 24,419 | 10 | 884 | 4,824 | 10-15 07:34 | 10-19 09:51 |
| polymarket_bbo | ligue1 | 24,264 | 9 | 715 | 5,184 | 10-15 06:55 | 10-18 20:40 |
| polymarket_bbo | lol | 1,290 | 8 | 832 | 358 | 10-14 19:27 | 10-18 20:14 |
| polymarket_bbo | mlb | 36,542 | 6 | 847 | 7,912 | 10-14 19:27 | 10-19 09:51 |
| polymarket_bbo | nba | 7,990 | 22 | 664 | 3,188 | 10-14 19:27 | 10-19 09:51 |
| polymarket_bbo | nfl | 24,136 | 14 | 607 | 4,375 | 10-14 19:27 | 10-19 09:51 |
| polymarket_bbo | nhl | 103,376 | 35 | 1,268 | 18,219 | 10-14 19:27 | 10-19 09:51 |
| polymarket_bbo | seriea | 24,357 | 10 | 875 | 4,704 | 10-15 06:55 | 10-19 09:51 |
| pinnacle | mlb | 1,148 | 7 | 219 |  | 10-14 21:29 | 10-19 09:28 |
| pinnacle | nba | 12,868 | 14 | 264 |  | 10-14 21:29 | 10-19 09:28 |
| pinnacle | nfl | 11,086 | 24 | 229 |  | 10-14 21:29 | 10-19 09:28 |
| pinnacle | nhl | 13,764 | 35 | 342 |  | 10-14 21:29 | 10-19 09:28 |
| polymarket_history | bundesliga | 163 | 163 | 176,203 |  | NaT | NaT |
| polymarket_history | cs2 | 462 | 434 | 430,192 |  | NaT | NaT |
| polymarket_history | epl | 163 | 163 | 176,203 |  | NaT | NaT |
| polymarket_history | laliga | 162 | 162 | 175,122 |  | NaT | NaT |
| polymarket_history | ligue1 | 167 | 167 | 180,527 |  | NaT | NaT |
| polymarket_history | lol | 8 | 8 | 8,648 |  | NaT | NaT |
| polymarket_history | mlb | 278 | 218 | 300,518 |  | NaT | NaT |
| polymarket_history | nba | 323 | 323 | 338,334 |  | NaT | NaT |
| polymarket_history | nfl | 511 | 511 | 552,391 |  | NaT | NaT |
| polymarket_history | nhl | 897 | 897 | 969,657 |  | NaT | NaT |
| polymarket_history | seriea | 141 | 141 | 152,421 |  | NaT | NaT |
| news_mlb | mlb | 225 |  |  |  | NaT | NaT |
| news_nhl | nhl | 240 |  |  |  | NaT | NaT |
| news_nhl_schedule | nhl | 276 |  |  |  | NaT | NaT |

Odds API quota at last pass: used 2403.0, remaining 17597.0 (421 Pinnacle passes recorded).

## Event matching (Polymarket US vs Pinnacle)

433 Polymarket events, 80 Pinnacle events, 56 matched (20 by full name, 36 by nickname).

Unmatched Polymarket events (377): bundesliga Eintracht Frankfurt vs. 1. FC Koln; bundesliga 1. FC Union Berlin vs. BV Borussia 09 Dortmund; bundesliga Hamburger SV vs. VfB Stuttgart; bundesliga SV Werder Bremen vs. SC Paderborn 07; bundesliga FC Schalke 04 vs. 1. FSV Mainz 05; bundesliga SV 07 Elversberg vs. FC Augsburg; bundesliga FC Bayern Munchen vs. RB Leipzig; bundesliga Bayer 04 Leverkusen vs. SC Freiburg; bundesliga Borussia Monchengladbach vs. TSG 1899 Hoffenheim; cs2  Phantom Academy vs. ZOTIX; cs2 FURIA vs. BetBoom Team; cs2 Pandaric eSports vs. BIG Academy; cs2 WBT vs. Esport Academy Copenhagen; cs2 ENCE vs. BOJONG; cs2 Heroic vs. Envy

## Polymarket mid vs Pinnacle fair, main winner contracts

mid_minus_fair > 0 means Polymarket prices the team higher than Pinnacle's de-vigged price. taker_edge_at_ask = fair − ask − fee: what a taker would expect if Pinnacle were exactly right.

| sport | bucket | n | mean_diff | mean_abs_diff | within_1c | within_2c | mean_spread | median_bid_shares | taker_edge_mean | taker_edge_pos_share |
|---|---|---|---|---|---|---|---|---|---|---|
| mlb | 0-15 min | 252 | -0.242 | 0.261 | 8% | 10% | 0.025 | 5,600 | 0.218 | 78% |
| mlb | 15-60 min | 338 | -0.266 | 0.266 | 11% | 11% | 0.010 | 28,000 | 0.249 | 89% |
| mlb | 1-3 h | 356 | -0.269 | 0.269 | 10% | 10% | 0.009 | 28,000 | 0.253 | 90% |
| mlb | 3-12 h | 508 | -0.269 | 0.270 | 9% | 9% | 0.023 | 5,700 | 0.246 | 90% |
| mlb | 12 h+ | 365 | -0.215 | 0.217 | 3% | 12% | 0.234 | 29,000 | 0.083 | 68% |
| nba | 12 h+ | 3 | 0.012 | 0.012 | 0% | 100% | 0.010 | 450,000 | -0.035 | 0% |
| nhl | 0-15 min | 2,494 | -0.104 | 0.131 | 12% | 18% | 0.090 | 28,000 | 0.044 | 60% |
| nhl | 15-60 min | 1,187 | -0.108 | 0.109 | 18% | 21% | 0.011 | 33,000 | 0.087 | 79% |
| nhl | 1-3 h | 2,555 | -0.112 | 0.113 | 16% | 18% | 0.011 | 32,000 | 0.091 | 81% |
| nhl | 3-12 h | 5,671 | -0.107 | 0.108 | 12% | 15% | 0.030 | 31,000 | 0.076 | 83% |
| nhl | 12 h+ | 7,852 | -0.120 | 0.121 | 16% | 19% | 0.106 | 29,000 | 0.050 | 70% |

Largest gaps seen:

| sport | team | pin_ts | minutes_to_start | fair | pm_mid | pm_spread | mid_minus_fair | taker_edge_at_ask |
|---|---|---|---|---|---|---|---|---|
| mlb | Tampa Bay Rays | 10-18 23:46 | -159 | 0.941 | 0.040 | 0.020 | -0.901 | 0.888 |
| mlb | Tampa Bay Rays | 10-18 22:49 | -102 | 0.872 | 0.105 | 0.130 | -0.767 | 0.692 |
| mlb | Tampa Bay Rays | 10-18 02:24 | -136 | 0.957 | 0.195 | 0.010 | -0.762 | 0.746 |
| mlb | Tampa Bay Rays | 10-18 02:24 | -136 | 0.957 | 0.215 | 0.050 | -0.742 | 0.705 |
| nhl | Islanders | 10-18 01:22 | -140 | 0.870 | 0.160 | 0.200 | -0.710 | 0.596 |
| nhl | Islanders | 10-18 01:15 | -140 | 0.870 | 0.160 | 0.200 | -0.710 | 0.596 |
| mlb | Tampa Bay Rays | 10-18 22:19 | -71 | 0.888 | 0.185 | 0.010 | -0.703 | 0.687 |
| mlb | Tampa Bay Rays | 10-18 22:19 | -71 | 0.888 | 0.195 | 0.010 | -0.693 | 0.677 |
| nhl | Golden Knights | 10-18 03:24 | -84 | 0.966 | 0.275 | 0.370 | -0.691 | 0.488 |
| mlb | Tampa Bay Rays | 10-18 22:49 | -102 | 0.872 | 0.185 | 0.010 | -0.687 | 0.671 |
| mlb | Tampa Bay Rays | 10-18 22:19 | -71 | 0.888 | 0.205 | 0.010 | -0.683 | 0.667 |
| mlb | Tampa Bay Rays | 10-18 22:19 | -71 | 0.888 | 0.205 | 0.010 | -0.683 | 0.667 |

## Test (b): calibration of last pre-game mids (settled games)

| sport | n | mean_mid | win_rate | brier_pm | log_loss_pm | slope | slope_se | intercept | n_with_pinnacle | brier_pm_matched | brier_pinnacle |
|---|---|---|---|---|---|---|---|---|---|---|---|
| bundesliga | 81 | 0.334 | 0.333 | 0.200 | 0.583 | 1.137 | 0.415 | 0.084 |  |  |  |
| cs2 | 390 | 0.535 | 0.569 | 0.220 | 0.627 | 1.009 | 0.174 | 0.153 |  |  |  |
| epl | 81 | 0.338 | 0.333 | 0.196 | 0.573 | 1.128 | 0.387 | 0.053 |  |  |  |
| laliga | 81 | 0.342 | 0.333 | 0.174 | 0.523 | 1.670 | 0.431 | 0.330 |  |  |  |
| ligue1 | 81 | 0.342 | 0.333 | 0.206 | 0.601 | 1.071 | 0.465 | 0.001 |  |  |  |
| lol | 8 | 0.725 | 0.625 |  |  |  |  |  |  |  |  |
| mlb | 65 | 0.348 | 0.369 | 0.225 | 0.644 | 0.562 | 0.272 | -0.152 | 45 | 0.201 | 0.248 |
| nba | 21 | 0.396 | 0.381 |  |  |  |  |  |  |  |  |
| nhl | 247 | 0.348 | 0.332 | 0.212 | 0.615 | 0.987 | 0.313 | -0.082 | 175 | 0.219 | 0.233 |
| seriea | 72 | 0.349 | 0.333 | 0.225 | 0.649 | 0.356 | 0.394 | -0.459 |  |  |  |

1127 settled main winner contracts so far; calibration is reported from 30 per sport.

## Test (a): news events and price reaction

113 news events recorded; 1463 joined to a Polymarket contract with a price path.

| sport | kind | n |
|---|---|---|
| mlb | lineup_away | 13 |
| mlb | lineup_home | 7 |
| mlb | probable_away | 4 |
| mlb | probable_home | 4 |
| nhl | goalie_confirmed | 61 |
| nhl | goalie_likely | 24 |

Most recent joined events:

| sport | kind | team | detail | news_ts | minutes_to_start | contract_is_news_team | mid_before | move_plus5 | move_plus15 | move_plus30 | pin_fair_before | pin_fair_after | minutes_to_within_1c |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| nhl | goalie_likely | Columbus Blue Jackets | Cam Talbot | 10-18 21:16 | 43 | False | 0.595 | -0.050 | 0.000 | 0.000 | 0.637 | 0.637 | 150.359 |
| nhl | goalie_confirmed | Columbus Blue Jackets | Cam Talbot | 10-18 21:16 | 43 | False | 0.595 | -0.050 | 0.000 | 0.000 | 0.637 | 0.637 | 150.359 |
| nhl | goalie_confirmed | Columbus Blue Jackets | Cam Talbot | 10-18 21:16 | 43 | True | 0.365 | 0.000 | 0.000 | 0.000 | 0.363 | 0.363 | 0.359 |
| nhl | goalie_confirmed | Columbus Blue Jackets | Cam Talbot | 10-18 21:16 | 43 | True | 0.285 | 0.000 | 0.000 | 0.000 | 0.363 | 0.363 |  |
| nhl | goalie_confirmed | Columbus Blue Jackets | Cam Talbot | 10-18 21:16 | 43 | False | 0.305 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Columbus Blue Jackets | Cam Talbot | 10-18 21:16 | 43 | False | 0.405 | 0.000 | 0.000 | 0.000 | 0.637 | 0.637 |  |
| nhl | goalie_confirmed | Columbus Blue Jackets | Cam Talbot | 10-18 21:16 | 43 | True | 0.325 | 0.000 | 0.000 | 0.000 | 0.363 | 0.363 |  |
| nhl | goalie_confirmed | Columbus Blue Jackets | Cam Talbot | 10-18 21:16 | 43 | False | 0.275 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Columbus Blue Jackets | Cam Talbot | 10-18 21:16 | 43 | True | 0.255 | 0.000 | 0.000 | 0.000 | 0.363 | 0.363 |  |
| nhl | goalie_confirmed | Columbus Blue Jackets | Cam Talbot | 10-18 21:16 | 43 | False | 0.295 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Columbus Blue Jackets | Cam Talbot | 10-18 21:16 | 43 | False | 0.475 | 0.000 | 0.000 | 0.000 | 0.637 | 0.637 | 181.359 |
| nhl | goalie_confirmed | Columbus Blue Jackets | Cam Talbot | 10-18 21:16 | 43 | True | 0.265 | 0.000 | 0.000 | 0.000 | 0.363 | 0.363 |  |
| nhl | goalie_confirmed | Columbus Blue Jackets | Cam Talbot | 10-18 21:16 | 43 | False | 0.195 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Columbus Blue Jackets | Cam Talbot | 10-18 21:16 | 43 | False | 0.445 | 0.000 | 0.000 | 0.000 | 0.637 | 0.637 | 111.359 |
| nhl | goalie_likely | Columbus Blue Jackets | Cam Talbot | 10-18 21:16 | 43 | True | 0.365 | 0.000 | 0.000 | 0.000 | 0.363 | 0.363 | 0.359 |
| nhl | goalie_likely | Columbus Blue Jackets | Cam Talbot | 10-18 21:16 | 43 | False | 0.445 | 0.000 | 0.000 | 0.000 | 0.637 | 0.637 | 111.359 |
| nhl | goalie_likely | Columbus Blue Jackets | Cam Talbot | 10-18 21:16 | 43 | True | 0.285 | 0.000 | 0.000 | 0.000 | 0.363 | 0.363 |  |
| nhl | goalie_likely | Columbus Blue Jackets | Cam Talbot | 10-18 21:16 | 43 | False | 0.195 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_likely | Columbus Blue Jackets | Cam Talbot | 10-18 21:16 | 43 | True | 0.265 | 0.000 | 0.000 | 0.000 | 0.363 | 0.363 |  |
| nhl | goalie_likely | Columbus Blue Jackets | Cam Talbot | 10-18 21:16 | 43 | False | 0.475 | 0.000 | 0.000 | 0.000 | 0.637 | 0.637 | 181.359 |
| nhl | goalie_likely | Columbus Blue Jackets | Cam Talbot | 10-18 21:16 | 43 | True | 0.255 | 0.000 | 0.000 | 0.000 | 0.363 | 0.363 |  |
| nhl | goalie_likely | Columbus Blue Jackets | Cam Talbot | 10-18 21:16 | 43 | False | 0.295 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_likely | Columbus Blue Jackets | Cam Talbot | 10-18 21:16 | 43 | False | 0.275 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_likely | Columbus Blue Jackets | Cam Talbot | 10-18 21:16 | 43 | True | 0.325 | 0.000 | 0.000 | 0.000 | 0.363 | 0.363 |  |
| nhl | goalie_likely | Columbus Blue Jackets | Cam Talbot | 10-18 21:16 | 43 | False | 0.405 | 0.000 | 0.000 | 0.000 | 0.637 | 0.637 |  |
| nhl | goalie_likely | Columbus Blue Jackets | Cam Talbot | 10-18 21:16 | 43 | False | 0.305 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-18 17:46 | 202 | False | 0.155 | 0.000 | 0.000 | 0.000 | 0.463 | 0.463 |  |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-18 17:46 | 202 | True | 0.195 | 0.000 | 0.000 | 0.000 | 0.537 | 0.537 |  |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-18 17:46 | 202 | True | 0.195 | 0.000 | 0.000 | 0.000 | 0.537 | 0.537 |  |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-18 17:46 | 202 | False | 0.645 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-18 17:46 | 202 | True | 0.145 | 0.000 | 0.030 | 0.040 | 0.537 | 0.537 |  |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-18 17:46 | 202 | False | 0.655 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-18 17:46 | 202 | False | 0.145 | 0.000 | 0.000 | 0.000 | 0.463 | 0.463 |  |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-18 17:46 | 202 | True | 0.542 | 0.000 | 0.000 | 0.000 | 0.537 | 0.537 | 0.833 |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-18 17:46 | 202 | False | 0.625 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-18 17:46 | 202 | False | 0.165 | 0.000 | 0.000 | 0.000 | 0.463 | 0.463 |  |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-18 17:46 | 202 | True | 0.435 | 0.000 | 0.000 | 0.000 | 0.537 | 0.537 |  |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-18 17:46 | 202 | False | 0.205 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-18 17:46 | 202 | False | 0.365 | 0.000 | 0.000 | 0.000 | 0.463 | 0.463 |  |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-18 17:46 | 202 | True | 0.205 | 0.000 | 0.000 | 0.000 | 0.537 | 0.537 |  |

Generated by method/analysis/report.py from the data branch.
