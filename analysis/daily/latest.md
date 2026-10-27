# Daily analysis 2026-10-27

## Coverage

| source | sport | rows | events | passes | window_rows | first | last |
|---|---|---|---|---|---|---|---|
| polymarket_bbo | bundesliga | 41,742 | 18 | 1,194 | 8,724 | 10-15 06:34 | 10-25 18:22 |
| polymarket_bbo | cs2 | 234,118 | 672 | 6,388 | 59,629 | 10-14 19:27 | 10-27 10:34 |
| polymarket_bbo | epl | 49,643 | 20 | 1,314 | 8,844 | 10-15 23:32 | 10-25 18:22 |
| polymarket_bbo | laliga | 51,107 | 21 | 1,892 | 10,416 | 10-15 07:34 | 10-26 21:24 |
| polymarket_bbo | ligue1 | 47,388 | 18 | 1,350 | 9,384 | 10-15 06:55 | 10-26 21:13 |
| polymarket_bbo | lol | 5,132 | 34 | 2,066 | 1,229 | 10-14 19:27 | 10-27 10:31 |
| polymarket_bbo | mlb | 70,625 | 10 | 1,520 | 14,908 | 10-14 19:27 | 10-27 10:31 |
| polymarket_bbo | nba | 169,631 | 77 | 2,254 | 59,006 | 10-14 19:27 | 10-27 10:31 |
| polymarket_bbo | nfl | 47,838 | 28 | 1,474 | 8,946 | 10-14 19:27 | 10-27 03:15 |
| polymarket_bbo | nhl | 325,682 | 93 | 2,967 | 58,119 | 10-14 19:27 | 10-27 10:31 |
| polymarket_bbo | seriea | 55,233 | 28 | 1,801 | 10,644 | 10-15 06:55 | 10-27 10:31 |
| pinnacle | mlb | 2,314 | 11 | 512 |  | 10-14 21:29 | 10-27 10:07 |
| pinnacle | nba | 32,202 | 56 | 733 |  | 10-14 21:29 | 10-27 10:07 |
| pinnacle | nfl | 27,502 | 38 | 573 |  | 10-14 21:29 | 10-27 10:07 |
| pinnacle | nhl | 33,070 | 93 | 835 |  | 10-14 21:29 | 10-27 10:07 |
| polymarket_history | bundesliga | 337 | 337 | 364,297 |  | NaT | NaT |
| polymarket_history | cs2 | 2,038 | 1,984 | 1,722,295 |  | NaT | NaT |
| polymarket_history | epl | 360 | 360 | 389,160 |  | NaT | NaT |
| polymarket_history | laliga | 382 | 382 | 412,942 |  | NaT | NaT |
| polymarket_history | ligue1 | 343 | 331 | 370,783 |  | NaT | NaT |
| polymarket_history | lol | 33 | 33 | 35,673 |  | NaT | NaT |
| polymarket_history | mlb | 518 | 458 | 559,958 |  | NaT | NaT |
| polymarket_history | nba | 4,326 | 4,326 | 3,888,596 |  | NaT | NaT |
| polymarket_history | nfl | 1,132 | 1,132 | 1,223,692 |  | NaT | NaT |
| polymarket_history | nhl | 2,761 | 2,761 | 2,984,641 |  | NaT | NaT |
| polymarket_history | seriea | 362 | 362 | 391,322 |  | NaT | NaT |
| news_mlb | mlb | 536 |  |  |  | NaT | NaT |
| news_nhl | nhl | 623 |  |  |  | NaT | NaT |
| news_nhl_schedule | nhl | 686 |  |  |  | NaT | NaT |

Odds API quota at last pass: used 7240.0, remaining 12760.0 (1005 Pinnacle passes recorded).

## Event matching (Polymarket US vs Pinnacle)

1019 Polymarket events, 198 Pinnacle events, 187 matched (51 by full name, 136 by nickname).

Unmatched Polymarket events (832): bundesliga Eintracht Frankfurt vs. 1. FC Koln; bundesliga 1. FC Union Berlin vs. BV Borussia 09 Dortmund; bundesliga Hamburger SV vs. VfB Stuttgart; bundesliga SV Werder Bremen vs. SC Paderborn 07; bundesliga FC Schalke 04 vs. 1. FSV Mainz 05; bundesliga SV 07 Elversberg vs. FC Augsburg; bundesliga FC Bayern Munchen vs. RB Leipzig; bundesliga Bayer 04 Leverkusen vs. SC Freiburg; bundesliga Borussia Monchengladbach vs. TSG 1899 Hoffenheim; bundesliga VfB Stuttgart vs. Borussia Monchengladbach; bundesliga RB Leipzig vs. SV 07 Elversberg; bundesliga FC Augsburg vs. 1. FC Union Berlin; bundesliga 1. FSV Mainz 05 vs. SV Werder Bremen; bundesliga 1. FC Koln vs. FC Schalke 04; bundesliga SC Paderborn 07 vs. Hamburger SV

## Polymarket mid vs Pinnacle fair, main winner contracts

mid_minus_fair > 0 means Polymarket prices the team higher than Pinnacle's de-vigged price. taker_edge_at_ask = fair − ask − fee: what a taker would expect if Pinnacle were exactly right.

| sport | bucket | n | mean_diff | mean_abs_diff | within_1c | within_2c | mean_spread | median_bid_shares | taker_edge_mean | taker_edge_pos_share |
|---|---|---|---|---|---|---|---|---|---|---|
| mlb | 0-15 min | 633 | -0.255 | 0.272 | 6% | 7% | 0.021 | 5,900 | 0.233 | 85% |
| mlb | 15-60 min | 863 | -0.270 | 0.270 | 7% | 7% | 0.010 | 30,000 | 0.253 | 93% |
| mlb | 1-3 h | 965 | -0.272 | 0.272 | 7% | 7% | 0.010 | 28,000 | 0.255 | 93% |
| mlb | 3-12 h | 1,474 | -0.272 | 0.272 | 6% | 7% | 0.049 | 26,000 | 0.235 | 91% |
| mlb | 12 h+ | 2,045 | -0.253 | 0.255 | 4% | 7% | 0.145 | 19,000 | 0.166 | 83% |
| nba | 0-15 min | 7,316 | -0.025 | 0.161 | 7% | 11% | 0.315 | 26,000 | -0.145 | 29% |
| nba | 15-60 min | 3,542 | -0.037 | 0.108 | 15% | 21% | 0.362 | 25,000 | -0.157 | 21% |
| nba | 1-3 h | 7,201 | -0.049 | 0.129 | 14% | 22% | 0.450 | 25,000 | -0.187 | 16% |
| nba | 3-12 h | 9,014 | -0.042 | 0.123 | 17% | 25% | 0.451 | 25,000 | -0.195 | 15% |
| nba | 12 h+ | 1,876 | -0.001 | 0.014 | 78% | 94% | 0.038 | 300,000 | -0.033 | 1% |
| nhl | 0-15 min | 8,289 | -0.108 | 0.147 | 9% | 13% | 0.090 | 28,000 | 0.049 | 61% |
| nhl | 15-60 min | 3,968 | -0.116 | 0.117 | 12% | 15% | 0.012 | 32,000 | 0.094 | 85% |
| nhl | 1-3 h | 7,550 | -0.116 | 0.117 | 12% | 14% | 0.012 | 32,000 | 0.095 | 86% |
| nhl | 3-12 h | 14,923 | -0.113 | 0.114 | 11% | 13% | 0.045 | 31,000 | 0.075 | 82% |
| nhl | 12 h+ | 27,049 | -0.126 | 0.127 | 12% | 14% | 0.132 | 29,000 | 0.043 | 71% |

Largest gaps seen:

| sport | team | pin_ts | minutes_to_start | fair | pm_mid | pm_spread | mid_minus_fair | taker_edge_at_ask |
|---|---|---|---|---|---|---|---|---|
| mlb | Milwaukee Brewers | 10-24 02:58 | -179 | 0.938 | 0.025 | 0.010 | -0.913 | 0.906 |
| mlb | Tampa Bay Rays | 10-18 23:46 | -159 | 0.941 | 0.040 | 0.020 | -0.901 | 0.888 |
| nba | Mavericks | 10-24 01:18 | -139 | 0.899 | 0.020 | 0.020 | -0.879 | 0.867 |
| nba | Pacers | 10-24 01:18 | -139 | 0.101 | 0.965 | 0.050 | 0.864 | -0.890 |
| nba | Mavericks | 10-24 01:25 | -151 | 0.899 | 0.045 | 0.050 | -0.854 | 0.825 |
| nba | Pacers | 10-24 01:25 | -151 | 0.101 | 0.950 | 0.080 | 0.849 | -0.890 |
| nba | Pistons | 10-26 02:07 | -157 | 0.950 | 0.115 | 0.210 | -0.835 | 0.718 |
| nba | Raptors | 10-26 00:39 | -109 | 0.157 | 0.985 | 0.010 | 0.828 | -0.834 |
| nba | Raptors | 10-26 00:44 | -109 | 0.157 | 0.985 | 0.010 | 0.828 | -0.834 |
| nba | Cavaliers | 10-23 00:36 | -97 | 0.940 | 0.115 | 0.030 | -0.825 | 0.802 |
| nba | Cavaliers | 10-23 00:31 | -97 | 0.940 | 0.115 | 0.030 | -0.825 | 0.802 |
| nhl | Kings | 10-23 01:22 | -105 | 0.848 | 0.025 | 0.030 | -0.823 | 0.805 |

## Test (b): calibration of last pre-game mids (settled games)

| sport | n | mean_mid | win_rate | brier_pm | log_loss_pm | slope | slope_se | intercept | n_with_pinnacle | brier_pm_matched | brier_pinnacle |
|---|---|---|---|---|---|---|---|---|---|---|---|
| bundesliga | 162 | 0.335 | 0.333 | 0.214 | 0.615 | 0.708 | 0.254 | -0.198 |  |  |  |
| cs2 | 1,460 | 0.530 | 0.564 | 0.223 | 0.633 | 0.908 | 0.088 | 0.163 |  |  |  |
| epl | 180 | 0.337 | 0.333 | 0.204 | 0.594 | 1.006 | 0.274 | -0.014 |  |  |  |
| laliga | 189 | 0.341 | 0.333 | 0.201 | 0.585 | 1.023 | 0.249 | -0.025 |  |  |  |
| ligue1 | 162 | 0.344 | 0.333 | 0.207 | 0.601 | 1.001 | 0.307 | -0.051 |  |  |  |
| lol | 33 | 0.572 | 0.364 | 0.243 | 0.678 | 0.933 | 0.447 | -1.020 |  |  |  |
| mlb | 189 | 0.345 | 0.344 | 0.202 | 0.594 | 0.750 | 0.170 | -0.150 | 129 | 0.182 | 0.246 |
| nba | 857 | 0.339 | 0.326 | 0.184 | 0.534 | 0.923 | 0.090 | -0.102 | 542 | 0.245 | 0.244 |
| nhl | 910 | 0.349 | 0.335 | 0.220 | 0.632 | 0.656 | 0.167 | -0.273 | 634 | 0.228 | 0.246 |
| seriea | 180 | 0.358 | 0.333 | 0.209 | 0.607 | 0.877 | 0.271 | -0.185 |  |  |  |

4322 settled main winner contracts so far; calibration is reported from 30 per sport.

## Test (a): news events and price reaction

276 news events recorded; 3852 joined to a Polymarket contract with a price path.

| sport | kind | n |
|---|---|---|
| mlb | lineup_away | 21 |
| mlb | lineup_home | 11 |
| mlb | probable_away | 6 |
| mlb | probable_home | 5 |
| nhl | goalie_confirmed | 163 |
| nhl | goalie_likely | 70 |

Most recent joined events:

| sport | kind | team | detail | news_ts | minutes_to_start | contract_is_news_team | mid_before | move_plus5 | move_plus15 | move_plus30 | pin_fair_before | pin_fair_after | minutes_to_within_1c |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| nhl | goalie_confirmed | Toronto Maple Leafs | Sergei Bobrovsky | 10-27 00:05 | 25 | True | 0.495 | 0.000 | 0.000 | 0.000 | 0.562 | 0.562 |  |
| nhl | goalie_confirmed | Toronto Maple Leafs | Sergei Bobrovsky | 10-27 00:05 | 25 | True | 0.375 | 0.000 | 0.000 | 0.000 | 0.562 | 0.562 |  |
| nhl | goalie_confirmed | Toronto Maple Leafs | Sergei Bobrovsky | 10-27 00:05 | 25 | True | 0.555 | 0.000 | 0.000 | 0.000 | 0.562 | 0.562 | 0.908 |
| nhl | goalie_confirmed | Toronto Maple Leafs | Sergei Bobrovsky | 10-27 00:05 | 25 | False | 0.285 | 0.000 | 0.000 | 0.000 | 0.438 | 0.438 |  |
| nhl | goalie_confirmed | Toronto Maple Leafs | Sergei Bobrovsky | 10-27 00:05 | 25 | False | 0.335 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Toronto Maple Leafs | Sergei Bobrovsky | 10-27 00:05 | 25 | True | 0.375 | 0.000 | 0.000 | 0.000 | 0.562 | 0.562 |  |
| nhl | goalie_confirmed | Toronto Maple Leafs | Sergei Bobrovsky | 10-27 00:05 | 25 | False | 0.275 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Toronto Maple Leafs | Sergei Bobrovsky | 10-27 00:05 | 25 | False | 0.325 | 0.000 | 0.000 | 0.000 | 0.438 | 0.438 |  |
| nhl | goalie_confirmed | Toronto Maple Leafs | Sergei Bobrovsky | 10-27 00:05 | 25 | False | 0.305 | 0.000 | 0.000 | 0.000 | 0.438 | 0.438 |  |
| nhl | goalie_confirmed | Toronto Maple Leafs | Sergei Bobrovsky | 10-27 00:05 | 25 | False | 0.275 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Toronto Maple Leafs | Sergei Bobrovsky | 10-27 00:05 | 25 | True | 0.415 | 0.000 | 0.000 | 0.000 | 0.562 | 0.562 | 177.908 |
| nhl | goalie_confirmed | Toronto Maple Leafs | Sergei Bobrovsky | 10-27 00:05 | 25 | False | 0.325 | 0.000 | 0.000 | 0.000 | 0.438 | 0.438 |  |
| nhl | goalie_confirmed | Toronto Maple Leafs | Sergei Bobrovsky | 10-27 00:05 | 25 | False | 0.225 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Los Angeles Kings | Darcy Kuemper | 10-26 22:30 | 29 | False | 0.335 | 0.000 | 0.000 | 0.000 | 0.550 | 0.550 |  |
| nhl | goalie_confirmed | Los Angeles Kings | Darcy Kuemper | 10-26 22:30 | 29 | True | 0.445 | 0.000 | 0.000 | 0.010 | 0.450 | 0.450 | 0.320 |
| nhl | goalie_confirmed | Los Angeles Kings | Darcy Kuemper | 10-26 22:30 | 29 | False | 0.365 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Los Angeles Kings | Darcy Kuemper | 10-26 22:30 | 29 | True | 0.305 | 0.000 | 0.000 | 0.000 | 0.450 | 0.450 |  |
| nhl | goalie_confirmed | Los Angeles Kings | Darcy Kuemper | 10-26 22:30 | 29 | False | 0.365 | 0.000 | 0.000 | 0.000 | 0.550 | 0.550 |  |
| nhl | goalie_confirmed | Los Angeles Kings | Darcy Kuemper | 10-26 22:30 | 29 | False | 0.335 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Los Angeles Kings | Darcy Kuemper | 10-26 22:30 | 29 | True | 0.315 | 0.000 | 0.000 | 0.000 | 0.450 | 0.450 |  |
| nhl | goalie_confirmed | Los Angeles Kings | Darcy Kuemper | 10-26 22:30 | 29 | False | 0.255 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Los Angeles Kings | Darcy Kuemper | 10-26 22:30 | 29 | True | 0.325 | 0.000 | 0.000 | 0.000 | 0.450 | 0.450 | 160.320 |
| nhl | goalie_confirmed | Los Angeles Kings | Darcy Kuemper | 10-26 22:30 | 29 | False | 0.375 | 0.000 | 0.000 | 0.000 | 0.550 | 0.550 |  |
| nhl | goalie_confirmed | Los Angeles Kings | Darcy Kuemper | 10-26 22:30 | 29 | False | 0.235 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Los Angeles Kings | Darcy Kuemper | 10-26 22:30 | 29 | True | 0.365 | 0.000 | 0.000 | 0.000 | 0.450 | 0.450 |  |
| nhl | goalie_confirmed | Los Angeles Kings | Darcy Kuemper | 10-26 22:30 | 29 | False | 0.445 | 0.000 | 0.000 | 0.000 | 0.550 | 0.550 |  |
| mlb | lineup_away | Milwaukee Brewers | 9 players | 10-26 20:30 | 210 | False | 0.575 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | lineup_away | Milwaukee Brewers | 9 players | 10-26 20:30 | 210 | False | 0.565 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | lineup_away | Milwaukee Brewers | 9 players | 10-26 20:30 | 210 | False | 0.245 | 0.000 | 0.000 | 0.000 | 0.516 | 0.514 |  |
| mlb | lineup_away | Milwaukee Brewers | 9 players | 10-26 20:30 | 210 | True | 0.215 | 0.000 | 0.000 | 0.000 | 0.484 | 0.486 |  |
| mlb | lineup_away | Milwaukee Brewers | 9 players | 10-26 20:30 | 210 | False | 0.565 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | lineup_away | Milwaukee Brewers | 9 players | 10-26 20:30 | 210 | False | 0.195 | 0.000 | 0.000 | 0.000 | 0.516 | 0.514 |  |
| mlb | lineup_away | Milwaukee Brewers | 9 players | 10-26 20:30 | 210 | True | 0.205 | 0.000 | 0.000 | 0.000 | 0.484 | 0.486 |  |
| mlb | lineup_away | Milwaukee Brewers | 9 players | 10-26 20:30 | 210 | False | 0.555 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | lineup_away | Milwaukee Brewers | 9 players | 10-26 20:30 | 210 | False | 0.245 | 0.000 | 0.000 | 0.000 | 0.516 | 0.514 |  |
| mlb | lineup_away | Milwaukee Brewers | 9 players | 10-26 20:30 | 210 | True | 0.215 | 0.000 | 0.000 | 0.000 | 0.484 | 0.486 |  |
| mlb | lineup_away | Milwaukee Brewers | 9 players | 10-26 20:30 | 210 | False | 0.225 | 0.000 | 0.000 | 0.000 | 0.516 | 0.514 |  |
| mlb | lineup_away | Milwaukee Brewers | 9 players | 10-26 20:30 | 210 | False | 0.465 | 0.000 | 0.000 | 0.000 | 0.516 | 0.514 | 234.950 |
| mlb | lineup_away | Milwaukee Brewers | 9 players | 10-26 20:30 | 210 | True | 0.375 | 0.000 | 0.000 | 0.000 | 0.484 | 0.486 |  |
| mlb | lineup_away | Milwaukee Brewers | 9 players | 10-26 20:30 | 210 | False | 0.165 | 0.000 | 0.000 | 0.000 |  |  |  |

Generated by method/analysis/report.py from the data branch.
