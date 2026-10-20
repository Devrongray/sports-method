# Daily analysis 2026-10-20

## Coverage

| source | sport | rows | events | passes | window_rows | first | last |
|---|---|---|---|---|---|---|---|
| polymarket_bbo | bundesliga | 20,562 | 9 | 639 | 4,644 | 10-15 06:34 | 10-18 17:21 |
| polymarket_bbo | cs2 | 96,916 | 400 | 3,266 | 22,264 | 10-14 19:27 | 10-20 10:26 |
| polymarket_bbo | epl | 25,295 | 10 | 725 | 4,728 | 10-15 23:32 | 10-19 20:25 |
| polymarket_bbo | laliga | 25,475 | 10 | 972 | 5,412 | 10-15 07:34 | 10-19 20:25 |
| polymarket_bbo | ligue1 | 24,264 | 9 | 715 | 5,184 | 10-15 06:55 | 10-18 20:40 |
| polymarket_bbo | lol | 1,290 | 8 | 832 | 358 | 10-14 19:27 | 10-18 20:14 |
| polymarket_bbo | mlb | 41,954 | 6 | 970 | 10,244 | 10-14 19:27 | 10-20 02:59 |
| polymarket_bbo | nba | 12,235 | 24 | 763 | 3,188 | 10-14 19:27 | 10-20 10:22 |
| polymarket_bbo | nfl | 25,018 | 14 | 733 | 4,760 | 10-14 19:27 | 10-20 03:11 |
| polymarket_bbo | nhl | 134,960 | 46 | 1,491 | 22,713 | 10-14 19:27 | 10-20 10:22 |
| polymarket_bbo | seriea | 26,205 | 10 | 999 | 5,724 | 10-15 06:55 | 10-19 20:25 |
| pinnacle | mlb | 1,314 | 8 | 261 |  | 10-14 21:29 | 10-20 09:59 |
| pinnacle | nba | 14,604 | 14 | 295 |  | 10-14 21:29 | 10-20 09:59 |
| pinnacle | nfl | 13,120 | 27 | 273 |  | 10-14 21:29 | 10-20 09:59 |
| pinnacle | nhl | 15,846 | 42 | 401 |  | 10-14 21:29 | 10-20 09:59 |
| polymarket_history | bundesliga | 163 | 163 | 176,203 |  | NaT | NaT |
| polymarket_history | cs2 | 670 | 607 | 615,625 |  | NaT | NaT |
| polymarket_history | epl | 180 | 180 | 194,580 |  | NaT | NaT |
| polymarket_history | laliga | 180 | 180 | 194,580 |  | NaT | NaT |
| polymarket_history | ligue1 | 167 | 167 | 180,527 |  | NaT | NaT |
| polymarket_history | lol | 8 | 8 | 8,648 |  | NaT | NaT |
| polymarket_history | mlb | 339 | 279 | 366,459 |  | NaT | NaT |
| polymarket_history | nba | 323 | 323 | 338,334 |  | NaT | NaT |
| polymarket_history | nfl | 555 | 555 | 599,955 |  | NaT | NaT |
| polymarket_history | nhl | 1,040 | 1,040 | 1,124,240 |  | NaT | NaT |
| polymarket_history | seriea | 175 | 175 | 189,175 |  | NaT | NaT |
| news_mlb | mlb | 266 |  |  |  | NaT | NaT |
| news_nhl | nhl | 282 |  |  |  | NaT | NaT |
| news_nhl_schedule | nhl | 327 |  |  |  | NaT | NaT |

Odds API quota at last pass: used 2852.0, remaining 17148.0 (482 Pinnacle passes recorded).

## Event matching (Polymarket US vs Pinnacle)

546 Polymarket events, 91 Pinnacle events, 65 matched (20 by full name, 45 by nickname).

Unmatched Polymarket events (481): bundesliga Eintracht Frankfurt vs. 1. FC Koln; bundesliga 1. FC Union Berlin vs. BV Borussia 09 Dortmund; bundesliga Hamburger SV vs. VfB Stuttgart; bundesliga SV Werder Bremen vs. SC Paderborn 07; bundesliga FC Schalke 04 vs. 1. FSV Mainz 05; bundesliga SV 07 Elversberg vs. FC Augsburg; bundesliga FC Bayern Munchen vs. RB Leipzig; bundesliga Bayer 04 Leverkusen vs. SC Freiburg; bundesliga Borussia Monchengladbach vs. TSG 1899 Hoffenheim; cs2  Phantom Academy vs. ZOTIX; cs2 FURIA vs. BetBoom Team; cs2 Pandaric eSports vs. BIG Academy; cs2 WBT vs. Esport Academy Copenhagen; cs2 ENCE vs. BOJONG; cs2 Heroic vs. Envy

## Polymarket mid vs Pinnacle fair, main winner contracts

mid_minus_fair > 0 means Polymarket prices the team higher than Pinnacle's de-vigged price. taker_edge_at_ask = fair − ask − fee: what a taker would expect if Pinnacle were exactly right.

| sport | bucket | n | mean_diff | mean_abs_diff | within_1c | within_2c | mean_spread | median_bid_shares | taker_edge_mean | taker_edge_pos_share |
|---|---|---|---|---|---|---|---|---|---|---|
| mlb | 0-15 min | 340 | -0.247 | 0.267 | 9% | 10% | 0.023 | 5,800 | 0.225 | 79% |
| mlb | 15-60 min | 506 | -0.267 | 0.267 | 9% | 9% | 0.010 | 29,000 | 0.251 | 91% |
| mlb | 1-3 h | 524 | -0.270 | 0.270 | 8% | 8% | 0.010 | 25,000 | 0.253 | 92% |
| mlb | 3-12 h | 718 | -0.270 | 0.270 | 8% | 8% | 0.047 | 24,000 | 0.234 | 88% |
| mlb | 12 h+ | 407 | -0.214 | 0.217 | 3% | 12% | 0.245 | 29,000 | 0.076 | 66% |
| nba | 3-12 h | 4 | 0.010 | 0.010 | 25% | 100% | 0.010 | 775,000 | -0.032 | 0% |
| nba | 12 h+ | 89 | 0.006 | 0.007 | 65% | 96% | 0.010 | 680,000 | -0.028 | 0% |
| nhl | 0-15 min | 3,026 | -0.104 | 0.132 | 11% | 17% | 0.086 | 28,000 | 0.046 | 60% |
| nhl | 15-60 min | 1,439 | -0.109 | 0.110 | 17% | 20% | 0.011 | 33,000 | 0.088 | 80% |
| nhl | 1-3 h | 2,987 | -0.113 | 0.114 | 15% | 17% | 0.011 | 32,000 | 0.091 | 82% |
| nhl | 3-12 h | 6,058 | -0.107 | 0.108 | 12% | 15% | 0.031 | 31,000 | 0.075 | 82% |
| nhl | 12 h+ | 10,849 | -0.123 | 0.124 | 15% | 17% | 0.114 | 29,000 | 0.049 | 72% |

Largest gaps seen:

| sport | team | pin_ts | minutes_to_start | fair | pm_mid | pm_spread | mid_minus_fair | taker_edge_at_ask |
|---|---|---|---|---|---|---|---|---|
| mlb | Tampa Bay Rays | 10-18 23:46 | -159 | 0.941 | 0.040 | 0.020 | -0.901 | 0.888 |
| mlb | Tampa Bay Rays | 10-20 01:12 | -64 | 0.881 | 0.075 | 0.010 | -0.806 | 0.796 |
| mlb | Tampa Bay Rays | 10-18 22:49 | -102 | 0.872 | 0.105 | 0.130 | -0.767 | 0.692 |
| mlb | Tampa Bay Rays | 10-18 02:24 | -136 | 0.957 | 0.195 | 0.010 | -0.762 | 0.746 |
| mlb | Tampa Bay Rays | 10-20 02:00 | -113 | 0.820 | 0.075 | 0.010 | -0.745 | 0.735 |
| mlb | Tampa Bay Rays | 10-18 02:24 | -136 | 0.957 | 0.215 | 0.050 | -0.742 | 0.705 |
| mlb | Tampa Bay Rays | 10-20 02:00 | -113 | 0.820 | 0.100 | 0.060 | -0.720 | 0.682 |
| nhl | Islanders | 10-18 01:22 | -140 | 0.870 | 0.160 | 0.200 | -0.710 | 0.596 |
| nhl | Islanders | 10-18 01:15 | -140 | 0.870 | 0.160 | 0.200 | -0.710 | 0.596 |
| mlb | Tampa Bay Rays | 10-18 22:19 | -71 | 0.888 | 0.185 | 0.010 | -0.703 | 0.687 |
| mlb | Tampa Bay Rays | 10-18 22:19 | -71 | 0.888 | 0.195 | 0.010 | -0.693 | 0.677 |
| nhl | Golden Knights | 10-18 03:24 | -84 | 0.966 | 0.275 | 0.370 | -0.691 | 0.488 |

## Test (b): calibration of last pre-game mids (settled games)

| sport | n | mean_mid | win_rate | brier_pm | log_loss_pm | slope | slope_se | intercept | n_with_pinnacle | brier_pm_matched | brier_pinnacle |
|---|---|---|---|---|---|---|---|---|---|---|---|
| bundesliga | 81 | 0.334 | 0.333 | 0.200 | 0.583 | 1.137 | 0.415 | 0.084 |  |  |  |
| cs2 | 549 | 0.531 | 0.568 | 0.218 | 0.628 | 0.979 | 0.143 | 0.173 |  |  |  |
| epl | 90 | 0.338 | 0.333 | 0.187 | 0.554 | 1.358 | 0.389 | 0.192 |  |  |  |
| laliga | 90 | 0.341 | 0.333 | 0.183 | 0.542 | 1.494 | 0.398 | 0.246 |  |  |  |
| ligue1 | 81 | 0.342 | 0.333 | 0.206 | 0.601 | 1.071 | 0.465 | 0.001 |  |  |  |
| lol | 8 | 0.725 | 0.625 |  |  |  |  |  |  |  |  |
| mlb | 96 | 0.348 | 0.354 | 0.214 | 0.617 | 0.660 | 0.233 | -0.163 | 66 | 0.191 | 0.242 |
| nba | 21 | 0.396 | 0.381 |  |  |  |  |  |  |  |  |
| nhl | 299 | 0.348 | 0.328 | 0.212 | 0.615 | 0.920 | 0.280 | -0.143 | 211 | 0.224 | 0.237 |
| seriea | 90 | 0.353 | 0.333 | 0.227 | 0.652 | 0.308 | 0.373 | -0.497 |  |  |  |

1405 settled main winner contracts so far; calibration is reported from 30 per sport.

## Test (a): news events and price reaction

132 news events recorded; 1782 joined to a Polymarket contract with a price path.

| sport | kind | n |
|---|---|---|
| mlb | lineup_away | 14 |
| mlb | lineup_home | 8 |
| mlb | probable_away | 5 |
| mlb | probable_home | 4 |
| nhl | goalie_confirmed | 72 |
| nhl | goalie_likely | 29 |

Most recent joined events:

| sport | kind | team | detail | news_ts | minutes_to_start | contract_is_news_team | mid_before | move_plus5 | move_plus15 | move_plus30 | pin_fair_before | pin_fair_after | minutes_to_within_1c |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mlb | lineup_away | Cleveland Guardians | 9 players | 10-19 20:17 | 231 | False | 0.065 | 0.000 | 0.000 | 0.010 | 0.585 | 0.585 |  |
| mlb | lineup_away | Cleveland Guardians | 9 players | 10-19 20:17 | 231 | False | 0.235 | 0.000 | 0.000 | 0.000 | 0.585 | 0.585 |  |
| mlb | lineup_away | Cleveland Guardians | 9 players | 10-19 20:17 | 231 | True | 0.417 | 0.000 | 0.000 | 0.000 | 0.415 | 0.415 | 0.667 |
| mlb | lineup_away | Cleveland Guardians | 9 players | 10-19 20:17 | 231 | True | 0.345 | 0.000 | 0.000 | 0.000 | 0.415 | 0.415 |  |
| mlb | lineup_away | Cleveland Guardians | 9 players | 10-19 20:17 | 231 | False | 0.195 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | lineup_away | Cleveland Guardians | 9 players | 10-19 20:17 | 231 | False | 0.475 | 0.000 | 0.000 | 0.000 | 0.585 | 0.585 |  |
| mlb | lineup_away | Cleveland Guardians | 9 players | 10-19 20:17 | 231 | True | 0.205 | 0.000 | 0.000 | 0.000 | 0.415 | 0.415 |  |
| mlb | lineup_away | Cleveland Guardians | 9 players | 10-19 20:17 | 231 | False | 0.615 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | lineup_away | Cleveland Guardians | 9 players | 10-19 20:17 | 231 | False | 0.215 | 0.000 | 0.000 | 0.000 | 0.585 | 0.585 |  |
| mlb | lineup_away | Cleveland Guardians | 9 players | 10-19 20:17 | 231 | True | 0.175 | 0.000 | 0.000 | 0.000 | 0.415 | 0.415 |  |
| mlb | lineup_away | Cleveland Guardians | 9 players | 10-19 20:17 | 231 | False | 0.215 | 0.000 | 0.000 | 0.000 | 0.585 | 0.585 |  |
| mlb | lineup_away | Cleveland Guardians | 9 players | 10-19 20:17 | 231 | True | 0.135 | 0.000 | 0.020 | 0.040 | 0.415 | 0.415 |  |
| mlb | lineup_away | Cleveland Guardians | 9 players | 10-19 20:17 | 231 | False | 0.585 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | lineup_away | Cleveland Guardians | 9 players | 10-19 20:17 | 231 | False | 0.245 | 0.000 | 0.000 | 0.000 | 0.585 | 0.585 |  |
| mlb | lineup_away | Cleveland Guardians | 9 players | 10-19 20:17 | 231 | True | 0.145 | 0.000 | 0.000 | 0.000 | 0.415 | 0.415 | 302.667 |
| mlb | lineup_away | Cleveland Guardians | 9 players | 10-19 20:17 | 231 | False | 0.645 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | lineup_away | Cleveland Guardians | 9 players | 10-19 20:17 | 231 | False | 0.635 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | lineup_away | Cleveland Guardians | 9 players | 10-19 20:17 | 231 | True | 0.195 | 0.000 | 0.000 | 0.000 | 0.415 | 0.415 |  |
| mlb | lineup_away | Cleveland Guardians | 9 players | 10-19 20:17 | 231 | False | 0.625 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | lineup_away | Cleveland Guardians | 9 players | 10-19 20:17 | 231 | False | 0.605 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | lineup_away | Cleveland Guardians | 9 players | 10-19 20:17 | 231 | True | 0.195 | 0.000 | 0.000 | 0.000 | 0.415 | 0.415 |  |
| mlb | lineup_away | Cleveland Guardians | 9 players | 10-19 20:17 | 231 | False | 0.205 | 0.000 | 0.000 | 0.000 | 0.585 | 0.585 |  |
| mlb | lineup_away | Cleveland Guardians | 9 players | 10-19 20:17 | 231 | False | 0.625 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | lineup_away | Cleveland Guardians | 9 players | 10-19 20:17 | 231 | True | 0.185 | 0.000 | 0.000 | 0.000 | 0.415 | 0.415 |  |
| mlb | lineup_away | Cleveland Guardians | 9 players | 10-19 20:17 | 231 | False | 0.215 | 0.000 | 0.000 | 0.000 | 0.585 | 0.585 |  |
| mlb | lineup_away | Cleveland Guardians | 9 players | 10-19 20:17 | 231 | False | 0.755 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | lineup_away | Cleveland Guardians | 9 players | 10-19 20:17 | 231 | True | 0.185 | 0.000 | 0.000 | 0.000 | 0.415 | 0.415 |  |
| mlb | lineup_away | Cleveland Guardians | 9 players | 10-19 20:17 | 231 | False | 0.175 | 0.000 | 0.000 | 0.000 | 0.585 | 0.585 |  |
| mlb | lineup_away | Cleveland Guardians | 9 players | 10-19 20:17 | 231 | False | 0.645 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | lineup_away | Cleveland Guardians | 9 players | 10-19 20:17 | 231 | True | 0.145 | 0.000 | 0.050 | 0.050 | 0.415 | 0.415 |  |
| mlb | lineup_away | Cleveland Guardians | 9 players | 10-19 20:17 | 231 | False | 0.225 | 0.000 | 0.000 | 0.000 | 0.585 | 0.585 |  |
| mlb | lineup_home | Tampa Bay Rays | 9 players | 10-19 20:01 | 247 | False | 0.175 | 0.000 | 0.000 | 0.000 | 0.415 | 0.415 |  |
| mlb | lineup_home | Tampa Bay Rays | 9 players | 10-19 20:01 | 247 | False | 0.145 | 0.000 | 0.000 | 0.000 | 0.415 | 0.415 | 318.700 |
| mlb | lineup_home | Tampa Bay Rays | 9 players | 10-19 20:01 | 247 | True | 0.245 | 0.000 | 0.000 | 0.000 | 0.585 | 0.585 |  |
| mlb | lineup_home | Tampa Bay Rays | 9 players | 10-19 20:01 | 247 | False | 0.585 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | lineup_home | Tampa Bay Rays | 9 players | 10-19 20:01 | 247 | False | 0.135 | 0.000 | 0.000 | 0.020 | 0.415 | 0.415 |  |
| mlb | lineup_home | Tampa Bay Rays | 9 players | 10-19 20:01 | 247 | True | 0.215 | 0.000 | 0.000 | 0.000 | 0.585 | 0.585 |  |
| mlb | lineup_home | Tampa Bay Rays | 9 players | 10-19 20:01 | 247 | False | 0.635 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | lineup_home | Tampa Bay Rays | 9 players | 10-19 20:01 | 247 | False | 0.615 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | lineup_home | Tampa Bay Rays | 9 players | 10-19 20:01 | 247 | True | 0.185 | 0.000 | 0.030 | 0.030 | 0.585 | 0.585 |  |

Generated by method/analysis/report.py from the data branch.
