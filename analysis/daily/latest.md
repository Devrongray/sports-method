# Daily analysis 2026-11-01

## Coverage

| source | sport | rows | events | passes | window_rows | first | last |
|---|---|---|---|---|---|---|---|
| polymarket_bbo | bundesliga | 55,962 | 27 | 1,503 | 10,692 | 10-15 06:34 | 11-01 09:57 |
| polymarket_bbo | cs2 | 272,753 | 788 | 7,978 | 71,079 | 10-14 19:27 | 11-01 10:01 |
| polymarket_bbo | epl | 64,979 | 30 | 1,614 | 11,568 | 10-15 23:32 | 11-01 09:57 |
| polymarket_bbo | laliga | 64,571 | 31 | 2,253 | 11,964 | 10-15 07:34 | 11-01 09:57 |
| polymarket_bbo | ligue1 | 58,728 | 27 | 1,650 | 10,440 | 10-15 06:55 | 11-01 09:57 |
| polymarket_bbo | lol | 6,160 | 42 | 2,558 | 1,389 | 10-14 19:27 | 10-31 23:25 |
| polymarket_bbo | mlb | 77,669 | 11 | 1,682 | 16,580 | 10-14 19:27 | 10-29 03:01 |
| polymarket_bbo | nba | 255,222 | 113 | 2,978 | 84,845 | 10-14 19:27 | 11-01 09:57 |
| polymarket_bbo | ncaab | 902 | 9 | 106 | 0 | 10-31 02:38 | 11-01 09:57 |
| polymarket_bbo | nfl | 56,343 | 41 | 1,709 | 9,114 | 10-14 19:27 | 11-01 09:57 |
| polymarket_bbo | nhl | 434,756 | 126 | 3,703 | 76,851 | 10-14 19:27 | 11-01 09:57 |
| polymarket_bbo | seriea | 79,581 | 40 | 2,375 | 14,376 | 10-15 06:55 | 11-01 10:01 |
| pinnacle | mlb | 2,522 | 12 | 564 |  | 10-14 21:29 | 10-29 02:39 |
| pinnacle | nba | 38,348 | 92 | 950 |  | 10-14 21:29 | 11-01 08:38 |
| pinnacle | ncaab | 46 | 1 | 21 |  | 10-31 15:59 | 11-01 08:38 |
| pinnacle | nfl | 34,630 | 42 | 706 |  | 10-14 21:29 | 11-01 08:38 |
| pinnacle | nhl | 41,966 | 126 | 1,057 |  | 10-14 21:29 | 11-01 08:38 |
| polymarket_history | bundesliga | 467 | 467 | 504,827 |  | NaT | NaT |
| polymarket_history | cs2 | 2,563 | 2,503 | 2,156,096 |  | NaT | NaT |
| polymarket_history | epl | 504 | 504 | 544,824 |  | NaT | NaT |
| polymarket_history | laliga | 468 | 468 | 505,908 |  | NaT | NaT |
| polymarket_history | ligue1 | 444 | 420 | 479,964 |  | NaT | NaT |
| polymarket_history | lol | 42 | 42 | 45,402 |  | NaT | NaT |
| polymarket_history | mlb | 640 | 580 | 691,840 |  | NaT | NaT |
| polymarket_history | nba | 7,281 | 7,281 | 6,889,318 |  | NaT | NaT |
| polymarket_history | nfl | 1,158 | 1,158 | 1,251,798 |  | NaT | NaT |
| polymarket_history | nhl | 4,137 | 4,137 | 4,472,097 |  | NaT | NaT |
| polymarket_history | seriea | 603 | 603 | 651,473 |  | NaT | NaT |
| news_mlb | mlb | 674 |  |  |  | NaT | NaT |
| news_nhl | nhl | 803 |  |  |  | NaT | NaT |
| news_nhl_schedule | nhl | 891 |  |  |  | NaT | NaT |

Odds API quota at last pass: used 99.0, remaining 19901.0 (1253 Pinnacle passes recorded).

## Event matching (Polymarket US vs Pinnacle)

1285 Polymarket events, 273 Pinnacle events, 270 matched (101 by full name, 169 by nickname).

Unmatched Polymarket events (1015): bundesliga Eintracht Frankfurt vs. 1. FC Koln; bundesliga 1. FC Union Berlin vs. BV Borussia 09 Dortmund; bundesliga Hamburger SV vs. VfB Stuttgart; bundesliga SV Werder Bremen vs. SC Paderborn 07; bundesliga FC Schalke 04 vs. 1. FSV Mainz 05; bundesliga SV 07 Elversberg vs. FC Augsburg; bundesliga FC Bayern Munchen vs. RB Leipzig; bundesliga Bayer 04 Leverkusen vs. SC Freiburg; bundesliga Borussia Monchengladbach vs. TSG 1899 Hoffenheim; bundesliga VfB Stuttgart vs. Borussia Monchengladbach; bundesliga RB Leipzig vs. SV 07 Elversberg; bundesliga FC Augsburg vs. 1. FC Union Berlin; bundesliga 1. FSV Mainz 05 vs. SV Werder Bremen; bundesliga 1. FC Koln vs. FC Schalke 04; bundesliga SC Paderborn 07 vs. Hamburger SV

## Polymarket mid vs Pinnacle fair, main winner contracts

mid_minus_fair > 0 means Polymarket prices the team higher than Pinnacle's de-vigged price. taker_edge_at_ask = fair − ask − fee: what a taker would expect if Pinnacle were exactly right.

| sport | bucket | n | mean_diff | mean_abs_diff | within_1c | within_2c | mean_spread | median_bid_shares | taker_edge_mean | taker_edge_pos_share |
|---|---|---|---|---|---|---|---|---|---|---|
| mlb | 0-15 min | 762 | -0.254 | 0.271 | 6% | 7% | 0.021 | 6,000 | 0.233 | 85% |
| mlb | 15-60 min | 1,115 | -0.270 | 0.270 | 7% | 7% | 0.010 | 48,000 | 0.253 | 93% |
| mlb | 1-3 h | 1,091 | -0.272 | 0.272 | 6% | 7% | 0.010 | 29,000 | 0.255 | 93% |
| mlb | 3-12 h | 1,852 | -0.274 | 0.274 | 6% | 6% | 0.047 | 26,000 | 0.238 | 92% |
| mlb | 12 h+ | 2,150 | -0.255 | 0.257 | 4% | 6% | 0.140 | 20,000 | 0.172 | 83% |
| nba | 0-15 min | 10,333 | -0.025 | 0.162 | 7% | 11% | 0.271 | 26,000 | -0.123 | 31% |
| nba | 15-60 min | 5,479 | -0.036 | 0.099 | 14% | 20% | 0.273 | 26,000 | -0.114 | 26% |
| nba | 1-3 h | 10,542 | -0.055 | 0.123 | 13% | 21% | 0.370 | 26,000 | -0.143 | 22% |
| nba | 3-12 h | 14,377 | -0.056 | 0.121 | 15% | 22% | 0.404 | 25,000 | -0.159 | 17% |
| nba | 12 h+ | 2,314 | -0.005 | 0.018 | 73% | 91% | 0.057 | 360,000 | -0.039 | 1% |
| nhl | 0-15 min | 10,780 | -0.111 | 0.149 | 9% | 13% | 0.085 | 28,000 | 0.054 | 63% |
| nhl | 15-60 min | 5,552 | -0.119 | 0.120 | 11% | 14% | 0.016 | 32,000 | 0.095 | 86% |
| nhl | 1-3 h | 10,277 | -0.120 | 0.120 | 12% | 14% | 0.017 | 32,000 | 0.096 | 86% |
| nhl | 3-12 h | 19,414 | -0.121 | 0.122 | 10% | 13% | 0.062 | 30,000 | 0.073 | 81% |
| nhl | 12 h+ | 34,798 | -0.138 | 0.139 | 12% | 13% | 0.162 | 29,000 | 0.040 | 70% |

Largest gaps seen:

| sport | team | pin_ts | minutes_to_start | fair | pm_mid | pm_spread | mid_minus_fair | taker_edge_at_ask |
|---|---|---|---|---|---|---|---|---|
| nhl | Panthers | 10-28 01:46 | -106 | 0.959 | 0.025 | 0.030 | -0.934 | 0.916 |
| mlb | Milwaukee Brewers | 10-24 02:58 | -179 | 0.938 | 0.025 | 0.010 | -0.913 | 0.906 |
| nhl | Kings | 10-30 04:37 | -157 | 0.920 | 0.015 | 0.010 | -0.905 | 0.898 |
| mlb | Tampa Bay Rays | 10-18 23:46 | -159 | 0.941 | 0.040 | 0.020 | -0.901 | 0.888 |
| nhl | Senators | 10-30 04:37 | -157 | 0.080 | 0.960 | 0.060 | 0.880 | -0.910 |
| nba | Mavericks | 10-24 01:18 | -139 | 0.899 | 0.020 | 0.020 | -0.879 | 0.867 |
| nhl | Stars | 11-01 01:14 | -74 | 0.893 | 0.015 | 0.010 | -0.878 | 0.872 |
| nhl | Stars | 11-01 01:01 | -62 | 0.885 | 0.015 | 0.010 | -0.870 | 0.864 |
| nhl | Stars | 11-01 01:09 | -74 | 0.885 | 0.015 | 0.010 | -0.870 | 0.864 |
| nba | Pacers | 10-24 01:18 | -139 | 0.101 | 0.965 | 0.050 | 0.864 | -0.890 |
| nba | Mavericks | 10-24 01:25 | -151 | 0.899 | 0.045 | 0.050 | -0.854 | 0.825 |
| nba | Pacers | 10-24 01:25 | -151 | 0.101 | 0.950 | 0.080 | 0.849 | -0.890 |

## Test (b): calibration of last pre-game mids (settled games)

| sport | n | mean_mid | win_rate | brier_pm | log_loss_pm | slope | slope_se | intercept | n_with_pinnacle | brier_pm_matched | brier_pinnacle |
|---|---|---|---|---|---|---|---|---|---|---|---|
| bundesliga | 225 | 0.340 | 0.333 | 0.220 | 0.632 | 0.543 | 0.217 | -0.321 |  |  |  |
| cs2 | 1,791 | 0.530 | 0.544 | 0.224 | 0.635 | 0.908 | 0.079 | 0.072 |  |  |  |
| epl | 252 | 0.335 | 0.333 | 0.207 | 0.601 | 0.997 | 0.249 | -0.009 |  |  |  |
| laliga | 234 | 0.340 | 0.333 | 0.197 | 0.576 | 0.979 | 0.202 | -0.049 |  |  |  |
| ligue1 | 207 | 0.342 | 0.333 | 0.192 | 0.562 | 1.199 | 0.289 | 0.078 |  |  |  |
| lol | 42 | 0.577 | 0.452 | 0.238 | 0.669 | 0.729 | 0.338 | -0.494 |  |  |  |
| mlb | 251 | 0.346 | 0.343 | 0.197 | 0.583 | 0.812 | 0.150 | -0.122 | 171 | 0.174 | 0.245 |
| nba | 1,541 | 0.339 | 0.332 | 0.182 | 0.530 | 0.922 | 0.065 | -0.069 | 1,010 | 0.241 | 0.244 |
| nhl | 1,417 | 0.347 | 0.339 | 0.215 | 0.621 | 0.995 | 0.140 | -0.040 | 985 | 0.222 | 0.239 |
| seriea | 297 | 0.352 | 0.333 | 0.205 | 0.596 | 0.982 | 0.209 | -0.100 |  |  |  |

6257 settled main winner contracts so far; calibration is reported from 30 per sport.

## Test (a): news events and price reaction

387 news events recorded; 5426 joined to a Polymarket contract with a price path.

| sport | kind | n |
|---|---|---|
| mlb | lineup_away | 23 |
| mlb | lineup_home | 13 |
| mlb | probable_away | 8 |
| mlb | probable_home | 6 |
| nhl | goalie_confirmed | 244 |
| nhl | goalie_likely | 92 |
| nhl | goalie_unknown | 1 |

Most recent joined events:

| sport | kind | team | detail | news_ts | minutes_to_start | contract_is_news_team | mid_before | move_plus5 | move_plus15 | move_plus30 | pin_fair_before | pin_fair_after | minutes_to_within_1c |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-31 22:37 | 23 | True | 0.190 | 0.000 | 0.000 | 0.010 | 0.359 | 0.359 |  |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-31 22:37 | 23 | True | 0.285 | 0.005 | -0.010 | -0.010 | 0.359 | 0.359 |  |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-31 22:37 | 23 | False | 0.635 | 0.000 | 0.000 | 0.000 | 0.641 | 0.641 | 0.956 |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-31 22:37 | 23 | False | 0.345 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-31 22:37 | 23 | False | 0.395 | 0.005 | 0.010 | 0.010 | 0.641 | 0.641 |  |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-31 22:37 | 23 | True | 0.275 | 0.000 | 0.000 | 0.000 | 0.359 | 0.359 |  |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-31 22:37 | 23 | False | 0.420 | 0.000 | -0.010 | -0.010 | 0.641 | 0.641 | 107.956 |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-31 22:37 | 23 | False | 0.275 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-31 22:37 | 23 | False | 0.225 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-31 22:37 | 23 | False | 0.465 | 0.000 | 0.000 | -0.050 | 0.641 | 0.641 |  |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-31 22:37 | 23 | True | 0.345 | 0.000 | -0.050 | -0.050 | 0.359 | 0.359 |  |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-31 22:37 | 23 | False | 0.175 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-31 22:37 | 23 | False | 0.480 | 0.000 | 0.000 | -0.005 | 0.641 | 0.641 | 42.956 |
| nhl | goalie_confirmed | Edmonton Oilers | Matt Tomkins | 10-31 20:58 | -178 | False | 0.000 | 0.000 | 0.000 | 0.000 | 0.162 |  |  |
| nhl | goalie_confirmed | Edmonton Oilers | Matt Tomkins | 10-31 20:58 | -178 | True | 1.000 | 0.000 | 0.000 | 0.000 | 0.838 |  |  |
| nhl | goalie_confirmed | Edmonton Oilers | Matt Tomkins | 10-31 20:58 | -178 | False | 1.000 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Edmonton Oilers | Matt Tomkins | 10-31 20:58 | -178 | True | 0.000 | 0.000 | 0.000 | 0.000 | 0.838 |  |  |
| nhl | goalie_confirmed | Edmonton Oilers | Matt Tomkins | 10-31 20:58 | -178 | False | 0.000 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Edmonton Oilers | Matt Tomkins | 10-31 20:58 | -178 | True | 1.000 | 0.000 | 0.000 | 0.000 | 0.838 |  |  |
| nhl | goalie_confirmed | Edmonton Oilers | Matt Tomkins | 10-31 20:58 | -178 | False | 0.000 | 0.000 | 0.000 | 0.000 | 0.162 |  |  |
| nhl | goalie_confirmed | Edmonton Oilers | Matt Tomkins | 10-31 20:58 | -178 | False | 0.000 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Edmonton Oilers | Matt Tomkins | 10-31 20:58 | -178 | True | 1.000 | 0.000 | 0.000 | 0.000 | 0.838 |  |  |
| nhl | goalie_confirmed | Edmonton Oilers | Matt Tomkins | 10-31 20:58 | -178 | False | 0.000 | 0.000 | 0.000 | 0.000 | 0.162 |  |  |
| nhl | goalie_confirmed | Edmonton Oilers | Matt Tomkins | 10-31 20:58 | -178 | False | 0.000 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Edmonton Oilers | Matt Tomkins | 10-31 20:58 | -178 | True | 1.000 | 0.000 | 0.000 | 0.000 | 0.838 |  |  |
| nhl | goalie_confirmed | Edmonton Oilers | Matt Tomkins | 10-31 20:58 | -178 | False | 0.000 | 0.000 | 0.000 | 0.000 | 0.162 |  |  |
| nhl | goalie_confirmed | Los Angeles Kings | Anton Forsberg | 10-31 19:37 | 23 | False | 0.555 | 0.000 | 0.000 | 0.000 | 0.559 | 0.559 | 0.800 |
| nhl | goalie_confirmed | Los Angeles Kings | Anton Forsberg | 10-31 19:37 | 23 | False | 0.365 | 0.000 | 0.000 | 0.000 | 0.559 | 0.559 |  |
| nhl | goalie_confirmed | Los Angeles Kings | Anton Forsberg | 10-31 19:37 | 23 | False | 0.385 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Los Angeles Kings | Anton Forsberg | 10-31 19:37 | 23 | True | 0.305 | 0.000 | 0.005 | 0.005 | 0.441 | 0.441 |  |
| nhl | goalie_confirmed | Los Angeles Kings | Anton Forsberg | 10-31 19:37 | 23 | False | 0.375 | 0.000 | 0.000 | 0.000 | 0.559 | 0.559 |  |
| nhl | goalie_confirmed | Los Angeles Kings | Anton Forsberg | 10-31 19:37 | 23 | False | 0.345 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Los Angeles Kings | Anton Forsberg | 10-31 19:37 | 23 | True | 0.335 | 0.000 | 0.000 | 0.000 | 0.441 | 0.441 |  |
| nhl | goalie_confirmed | Los Angeles Kings | Anton Forsberg | 10-31 19:37 | 23 | False | 0.365 | 0.000 | 0.000 | 0.000 | 0.559 | 0.559 |  |
| nhl | goalie_confirmed | Los Angeles Kings | Anton Forsberg | 10-31 19:37 | 23 | False | 0.275 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Los Angeles Kings | Anton Forsberg | 10-31 19:37 | 23 | True | 0.335 | 0.000 | 0.000 | 0.000 | 0.441 | 0.441 |  |
| nhl | goalie_confirmed | Los Angeles Kings | Anton Forsberg | 10-31 19:37 | 23 | False | 0.310 | 0.000 | 0.000 | 0.130 | 0.559 | 0.559 |  |
| nhl | goalie_confirmed | Los Angeles Kings | Anton Forsberg | 10-31 19:37 | 23 | False | 0.175 | 0.000 | 0.000 | 0.015 |  |  |  |
| nhl | goalie_confirmed | Los Angeles Kings | Anton Forsberg | 10-31 19:37 | 23 | True | 0.245 | 0.000 | 0.000 | 0.015 | 0.441 | 0.441 |  |
| nhl | goalie_confirmed | Buffalo Sabres | Ukko-Pekka Luukkonen | 10-31 19:31 | 29 | False | 0.335 | 0.000 | 0.000 | 0.000 | 0.441 | 0.441 |  |

Generated by method/analysis/report.py from the data branch.
