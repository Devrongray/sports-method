# Daily analysis 2026-10-16

## Coverage

| source | sport | rows | events | passes | window_rows | first | last |
|---|---|---|---|---|---|---|---|
| polymarket_bbo | bundesliga | 1,071 | 7 | 112 | 0 | 10-15 06:34 | 10-16 10:20 |
| polymarket_bbo | cs2 | 12,156 | 133 | 884 | 2,659 | 10-14 19:27 | 10-16 10:25 |
| polymarket_bbo | epl | 519 | 5 | 47 | 0 | 10-15 23:32 | 10-16 10:20 |
| polymarket_bbo | laliga | 783 | 5 | 109 | 0 | 10-15 07:34 | 10-16 10:20 |
| polymarket_bbo | ligue1 | 612 | 4 | 110 | 0 | 10-15 06:55 | 10-16 10:20 |
| polymarket_bbo | lol | 579 | 6 | 300 | 137 | 10-14 19:27 | 10-16 10:20 |
| polymarket_bbo | mlb | 4,888 | 4 | 322 | 1,224 | 10-14 19:27 | 10-16 10:20 |
| polymarket_bbo | nba | 3,751 | 21 | 413 | 1,406 | 10-14 19:27 | 10-16 10:20 |
| polymarket_bbo | nfl | 672 | 1 | 96 | 0 | 10-14 19:27 | 10-15 19:56 |
| polymarket_bbo | nhl | 13,005 | 19 | 456 | 1,902 | 10-14 19:27 | 10-16 10:20 |
| polymarket_bbo | seriea | 681 | 4 | 110 | 0 | 10-15 06:55 | 10-16 10:20 |
| pinnacle | mlb | 630 | 4 | 89 |  | 10-14 21:29 | 10-16 09:59 |
| pinnacle | nba | 5,136 | 12 | 107 |  | 10-14 21:29 | 10-16 09:59 |
| pinnacle | nfl | 3,042 | 14 | 55 |  | 10-14 21:29 | 10-16 09:59 |
| pinnacle | nhl | 5,214 | 15 | 117 |  | 10-14 21:29 | 10-16 09:59 |
| polymarket_history | cs2 | 116 | 107 | 97,167 |  | NaT | NaT |
| polymarket_history | lol | 3 | 3 | 3,243 |  | NaT | NaT |
| polymarket_history | mlb | 93 | 93 | 100,533 |  | NaT | NaT |
| polymarket_history | nba | 140 | 140 | 146,552 |  | NaT | NaT |
| polymarket_history | nfl | 23 | 23 | 24,863 |  | NaT | NaT |
| polymarket_history | nhl | 243 | 243 | 262,683 |  | NaT | NaT |
| news_mlb | mlb | 71 |  |  |  | NaT | NaT |
| news_nhl | nhl | 74 |  |  |  | NaT | NaT |
| news_nhl_schedule | nhl | 87 |  |  |  | NaT | NaT |

Odds API quota at last pass: used 666.0, remaining 19334.0 (137 Pinnacle passes recorded).

## Event matching (Polymarket US vs Pinnacle)

209 Polymarket events, 45 Pinnacle events, 20 matched (5 by full name, 15 by nickname).

Unmatched Polymarket events (189): bundesliga Eintracht Frankfurt vs. 1. FC Koln; bundesliga 1. FC Union Berlin vs. BV Borussia 09 Dortmund; bundesliga Hamburger SV vs. VfB Stuttgart; bundesliga SV Werder Bremen vs. SC Paderborn 07; bundesliga FC Schalke 04 vs. 1. FSV Mainz 05; bundesliga SV 07 Elversberg vs. FC Augsburg; bundesliga FC Bayern Munchen vs. RB Leipzig; cs2  Phantom Academy vs. ZOTIX; cs2 FURIA vs. BetBoom Team; cs2 Pandaric eSports vs. BIG Academy; cs2 WBT vs. Esport Academy Copenhagen; cs2 ENCE vs. BOJONG; cs2 Heroic vs. Envy; cs2 MIBR vs. BC.Game Esports; cs2 WBT vs. ENCE

## Polymarket mid vs Pinnacle fair, main winner contracts

mid_minus_fair > 0 means Polymarket prices the team higher than Pinnacle's de-vigged price. taker_edge_at_ask = fair − ask − fee: what a taker would expect if Pinnacle were exactly right.

| sport | bucket | n | mean_diff | mean_abs_diff | within_1c | within_2c | mean_spread | median_bid_shares | taker_edge_mean | taker_edge_pos_share |
|---|---|---|---|---|---|---|---|---|---|---|
| mlb | 0-15 min | 19 | 0.016 | 0.032 | 53% | 63% | 0.005 | 700,000 | -0.033 | 11% |
| mlb | 15-60 min | 23 | -0.003 | 0.003 | 100% | 100% | 0.005 | 4,000,000 | -0.017 | 0% |
| mlb | 1-3 h | 20 | -0.001 | 0.002 | 95% | 100% | 0.005 | 3,900,000 | -0.018 | 0% |
| mlb | 3-12 h | 25 | 0.002 | 0.002 | 100% | 100% | 0.005 | 2,500,000 | -0.021 | 0% |
| mlb | 12 h+ | 66 | 0.009 | 0.009 | 61% | 100% | 0.005 | 2,000,000 | -0.029 | 0% |
| nhl | 0-15 min | 271 | 0.002 | 0.043 | 48% | 64% | 0.010 | 68,000 | -0.022 | 15% |
| nhl | 15-60 min | 116 | -0.000 | 0.004 | 92% | 100% | 0.010 | 590,000 | -0.021 | 0% |
| nhl | 1-3 h | 188 | 0.000 | 0.004 | 98% | 98% | 0.010 | 570,000 | -0.022 | 2% |
| nhl | 3-12 h | 145 | -0.001 | 0.005 | 92% | 100% | 0.010 | 410,000 | -0.020 | 0% |
| nhl | 12 h+ | 553 | 0.004 | 0.006 | 80% | 100% | 0.010 | 140,000 | -0.025 | 0% |

Largest gaps seen:

| sport | team | pin_ts | minutes_to_start | fair | pm_mid | pm_spread | mid_minus_fair | taker_edge_at_ask |
|---|---|---|---|---|---|---|---|---|
| nhl | Kraken | 10-16 01:22 | -147 | 0.379 | 0.115 | 0.010 | -0.264 | 0.252 |
| nhl | Kraken | 10-16 01:32 | -147 | 0.379 | 0.115 | 0.010 | -0.264 | 0.252 |
| nhl | Kraken | 10-16 01:27 | -147 | 0.379 | 0.115 | 0.010 | -0.264 | 0.252 |
| nhl | Kraken | 10-16 01:17 | -137 | 0.170 | 0.365 | 0.010 | 0.195 | -0.216 |
| nhl | Kraken | 10-16 01:11 | -137 | 0.170 | 0.365 | 0.010 | 0.195 | -0.216 |
| nhl | Flyers | 10-16 00:16 | -51 | 0.435 | 0.625 | 0.010 | 0.190 | -0.211 |
| nhl | Sabres | 10-16 00:41 | -101 | 0.323 | 0.135 | 0.010 | -0.188 | 0.175 |
| nhl | Sabres | 10-16 00:46 | -101 | 0.323 | 0.135 | 0.010 | -0.188 | 0.175 |
| nhl | Sabres | 10-16 00:36 | -101 | 0.323 | 0.135 | 0.010 | -0.188 | 0.175 |
| nhl | Islanders | 10-15 23:48 | -50 | 0.417 | 0.605 | 0.010 | 0.188 | -0.209 |
| nhl | Canucks | 10-15 23:48 | -50 | 0.450 | 0.635 | 0.010 | 0.185 | -0.206 |
| nhl | Sabres | 10-16 00:25 | -91 | 0.489 | 0.305 | 0.010 | -0.184 | 0.164 |

## Test (b): calibration of last pre-game mids (settled games)

| sport | n | mean_mid | win_rate | brier_pm | log_loss_pm | slope | slope_se | intercept |
|---|---|---|---|---|---|---|---|---|
| cs2 | 79 | 0.546 | 0.456 | 0.181 | 0.538 | 2.177 | 0.507 | -0.721 |
| lol | 3 | 0.628 | 0.667 |  |  |  |  |  |
| mlb | 3 | 0.419 | 0.667 |  |  |  |  |  |
| nba | 9 | 0.453 | 0.333 |  |  |  |  |  |
| nhl | 13 | 0.417 | 0.308 |  |  |  |  |  |

107 settled main winner contracts so far; calibration is reported from 30 per sport.

## Test (a): news events and price reaction

49 news events recorded; 46 joined to a Polymarket contract with a price path.

| sport | kind | n |
|---|---|---|
| mlb | lineup_away | 8 |
| mlb | lineup_home | 2 |
| mlb | probable_away | 2 |
| nhl | goalie_confirmed | 26 |
| nhl | goalie_likely | 11 |

Most recent joined events:

| sport | kind | team | detail | news_ts | minutes_to_start | contract_is_news_team | mid_before | move_plus5 | move_plus15 | move_plus30 | pin_fair_before | pin_fair_after | minutes_to_within_1c |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| nhl | goalie_confirmed | Winnipeg Jets | Stuart Skinner | 10-15 23:33 | 27 | True | 0.535 | 0.000 | 0.000 | 0.000 | 0.534 | 0.534 | 0.793 |
| nhl | goalie_confirmed | Nashville Predators | Juuse Saros | 10-15 23:32 | 27 | False | 0.455 | 0.000 | 0.000 | 0.010 | 0.453 | 0.453 | 0.215 |
| nhl | goalie_confirmed | St Louis Blues | Joel Hofer | 10-15 23:31 | 28 | True | 0.435 | 0.000 | 0.000 | 0.000 | 0.435 | 0.435 | 0.090 |
| nhl | goalie_confirmed | Seattle Kraken | Philipp Grubauer | 10-15 22:46 | 13 | True | 0.285 | 0.000 | 0.000 | 0.010 | 0.299 | 0.299 | 28.069 |
| nhl | goalie_confirmed | Tampa Bay Lightning | Andrei Vasilevskiy | 10-15 22:32 | 27 | False | 0.285 | 0.000 | 0.000 | 0.000 | 0.299 | 0.299 | 42.436 |
| nhl | goalie_confirmed | Buffalo Sabres | Ukko-Pekka Luukkonen | 10-15 22:31 | 28 | True | 0.475 | 0.000 | 0.000 | 0.010 | 0.475 | 0.475 | 0.414 |
| nhl | goalie_confirmed | Toronto Maple Leafs | Sergei Bobrovsky | 10-15 22:31 | 29 | False | 0.475 | 0.000 | 0.000 | 0.010 | 0.475 | 0.475 | 0.891 |
| nhl | goalie_confirmed | New Jersey Devils | Nico Daws | 10-15 22:30 | 30 | False | 0.445 | 0.000 | 0.000 | 0.000 | 0.450 | 0.450 | 0.904 |
| nhl | goalie_confirmed | Philadelphia Flyers | Joseph Woll | 10-15 21:28 | 122 | True | 0.435 | 0.000 | 0.000 | 0.000 | 0.441 | 0.428 | 0.868 |
| mlb | lineup_away | Milwaukee Brewers | 9 players | 10-15 21:09 | 171 | True | 0.417 | 0.000 | 0.000 | 0.000 | 0.416 | 0.415 | 0.800 |
| mlb | lineup_home | Los Angeles Dodgers | 9 players | 10-15 20:31 | 209 | False | 0.417 | 0.000 | 0.000 | 0.000 | 0.415 | 0.416 | 0.600 |
| nhl | goalie_confirmed | Vegas Golden Knights | Carter Hart | 10-15 18:36 | 444 | False | 0.255 | 0.000 | 0.000 | 0.000 | 0.258 | 0.258 | 0.732 |
| nhl | goalie_confirmed | Utah Mammoth | Karel Vejmelka | 10-15 18:31 | 388 | True | 0.475 | 0.030 | 0.040 | 0.040 | 0.487 | 0.513 | 5.406 |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-15 18:30 | -91 | True | 0.537 | -0.310 | -0.260 | -0.280 | 0.615 | 0.269 | 2.433 |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-15 18:28 | -89 | True | 0.583 | -0.355 | -0.280 | -0.315 | 0.615 | 0.269 | 4.450 |
| nhl | goalie_confirmed | Calgary Flames | Dustin Wolf | 10-15 17:57 | 482 | True | 0.255 | 0.000 | 0.000 | 0.000 | 0.258 | 0.258 | 0.155 |
| mlb | probable_away | Milwaukee Brewers | Shane Drohan | 10-15 17:55 | 365 | True | 0.417 | 0.000 | 0.000 | 0.000 | 0.415 | 0.416 | 0.967 |
| nhl | goalie_confirmed | San Jose Sharks | Alex Nedeljkovic | 10-15 16:54 | 425 | True | 0.445 | 0.000 | 0.000 | 0.000 | 0.438 | 0.441 | 0.387 |
| nhl | goalie_confirmed | Chicago Blackhawks | Spencer Knight | 10-15 16:52 | 427 | False | 0.555 | 0.000 | 0.000 | -0.010 | 0.550 | 0.550 | 0.454 |
| nhl | goalie_confirmed | Edmonton Oilers | Devon Levi | 10-15 16:45 | 494 | False | 0.475 | 0.000 | 0.000 | 0.000 | 0.488 | 0.487 | 105.428 |
| nhl | goalie_confirmed | Ottawa Senators | Linus Ullmark | 10-15 16:39 | 380 | False | 0.395 | 0.000 | 0.000 | 0.000 | 0.403 | 0.400 | 0.295 |
| nhl | goalie_likely | Winnipeg Jets | Stuart Skinner | 10-15 16:21 | 458 | True | 0.555 | 0.000 | 0.000 | 0.000 | 0.550 | 0.550 | 0.104 |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-15 16:19 | 400 | True | 0.275 | 0.000 | 0.000 | 0.000 | 0.269 | 0.272 | 0.261 |
| nhl | goalie_confirmed | New York Islanders | Semyon Varlamov | 10-15 15:55 | 424 | True | 0.395 | 0.000 | 0.000 | 0.000 | 0.417 | 0.403 | 0.324 |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-15 15:54 | 65 | True | 0.458 | 0.000 | 0.000 | 0.000 | 0.466 | 0.464 | 0.200 |
| nhl | goalie_likely | Nashville Predators | Juuse Saros | 10-15 15:53 | 486 | False | 0.445 | 0.000 | 0.000 | 0.000 | 0.438 | 0.438 | 0.472 |
| nhl | goalie_confirmed | New York Rangers | Dylan Garand | 10-15 15:43 | 437 | True | 0.445 | 0.000 | 0.000 | 0.000 | 0.441 | 0.448 | 0.610 |
| nhl | goalie_confirmed | Minnesota Wild | Jesper Wallstedt | 10-15 15:41 | 499 | False | 0.425 | 0.000 | 0.000 | 0.000 | 0.437 | 0.429 | 0.784 |
| nhl | goalie_likely | Vancouver Canucks | Leevi Merilainen | 10-15 15:30 | 449 | True | 0.275 | 0.000 | 0.000 | 0.000 | 0.269 | 0.269 | 0.265 |
| nhl | goalie_likely | New York Islanders | Ilya Sorokin | 10-15 15:30 | 450 | True | 0.415 | -0.020 | -0.020 | -0.020 | 0.417 | 0.403 | 4.750 |
| nhl | goalie_likely | Buffalo Sabres | Ukko-Pekka Luukkonen | 10-15 15:29 | 451 | True | 0.485 | 0.000 | 0.000 | 0.000 | 0.480 | 0.479 | 0.886 |
| nhl | goalie_likely | Chicago Blackhawks | Spencer Knight | 10-15 15:25 | 514 | False | 0.555 | 0.000 | 0.000 | 0.000 | 0.546 | 0.550 | 0.277 |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-15 15:00 | 120 | True | 0.453 | 0.000 | 0.000 | 0.005 | 0.451 | 0.466 | 26.000 |
| nhl | goalie_confirmed | Florida Panthers | Akira Schmid | 10-15 14:54 | 486 | False | 0.275 | 0.000 | 0.000 | 0.000 | 0.267 | 0.269 | 0.574 |
| nhl | goalie_likely | New Jersey Devils | Nico Daws | 10-15 14:53 | 487 | False | 0.445 | 0.000 | 0.000 | 0.000 | 0.428 | 0.441 | 0.909 |
| nhl | goalie_likely | Tampa Bay Lightning | Andrei Vasilevskiy | 10-15 14:50 | 489 | False | 0.295 | 0.000 | 0.000 | 0.000 | 0.301 | 0.294 | 0.449 |
| nhl | goalie_likely | Ottawa Senators | Linus Ullmark | 10-15 14:33 | 506 | False | 0.405 | 0.000 | 0.000 | 0.010 | 0.417 | 0.417 | 16.273 |
| nhl | goalie_likely | Toronto Maple Leafs | Sergei Bobrovsky | 10-15 14:32 | 507 | False | 0.485 | 0.000 | 0.000 | 0.000 | 0.480 | 0.480 | 0.370 |
| mlb | lineup_home | Cleveland Guardians | 9 players | 10-15 14:05 | 174 | False | 0.453 | 0.000 | 0.000 | 0.000 | 0.452 | 0.451 | 0.083 |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-15 14:05 | 174 | True | 0.453 | 0.000 | 0.000 | 0.000 | 0.452 | 0.451 | 0.083 |

Generated by method/analysis/report.py from the data branch.
