# Daily analysis 2026-10-31

## Coverage

| source | sport | rows | events | passes | window_rows | first | last |
|---|---|---|---|---|---|---|---|
| polymarket_bbo | bundesliga | 50,754 | 27 | 1,370 | 9,024 | 10-15 06:34 | 10-31 09:35 |
| polymarket_bbo | cs2 | 265,551 | 768 | 7,657 | 69,239 | 10-14 19:27 | 10-31 09:35 |
| polymarket_bbo | epl | 58,823 | 29 | 1,417 | 8,844 | 10-15 23:32 | 10-31 09:35 |
| polymarket_bbo | laliga | 57,875 | 30 | 2,059 | 10,620 | 10-15 07:34 | 10-31 09:35 |
| polymarket_bbo | ligue1 | 53,904 | 26 | 1,544 | 10,152 | 10-15 06:55 | 10-31 09:35 |
| polymarket_bbo | lol | 6,007 | 42 | 2,474 | 1,352 | 10-14 19:27 | 10-31 09:35 |
| polymarket_bbo | mlb | 77,669 | 11 | 1,682 | 16,580 | 10-14 19:27 | 10-29 03:01 |
| polymarket_bbo | nba | 237,303 | 110 | 2,780 | 78,542 | 10-14 19:27 | 10-31 09:35 |
| polymarket_bbo | ncaab | 72 | 1 | 24 | 0 | 10-31 02:38 | 10-31 09:35 |
| polymarket_bbo | nfl | 49,532 | 40 | 1,627 | 9,114 | 10-14 19:27 | 10-31 09:35 |
| polymarket_bbo | nhl | 411,152 | 124 | 3,489 | 71,244 | 10-14 19:27 | 10-31 09:35 |
| polymarket_bbo | seriea | 72,369 | 38 | 2,214 | 13,428 | 10-15 06:55 | 10-31 09:35 |
| pinnacle | mlb | 2,522 | 12 | 564 |  | 10-14 21:29 | 10-29 02:39 |
| pinnacle | nba | 36,998 | 88 | 895 |  | 10-14 21:29 | 10-31 09:08 |
| pinnacle | nfl | 33,174 | 42 | 678 |  | 10-14 21:29 | 10-31 09:08 |
| pinnacle | nhl | 39,846 | 120 | 997 |  | 10-14 21:29 | 10-31 09:08 |
| polymarket_history | bundesliga | 354 | 354 | 382,674 |  | NaT | NaT |
| polymarket_history | cs2 | 2,498 | 2,434 | 2,098,622 |  | NaT | NaT |
| polymarket_history | epl | 360 | 360 | 389,160 |  | NaT | NaT |
| polymarket_history | laliga | 401 | 401 | 433,481 |  | NaT | NaT |
| polymarket_history | ligue1 | 400 | 388 | 432,400 |  | NaT | NaT |
| polymarket_history | lol | 39 | 39 | 42,159 |  | NaT | NaT |
| polymarket_history | mlb | 640 | 580 | 691,840 |  | NaT | NaT |
| polymarket_history | nba | 6,637 | 6,637 | 6,257,822 |  | NaT | NaT |
| polymarket_history | nfl | 1,158 | 1,158 | 1,251,798 |  | NaT | NaT |
| polymarket_history | nhl | 3,773 | 3,773 | 4,078,613 |  | NaT | NaT |
| polymarket_history | seriea | 544 | 544 | 588,064 |  | NaT | NaT |
| news_mlb | mlb | 644 |  |  |  | NaT | NaT |
| news_nhl | nhl | 757 |  |  |  | NaT | NaT |
| news_nhl_schedule | nhl | 838 |  |  |  | NaT | NaT |

Odds API quota at last pass: used 9023.0, remaining 10977.0 (1182 Pinnacle passes recorded).

## Event matching (Polymarket US vs Pinnacle)

1246 Polymarket events, 262 Pinnacle events, 259 matched (96 by full name, 163 by nickname).

Unmatched Polymarket events (987): bundesliga Eintracht Frankfurt vs. 1. FC Koln; bundesliga 1. FC Union Berlin vs. BV Borussia 09 Dortmund; bundesliga Hamburger SV vs. VfB Stuttgart; bundesliga SV Werder Bremen vs. SC Paderborn 07; bundesliga FC Schalke 04 vs. 1. FSV Mainz 05; bundesliga SV 07 Elversberg vs. FC Augsburg; bundesliga FC Bayern Munchen vs. RB Leipzig; bundesliga Bayer 04 Leverkusen vs. SC Freiburg; bundesliga Borussia Monchengladbach vs. TSG 1899 Hoffenheim; bundesliga VfB Stuttgart vs. Borussia Monchengladbach; bundesliga RB Leipzig vs. SV 07 Elversberg; bundesliga FC Augsburg vs. 1. FC Union Berlin; bundesliga 1. FSV Mainz 05 vs. SV Werder Bremen; bundesliga 1. FC Koln vs. FC Schalke 04; bundesliga SC Paderborn 07 vs. Hamburger SV

## Polymarket mid vs Pinnacle fair, main winner contracts

mid_minus_fair > 0 means Polymarket prices the team higher than Pinnacle's de-vigged price. taker_edge_at_ask = fair − ask − fee: what a taker would expect if Pinnacle were exactly right.

| sport | bucket | n | mean_diff | mean_abs_diff | within_1c | within_2c | mean_spread | median_bid_shares | taker_edge_mean | taker_edge_pos_share |
|---|---|---|---|---|---|---|---|---|---|---|
| mlb | 0-15 min | 762 | -0.254 | 0.271 | 6% | 7% | 0.021 | 6,000 | 0.233 | 85% |
| mlb | 15-60 min | 1,115 | -0.270 | 0.270 | 7% | 7% | 0.010 | 48,000 | 0.253 | 93% |
| mlb | 1-3 h | 1,091 | -0.272 | 0.272 | 6% | 7% | 0.010 | 29,000 | 0.255 | 93% |
| mlb | 3-12 h | 1,852 | -0.274 | 0.274 | 6% | 6% | 0.047 | 26,000 | 0.238 | 92% |
| mlb | 12 h+ | 2,150 | -0.255 | 0.257 | 4% | 6% | 0.140 | 20,000 | 0.172 | 83% |
| nba | 0-15 min | 9,708 | -0.025 | 0.163 | 7% | 11% | 0.272 | 26,000 | -0.124 | 31% |
| nba | 15-60 min | 5,076 | -0.034 | 0.100 | 14% | 20% | 0.277 | 26,000 | -0.118 | 26% |
| nba | 1-3 h | 9,606 | -0.050 | 0.122 | 13% | 21% | 0.376 | 25,000 | -0.150 | 21% |
| nba | 3-12 h | 12,727 | -0.048 | 0.117 | 15% | 23% | 0.403 | 25,000 | -0.166 | 17% |
| nba | 12 h+ | 2,279 | -0.005 | 0.018 | 73% | 91% | 0.058 | 360,000 | -0.039 | 1% |
| nhl | 0-15 min | 10,065 | -0.109 | 0.148 | 9% | 13% | 0.086 | 28,000 | 0.052 | 62% |
| nhl | 15-60 min | 5,174 | -0.118 | 0.118 | 12% | 14% | 0.012 | 32,000 | 0.096 | 86% |
| nhl | 1-3 h | 9,665 | -0.118 | 0.118 | 12% | 14% | 0.012 | 32,000 | 0.096 | 86% |
| nhl | 3-12 h | 17,830 | -0.117 | 0.118 | 10% | 13% | 0.053 | 31,000 | 0.074 | 82% |
| nhl | 12 h+ | 33,574 | -0.136 | 0.137 | 12% | 13% | 0.157 | 29,000 | 0.041 | 70% |

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
| bundesliga | 171 | 0.335 | 0.333 | 0.217 | 0.622 | 0.637 | 0.249 | -0.245 |  |  |  |
| cs2 | 1,745 | 0.530 | 0.546 | 0.224 | 0.636 | 0.896 | 0.079 | 0.079 |  |  |  |
| epl | 180 | 0.337 | 0.333 | 0.204 | 0.594 | 1.006 | 0.274 | -0.014 |  |  |  |
| laliga | 198 | 0.341 | 0.333 | 0.208 | 0.603 | 0.811 | 0.226 | -0.152 |  |  |  |
| ligue1 | 189 | 0.343 | 0.333 | 0.201 | 0.587 | 1.174 | 0.290 | 0.060 |  |  |  |
| lol | 39 | 0.589 | 0.436 | 0.242 | 0.678 | 0.769 | 0.362 | -0.637 |  |  |  |
| mlb | 251 | 0.346 | 0.343 | 0.197 | 0.583 | 0.812 | 0.150 | -0.122 | 171 | 0.174 | 0.245 |
| nba | 1,408 | 0.339 | 0.331 | 0.184 | 0.537 | 0.880 | 0.066 | -0.090 | 919 | 0.243 | 0.247 |
| nhl | 1,287 | 0.348 | 0.338 | 0.216 | 0.623 | 0.969 | 0.149 | -0.066 | 895 | 0.226 | 0.241 |
| seriea | 270 | 0.352 | 0.333 | 0.205 | 0.597 | 0.969 | 0.218 | -0.105 |  |  |  |

5738 settled main winner contracts so far; calibration is reported from 30 per sport.

## Test (a): news events and price reaction

365 news events recorded; 5127 joined to a Polymarket contract with a price path.

| sport | kind | n |
|---|---|---|
| mlb | lineup_away | 23 |
| mlb | lineup_home | 13 |
| mlb | probable_away | 8 |
| mlb | probable_home | 6 |
| nhl | goalie_confirmed | 224 |
| nhl | goalie_likely | 90 |
| nhl | goalie_unknown | 1 |

Most recent joined events:

| sport | kind | team | detail | news_ts | minutes_to_start | contract_is_news_team | mid_before | move_plus5 | move_plus15 | move_plus30 | pin_fair_before | pin_fair_after | minutes_to_within_1c |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| nhl | goalie_confirmed | Seattle Kraken | Philipp Grubauer | 10-30 23:30 | 30 | True | 0.385 | 0.000 | 0.000 | 0.000 | 0.507 | 0.511 |  |
| nhl | goalie_confirmed | Seattle Kraken | Philipp Grubauer | 10-30 23:30 | 30 | True | 0.385 | 0.000 | 0.000 | 0.000 | 0.507 | 0.511 |  |
| nhl | goalie_confirmed | Seattle Kraken | Philipp Grubauer | 10-30 23:30 | 30 | True | 0.505 | 0.000 | 0.000 | 0.000 | 0.507 | 0.511 | 0.602 |
| nhl | goalie_confirmed | Seattle Kraken | Philipp Grubauer | 10-30 23:30 | 30 | False | 0.315 | 0.000 | 0.000 | 0.000 | 0.493 | 0.489 |  |
| nhl | goalie_confirmed | Seattle Kraken | Philipp Grubauer | 10-30 23:30 | 30 | False | 0.345 | 0.000 | 0.000 | -0.025 |  |  |  |
| nhl | goalie_confirmed | Seattle Kraken | Philipp Grubauer | 10-30 23:30 | 30 | True | 0.345 | 0.010 | 0.010 | 0.010 | 0.507 | 0.511 |  |
| nhl | goalie_confirmed | Seattle Kraken | Philipp Grubauer | 10-30 23:30 | 30 | False | 0.305 | 0.000 | 0.000 | -0.010 |  |  |  |
| nhl | goalie_confirmed | Seattle Kraken | Philipp Grubauer | 10-30 23:30 | 30 | False | 0.345 | 0.000 | 0.000 | -0.005 | 0.493 | 0.489 | 106.602 |
| nhl | goalie_confirmed | Seattle Kraken | Philipp Grubauer | 10-30 23:30 | 30 | False | 0.385 | 0.000 | 0.000 | 0.000 | 0.493 | 0.489 |  |
| nhl | goalie_confirmed | Seattle Kraken | Philipp Grubauer | 10-30 23:30 | 30 | False | 0.285 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Seattle Kraken | Philipp Grubauer | 10-30 23:30 | 30 | True | 0.365 | 0.000 | 0.000 | 0.000 | 0.507 | 0.511 |  |
| nhl | goalie_confirmed | Seattle Kraken | Philipp Grubauer | 10-30 23:30 | 30 | False | 0.365 | 0.000 | 0.000 | 0.000 | 0.493 | 0.489 | 60.602 |
| nhl | goalie_confirmed | Seattle Kraken | Philipp Grubauer | 10-30 23:30 | 30 | False | 0.235 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Winnipeg Jets | Nico Daws | 10-30 22:31 | 28 | True | 0.265 | 0.000 | 0.000 | 0.000 | 0.338 | 0.334 |  |
| nhl | goalie_confirmed | Winnipeg Jets | Nico Daws | 10-30 22:31 | 28 | True | 0.335 | 0.000 | 0.000 | 0.000 | 0.338 | 0.334 | 0.035 |
| nhl | goalie_confirmed | Winnipeg Jets | Nico Daws | 10-30 22:31 | 28 | False | 0.345 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Winnipeg Jets | Nico Daws | 10-30 22:31 | 28 | False | 0.425 | 0.000 | 0.000 | 0.000 | 0.662 | 0.666 |  |
| nhl | goalie_confirmed | Winnipeg Jets | Nico Daws | 10-30 22:31 | 28 | False | 0.335 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Winnipeg Jets | Nico Daws | 10-30 22:31 | 28 | False | 0.425 | 0.000 | 0.000 | 0.000 | 0.662 | 0.666 | 100.035 |
| nhl | goalie_confirmed | Winnipeg Jets | Nico Daws | 10-30 22:31 | 28 | True | 0.245 | 0.000 | 0.000 | 0.000 | 0.338 | 0.334 | 37.035 |
| nhl | goalie_confirmed | Winnipeg Jets | Nico Daws | 10-30 22:31 | 28 | False | 0.265 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Winnipeg Jets | Nico Daws | 10-30 22:31 | 28 | False | 0.465 | 0.000 | 0.000 | 0.000 | 0.662 | 0.666 |  |
| nhl | goalie_confirmed | Winnipeg Jets | Nico Daws | 10-30 22:31 | 28 | True | 0.265 | 0.000 | 0.000 | 0.000 | 0.338 | 0.334 |  |
| nhl | goalie_confirmed | Winnipeg Jets | Nico Daws | 10-30 22:31 | 28 | False | 0.185 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Winnipeg Jets | Nico Daws | 10-30 22:31 | 28 | False | 0.630 | -0.015 | -0.015 | -0.015 | 0.662 | 0.666 |  |
| nhl | goalie_confirmed | Winnipeg Jets | Nico Daws | 10-30 22:31 | 28 | True | 0.235 | 0.000 | 0.000 | 0.000 | 0.338 | 0.334 |  |
| nhl | goalie_confirmed | Vegas Golden Knights | Adin Hill | 10-30 21:30 | 29 | False | 0.495 | 0.000 | 0.000 | 0.000 | 0.488 | 0.488 | 0.312 |
| nhl | goalie_confirmed | Vegas Golden Knights | Adin Hill | 10-30 21:30 | 29 | False | 0.365 | 0.000 | 0.000 | -0.040 |  |  |  |
| nhl | goalie_confirmed | Vegas Golden Knights | Adin Hill | 10-30 21:30 | 29 | False | 0.335 | 0.000 | 0.000 | 0.010 | 0.488 | 0.488 |  |
| nhl | goalie_confirmed | Vegas Golden Knights | Adin Hill | 10-30 21:30 | 29 | True | 0.355 | 0.000 | 0.000 | 0.000 | 0.512 | 0.512 |  |
| nhl | goalie_confirmed | Vegas Golden Knights | Adin Hill | 10-30 21:30 | 29 | False | 0.335 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Vegas Golden Knights | Adin Hill | 10-30 21:30 | 29 | False | 0.355 | 0.000 | 0.000 | 0.000 | 0.488 | 0.488 |  |
| nhl | goalie_confirmed | Vegas Golden Knights | Adin Hill | 10-30 21:30 | 29 | True | 0.335 | 0.000 | 0.000 | 0.000 | 0.512 | 0.512 |  |
| nhl | goalie_confirmed | Vegas Golden Knights | Adin Hill | 10-30 21:30 | 29 | False | 0.255 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Vegas Golden Knights | Adin Hill | 10-30 21:30 | 29 | False | 0.385 | 0.000 | 0.000 | 0.000 | 0.488 | 0.488 | 160.312 |
| nhl | goalie_confirmed | Vegas Golden Knights | Adin Hill | 10-30 21:30 | 29 | True | 0.385 | 0.000 | 0.000 | -0.010 | 0.512 | 0.512 |  |
| nhl | goalie_confirmed | Vegas Golden Knights | Adin Hill | 10-30 21:30 | 29 | False | 0.225 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Vegas Golden Knights | Adin Hill | 10-30 21:30 | 29 | False | 0.395 | 0.000 | 0.000 | 0.000 | 0.488 | 0.488 |  |
| nhl | goalie_confirmed | Vegas Golden Knights | Adin Hill | 10-30 21:30 | 29 | True | 0.405 | 0.000 | 0.000 | 0.000 | 0.512 | 0.512 |  |
| nhl | goalie_confirmed | New Jersey Devils | Connor Hellebuyck | 10-30 20:01 | 118 | False | 0.335 | 0.000 | 0.000 | 0.000 | 0.512 | 0.512 |  |

Generated by method/analysis/report.py from the data branch.
