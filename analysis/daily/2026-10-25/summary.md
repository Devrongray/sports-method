# Daily analysis 2026-10-25

## Coverage

| source | sport | rows | events | passes | window_rows | first | last |
|---|---|---|---|---|---|---|---|
| polymarket_bbo | bundesliga | 39,822 | 18 | 1,067 | 7,740 | 10-15 06:34 | 10-25 10:20 |
| polymarket_bbo | cs2 | 212,675 | 635 | 5,656 | 54,249 | 10-14 19:27 | 10-25 10:22 |
| polymarket_bbo | epl | 45,707 | 20 | 1,195 | 6,912 | 10-15 23:32 | 10-25 10:20 |
| polymarket_bbo | laliga | 44,963 | 21 | 1,556 | 8,064 | 10-15 07:34 | 10-25 10:20 |
| polymarket_bbo | ligue1 | 39,588 | 18 | 1,112 | 6,192 | 10-15 06:55 | 10-25 10:20 |
| polymarket_bbo | lol | 4,106 | 33 | 1,710 | 982 | 10-14 19:27 | 10-25 10:20 |
| polymarket_bbo | mlb | 59,627 | 8 | 1,315 | 13,588 | 10-14 19:27 | 10-25 03:24 |
| polymarket_bbo | nba | 116,374 | 64 | 1,797 | 38,645 | 10-14 19:27 | 10-25 10:20 |
| polymarket_bbo | nfl | 37,821 | 27 | 1,086 | 5,103 | 10-14 19:27 | 10-25 10:20 |
| polymarket_bbo | nhl | 284,711 | 79 | 2,501 | 51,273 | 10-14 19:27 | 10-25 10:20 |
| polymarket_bbo | seriea | 47,037 | 20 | 1,500 | 8,496 | 10-15 06:55 | 10-25 10:22 |
| pinnacle | mlb | 2,058 | 10 | 447 |  | 10-14 21:29 | 10-25 09:56 |
| pinnacle | nba | 28,398 | 43 | 605 |  | 10-14 21:29 | 10-25 09:56 |
| pinnacle | nfl | 22,892 | 28 | 455 |  | 10-14 21:29 | 10-25 09:56 |
| pinnacle | nhl | 28,930 | 78 | 706 |  | 10-14 21:29 | 10-25 09:56 |
| polymarket_history | bundesliga | 300 | 300 | 324,300 |  | NaT | NaT |
| polymarket_history | cs2 | 1,839 | 1,779 | 1,539,938 |  | NaT | NaT |
| polymarket_history | epl | 271 | 271 | 292,951 |  | NaT | NaT |
| polymarket_history | laliga | 287 | 287 | 310,247 |  | NaT | NaT |
| polymarket_history | ligue1 | 215 | 203 | 232,415 |  | NaT | NaT |
| polymarket_history | lol | 25 | 25 | 27,025 |  | NaT | NaT |
| polymarket_history | mlb | 457 | 397 | 494,017 |  | NaT | NaT |
| polymarket_history | nba | 3,022 | 3,022 | 2,644,590 |  | NaT | NaT |
| polymarket_history | nfl | 595 | 595 | 643,195 |  | NaT | NaT |
| polymarket_history | nhl | 2,470 | 2,470 | 2,670,070 |  | NaT | NaT |
| polymarket_history | seriea | 270 | 270 | 291,870 |  | NaT | NaT |
| news_mlb | mlb | 470 |  |  |  | NaT | NaT |
| news_nhl | nhl | 542 |  |  |  | NaT | NaT |
| news_nhl_schedule | nhl | 597 |  |  |  | NaT | NaT |

Odds API quota at last pass: used 5880.0, remaining 14120.0 (838 Pinnacle passes recorded).

## Event matching (Polymarket US vs Pinnacle)

943 Polymarket events, 159 Pinnacle events, 156 matched (35 by full name, 121 by nickname).

Unmatched Polymarket events (787): bundesliga Eintracht Frankfurt vs. 1. FC Koln; bundesliga 1. FC Union Berlin vs. BV Borussia 09 Dortmund; bundesliga Hamburger SV vs. VfB Stuttgart; bundesliga SV Werder Bremen vs. SC Paderborn 07; bundesliga FC Schalke 04 vs. 1. FSV Mainz 05; bundesliga SV 07 Elversberg vs. FC Augsburg; bundesliga FC Bayern Munchen vs. RB Leipzig; bundesliga Bayer 04 Leverkusen vs. SC Freiburg; bundesliga Borussia Monchengladbach vs. TSG 1899 Hoffenheim; bundesliga VfB Stuttgart vs. Borussia Monchengladbach; bundesliga RB Leipzig vs. SV 07 Elversberg; bundesliga FC Augsburg vs. 1. FC Union Berlin; bundesliga 1. FSV Mainz 05 vs. SV Werder Bremen; bundesliga 1. FC Koln vs. FC Schalke 04; bundesliga SC Paderborn 07 vs. Hamburger SV

## Polymarket mid vs Pinnacle fair, main winner contracts

mid_minus_fair > 0 means Polymarket prices the team higher than Pinnacle's de-vigged price. taker_edge_at_ask = fair − ask − fee: what a taker would expect if Pinnacle were exactly right.

| sport | bucket | n | mean_diff | mean_abs_diff | within_1c | within_2c | mean_spread | median_bid_shares | taker_edge_mean | taker_edge_pos_share |
|---|---|---|---|---|---|---|---|---|---|---|
| mlb | 0-15 min | 557 | -0.253 | 0.272 | 6% | 8% | 0.022 | 5,800 | 0.231 | 83% |
| mlb | 15-60 min | 779 | -0.270 | 0.271 | 8% | 8% | 0.010 | 29,000 | 0.254 | 92% |
| mlb | 1-3 h | 818 | -0.272 | 0.273 | 7% | 7% | 0.010 | 28,000 | 0.256 | 93% |
| mlb | 3-12 h | 1,327 | -0.272 | 0.273 | 6% | 7% | 0.050 | 26,000 | 0.235 | 91% |
| mlb | 12 h+ | 1,268 | -0.247 | 0.249 | 4% | 7% | 0.180 | 21,000 | 0.143 | 76% |
| nba | 0-15 min | 4,610 | -0.021 | 0.160 | 7% | 12% | 0.374 | 26,000 | -0.177 | 25% |
| nba | 15-60 min | 2,242 | -0.035 | 0.116 | 16% | 22% | 0.450 | 25,000 | -0.201 | 16% |
| nba | 1-3 h | 4,510 | -0.043 | 0.134 | 15% | 23% | 0.503 | 1,500 | -0.219 | 12% |
| nba | 3-12 h | 6,213 | -0.030 | 0.115 | 17% | 25% | 0.384 | 25,000 | -0.174 | 16% |
| nba | 12 h+ | 1,719 | -0.000 | 0.013 | 78% | 94% | 0.036 | 290,000 | -0.033 | 1% |
| nhl | 0-15 min | 7,468 | -0.109 | 0.146 | 9% | 14% | 0.092 | 28,000 | 0.048 | 61% |
| nhl | 15-60 min | 3,509 | -0.116 | 0.117 | 12% | 15% | 0.012 | 32,000 | 0.094 | 85% |
| nhl | 1-3 h | 6,668 | -0.117 | 0.118 | 12% | 14% | 0.012 | 32,000 | 0.095 | 86% |
| nhl | 3-12 h | 13,411 | -0.113 | 0.114 | 11% | 13% | 0.045 | 31,000 | 0.074 | 82% |
| nhl | 12 h+ | 21,604 | -0.124 | 0.125 | 12% | 14% | 0.127 | 29,000 | 0.044 | 71% |

Largest gaps seen:

| sport | team | pin_ts | minutes_to_start | fair | pm_mid | pm_spread | mid_minus_fair | taker_edge_at_ask |
|---|---|---|---|---|---|---|---|---|
| mlb | Milwaukee Brewers | 10-24 02:58 | -179 | 0.938 | 0.025 | 0.010 | -0.913 | 0.906 |
| mlb | Tampa Bay Rays | 10-18 23:46 | -159 | 0.941 | 0.040 | 0.020 | -0.901 | 0.888 |
| nba | Mavericks | 10-24 01:18 | -139 | 0.899 | 0.020 | 0.020 | -0.879 | 0.867 |
| nba | Pacers | 10-24 01:18 | -139 | 0.101 | 0.965 | 0.050 | 0.864 | -0.890 |
| nba | Mavericks | 10-24 01:25 | -151 | 0.899 | 0.045 | 0.050 | -0.854 | 0.825 |
| nba | Pacers | 10-24 01:25 | -151 | 0.101 | 0.950 | 0.080 | 0.849 | -0.890 |
| nba | Cavaliers | 10-23 00:31 | -97 | 0.940 | 0.115 | 0.030 | -0.825 | 0.802 |
| nba | Cavaliers | 10-23 00:36 | -97 | 0.940 | 0.115 | 0.030 | -0.825 | 0.802 |
| nhl | Kings | 10-23 01:15 | -105 | 0.848 | 0.025 | 0.030 | -0.823 | 0.805 |
| nhl | Kings | 10-23 01:22 | -105 | 0.848 | 0.025 | 0.030 | -0.823 | 0.805 |
| nba | Cavaliers | 10-23 00:31 | -97 | 0.940 | 0.120 | 0.020 | -0.820 | 0.802 |
| nba | Cavaliers | 10-23 00:36 | -97 | 0.940 | 0.120 | 0.020 | -0.820 | 0.802 |

## Test (b): calibration of last pre-game mids (settled games)

| sport | n | mean_mid | win_rate | brier_pm | log_loss_pm | slope | slope_se | intercept | n_with_pinnacle | brier_pm_matched | brier_pinnacle |
|---|---|---|---|---|---|---|---|---|---|---|---|
| bundesliga | 144 | 0.336 | 0.333 | 0.216 | 0.619 | 0.664 | 0.268 | -0.229 |  |  |  |
| cs2 | 1,321 | 0.531 | 0.569 | 0.223 | 0.635 | 0.914 | 0.093 | 0.181 |  |  |  |
| epl | 135 | 0.337 | 0.333 | 0.196 | 0.573 | 1.170 | 0.310 | 0.083 |  |  |  |
| laliga | 144 | 0.346 | 0.333 | 0.202 | 0.589 | 0.969 | 0.279 | -0.080 |  |  |  |
| ligue1 | 99 | 0.346 | 0.333 | 0.212 | 0.613 | 0.939 | 0.440 | -0.097 |  |  |  |
| lol | 25 | 0.570 | 0.400 |  |  |  |  |  |  |  |  |
| mlb | 158 | 0.346 | 0.342 | 0.204 | 0.595 | 0.736 | 0.185 | -0.172 | 108 | 0.183 | 0.244 |
| nba | 567 | 0.345 | 0.321 | 0.184 | 0.531 | 0.994 | 0.121 | -0.134 | 348 | 0.246 | 0.236 |
| nhl | 806 | 0.348 | 0.333 | 0.220 | 0.631 | 0.638 | 0.179 | -0.294 | 562 | 0.226 | 0.244 |
| seriea | 135 | 0.358 | 0.333 | 0.218 | 0.628 | 0.609 | 0.305 | -0.330 |  |  |  |

3534 settled main winner contracts so far; calibration is reported from 30 per sport.

## Test (a): news events and price reaction

252 news events recorded; 3504 joined to a Polymarket contract with a price path.

| sport | kind | n |
|---|---|---|
| mlb | lineup_away | 20 |
| mlb | lineup_home | 10 |
| mlb | probable_away | 6 |
| mlb | probable_home | 4 |
| nhl | goalie_confirmed | 149 |
| nhl | goalie_likely | 63 |

Most recent joined events:

| sport | kind | team | detail | news_ts | minutes_to_start | contract_is_news_team | mid_before | move_plus5 | move_plus15 | move_plus30 | pin_fair_before | pin_fair_after | minutes_to_within_1c |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| nhl | goalie_confirmed | Seattle Kraken | Joey Daccord | 10-25 01:44 | 16 | True | 0.335 | -0.030 | -0.030 | -0.145 | 0.376 | 0.367 |  |
| nhl | goalie_confirmed | Seattle Kraken | Joey Daccord | 10-25 01:44 | 16 | True | 0.315 | 0.000 | 0.000 | 0.000 | 0.376 | 0.367 |  |
| nhl | goalie_confirmed | Seattle Kraken | Joey Daccord | 10-25 01:44 | 16 | False | 0.635 | 0.000 | 0.000 | 0.145 | 0.624 | 0.633 | 0.836 |
| nhl | goalie_confirmed | Seattle Kraken | Joey Daccord | 10-25 01:44 | 16 | False | 0.325 | 0.000 | 0.000 | -0.110 |  |  |  |
| nhl | goalie_confirmed | Seattle Kraken | Joey Daccord | 10-25 01:44 | 16 | False | 0.425 | 0.000 | 0.000 | 0.170 | 0.624 | 0.633 | 24.836 |
| nhl | goalie_confirmed | Seattle Kraken | Joey Daccord | 10-25 01:44 | 16 | False | 0.325 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Seattle Kraken | Joey Daccord | 10-25 01:44 | 16 | False | 0.400 | 0.000 | -0.015 | 0.020 | 0.624 | 0.633 | 85.836 |
| nhl | goalie_confirmed | Seattle Kraken | Joey Daccord | 10-25 01:44 | 16 | True | 0.295 | 0.000 | 0.000 | -0.240 | 0.376 | 0.367 |  |
| nhl | goalie_confirmed | Seattle Kraken | Joey Daccord | 10-25 01:44 | 16 | False | 0.285 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Seattle Kraken | Joey Daccord | 10-25 01:44 | 16 | False | 0.435 | 0.000 | 0.000 | 0.000 | 0.624 | 0.633 |  |
| nhl | goalie_confirmed | Seattle Kraken | Joey Daccord | 10-25 01:44 | 16 | True | 0.335 | 0.000 | 0.000 | -0.100 | 0.376 | 0.367 |  |
| nhl | goalie_confirmed | Seattle Kraken | Joey Daccord | 10-25 01:44 | 16 | False | 0.205 | -0.005 | -0.005 | -0.005 |  |  |  |
| nhl | goalie_confirmed | Seattle Kraken | Joey Daccord | 10-25 01:44 | 16 | False | 0.545 | -0.030 | -0.030 | 0.170 | 0.624 | 0.633 | 45.836 |
| nhl | goalie_confirmed | Tampa Bay Lightning | Dennis Hildeby | 10-25 00:33 | 27 | False | 0.385 | 0.000 | 0.000 | 0.000 | 0.573 | 0.573 | 106.672 |
| nhl | goalie_confirmed | Tampa Bay Lightning | Dennis Hildeby | 10-25 00:33 | 27 | True | 0.425 | 0.000 | 0.000 | 0.000 | 0.427 | 0.427 | 0.672 |
| nhl | goalie_confirmed | Tampa Bay Lightning | Dennis Hildeby | 10-25 00:33 | 27 | False | 0.315 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Tampa Bay Lightning | Dennis Hildeby | 10-25 00:33 | 27 | True | 0.315 | 0.000 | 0.000 | 0.000 | 0.427 | 0.427 |  |
| nhl | goalie_confirmed | Tampa Bay Lightning | Dennis Hildeby | 10-25 00:33 | 27 | False | 0.360 | 0.000 | 0.005 | 0.000 | 0.573 | 0.573 |  |
| nhl | goalie_confirmed | Tampa Bay Lightning | Dennis Hildeby | 10-25 00:33 | 27 | False | 0.245 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Tampa Bay Lightning | Dennis Hildeby | 10-25 00:33 | 27 | True | 0.305 | 0.000 | 0.000 | 0.000 | 0.427 | 0.427 |  |
| nhl | goalie_confirmed | Tampa Bay Lightning | Dennis Hildeby | 10-25 00:33 | 27 | False | 0.205 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Tampa Bay Lightning | Dennis Hildeby | 10-25 00:33 | 27 | False | 0.275 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Tampa Bay Lightning | Dennis Hildeby | 10-25 00:33 | 27 | True | 0.325 | 0.000 | 0.000 | 0.000 | 0.427 | 0.427 |  |
| nhl | goalie_confirmed | Tampa Bay Lightning | Dennis Hildeby | 10-25 00:33 | 27 | False | 0.415 | 0.000 | 0.000 | 0.000 | 0.573 | 0.573 |  |
| nhl | goalie_confirmed | Tampa Bay Lightning | Dennis Hildeby | 10-25 00:33 | 27 | True | 0.345 | 0.000 | 0.000 | 0.000 | 0.427 | 0.427 | 43.672 |
| nhl | goalie_confirmed | Tampa Bay Lightning | Dennis Hildeby | 10-25 00:33 | 27 | False | 0.480 | 0.000 | 0.000 | 0.005 | 0.573 | 0.573 |  |
| nhl | goalie_confirmed | Utah Mammoth | Karel Vejmelka | 10-25 00:32 | 28 | True | 0.385 | 0.000 | 0.000 | 0.000 | 0.573 | 0.573 | 107.826 |
| nhl | goalie_confirmed | Utah Mammoth | Karel Vejmelka | 10-25 00:32 | 28 | False | 0.425 | 0.000 | 0.000 | 0.000 | 0.427 | 0.427 | 0.826 |
| nhl | goalie_confirmed | Utah Mammoth | Karel Vejmelka | 10-25 00:32 | 28 | False | 0.315 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Utah Mammoth | Karel Vejmelka | 10-25 00:32 | 28 | False | 0.315 | 0.000 | 0.000 | 0.000 | 0.427 | 0.427 |  |
| nhl | goalie_confirmed | Utah Mammoth | Karel Vejmelka | 10-25 00:32 | 28 | True | 0.360 | 0.000 | 0.005 | 0.000 | 0.573 | 0.573 |  |
| nhl | goalie_confirmed | Utah Mammoth | Karel Vejmelka | 10-25 00:32 | 28 | False | 0.245 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Utah Mammoth | Karel Vejmelka | 10-25 00:32 | 28 | False | 0.305 | 0.000 | 0.000 | 0.000 | 0.427 | 0.427 |  |
| nhl | goalie_confirmed | Utah Mammoth | Karel Vejmelka | 10-25 00:32 | 28 | True | 0.480 | 0.005 | 0.005 | 0.005 | 0.573 | 0.573 |  |
| nhl | goalie_confirmed | Utah Mammoth | Karel Vejmelka | 10-25 00:32 | 28 | False | 0.275 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Utah Mammoth | Karel Vejmelka | 10-25 00:32 | 28 | True | 0.415 | 0.000 | 0.000 | 0.000 | 0.573 | 0.573 |  |
| nhl | goalie_confirmed | Utah Mammoth | Karel Vejmelka | 10-25 00:32 | 28 | False | 0.205 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Utah Mammoth | Karel Vejmelka | 10-25 00:32 | 28 | False | 0.345 | 0.000 | 0.000 | 0.000 | 0.427 | 0.427 | 44.826 |
| nhl | goalie_confirmed | Utah Mammoth | Karel Vejmelka | 10-25 00:32 | 28 | False | 0.325 | 0.000 | 0.000 | 0.000 | 0.427 | 0.427 |  |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-24 22:56 | 64 | True | 0.205 | 0.000 | 0.000 | 0.000 | 0.478 | 0.478 |  |

Generated by method/analysis/report.py from the data branch.
