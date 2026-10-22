# Daily analysis 2026-10-22

## Coverage

| source | sport | rows | events | passes | window_rows | first | last |
|---|---|---|---|---|---|---|---|
| polymarket_bbo | bundesliga | 20,742 | 10 | 654 | 4,644 | 10-15 06:34 | 10-22 10:26 |
| polymarket_bbo | cs2 | 153,810 | 534 | 4,264 | 38,459 | 10-14 19:27 | 10-22 10:28 |
| polymarket_bbo | epl | 25,451 | 11 | 738 | 4,728 | 10-15 23:32 | 10-22 10:26 |
| polymarket_bbo | laliga | 26,447 | 12 | 1,053 | 5,616 | 10-15 07:34 | 10-22 10:26 |
| polymarket_bbo | ligue1 | 24,432 | 10 | 729 | 5,184 | 10-15 06:55 | 10-22 10:26 |
| polymarket_bbo | lol | 1,491 | 15 | 963 | 358 | 10-14 19:27 | 10-22 10:26 |
| polymarket_bbo | mlb | 41,954 | 6 | 970 | 10,244 | 10-14 19:27 | 10-20 02:59 |
| polymarket_bbo | nba | 41,688 | 38 | 1,157 | 13,790 | 10-14 19:27 | 10-22 10:26 |
| polymarket_bbo | nfl | 25,613 | 15 | 818 | 4,760 | 10-14 19:27 | 10-22 10:26 |
| polymarket_bbo | nhl | 188,972 | 60 | 1,848 | 32,247 | 10-14 19:27 | 10-22 10:26 |
| polymarket_bbo | seriea | 26,373 | 11 | 1,013 | 5,724 | 10-15 06:55 | 10-22 10:26 |
| pinnacle | mlb | 1,566 | 8 | 324 |  | 10-14 21:29 | 10-22 10:04 |
| pinnacle | nba | 20,366 | 28 | 410 |  | 10-14 21:29 | 10-22 10:04 |
| pinnacle | nfl | 16,596 | 28 | 336 |  | 10-14 21:29 | 10-22 10:04 |
| pinnacle | nhl | 20,202 | 60 | 508 |  | 10-14 21:29 | 10-22 10:04 |
| polymarket_history | bundesliga | 163 | 163 | 176,203 |  | NaT | NaT |
| polymarket_history | cs2 | 1,287 | 1,235 | 1,082,930 |  | NaT | NaT |
| polymarket_history | epl | 180 | 180 | 194,580 |  | NaT | NaT |
| polymarket_history | laliga | 197 | 197 | 212,957 |  | NaT | NaT |
| polymarket_history | ligue1 | 167 | 167 | 180,527 |  | NaT | NaT |
| polymarket_history | lol | 8 | 8 | 8,648 |  | NaT | NaT |
| polymarket_history | mlb | 339 | 279 | 366,459 |  | NaT | NaT |
| polymarket_history | nba | 1,225 | 1,225 | 1,098,840 |  | NaT | NaT |
| polymarket_history | nfl | 555 | 555 | 599,955 |  | NaT | NaT |
| polymarket_history | nhl | 1,521 | 1,521 | 1,644,201 |  | NaT | NaT |
| polymarket_history | seriea | 175 | 175 | 189,175 |  | NaT | NaT |
| news_mlb | mlb | 338 |  |  |  | NaT | NaT |
| news_nhl | nhl | 373 |  |  |  | NaT | NaT |
| news_nhl_schedule | nhl | 425 |  |  |  | NaT | NaT |

Odds API quota at last pass: used 3878.0, remaining 16122.0 (612 Pinnacle passes recorded).

## Event matching (Polymarket US vs Pinnacle)

722 Polymarket events, 124 Pinnacle events, 98 matched (21 by full name, 77 by nickname).

Unmatched Polymarket events (624): bundesliga Eintracht Frankfurt vs. 1. FC Koln; bundesliga 1. FC Union Berlin vs. BV Borussia 09 Dortmund; bundesliga Hamburger SV vs. VfB Stuttgart; bundesliga SV Werder Bremen vs. SC Paderborn 07; bundesliga FC Schalke 04 vs. 1. FSV Mainz 05; bundesliga SV 07 Elversberg vs. FC Augsburg; bundesliga FC Bayern Munchen vs. RB Leipzig; bundesliga Bayer 04 Leverkusen vs. SC Freiburg; bundesliga Borussia Monchengladbach vs. TSG 1899 Hoffenheim; bundesliga VfB Stuttgart vs. Borussia Monchengladbach; cs2  Phantom Academy vs. ZOTIX; cs2 FURIA vs. BetBoom Team; cs2 Pandaric eSports vs. BIG Academy; cs2 WBT vs. Esport Academy Copenhagen; cs2 ENCE vs. BOJONG

## Polymarket mid vs Pinnacle fair, main winner contracts

mid_minus_fair > 0 means Polymarket prices the team higher than Pinnacle's de-vigged price. taker_edge_at_ask = fair − ask − fee: what a taker would expect if Pinnacle were exactly right.

| sport | bucket | n | mean_diff | mean_abs_diff | within_1c | within_2c | mean_spread | median_bid_shares | taker_edge_mean | taker_edge_pos_share |
|---|---|---|---|---|---|---|---|---|---|---|
| mlb | 0-15 min | 340 | -0.247 | 0.267 | 9% | 10% | 0.023 | 5,800 | 0.225 | 79% |
| mlb | 15-60 min | 506 | -0.267 | 0.267 | 9% | 9% | 0.010 | 29,000 | 0.251 | 91% |
| mlb | 1-3 h | 524 | -0.270 | 0.270 | 8% | 8% | 0.010 | 25,000 | 0.253 | 92% |
| mlb | 3-12 h | 718 | -0.270 | 0.270 | 8% | 8% | 0.047 | 24,000 | 0.234 | 88% |
| mlb | 12 h+ | 407 | -0.214 | 0.217 | 3% | 12% | 0.245 | 29,000 | 0.076 | 66% |
| nba | 0-15 min | 1,644 | -0.016 | 0.132 | 5% | 10% | 0.604 | 1,000 | -0.294 | 13% |
| nba | 15-60 min | 591 | -0.031 | 0.103 | 13% | 16% | 0.608 | 420 | -0.282 | 7% |
| nba | 1-3 h | 818 | -0.043 | 0.123 | 13% | 16% | 0.687 | 380 | -0.308 | 2% |
| nba | 3-12 h | 350 | -0.024 | 0.062 | 47% | 62% | 0.322 | 720,000 | -0.149 | 0% |
| nba | 12 h+ | 835 | 0.002 | 0.006 | 85% | 99% | 0.010 | 260,000 | -0.024 | 0% |
| nhl | 0-15 min | 4,567 | -0.106 | 0.138 | 10% | 15% | 0.094 | 28,000 | 0.045 | 61% |
| nhl | 15-60 min | 2,123 | -0.112 | 0.113 | 14% | 17% | 0.011 | 33,000 | 0.090 | 83% |
| nhl | 1-3 h | 4,247 | -0.114 | 0.115 | 13% | 16% | 0.011 | 33,000 | 0.092 | 84% |
| nhl | 3-12 h | 7,768 | -0.108 | 0.109 | 12% | 15% | 0.032 | 31,000 | 0.076 | 82% |
| nhl | 12 h+ | 15,106 | -0.123 | 0.124 | 13% | 16% | 0.118 | 29,000 | 0.048 | 71% |

Largest gaps seen:

| sport | team | pin_ts | minutes_to_start | fair | pm_mid | pm_spread | mid_minus_fair | taker_edge_at_ask |
|---|---|---|---|---|---|---|---|---|
| mlb | Tampa Bay Rays | 10-18 23:46 | -159 | 0.941 | 0.040 | 0.020 | -0.901 | 0.888 |
| mlb | Tampa Bay Rays | 10-20 01:12 | -64 | 0.881 | 0.075 | 0.010 | -0.806 | 0.796 |
| nhl | Oilers | 10-21 03:31 | -151 | 0.924 | 0.125 | 0.190 | -0.799 | 0.692 |
| nhl | Canadiens | 10-21 01:30 | -156 | 0.832 | 0.045 | 0.070 | -0.787 | 0.747 |
| nhl | Devils | 10-21 01:30 | -156 | 0.944 | 0.165 | 0.270 | -0.779 | 0.629 |
| nhl | Devils | 10-21 01:35 | -156 | 0.944 | 0.165 | 0.270 | -0.779 | 0.629 |
| nhl | Sharks | 10-21 01:30 | -156 | 0.168 | 0.940 | 0.040 | 0.772 | -0.795 |
| mlb | Tampa Bay Rays | 10-18 22:49 | -102 | 0.872 | 0.105 | 0.130 | -0.767 | 0.692 |
| mlb | Tampa Bay Rays | 10-18 02:24 | -136 | 0.957 | 0.195 | 0.010 | -0.762 | 0.746 |
| mlb | Tampa Bay Rays | 10-20 02:00 | -113 | 0.820 | 0.075 | 0.010 | -0.745 | 0.735 |
| mlb | Tampa Bay Rays | 10-18 02:24 | -136 | 0.957 | 0.215 | 0.050 | -0.742 | 0.705 |
| nhl | Islanders | 10-21 00:37 | -95 | 0.904 | 0.165 | 0.010 | -0.739 | 0.725 |

## Test (b): calibration of last pre-game mids (settled games)

| sport | n | mean_mid | win_rate | brier_pm | log_loss_pm | slope | slope_se | intercept | n_with_pinnacle | brier_pm_matched | brier_pinnacle |
|---|---|---|---|---|---|---|---|---|---|---|---|
| bundesliga | 81 | 0.334 | 0.333 | 0.200 | 0.583 | 1.137 | 0.415 | 0.084 |  |  |  |
| cs2 | 962 | 0.532 | 0.570 | 0.220 | 0.629 | 0.951 | 0.108 | 0.174 |  |  |  |
| epl | 90 | 0.338 | 0.333 | 0.187 | 0.554 | 1.358 | 0.389 | 0.192 |  |  |  |
| laliga | 99 | 0.346 | 0.333 | 0.190 | 0.560 | 1.313 | 0.367 | 0.114 |  |  |  |
| ligue1 | 81 | 0.342 | 0.333 | 0.206 | 0.601 | 1.071 | 0.465 | 0.001 |  |  |  |
| lol | 8 | 0.725 | 0.625 |  |  |  |  |  |  |  |  |
| mlb | 96 | 0.348 | 0.354 | 0.214 | 0.617 | 0.660 | 0.233 | -0.163 | 66 | 0.191 | 0.242 |
| nba | 217 | 0.405 | 0.332 | 0.209 | 0.597 | 0.984 | 0.276 | -0.353 | 130 | 0.236 | 0.208 |
| nhl | 468 | 0.349 | 0.333 | 0.219 | 0.629 | 0.691 | 0.228 | -0.257 | 328 | 0.225 | 0.246 |
| seriea | 90 | 0.353 | 0.333 | 0.227 | 0.652 | 0.308 | 0.373 | -0.497 |  |  |  |

2192 settled main winner contracts so far; calibration is reported from 30 per sport.

## Test (a): news events and price reaction

167 news events recorded; 2250 joined to a Polymarket contract with a price path.

| sport | kind | n |
|---|---|---|
| mlb | lineup_away | 14 |
| mlb | lineup_home | 8 |
| mlb | probable_away | 5 |
| mlb | probable_home | 4 |
| nhl | goalie_confirmed | 95 |
| nhl | goalie_likely | 41 |

Most recent joined events:

| sport | kind | team | detail | news_ts | minutes_to_start | contract_is_news_team | mid_before | move_plus5 | move_plus15 | move_plus30 | pin_fair_before | pin_fair_after | minutes_to_within_1c |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| nhl | goalie_confirmed | Ottawa Senators | Linus Ullmark | 10-21 23:17 | 12 | True | 0.415 | 0.015 | 0.020 | 0.020 | 0.513 | 0.513 |  |
| nhl | goalie_confirmed | Ottawa Senators | Linus Ullmark | 10-21 23:17 | 12 | True | 0.385 | 0.000 | 0.000 | -0.080 | 0.513 | 0.513 |  |
| nhl | goalie_confirmed | Ottawa Senators | Linus Ullmark | 10-21 23:17 | 12 | False | 0.485 | 0.000 | 0.010 | 0.020 | 0.487 | 0.487 | 0.142 |
| nhl | goalie_confirmed | Ottawa Senators | Linus Ullmark | 10-21 23:17 | 12 | False | 0.365 | 0.000 | 0.000 | -0.130 |  |  |  |
| nhl | goalie_confirmed | Ottawa Senators | Linus Ullmark | 10-21 23:17 | 12 | False | 0.315 | 0.000 | 0.000 | 0.120 | 0.487 | 0.487 | 33.142 |
| nhl | goalie_confirmed | Ottawa Senators | Linus Ullmark | 10-21 23:17 | 12 | False | 0.325 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Ottawa Senators | Linus Ullmark | 10-21 23:17 | 12 | False | 0.345 | 0.000 | 0.000 | 0.000 | 0.487 | 0.487 |  |
| nhl | goalie_confirmed | Ottawa Senators | Linus Ullmark | 10-21 23:17 | 12 | True | 0.345 | 0.000 | 0.000 | 0.000 | 0.513 | 0.513 |  |
| nhl | goalie_confirmed | Ottawa Senators | Linus Ullmark | 10-21 23:17 | 12 | False | 0.285 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Ottawa Senators | Linus Ullmark | 10-21 23:17 | 12 | False | 0.375 | 0.000 | 0.010 | 0.010 | 0.487 | 0.487 |  |
| nhl | goalie_confirmed | Ottawa Senators | Linus Ullmark | 10-21 23:17 | 12 | True | 0.385 | 0.000 | 0.000 | 0.000 | 0.513 | 0.513 |  |
| nhl | goalie_confirmed | Ottawa Senators | Linus Ullmark | 10-21 23:17 | 12 | False | 0.235 | -0.010 | -0.020 | -0.020 |  |  |  |
| nhl | goalie_confirmed | Ottawa Senators | Linus Ullmark | 10-21 23:17 | 12 | False | 0.405 | 0.000 | 0.000 | 0.000 | 0.487 | 0.487 |  |
| nhl | goalie_confirmed | Florida Panthers | Akira Schmid | 10-21 16:23 | 426 | False | 0.360 | 0.000 | 0.000 | 0.000 | 0.495 | 0.505 |  |
| nhl | goalie_confirmed | Florida Panthers | Akira Schmid | 10-21 16:23 | 426 | True | 0.495 | 0.000 | 0.000 | 0.000 | 0.505 | 0.495 | 0.126 |
| nhl | goalie_confirmed | Florida Panthers | Akira Schmid | 10-21 16:23 | 426 | False | 0.365 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Florida Panthers | Akira Schmid | 10-21 16:23 | 426 | True | 0.345 | 0.000 | 0.000 | 0.000 | 0.505 | 0.495 | 447.126 |
| nhl | goalie_confirmed | Florida Panthers | Akira Schmid | 10-21 16:23 | 426 | False | 0.345 | -0.010 | -0.010 | -0.005 | 0.495 | 0.505 |  |
| nhl | goalie_confirmed | Florida Panthers | Akira Schmid | 10-21 16:23 | 426 | False | 0.330 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Florida Panthers | Akira Schmid | 10-21 16:23 | 426 | True | 0.355 | -0.010 | -0.010 | -0.010 | 0.505 | 0.495 |  |
| nhl | goalie_confirmed | Florida Panthers | Akira Schmid | 10-21 16:23 | 426 | False | 0.220 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Florida Panthers | Akira Schmid | 10-21 16:23 | 426 | False | 0.290 | -0.010 | -0.010 | -0.010 |  |  |  |
| nhl | goalie_confirmed | Florida Panthers | Akira Schmid | 10-21 16:23 | 426 | True | 0.380 | 0.000 | 0.000 | 0.005 | 0.505 | 0.495 |  |
| nhl | goalie_confirmed | Florida Panthers | Akira Schmid | 10-21 16:23 | 426 | False | 0.385 | -0.010 | -0.010 | -0.010 | 0.495 | 0.505 |  |
| nhl | goalie_confirmed | Florida Panthers | Akira Schmid | 10-21 16:23 | 426 | True | 0.355 | 0.000 | 0.000 | 0.000 | 0.505 | 0.495 |  |
| nhl | goalie_confirmed | Florida Panthers | Akira Schmid | 10-21 16:23 | 426 | False | 0.370 | 0.000 | 0.000 | 0.000 | 0.495 | 0.505 |  |
| nhl | goalie_confirmed | Philadelphia Flyers | Dan Vladar | 10-21 16:10 | 440 | True | 0.300 | 0.005 | -0.005 | -0.005 | 0.367 | 0.365 | 524.658 |
| nhl | goalie_confirmed | Philadelphia Flyers | Dan Vladar | 10-21 16:10 | 440 | True | 0.365 | 0.000 | 0.000 | 0.000 | 0.367 | 0.365 | 0.658 |
| nhl | goalie_confirmed | Philadelphia Flyers | Dan Vladar | 10-21 16:10 | 440 | False | 0.400 | -0.005 | -0.005 | -0.005 | 0.633 | 0.635 |  |
| nhl | goalie_confirmed | Philadelphia Flyers | Dan Vladar | 10-21 16:10 | 440 | False | 0.365 | 0.005 | 0.005 | 0.005 |  |  |  |
| nhl | goalie_confirmed | Philadelphia Flyers | Dan Vladar | 10-21 16:10 | 440 | False | 0.440 | -0.005 | -0.005 | -0.015 | 0.633 | 0.635 |  |
| nhl | goalie_confirmed | Philadelphia Flyers | Dan Vladar | 10-21 16:10 | 440 | False | 0.335 | -0.015 | -0.015 | -0.015 |  |  |  |
| nhl | goalie_confirmed | Philadelphia Flyers | Dan Vladar | 10-21 16:10 | 440 | True | 0.295 | 0.000 | -0.015 | -0.015 | 0.367 | 0.365 |  |
| nhl | goalie_confirmed | Philadelphia Flyers | Dan Vladar | 10-21 16:10 | 440 | False | 0.485 | -0.020 | -0.030 | -0.030 | 0.633 | 0.635 |  |
| nhl | goalie_confirmed | Philadelphia Flyers | Dan Vladar | 10-21 16:10 | 440 | True | 0.325 | -0.025 | -0.025 | -0.025 | 0.367 | 0.365 | 562.658 |
| nhl | goalie_confirmed | Philadelphia Flyers | Dan Vladar | 10-21 16:10 | 440 | False | 0.280 | -0.005 | -0.005 | -0.005 |  |  |  |
| nhl | goalie_confirmed | Philadelphia Flyers | Dan Vladar | 10-21 16:10 | 440 | False | 0.490 | -0.005 | 0.000 | 0.000 | 0.633 | 0.635 |  |
| nhl | goalie_confirmed | Philadelphia Flyers | Dan Vladar | 10-21 16:10 | 440 | False | 0.210 | 0.000 | -0.005 | -0.005 |  |  |  |
| nhl | goalie_confirmed | Philadelphia Flyers | Dan Vladar | 10-21 16:10 | 440 | True | 0.250 | 0.000 | 0.000 | 0.000 | 0.367 | 0.365 |  |
| nhl | goalie_likely | Ottawa Senators | Linus Ullmark | 10-21 15:53 | 456 | True | 0.360 | 0.000 | 0.000 | 0.000 | 0.493 | 0.495 | 553.071 |

Generated by method/analysis/report.py from the data branch.
