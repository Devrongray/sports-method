# Daily analysis 2026-10-30

## Coverage

| source | sport | rows | events | passes | window_rows | first | last |
|---|---|---|---|---|---|---|---|
| polymarket_bbo | bundesliga | 44,298 | 25 | 1,272 | 8,724 | 10-15 06:34 | 10-30 10:06 |
| polymarket_bbo | cs2 | 258,623 | 753 | 7,348 | 66,970 | 10-14 19:27 | 10-30 10:06 |
| polymarket_bbo | epl | 51,599 | 28 | 1,344 | 8,844 | 10-15 23:32 | 10-30 10:06 |
| polymarket_bbo | laliga | 52,907 | 26 | 1,969 | 10,416 | 10-15 07:34 | 10-30 10:06 |
| polymarket_bbo | ligue1 | 50,352 | 22 | 1,431 | 9,384 | 10-15 06:55 | 10-30 10:06 |
| polymarket_bbo | lol | 5,810 | 39 | 2,368 | 1,316 | 10-14 19:27 | 10-30 10:06 |
| polymarket_bbo | mlb | 77,669 | 11 | 1,682 | 16,580 | 10-14 19:27 | 10-29 03:01 |
| polymarket_bbo | nba | 216,221 | 104 | 2,658 | 72,305 | 10-14 19:27 | 10-30 10:06 |
| polymarket_bbo | nfl | 48,825 | 29 | 1,615 | 9,114 | 10-14 19:27 | 10-30 03:01 |
| polymarket_bbo | nhl | 392,021 | 117 | 3,375 | 70,299 | 10-14 19:27 | 10-30 10:06 |
| polymarket_bbo | seriea | 68,457 | 33 | 2,141 | 13,428 | 10-15 06:55 | 10-30 10:06 |
| pinnacle | mlb | 2,522 | 12 | 564 |  | 10-14 21:29 | 10-29 02:39 |
| pinnacle | nba | 35,682 | 81 | 858 |  | 10-14 21:29 | 10-30 09:41 |
| pinnacle | nfl | 31,874 | 42 | 653 |  | 10-14 21:29 | 10-30 09:41 |
| pinnacle | nhl | 38,460 | 110 | 960 |  | 10-14 21:29 | 10-30 09:41 |
| polymarket_history | bundesliga | 337 | 337 | 364,297 |  | NaT | NaT |
| polymarket_history | cs2 | 2,385 | 2,326 | 2,021,339 |  | NaT | NaT |
| polymarket_history | epl | 360 | 360 | 389,160 |  | NaT | NaT |
| polymarket_history | laliga | 382 | 382 | 412,942 |  | NaT | NaT |
| polymarket_history | ligue1 | 343 | 331 | 370,783 |  | NaT | NaT |
| polymarket_history | lol | 37 | 37 | 39,997 |  | NaT | NaT |
| polymarket_history | mlb | 640 | 580 | 691,840 |  | NaT | NaT |
| polymarket_history | nba | 5,741 | 5,741 | 5,333,610 |  | NaT | NaT |
| polymarket_history | nfl | 1,158 | 1,158 | 1,251,798 |  | NaT | NaT |
| polymarket_history | nhl | 3,666 | 3,666 | 3,962,946 |  | NaT | NaT |
| polymarket_history | seriea | 544 | 544 | 588,064 |  | NaT | NaT |
| news_mlb | mlb | 618 |  |  |  | NaT | NaT |
| news_nhl | nhl | 728 |  |  |  | NaT | NaT |
| news_nhl_schedule | nhl | 804 |  |  |  | NaT | NaT |

Odds API quota at last pass: used 8643.0, remaining 11357.0 (1141 Pinnacle passes recorded).

## Event matching (Polymarket US vs Pinnacle)

1187 Polymarket events, 245 Pinnacle events, 231 matched (78 by full name, 153 by nickname).

Unmatched Polymarket events (956): bundesliga Eintracht Frankfurt vs. 1. FC Koln; bundesliga 1. FC Union Berlin vs. BV Borussia 09 Dortmund; bundesliga Hamburger SV vs. VfB Stuttgart; bundesliga SV Werder Bremen vs. SC Paderborn 07; bundesliga FC Schalke 04 vs. 1. FSV Mainz 05; bundesliga SV 07 Elversberg vs. FC Augsburg; bundesliga FC Bayern Munchen vs. RB Leipzig; bundesliga Bayer 04 Leverkusen vs. SC Freiburg; bundesliga Borussia Monchengladbach vs. TSG 1899 Hoffenheim; bundesliga VfB Stuttgart vs. Borussia Monchengladbach; bundesliga RB Leipzig vs. SV 07 Elversberg; bundesliga FC Augsburg vs. 1. FC Union Berlin; bundesliga 1. FSV Mainz 05 vs. SV Werder Bremen; bundesliga 1. FC Koln vs. FC Schalke 04; bundesliga SC Paderborn 07 vs. Hamburger SV

## Polymarket mid vs Pinnacle fair, main winner contracts

mid_minus_fair > 0 means Polymarket prices the team higher than Pinnacle's de-vigged price. taker_edge_at_ask = fair − ask − fee: what a taker would expect if Pinnacle were exactly right.

| sport | bucket | n | mean_diff | mean_abs_diff | within_1c | within_2c | mean_spread | median_bid_shares | taker_edge_mean | taker_edge_pos_share |
|---|---|---|---|---|---|---|---|---|---|---|
| mlb | 0-15 min | 762 | -0.254 | 0.271 | 6% | 7% | 0.021 | 6,000 | 0.233 | 85% |
| mlb | 15-60 min | 1,115 | -0.270 | 0.270 | 7% | 7% | 0.010 | 48,000 | 0.253 | 93% |
| mlb | 1-3 h | 1,091 | -0.272 | 0.272 | 6% | 7% | 0.010 | 29,000 | 0.255 | 93% |
| mlb | 3-12 h | 1,852 | -0.274 | 0.274 | 6% | 6% | 0.047 | 26,000 | 0.238 | 92% |
| mlb | 12 h+ | 2,150 | -0.255 | 0.257 | 4% | 6% | 0.140 | 20,000 | 0.172 | 83% |
| nba | 0-15 min | 9,105 | -0.025 | 0.163 | 6% | 11% | 0.284 | 26,000 | -0.129 | 30% |
| nba | 15-60 min | 4,673 | -0.035 | 0.102 | 14% | 20% | 0.297 | 26,000 | -0.127 | 25% |
| nba | 1-3 h | 8,774 | -0.051 | 0.125 | 14% | 22% | 0.403 | 25,000 | -0.162 | 19% |
| nba | 3-12 h | 11,545 | -0.047 | 0.120 | 16% | 23% | 0.425 | 25,000 | -0.178 | 15% |
| nba | 12 h+ | 2,193 | -0.004 | 0.017 | 74% | 92% | 0.053 | 340,000 | -0.038 | 1% |
| nhl | 0-15 min | 9,923 | -0.109 | 0.148 | 9% | 13% | 0.087 | 28,000 | 0.052 | 62% |
| nhl | 15-60 min | 5,048 | -0.118 | 0.118 | 12% | 14% | 0.012 | 32,000 | 0.096 | 86% |
| nhl | 1-3 h | 9,485 | -0.118 | 0.118 | 12% | 14% | 0.012 | 32,000 | 0.096 | 86% |
| nhl | 3-12 h | 17,398 | -0.116 | 0.117 | 10% | 13% | 0.050 | 31,000 | 0.075 | 83% |
| nhl | 12 h+ | 31,360 | -0.131 | 0.132 | 12% | 13% | 0.144 | 29,000 | 0.043 | 71% |

Largest gaps seen:

| sport | team | pin_ts | minutes_to_start | fair | pm_mid | pm_spread | mid_minus_fair | taker_edge_at_ask |
|---|---|---|---|---|---|---|---|---|
| nhl | Panthers | 10-28 01:46 | -106 | 0.959 | 0.025 | 0.030 | -0.934 | 0.916 |
| mlb | Milwaukee Brewers | 10-24 02:58 | -179 | 0.938 | 0.025 | 0.010 | -0.913 | 0.906 |
| nhl | Kings | 10-30 04:37 | -157 | 0.920 | 0.015 | 0.010 | -0.905 | 0.898 |
| mlb | Tampa Bay Rays | 10-18 23:46 | -159 | 0.941 | 0.040 | 0.020 | -0.901 | 0.888 |
| nhl | Senators | 10-30 04:37 | -157 | 0.080 | 0.960 | 0.060 | 0.880 | -0.910 |
| nba | Mavericks | 10-24 01:18 | -139 | 0.899 | 0.020 | 0.020 | -0.879 | 0.867 |
| nba | Pacers | 10-24 01:18 | -139 | 0.101 | 0.965 | 0.050 | 0.864 | -0.890 |
| nba | Mavericks | 10-24 01:25 | -151 | 0.899 | 0.045 | 0.050 | -0.854 | 0.825 |
| nba | Pacers | 10-24 01:25 | -151 | 0.101 | 0.950 | 0.080 | 0.849 | -0.890 |
| nhl | Blue Jackets | 10-28 00:42 | -94 | 0.902 | 0.065 | 0.010 | -0.837 | 0.827 |
| nba | Pistons | 10-26 02:07 | -157 | 0.950 | 0.115 | 0.210 | -0.835 | 0.718 |
| nba | Denver Nuggets | 10-29 00:57 | -62 | 0.939 | 0.110 | 0.180 | -0.829 | 0.728 |

## Test (b): calibration of last pre-game mids (settled games)

| sport | n | mean_mid | win_rate | brier_pm | log_loss_pm | slope | slope_se | intercept | n_with_pinnacle | brier_pm_matched | brier_pinnacle |
|---|---|---|---|---|---|---|---|---|---|---|---|
| bundesliga | 162 | 0.335 | 0.333 | 0.214 | 0.615 | 0.708 | 0.254 | -0.198 |  |  |  |
| cs2 | 1,676 | 0.530 | 0.545 | 0.224 | 0.636 | 0.902 | 0.081 | 0.078 |  |  |  |
| epl | 180 | 0.337 | 0.333 | 0.204 | 0.594 | 1.006 | 0.274 | -0.014 |  |  |  |
| laliga | 189 | 0.341 | 0.333 | 0.201 | 0.585 | 1.023 | 0.249 | -0.025 |  |  |  |
| ligue1 | 162 | 0.344 | 0.333 | 0.207 | 0.601 | 1.001 | 0.307 | -0.051 |  |  |  |
| lol | 37 | 0.594 | 0.405 | 0.237 | 0.666 | 1.001 | 0.434 | -0.953 |  |  |  |
| mlb | 251 | 0.346 | 0.343 | 0.197 | 0.583 | 0.812 | 0.150 | -0.122 | 171 | 0.174 | 0.245 |
| nba | 1,218 | 0.339 | 0.331 | 0.186 | 0.540 | 0.869 | 0.070 | -0.095 | 789 | 0.244 | 0.247 |
| nhl | 1,248 | 0.348 | 0.338 | 0.217 | 0.625 | 0.916 | 0.150 | -0.098 | 868 | 0.226 | 0.242 |
| seriea | 270 | 0.352 | 0.333 | 0.205 | 0.597 | 0.969 | 0.218 | -0.105 |  |  |  |

5393 settled main winner contracts so far; calibration is reported from 30 per sport.

## Test (a): news events and price reaction

356 news events recorded; 5049 joined to a Polymarket contract with a price path.

| sport | kind | n |
|---|---|---|
| mlb | lineup_away | 23 |
| mlb | lineup_home | 13 |
| mlb | probable_away | 8 |
| mlb | probable_home | 6 |
| nhl | goalie_confirmed | 215 |
| nhl | goalie_likely | 90 |
| nhl | goalie_unknown | 1 |

Most recent joined events:

| sport | kind | team | detail | news_ts | minutes_to_start | contract_is_news_team | mid_before | move_plus5 | move_plus15 | move_plus30 | pin_fair_before | pin_fair_after | minutes_to_within_1c |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| nhl | goalie_confirmed | Buffalo Sabres | Colten Ellis | 10-30 01:31 | 28 | False | 0.205 | 0.020 | 0.010 | 0.010 |  |  |  |
| nhl | goalie_confirmed | Buffalo Sabres | Colten Ellis | 10-30 01:31 | 28 | False | 0.315 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Buffalo Sabres | Colten Ellis | 10-30 01:31 | 28 | True | 0.575 | 0.000 | 0.010 | 0.020 | 0.578 | 0.583 | 0.192 |
| nhl | goalie_confirmed | Buffalo Sabres | Colten Ellis | 10-30 01:31 | 28 | False | 0.295 | 0.000 | 0.000 | 0.000 | 0.422 | 0.417 | 75.192 |
| nhl | goalie_confirmed | Buffalo Sabres | Colten Ellis | 10-30 01:31 | 28 | True | 0.375 | 0.000 | 0.000 | 0.000 | 0.578 | 0.583 |  |
| nhl | goalie_confirmed | Buffalo Sabres | Colten Ellis | 10-30 01:31 | 28 | False | 0.345 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Buffalo Sabres | Colten Ellis | 10-30 01:31 | 28 | True | 0.375 | 0.000 | 0.000 | 0.000 | 0.578 | 0.583 |  |
| nhl | goalie_confirmed | Buffalo Sabres | Colten Ellis | 10-30 01:31 | 28 | False | 0.345 | 0.000 | 0.000 | 0.000 | 0.422 | 0.417 |  |
| nhl | goalie_confirmed | Buffalo Sabres | Colten Ellis | 10-30 01:31 | 28 | False | 0.365 | 0.000 | 0.000 | 0.000 | 0.422 | 0.417 |  |
| nhl | goalie_confirmed | Buffalo Sabres | Colten Ellis | 10-30 01:31 | 28 | True | 0.455 | -0.045 | -0.045 | -0.060 | 0.578 | 0.583 |  |
| nhl | goalie_confirmed | Buffalo Sabres | Colten Ellis | 10-30 01:31 | 28 | False | 0.225 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Buffalo Sabres | Colten Ellis | 10-30 01:31 | 28 | False | 0.325 | 0.000 | 0.000 | 0.000 | 0.422 | 0.417 |  |
| nhl | goalie_confirmed | Buffalo Sabres | Colten Ellis | 10-30 01:31 | 28 | True | 0.425 | 0.035 | 0.020 | 0.020 | 0.578 | 0.583 |  |
| nhl | goalie_confirmed | Anaheim Ducks | Ville Husso | 10-30 01:31 | 29 | False | 0.315 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Anaheim Ducks | Ville Husso | 10-30 01:31 | 29 | False | 0.575 | 0.000 | 0.010 | 0.020 | 0.578 | 0.583 | 0.697 |
| nhl | goalie_confirmed | Anaheim Ducks | Ville Husso | 10-30 01:31 | 29 | True | 0.295 | 0.000 | 0.000 | 0.000 | 0.422 | 0.417 | 75.697 |
| nhl | goalie_confirmed | Anaheim Ducks | Ville Husso | 10-30 01:31 | 29 | False | 0.375 | 0.000 | 0.000 | 0.000 | 0.578 | 0.583 |  |
| nhl | goalie_confirmed | Anaheim Ducks | Ville Husso | 10-30 01:31 | 29 | True | 0.345 | 0.000 | 0.000 | 0.000 | 0.422 | 0.417 |  |
| nhl | goalie_confirmed | Anaheim Ducks | Ville Husso | 10-30 01:31 | 29 | False | 0.375 | 0.000 | 0.000 | 0.000 | 0.578 | 0.583 |  |
| nhl | goalie_confirmed | Anaheim Ducks | Ville Husso | 10-30 01:31 | 29 | False | 0.345 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Anaheim Ducks | Ville Husso | 10-30 01:31 | 29 | True | 0.365 | 0.000 | 0.000 | 0.000 | 0.422 | 0.417 |  |
| nhl | goalie_confirmed | Anaheim Ducks | Ville Husso | 10-30 01:31 | 29 | False | 0.455 | -0.045 | -0.045 | -0.060 | 0.578 | 0.583 |  |
| nhl | goalie_confirmed | Anaheim Ducks | Ville Husso | 10-30 01:31 | 29 | False | 0.225 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Anaheim Ducks | Ville Husso | 10-30 01:31 | 29 | True | 0.325 | 0.000 | 0.000 | 0.000 | 0.422 | 0.417 |  |
| nhl | goalie_confirmed | Anaheim Ducks | Ville Husso | 10-30 01:31 | 29 | False | 0.425 | 0.035 | 0.020 | 0.020 | 0.578 | 0.583 |  |
| nhl | goalie_confirmed | Anaheim Ducks | Ville Husso | 10-30 01:31 | 29 | False | 0.205 | 0.020 | 0.010 | 0.010 |  |  |  |
| nhl | goalie_confirmed | Chicago Blackhawks | Spencer Knight | 10-29 23:04 | 26 | True | 0.405 | 0.000 | 0.000 | 0.000 | 0.410 | 0.413 | 0.749 |
| nhl | goalie_confirmed | Chicago Blackhawks | Spencer Knight | 10-29 23:04 | 26 | True | 0.265 | 0.000 | 0.000 | 0.040 | 0.410 | 0.413 |  |
| nhl | goalie_confirmed | Chicago Blackhawks | Spencer Knight | 10-29 23:04 | 26 | False | 0.335 | 0.000 | 0.000 | 0.000 | 0.590 | 0.587 |  |
| nhl | goalie_confirmed | Chicago Blackhawks | Spencer Knight | 10-29 23:04 | 26 | False | 0.345 | 0.000 | -0.015 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Chicago Blackhawks | Spencer Knight | 10-29 23:04 | 26 | True | 0.295 | 0.000 | 0.000 | 0.000 | 0.410 | 0.413 |  |
| nhl | goalie_confirmed | Chicago Blackhawks | Spencer Knight | 10-29 23:04 | 26 | False | 0.415 | 0.000 | 0.000 | 0.000 | 0.590 | 0.587 |  |
| nhl | goalie_confirmed | Chicago Blackhawks | Spencer Knight | 10-29 23:04 | 26 | False | 0.275 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Chicago Blackhawks | Spencer Knight | 10-29 23:04 | 26 | True | 0.305 | 0.000 | 0.000 | 0.000 | 0.410 | 0.413 |  |
| nhl | goalie_confirmed | Chicago Blackhawks | Spencer Knight | 10-29 23:04 | 26 | False | 0.405 | 0.000 | 0.000 | 0.000 | 0.590 | 0.587 |  |
| nhl | goalie_confirmed | Chicago Blackhawks | Spencer Knight | 10-29 23:04 | 26 | False | 0.305 | 0.000 | -0.045 | -0.045 |  |  |  |
| nhl | goalie_confirmed | Chicago Blackhawks | Spencer Knight | 10-29 23:04 | 26 | True | 0.305 | 0.000 | 0.000 | 0.000 | 0.410 | 0.413 |  |
| nhl | goalie_confirmed | Chicago Blackhawks | Spencer Knight | 10-29 23:04 | 26 | False | 0.445 | 0.000 | 0.000 | 0.000 | 0.590 | 0.587 |  |
| nhl | goalie_confirmed | Chicago Blackhawks | Spencer Knight | 10-29 23:04 | 26 | False | 0.235 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Washington Capitals | Charlie Lindgren | 10-29 22:50 | 70 | True | 0.385 | 0.000 | 0.000 | 0.000 | 0.497 | 0.495 |  |

Generated by method/analysis/report.py from the data branch.
