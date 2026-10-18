# Daily analysis 2026-10-18

## Coverage

| source | sport | rows | events | passes | window_rows | first | last |
|---|---|---|---|---|---|---|---|
| polymarket_bbo | bundesliga | 18,594 | 9 | 503 | 3,492 | 10-15 06:34 | 10-18 10:17 |
| polymarket_bbo | cs2 | 50,500 | 254 | 2,146 | 11,729 | 10-14 19:27 | 10-18 10:20 |
| polymarket_bbo | epl | 19,319 | 10 | 426 | 2,004 | 10-15 23:32 | 10-18 10:17 |
| polymarket_bbo | laliga | 18,851 | 10 | 579 | 2,568 | 10-15 07:34 | 10-18 10:17 |
| polymarket_bbo | ligue1 | 18,984 | 9 | 510 | 2,316 | 10-15 06:55 | 10-18 10:17 |
| polymarket_bbo | lol | 1,178 | 8 | 720 | 303 | 10-14 19:27 | 10-18 10:17 |
| polymarket_bbo | mlb | 26,184 | 5 | 679 | 5,668 | 10-14 19:27 | 10-18 10:17 |
| polymarket_bbo | nba | 7,840 | 21 | 654 | 3,188 | 10-14 19:27 | 10-17 04:55 |
| polymarket_bbo | nfl | 13,713 | 13 | 277 | 0 | 10-14 19:27 | 10-18 10:17 |
| polymarket_bbo | nhl | 88,256 | 31 | 1,042 | 15,930 | 10-14 19:27 | 10-18 10:17 |
| polymarket_bbo | seriea | 18,009 | 10 | 603 | 2,844 | 10-15 06:55 | 10-18 10:20 |
| pinnacle | mlb | 984 | 5 | 178 |  | 10-14 21:29 | 10-18 03:24 |
| pinnacle | nba | 10,792 | 12 | 225 |  | 10-14 21:29 | 10-18 09:53 |
| pinnacle | nfl | 7,566 | 14 | 142 |  | 10-14 21:29 | 10-18 09:53 |
| pinnacle | nhl | 12,564 | 31 | 279 |  | 10-14 21:29 | 10-18 09:53 |
| polymarket_history | bundesliga | 128 | 128 | 138,368 |  | NaT | NaT |
| polymarket_history | cs2 | 346 | 327 | 309,378 |  | NaT | NaT |
| polymarket_history | epl | 89 | 89 | 96,209 |  | NaT | NaT |
| polymarket_history | laliga | 91 | 91 | 98,371 |  | NaT | NaT |
| polymarket_history | ligue1 | 71 | 71 | 76,751 |  | NaT | NaT |
| polymarket_history | lol | 7 | 7 | 7,567 |  | NaT | NaT |
| polymarket_history | mlb | 270 | 156 | 291,870 |  | NaT | NaT |
| polymarket_history | nba | 323 | 323 | 338,334 |  | NaT | NaT |
| polymarket_history | nfl | 23 | 23 | 24,863 |  | NaT | NaT |
| polymarket_history | nhl | 816 | 816 | 882,096 |  | NaT | NaT |
| polymarket_history | seriea | 68 | 68 | 73,508 |  | NaT | NaT |
| news_mlb | mlb | 177 |  |  |  | NaT | NaT |
| news_nhl | nhl | 195 |  |  |  | NaT | NaT |
| news_nhl_schedule | nhl | 224 |  |  |  | NaT | NaT |

Odds API quota at last pass: used 1837.0, remaining 18163.0 (319 Pinnacle passes recorded).

## Event matching (Polymarket US vs Pinnacle)

380 Polymarket events, 62 Pinnacle events, 48 matched (17 by full name, 31 by nickname).

Unmatched Polymarket events (332): bundesliga Eintracht Frankfurt vs. 1. FC Koln; bundesliga 1. FC Union Berlin vs. BV Borussia 09 Dortmund; bundesliga Hamburger SV vs. VfB Stuttgart; bundesliga SV Werder Bremen vs. SC Paderborn 07; bundesliga FC Schalke 04 vs. 1. FSV Mainz 05; bundesliga SV 07 Elversberg vs. FC Augsburg; bundesliga FC Bayern Munchen vs. RB Leipzig; bundesliga Bayer 04 Leverkusen vs. SC Freiburg; bundesliga Borussia Monchengladbach vs. TSG 1899 Hoffenheim; cs2  Phantom Academy vs. ZOTIX; cs2 FURIA vs. BetBoom Team; cs2 Pandaric eSports vs. BIG Academy; cs2 WBT vs. Esport Academy Copenhagen; cs2 ENCE vs. BOJONG; cs2 Heroic vs. Envy

## Polymarket mid vs Pinnacle fair, main winner contracts

mid_minus_fair > 0 means Polymarket prices the team higher than Pinnacle's de-vigged price. taker_edge_at_ask = fair − ask − fee: what a taker would expect if Pinnacle were exactly right.

| sport | bucket | n | mean_diff | mean_abs_diff | within_1c | within_2c | mean_spread | median_bid_shares | taker_edge_mean | taker_edge_pos_share |
|---|---|---|---|---|---|---|---|---|---|---|
| mlb | 0-15 min | 136 | -0.231 | 0.244 | 10% | 12% | 0.026 | 5,900 | 0.206 | 77% |
| mlb | 15-60 min | 170 | -0.247 | 0.247 | 18% | 18% | 0.009 | 28,000 | 0.230 | 82% |
| mlb | 1-3 h | 188 | -0.255 | 0.255 | 14% | 15% | 0.009 | 28,000 | 0.238 | 85% |
| mlb | 3-12 h | 382 | -0.261 | 0.262 | 11% | 11% | 0.028 | 540 | 0.235 | 88% |
| mlb | 12 h+ | 134 | -0.206 | 0.212 | 2% | 25% | 0.066 | 100 | 0.160 | 67% |
| nhl | 0-15 min | 2,288 | -0.102 | 0.131 | 13% | 18% | 0.090 | 28,000 | 0.043 | 58% |
| nhl | 15-60 min | 1,052 | -0.108 | 0.109 | 20% | 22% | 0.011 | 33,000 | 0.086 | 78% |
| nhl | 1-3 h | 2,339 | -0.112 | 0.113 | 17% | 19% | 0.011 | 33,000 | 0.091 | 81% |
| nhl | 3-12 h | 5,347 | -0.106 | 0.107 | 12% | 15% | 0.030 | 31,000 | 0.075 | 83% |
| nhl | 12 h+ | 6,079 | -0.119 | 0.120 | 18% | 21% | 0.102 | 29,000 | 0.051 | 69% |

Largest gaps seen:

| sport | team | pin_ts | minutes_to_start | fair | pm_mid | pm_spread | mid_minus_fair | taker_edge_at_ask |
|---|---|---|---|---|---|---|---|---|
| mlb | Tampa Bay Rays | 10-18 02:24 | -136 | 0.957 | 0.195 | 0.010 | -0.762 | 0.746 |
| mlb | Tampa Bay Rays | 10-18 02:24 | -136 | 0.957 | 0.215 | 0.050 | -0.742 | 0.705 |
| nhl | Islanders | 10-18 01:22 | -140 | 0.870 | 0.160 | 0.200 | -0.710 | 0.596 |
| nhl | Islanders | 10-18 01:15 | -140 | 0.870 | 0.160 | 0.200 | -0.710 | 0.596 |
| nhl | Golden Knights | 10-18 03:24 | -84 | 0.966 | 0.275 | 0.370 | -0.691 | 0.488 |
| mlb | Tampa Bay Rays | 10-18 02:56 | -169 | 0.915 | 0.235 | 0.010 | -0.680 | 0.662 |
| nhl | Canadiens | 10-18 01:27 | -152 | 0.818 | 0.165 | 0.230 | -0.653 | 0.524 |
| nhl | Canadiens | 10-18 01:34 | -152 | 0.818 | 0.165 | 0.230 | -0.653 | 0.524 |
| nhl | Ducks | 10-17 03:24 | -85 | 0.680 | 0.030 | 0.020 | -0.650 | 0.638 |
| nhl | Predators | 10-18 01:34 | -92 | 0.685 | 0.055 | 0.050 | -0.630 | 0.599 |
| nhl | Predators | 10-18 01:27 | -92 | 0.685 | 0.055 | 0.050 | -0.630 | 0.599 |
| nhl | Oilers | 10-18 03:24 | -84 | 0.906 | 0.295 | 0.010 | -0.611 | 0.591 |

## Test (b): calibration of last pre-game mids (settled games)

| sport | n | mean_mid | win_rate | brier_pm | log_loss_pm | slope | slope_se | intercept | n_with_pinnacle | brier_pm_matched | brier_pinnacle |
|---|---|---|---|---|---|---|---|---|---|---|---|
| bundesliga | 63 | 0.334 | 0.333 | 0.207 | 0.598 | 0.887 | 0.421 | -0.077 |  |  |  |
| cs2 | 284 | 0.537 | 0.553 | 0.219 | 0.626 | 0.962 | 0.191 | 0.077 |  |  |  |
| epl | 45 | 0.326 | 0.333 | 0.198 | 0.578 | 1.153 | 0.562 | 0.139 |  |  |  |
| laliga | 45 | 0.337 | 0.333 | 0.179 | 0.536 | 1.561 | 0.558 | 0.318 |  |  |  |
| ligue1 | 36 | 0.319 | 0.333 | 0.195 | 0.578 | 1.437 | 0.725 | 0.386 |  |  |  |
| lol | 7 | 0.704 | 0.571 |  |  |  |  |  |  |  |  |
| mlb | 34 | 0.353 | 0.382 | 0.255 | 0.715 | 0.270 | 0.365 | -0.293 |  |  |  |
| nba | 21 | 0.396 | 0.381 |  |  |  |  |  |  |  |  |
| nhl | 221 | 0.347 | 0.335 | 0.209 | 0.609 | 1.213 | 0.352 | 0.069 | 157 | 0.219 | 0.227 |
| seriea | 36 | 0.344 | 0.333 | 0.188 | 0.559 | 1.509 | 0.673 | 0.235 |  |  |  |

792 settled main winner contracts so far; calibration is reported from 30 per sport.

## Test (a): news events and price reaction

106 news events recorded; 1336 joined to a Polymarket contract with a price path.

| sport | kind | n |
|---|---|---|
| mlb | lineup_away | 12 |
| mlb | lineup_home | 6 |
| mlb | probable_away | 4 |
| mlb | probable_home | 3 |
| nhl | goalie_confirmed | 58 |
| nhl | goalie_likely | 23 |

Most recent joined events:

| sport | kind | team | detail | news_ts | minutes_to_start | contract_is_news_team | mid_before | move_plus5 | move_plus15 | move_plus30 | pin_fair_before | pin_fair_after | minutes_to_within_1c |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mlb | probable_away | Tampa Bay Rays | Drew Rasmussen | 10-18 03:40 | 1,048 | True | 0.310 | 0.000 | 0.010 | 0.010 |  |  |  |
| mlb | probable_away | Tampa Bay Rays | Drew Rasmussen | 10-18 03:40 | 1,048 | True | 0.215 | -0.010 | 0.000 | 0.000 |  |  |  |
| mlb | probable_away | Tampa Bay Rays | Drew Rasmussen | 10-18 03:40 | 1,048 | True | 0.547 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | probable_away | Tampa Bay Rays | Drew Rasmussen | 10-18 03:40 | 1,048 | False | 0.350 | 0.005 | 0.005 | 0.005 |  |  |  |
| mlb | probable_away | Tampa Bay Rays | Drew Rasmussen | 10-18 03:40 | 1,048 | False | 0.200 | -0.005 | 0.000 | 0.005 |  |  |  |
| mlb | probable_away | Tampa Bay Rays | Drew Rasmussen | 10-18 03:40 | 1,048 | True | 0.435 | 0.000 | 0.010 | 0.005 |  |  |  |
| mlb | probable_away | Tampa Bay Rays | Drew Rasmussen | 10-18 03:40 | 1,048 | False | 0.180 | 0.000 | 0.010 | 0.010 |  |  |  |
| mlb | probable_away | Tampa Bay Rays | Drew Rasmussen | 10-18 03:40 | 1,048 | False | 0.625 | 0.000 | -0.005 | 0.005 |  |  |  |
| mlb | probable_away | Tampa Bay Rays | Drew Rasmussen | 10-18 03:40 | 1,048 | True | 0.205 | 0.000 | 0.010 | 0.000 |  |  |  |
| mlb | probable_away | Tampa Bay Rays | Drew Rasmussen | 10-18 03:40 | 1,048 | False | 0.165 | 0.000 | -0.010 | 0.000 |  |  |  |
| mlb | probable_away | Tampa Bay Rays | Drew Rasmussen | 10-18 03:40 | 1,048 | True | 0.185 | 0.010 | 0.010 | 0.010 |  |  |  |
| mlb | probable_away | Tampa Bay Rays | Drew Rasmussen | 10-18 03:40 | 1,048 | False | 0.175 | -0.010 | 0.010 | 0.010 |  |  |  |
| mlb | probable_away | Tampa Bay Rays | Drew Rasmussen | 10-18 03:40 | 1,048 | False | 0.645 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | probable_away | Tampa Bay Rays | Drew Rasmussen | 10-18 03:40 | 1,048 | True | 0.205 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | probable_away | Tampa Bay Rays | Drew Rasmussen | 10-18 03:40 | 1,048 | False | 0.185 | 0.000 | -0.010 | -0.010 |  |  |  |
| mlb | probable_away | Tampa Bay Rays | Drew Rasmussen | 10-18 03:40 | 1,048 | False | 0.635 | 0.010 | -0.010 | 0.000 |  |  |  |
| mlb | probable_away | Tampa Bay Rays | Drew Rasmussen | 10-18 03:40 | 1,048 | False | 0.665 | 0.000 | -0.010 | -0.010 |  |  |  |
| mlb | probable_away | Tampa Bay Rays | Drew Rasmussen | 10-18 03:40 | 1,048 | False | 0.185 | 0.000 | -0.005 | 0.000 |  |  |  |
| mlb | probable_away | Tampa Bay Rays | Drew Rasmussen | 10-18 03:40 | 1,048 | False | 0.665 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | probable_away | Tampa Bay Rays | Drew Rasmussen | 10-18 03:40 | 1,048 | False | 0.645 | -0.005 | -0.005 | 0.000 |  |  |  |
| mlb | probable_away | Tampa Bay Rays | Drew Rasmussen | 10-18 03:40 | 1,048 | False | 0.115 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | probable_away | Tampa Bay Rays | Drew Rasmussen | 10-18 03:40 | 1,048 | False | 0.135 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | probable_away | Tampa Bay Rays | Drew Rasmussen | 10-18 03:40 | 1,048 | True | 0.175 | -0.010 | 0.000 | 0.010 |  |  |  |
| mlb | probable_away | Tampa Bay Rays | Drew Rasmussen | 10-18 03:40 | 1,048 | False | 0.655 | 0.000 | -0.005 | -0.005 |  |  |  |
| mlb | probable_away | Tampa Bay Rays | Drew Rasmussen | 10-18 03:40 | 1,048 | True | 0.185 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | probable_away | Tampa Bay Rays | Drew Rasmussen | 10-18 03:40 | 1,048 | False | 0.175 | 0.020 | 0.010 | 0.020 |  |  |  |
| mlb | probable_away | Tampa Bay Rays | Drew Rasmussen | 10-18 03:40 | 1,048 | False | 0.180 | -0.005 | -0.005 | -0.005 |  |  |  |
| mlb | probable_away | Tampa Bay Rays | Drew Rasmussen | 10-18 03:40 | 1,048 | True | 0.195 | 0.010 | 0.010 | 0.010 |  |  |  |
| mlb | probable_away | Tampa Bay Rays | Drew Rasmussen | 10-18 03:40 | 1,048 | False | 0.655 | -0.020 | -0.020 | -0.020 |  |  |  |
| mlb | probable_away | Tampa Bay Rays | Drew Rasmussen | 10-18 03:40 | 1,048 | False | 0.185 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | probable_away | Tampa Bay Rays | Drew Rasmussen | 10-18 03:40 | 1,048 | True | 0.205 | -0.010 | 0.000 | 0.000 |  |  |  |
| mlb | probable_home | Cleveland Guardians | Parker Messick | 10-18 03:30 | 1,058 | True | 0.165 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | probable_home | Cleveland Guardians | Parker Messick | 10-18 03:30 | 1,058 | True | 0.185 | 0.000 | 0.000 | -0.010 |  |  |  |
| mlb | probable_home | Cleveland Guardians | Parker Messick | 10-18 03:30 | 1,058 | False | 0.195 | 0.010 | 0.010 | 0.010 |  |  |  |
| mlb | probable_home | Cleveland Guardians | Parker Messick | 10-18 03:30 | 1,058 | False | 0.655 | -0.020 | -0.010 | -0.010 |  |  |  |
| mlb | probable_home | Cleveland Guardians | Parker Messick | 10-18 03:30 | 1,058 | True | 0.165 | 0.020 | 0.000 | 0.020 |  |  |  |
| mlb | probable_home | Cleveland Guardians | Parker Messick | 10-18 03:30 | 1,058 | False | 0.195 | -0.020 | 0.000 | 0.000 |  |  |  |
| mlb | probable_home | Cleveland Guardians | Parker Messick | 10-18 03:30 | 1,058 | False | 0.675 | 0.000 | -0.010 | -0.020 |  |  |  |
| mlb | probable_home | Cleveland Guardians | Parker Messick | 10-18 03:30 | 1,058 | False | 0.547 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | probable_home | Cleveland Guardians | Parker Messick | 10-18 03:30 | 1,058 | False | 0.205 | 0.000 | 0.000 | 0.010 |  |  |  |

Generated by method/analysis/report.py from the data branch.
