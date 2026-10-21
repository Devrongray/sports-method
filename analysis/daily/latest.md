# Daily analysis 2026-10-21

## Coverage

| source | sport | rows | events | passes | window_rows | first | last |
|---|---|---|---|---|---|---|---|
| polymarket_bbo | bundesliga | 20,562 | 9 | 639 | 4,644 | 10-15 06:34 | 10-18 17:21 |
| polymarket_bbo | cs2 | 129,389 | 443 | 3,800 | 30,606 | 10-14 19:27 | 10-21 10:27 |
| polymarket_bbo | epl | 25,295 | 10 | 725 | 4,728 | 10-15 23:32 | 10-19 20:25 |
| polymarket_bbo | laliga | 25,679 | 11 | 989 | 5,412 | 10-15 07:34 | 10-21 10:24 |
| polymarket_bbo | ligue1 | 24,264 | 9 | 715 | 5,184 | 10-15 06:55 | 10-18 20:40 |
| polymarket_bbo | lol | 1,331 | 9 | 873 | 358 | 10-14 19:27 | 10-21 10:24 |
| polymarket_bbo | mlb | 41,954 | 6 | 970 | 10,244 | 10-14 19:27 | 10-20 02:59 |
| polymarket_bbo | nba | 19,591 | 35 | 964 | 4,718 | 10-14 19:27 | 10-21 10:24 |
| polymarket_bbo | nfl | 25,018 | 14 | 733 | 4,760 | 10-14 19:27 | 10-20 03:11 |
| polymarket_bbo | nhl | 163,163 | 48 | 1,720 | 30,651 | 10-14 19:27 | 10-21 10:24 |
| polymarket_bbo | seriea | 26,205 | 10 | 999 | 5,724 | 10-15 06:55 | 10-19 20:25 |
| pinnacle | mlb | 1,446 | 8 | 294 |  | 10-14 21:29 | 10-21 10:01 |
| pinnacle | nba | 17,692 | 16 | 353 |  | 10-14 21:29 | 10-21 10:01 |
| pinnacle | nfl | 14,916 | 28 | 306 |  | 10-14 21:29 | 10-21 10:01 |
| pinnacle | nhl | 18,486 | 48 | 466 |  | 10-14 21:29 | 10-21 10:01 |
| polymarket_history | bundesliga | 163 | 163 | 176,203 |  | NaT | NaT |
| polymarket_history | cs2 | 967 | 893 | 837,724 |  | NaT | NaT |
| polymarket_history | epl | 180 | 180 | 194,580 |  | NaT | NaT |
| polymarket_history | laliga | 180 | 180 | 194,580 |  | NaT | NaT |
| polymarket_history | ligue1 | 167 | 167 | 180,527 |  | NaT | NaT |
| polymarket_history | lol | 8 | 8 | 8,648 |  | NaT | NaT |
| polymarket_history | mlb | 339 | 279 | 366,459 |  | NaT | NaT |
| polymarket_history | nba | 484 | 484 | 505,677 |  | NaT | NaT |
| polymarket_history | nfl | 555 | 555 | 599,955 |  | NaT | NaT |
| polymarket_history | nhl | 1,444 | 1,444 | 1,560,964 |  | NaT | NaT |
| polymarket_history | seriea | 175 | 175 | 189,175 |  | NaT | NaT |
| news_mlb | mlb | 303 |  |  |  | NaT | NaT |
| news_nhl | nhl | 333 |  |  |  | NaT | NaT |
| news_nhl_schedule | nhl | 384 |  |  |  | NaT | NaT |

Odds API quota at last pass: used 3407.0, remaining 16593.0 (555 Pinnacle passes recorded).

## Event matching (Polymarket US vs Pinnacle)

604 Polymarket events, 100 Pinnacle events, 82 matched (20 by full name, 62 by nickname).

Unmatched Polymarket events (522): bundesliga Eintracht Frankfurt vs. 1. FC Koln; bundesliga 1. FC Union Berlin vs. BV Borussia 09 Dortmund; bundesliga Hamburger SV vs. VfB Stuttgart; bundesliga SV Werder Bremen vs. SC Paderborn 07; bundesliga FC Schalke 04 vs. 1. FSV Mainz 05; bundesliga SV 07 Elversberg vs. FC Augsburg; bundesliga FC Bayern Munchen vs. RB Leipzig; bundesliga Bayer 04 Leverkusen vs. SC Freiburg; bundesliga Borussia Monchengladbach vs. TSG 1899 Hoffenheim; cs2  Phantom Academy vs. ZOTIX; cs2 FURIA vs. BetBoom Team; cs2 Pandaric eSports vs. BIG Academy; cs2 WBT vs. Esport Academy Copenhagen; cs2 ENCE vs. BOJONG; cs2 Heroic vs. Envy

## Polymarket mid vs Pinnacle fair, main winner contracts

mid_minus_fair > 0 means Polymarket prices the team higher than Pinnacle's de-vigged price. taker_edge_at_ask = fair − ask − fee: what a taker would expect if Pinnacle were exactly right.

| sport | bucket | n | mean_diff | mean_abs_diff | within_1c | within_2c | mean_spread | median_bid_shares | taker_edge_mean | taker_edge_pos_share |
|---|---|---|---|---|---|---|---|---|---|---|
| mlb | 0-15 min | 340 | -0.247 | 0.267 | 9% | 10% | 0.023 | 5,800 | 0.225 | 79% |
| mlb | 15-60 min | 506 | -0.267 | 0.267 | 9% | 9% | 0.010 | 29,000 | 0.251 | 91% |
| mlb | 1-3 h | 524 | -0.270 | 0.270 | 8% | 8% | 0.010 | 25,000 | 0.253 | 92% |
| mlb | 3-12 h | 718 | -0.270 | 0.270 | 8% | 8% | 0.047 | 24,000 | 0.234 | 88% |
| mlb | 12 h+ | 407 | -0.214 | 0.217 | 3% | 12% | 0.245 | 29,000 | 0.076 | 66% |
| nba | 0-15 min | 27 | 0.004 | 0.042 | 37% | 63% | 0.010 | 540,000 | -0.023 | 19% |
| nba | 15-60 min | 15 | -0.000 | 0.004 | 100% | 100% | 0.010 | 3,100,000 | -0.022 | 0% |
| nba | 1-3 h | 18 | 0.001 | 0.004 | 100% | 100% | 0.010 | 2,650,000 | -0.023 | 0% |
| nba | 3-12 h | 60 | 0.001 | 0.005 | 92% | 100% | 0.010 | 2,200,000 | -0.023 | 0% |
| nba | 12 h+ | 699 | 0.003 | 0.006 | 84% | 99% | 0.010 | 240,000 | -0.025 | 0% |
| nhl | 0-15 min | 4,465 | -0.106 | 0.138 | 10% | 15% | 0.095 | 28,000 | 0.044 | 60% |
| nhl | 15-60 min | 1,997 | -0.112 | 0.112 | 14% | 17% | 0.011 | 33,000 | 0.090 | 83% |
| nhl | 1-3 h | 4,139 | -0.114 | 0.115 | 14% | 16% | 0.011 | 33,000 | 0.092 | 84% |
| nhl | 3-12 h | 7,552 | -0.108 | 0.109 | 12% | 15% | 0.031 | 31,000 | 0.076 | 82% |
| nhl | 12 h+ | 11,812 | -0.123 | 0.124 | 14% | 17% | 0.115 | 29,000 | 0.049 | 72% |

Largest gaps seen:

| sport | team | pin_ts | minutes_to_start | fair | pm_mid | pm_spread | mid_minus_fair | taker_edge_at_ask |
|---|---|---|---|---|---|---|---|---|
| mlb | Tampa Bay Rays | 10-18 23:46 | -159 | 0.941 | 0.040 | 0.020 | -0.901 | 0.888 |
| mlb | Tampa Bay Rays | 10-20 01:12 | -64 | 0.881 | 0.075 | 0.010 | -0.806 | 0.796 |
| nhl | Oilers | 10-21 03:31 | -151 | 0.924 | 0.125 | 0.190 | -0.799 | 0.692 |
| nhl | Canadiens | 10-21 01:30 | -156 | 0.832 | 0.045 | 0.070 | -0.787 | 0.747 |
| nhl | Devils | 10-21 01:35 | -156 | 0.944 | 0.165 | 0.270 | -0.779 | 0.629 |
| nhl | Devils | 10-21 01:30 | -156 | 0.944 | 0.165 | 0.270 | -0.779 | 0.629 |
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
| cs2 | 734 | 0.539 | 0.587 | 0.218 | 0.624 | 0.942 | 0.122 | 0.229 |  |  |  |
| epl | 90 | 0.338 | 0.333 | 0.187 | 0.554 | 1.358 | 0.389 | 0.192 |  |  |  |
| laliga | 90 | 0.341 | 0.333 | 0.183 | 0.542 | 1.494 | 0.398 | 0.246 |  |  |  |
| ligue1 | 81 | 0.342 | 0.333 | 0.206 | 0.601 | 1.071 | 0.465 | 0.001 |  |  |  |
| lol | 8 | 0.725 | 0.625 |  |  |  |  |  |  |  |  |
| mlb | 96 | 0.348 | 0.354 | 0.214 | 0.617 | 0.660 | 0.233 | -0.163 | 66 | 0.191 | 0.242 |
| nba | 24 | 0.405 | 0.417 |  |  |  |  |  |  |  |  |
| nhl | 442 | 0.348 | 0.333 | 0.218 | 0.626 | 0.738 | 0.234 | -0.232 | 310 | 0.221 | 0.242 |
| seriea | 90 | 0.353 | 0.333 | 0.227 | 0.652 | 0.308 | 0.373 | -0.497 |  |  |  |

1736 settled main winner contracts so far; calibration is reported from 30 per sport.

## Test (a): news events and price reaction

160 news events recorded; 2159 joined to a Polymarket contract with a price path.

| sport | kind | n |
|---|---|---|
| mlb | lineup_away | 14 |
| mlb | lineup_home | 8 |
| mlb | probable_away | 5 |
| mlb | probable_home | 4 |
| nhl | goalie_confirmed | 91 |
| nhl | goalie_likely | 38 |

Most recent joined events:

| sport | kind | team | detail | news_ts | minutes_to_start | contract_is_news_team | mid_before | move_plus5 | move_plus15 | move_plus30 | pin_fair_before | pin_fair_after | minutes_to_within_1c |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| nhl | goalie_confirmed | Tampa Bay Lightning | Andrei Vasilevskiy | 10-21 02:07 | 23 | False | 0.425 | 0.000 | 0.000 | -0.020 | 0.503 | 0.503 |  |
| nhl | goalie_confirmed | Tampa Bay Lightning | Andrei Vasilevskiy | 10-21 02:07 | 23 | False | 0.335 | 0.000 | 0.000 | 0.000 | 0.503 | 0.503 |  |
| nhl | goalie_confirmed | Tampa Bay Lightning | Andrei Vasilevskiy | 10-21 02:07 | 23 | True | 0.505 | 0.000 | 0.000 | 0.000 | 0.497 | 0.497 | 0.573 |
| nhl | goalie_confirmed | Tampa Bay Lightning | Andrei Vasilevskiy | 10-21 02:07 | 23 | False | 0.365 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Tampa Bay Lightning | Andrei Vasilevskiy | 10-21 02:07 | 23 | True | 0.335 | 0.000 | 0.000 | 0.010 | 0.497 | 0.497 |  |
| nhl | goalie_confirmed | Tampa Bay Lightning | Andrei Vasilevskiy | 10-21 02:07 | 23 | False | 0.335 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Tampa Bay Lightning | Andrei Vasilevskiy | 10-21 02:07 | 23 | True | 0.335 | 0.000 | 0.000 | 0.000 | 0.497 | 0.497 |  |
| nhl | goalie_confirmed | Tampa Bay Lightning | Andrei Vasilevskiy | 10-21 02:07 | 23 | False | 0.345 | 0.000 | 0.000 | 0.000 | 0.503 | 0.503 |  |
| nhl | goalie_confirmed | Tampa Bay Lightning | Andrei Vasilevskiy | 10-21 02:07 | 23 | False | 0.245 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Tampa Bay Lightning | Andrei Vasilevskiy | 10-21 02:07 | 23 | True | 0.335 | 0.000 | 0.000 | 0.000 | 0.497 | 0.497 |  |
| nhl | goalie_confirmed | Tampa Bay Lightning | Andrei Vasilevskiy | 10-21 02:07 | 23 | False | 0.395 | 0.000 | 0.000 | 0.000 | 0.503 | 0.503 |  |
| nhl | goalie_confirmed | Tampa Bay Lightning | Andrei Vasilevskiy | 10-21 02:07 | 23 | False | 0.215 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Tampa Bay Lightning | Andrei Vasilevskiy | 10-21 02:07 | 23 | True | 0.405 | 0.000 | 0.000 | 0.000 | 0.497 | 0.497 |  |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-21 01:37 | 23 | True | 0.255 | 0.000 | 0.000 | 0.000 | 0.279 | 0.279 |  |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-21 01:37 | 23 | False | 0.725 | 0.000 | 0.000 | -0.010 | 0.721 | 0.721 | 0.999 |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-21 01:37 | 23 | False | 0.470 | 0.000 | 0.005 | -0.025 | 0.721 | 0.721 | 43.999 |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-21 01:37 | 23 | False | 0.335 | -0.030 | -0.030 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-21 01:37 | 23 | True | 0.255 | 0.000 | 0.000 | -0.020 | 0.279 | 0.279 |  |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-21 01:37 | 23 | False | 0.475 | 0.000 | 0.000 | 0.000 | 0.721 | 0.721 | 93.999 |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-21 01:37 | 23 | False | 0.295 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-21 01:37 | 23 | False | 0.610 | 0.000 | 0.000 | -0.025 | 0.721 | 0.721 | 39.999 |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-21 01:37 | 23 | False | 0.545 | 0.000 | 0.000 | 0.000 | 0.721 | 0.721 |  |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-21 01:37 | 23 | False | 0.245 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-21 01:37 | 23 | True | 0.205 | 0.000 | 0.000 | 0.000 | 0.279 | 0.279 |  |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-21 01:37 | 23 | False | 0.190 | 0.000 | 0.000 | -0.015 |  |  |  |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-21 01:37 | 23 | True | 0.220 | 0.000 | 0.000 | 0.000 | 0.279 | 0.279 |  |
| nhl | goalie_confirmed | Minnesota Wild | Jesper Wallstedt | 10-21 00:50 | 9 | True | 0.285 | 0.000 | 0.000 | 0.000 | 0.453 | 0.480 |  |
| nhl | goalie_confirmed | Minnesota Wild | Jesper Wallstedt | 10-21 00:50 | 9 | True | 0.465 | 0.000 | 0.000 | 0.175 | 0.453 | 0.480 | 17.162 |
| nhl | goalie_confirmed | Minnesota Wild | Jesper Wallstedt | 10-21 00:50 | 9 | False | 0.365 | 0.000 | 0.000 | -0.150 |  |  |  |
| nhl | goalie_confirmed | Minnesota Wild | Jesper Wallstedt | 10-21 00:50 | 9 | False | 0.355 | 0.000 | -0.005 | -0.235 | 0.547 | 0.520 |  |
| nhl | goalie_confirmed | Minnesota Wild | Jesper Wallstedt | 10-21 00:50 | 9 | False | 0.285 | 0.000 | 0.000 | 0.050 |  |  |  |
| nhl | goalie_confirmed | Minnesota Wild | Jesper Wallstedt | 10-21 00:50 | 9 | False | 0.395 | 0.000 | 0.000 | 0.000 | 0.547 | 0.520 |  |
| nhl | goalie_confirmed | Minnesota Wild | Jesper Wallstedt | 10-21 00:50 | 9 | True | 0.335 | 0.000 | 0.000 | 0.220 | 0.453 | 0.480 | 58.162 |
| nhl | goalie_confirmed | Minnesota Wild | Jesper Wallstedt | 10-21 00:50 | 9 | False | 0.245 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Minnesota Wild | Jesper Wallstedt | 10-21 00:50 | 9 | True | 0.315 | 0.000 | 0.000 | 0.030 | 0.453 | 0.480 |  |
| nhl | goalie_confirmed | Minnesota Wild | Jesper Wallstedt | 10-21 00:50 | 9 | False | 0.435 | 0.000 | 0.000 | -0.080 | 0.547 | 0.520 | 137.162 |
| nhl | goalie_confirmed | Minnesota Wild | Jesper Wallstedt | 10-21 00:50 | 9 | False | 0.245 | 0.000 | 0.005 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Minnesota Wild | Jesper Wallstedt | 10-21 00:50 | 9 | False | 0.455 | 0.000 | 0.120 | -0.170 | 0.547 | 0.520 | 82.162 |
| nhl | goalie_confirmed | Minnesota Wild | Jesper Wallstedt | 10-21 00:50 | 9 | True | 0.355 | 0.000 | -0.120 | 0.085 | 0.453 | 0.480 |  |
| nhl | goalie_confirmed | Edmonton Oilers | Devon Levi | 10-20 23:40 | 79 | False | 0.285 | 0.000 | 0.000 | 0.000 | 0.454 | 0.454 |  |

Generated by method/analysis/report.py from the data branch.
