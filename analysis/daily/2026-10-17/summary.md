# Daily analysis 2026-10-17

## Coverage

| source | sport | rows | events | passes | window_rows | first | last |
|---|---|---|---|---|---|---|---|
| polymarket_bbo | bundesliga | 10,386 | 9 | 283 | 576 | 10-15 06:34 | 10-17 10:16 |
| polymarket_bbo | cs2 | 28,896 | 184 | 1,594 | 7,020 | 10-14 19:27 | 10-17 10:19 |
| polymarket_bbo | epl | 9,107 | 9 | 185 | 180 | 10-15 23:32 | 10-17 10:19 |
| polymarket_bbo | laliga | 8,435 | 9 | 280 | 576 | 10-15 07:34 | 10-17 10:16 |
| polymarket_bbo | ligue1 | 7,452 | 9 | 281 | 576 | 10-15 06:55 | 10-17 10:16 |
| polymarket_bbo | lol | 985 | 7 | 538 | 252 | 10-14 19:27 | 10-17 10:16 |
| polymarket_bbo | mlb | 14,084 | 5 | 498 | 3,556 | 10-14 19:27 | 10-17 10:16 |
| polymarket_bbo | nba | 7,840 | 21 | 654 | 3,188 | 10-14 19:27 | 10-17 04:55 |
| polymarket_bbo | nfl | 2,632 | 12 | 144 | 0 | 10-14 19:27 | 10-17 10:16 |
| polymarket_bbo | nhl | 46,067 | 30 | 650 | 3,687 | 10-14 19:27 | 10-17 10:16 |
| polymarket_bbo | seriea | 7,293 | 8 | 281 | 576 | 10-15 06:55 | 10-17 10:16 |
| pinnacle | mlb | 822 | 5 | 137 |  | 10-14 21:29 | 10-17 05:55 |
| pinnacle | nba | 8,632 | 12 | 180 |  | 10-14 21:29 | 10-17 09:53 |
| pinnacle | nfl | 5,226 | 14 | 97 |  | 10-14 21:29 | 10-17 09:53 |
| pinnacle | nhl | 7,798 | 27 | 174 |  | 10-14 21:29 | 10-17 09:53 |
| polymarket_history | bundesliga | 19 | 19 | 20,539 |  | NaT | NaT |
| polymarket_history | cs2 | 223 | 205 | 192,245 |  | NaT | NaT |
| polymarket_history | laliga | 18 | 18 | 19,458 |  | NaT | NaT |
| polymarket_history | ligue1 | 18 | 18 | 19,458 |  | NaT | NaT |
| polymarket_history | lol | 6 | 5 | 6,175 |  | NaT | NaT |
| polymarket_history | mlb | 150 | 93 | 162,150 |  | NaT | NaT |
| polymarket_history | nba | 323 | 323 | 338,334 |  | NaT | NaT |
| polymarket_history | nfl | 23 | 23 | 24,863 |  | NaT | NaT |
| polymarket_history | nhl | 319 | 319 | 344,839 |  | NaT | NaT |
| polymarket_history | seriea | 16 | 16 | 17,296 |  | NaT | NaT |
| news_mlb | mlb | 122 |  |  |  | NaT | NaT |
| news_nhl | nhl | 121 |  |  |  | NaT | NaT |
| news_nhl_schedule | nhl | 141 |  |  |  | NaT | NaT |

Odds API quota at last pass: used 1154.0, remaining 18846.0 (214 Pinnacle passes recorded).

## Event matching (Polymarket US vs Pinnacle)

303 Polymarket events, 58 Pinnacle events, 43 matched (16 by full name, 27 by nickname).

Unmatched Polymarket events (260): bundesliga Eintracht Frankfurt vs. 1. FC Koln; bundesliga 1. FC Union Berlin vs. BV Borussia 09 Dortmund; bundesliga Hamburger SV vs. VfB Stuttgart; bundesliga SV Werder Bremen vs. SC Paderborn 07; bundesliga FC Schalke 04 vs. 1. FSV Mainz 05; bundesliga SV 07 Elversberg vs. FC Augsburg; bundesliga FC Bayern Munchen vs. RB Leipzig; bundesliga Bayer 04 Leverkusen vs. SC Freiburg; bundesliga Borussia Monchengladbach vs. TSG 1899 Hoffenheim; cs2  Phantom Academy vs. ZOTIX; cs2 FURIA vs. BetBoom Team; cs2 Pandaric eSports vs. BIG Academy; cs2 WBT vs. Esport Academy Copenhagen; cs2 ENCE vs. BOJONG; cs2 Heroic vs. Envy

## Polymarket mid vs Pinnacle fair, main winner contracts

mid_minus_fair > 0 means Polymarket prices the team higher than Pinnacle's de-vigged price. taker_edge_at_ask = fair − ask − fee: what a taker would expect if Pinnacle were exactly right.

| sport | bucket | n | mean_diff | mean_abs_diff | within_1c | within_2c | mean_spread | median_bid_shares | taker_edge_mean | taker_edge_pos_share |
|---|---|---|---|---|---|---|---|---|---|---|
| mlb | 0-15 min | 19 | 0.016 | 0.032 | 53% | 63% | 0.005 | 700,000 | -0.033 | 11% |
| mlb | 15-60 min | 23 | -0.003 | 0.003 | 100% | 100% | 0.005 | 4,000,000 | -0.017 | 0% |
| mlb | 1-3 h | 20 | -0.001 | 0.002 | 95% | 100% | 0.005 | 3,900,000 | -0.018 | 0% |
| mlb | 3-12 h | 25 | 0.002 | 0.002 | 100% | 100% | 0.005 | 2,500,000 | -0.021 | 0% |
| mlb | 12 h+ | 134 | -0.206 | 0.212 | 2% | 25% | 0.066 | 100 | 0.160 | 67% |
| nhl | 0-15 min | 390 | -0.030 | 0.078 | 35% | 47% | 0.034 | 57,000 | -0.001 | 29% |
| nhl | 15-60 min | 224 | -0.055 | 0.057 | 53% | 58% | 0.011 | 425,000 | 0.033 | 42% |
| nhl | 1-3 h | 386 | -0.060 | 0.063 | 52% | 54% | 0.010 | 390,000 | 0.039 | 46% |
| nhl | 3-12 h | 532 | -0.085 | 0.087 | 34% | 36% | 0.051 | 31,000 | 0.043 | 58% |
| nhl | 12 h+ | 5,386 | -0.118 | 0.120 | 19% | 22% | 0.104 | 29,000 | 0.050 | 69% |

Largest gaps seen:

| sport | team | pin_ts | minutes_to_start | fair | pm_mid | pm_spread | mid_minus_fair | taker_edge_at_ask |
|---|---|---|---|---|---|---|---|---|
| nhl | Ducks | 10-17 03:24 | -85 | 0.680 | 0.030 | 0.020 | -0.650 | 0.638 |
| nhl | Avalanche | 10-17 01:26 | -32 | 0.630 | 0.020 | 0.020 | -0.610 | 0.598 |
| nhl | Penguins | 10-17 02:24 | -84 | 0.552 | 0.045 | 0.070 | -0.507 | 0.467 |
| nhl | Lightning | 10-16 16:59 | 1,620 | 0.769 | 0.295 | 0.530 | -0.474 | 0.192 |
| nhl | Avalanche | 10-17 03:24 | -145 | 0.946 | 0.475 | 0.010 | -0.471 | 0.448 |
| nhl | Avalanche | 10-17 02:24 | -84 | 0.448 | 0.910 | 0.120 | 0.462 | -0.524 |
| nhl | Lightning | 10-16 16:59 | 1,620 | 0.769 | 0.310 | 0.560 | -0.459 | 0.163 |
| nhl | Lightning | 10-16 18:00 | 1,559 | 0.769 | 0.310 | 0.560 | -0.459 | 0.163 |
| nhl | Lightning | 10-16 17:30 | 1,590 | 0.769 | 0.315 | 0.550 | -0.454 | 0.163 |
| nhl | Lightning | 10-16 19:04 | 1,495 | 0.771 | 0.325 | 0.510 | -0.446 | 0.174 |
| nhl | Lightning | 10-16 18:28 | 1,532 | 0.769 | 0.325 | 0.510 | -0.444 | 0.172 |
| nhl | Penguins | 10-17 01:26 | -32 | 0.370 | 0.810 | 0.100 | 0.440 | -0.498 |

## Test (b): calibration of last pre-game mids (settled games)

| sport | n | mean_mid | win_rate | brier_pm | log_loss_pm | slope | slope_se | intercept | n_with_pinnacle | brier_pm_matched | brier_pinnacle |
|---|---|---|---|---|---|---|---|---|---|---|---|
| bundesliga | 9 | 0.336 | 0.333 |  |  |  |  |  |  |  |  |
| cs2 | 169 | 0.554 | 0.509 | 0.200 | 0.585 | 1.336 | 0.267 | -0.292 |  |  |  |
| laliga | 9 | 0.335 | 0.333 |  |  |  |  |  |  |  |  |
| ligue1 | 9 | 0.336 | 0.333 |  |  |  |  |  |  |  |  |
| lol | 5 | 0.721 | 0.600 |  |  |  |  |  |  |  |  |
| mlb | 3 | 0.419 | 0.667 |  |  |  |  |  |  |  |  |
| nba | 21 | 0.396 | 0.381 |  |  |  |  |  |  |  |  |
| nhl | 39 | 0.370 | 0.333 | 0.189 | 0.562 | 2.784 | 1.076 | 0.638 | 31 | 0.218 | 0.211 |
| seriea | 9 | 0.333 | 0.333 |  |  |  |  |  |  |  |  |

273 settled main winner contracts so far; calibration is reported from 30 per sport.

## Test (a): news events and price reaction

60 news events recorded; 253 joined to a Polymarket contract with a price path.

| sport | kind | n |
|---|---|---|
| mlb | lineup_away | 9 |
| mlb | lineup_home | 3 |
| mlb | probable_away | 3 |
| mlb | probable_home | 2 |
| nhl | goalie_confirmed | 31 |
| nhl | goalie_likely | 12 |

Most recent joined events:

| sport | kind | team | detail | news_ts | minutes_to_start | contract_is_news_team | mid_before | move_plus5 | move_plus15 | move_plus30 | pin_fair_before | pin_fair_after | minutes_to_within_1c |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mlb | probable_away | Tampa Bay Rays | Nick Martinez | 10-17 01:24 | 1,355 | True | 0.195 | 0.000 | 0.000 | 0.000 |  | 0.520 |  |
| mlb | probable_home | Cleveland Guardians | Shawn Armstrong | 10-17 01:24 | 1,355 | False | 0.635 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | probable_home | Cleveland Guardians | Shawn Armstrong | 10-17 01:24 | 1,355 | True | 0.115 | 0.000 | 0.000 | 0.000 |  | 0.480 |  |
| mlb | probable_home | Cleveland Guardians | Shawn Armstrong | 10-17 01:24 | 1,355 | False | 0.175 | 0.000 | 0.000 | 0.000 |  | 0.520 |  |
| mlb | probable_home | Cleveland Guardians | Shawn Armstrong | 10-17 01:24 | 1,355 | False | 0.665 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | probable_home | Cleveland Guardians | Shawn Armstrong | 10-17 01:24 | 1,355 | True | 0.185 | 0.000 | 0.000 | 0.000 |  | 0.480 |  |
| mlb | probable_home | Cleveland Guardians | Shawn Armstrong | 10-17 01:24 | 1,355 | False | 0.140 | 0.000 | 0.000 | 0.000 |  | 0.520 |  |
| mlb | probable_home | Cleveland Guardians | Shawn Armstrong | 10-17 01:24 | 1,355 | True | 0.185 | 0.000 | 0.000 | 0.000 |  | 0.480 |  |
| mlb | probable_home | Cleveland Guardians | Shawn Armstrong | 10-17 01:24 | 1,355 | False | 0.185 | 0.000 | 0.000 | 0.000 |  | 0.520 |  |
| mlb | probable_home | Cleveland Guardians | Shawn Armstrong | 10-17 01:24 | 1,355 | False | 0.650 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | probable_home | Cleveland Guardians | Shawn Armstrong | 10-17 01:24 | 1,355 | True | 0.195 | 0.000 | 0.000 | 0.000 |  | 0.480 |  |
| mlb | probable_home | Cleveland Guardians | Shawn Armstrong | 10-17 01:24 | 1,355 | False | 0.185 | 0.000 | 0.000 | 0.000 |  | 0.520 |  |
| mlb | probable_home | Cleveland Guardians | Shawn Armstrong | 10-17 01:24 | 1,355 | False | 0.645 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | probable_home | Cleveland Guardians | Shawn Armstrong | 10-17 01:24 | 1,355 | True | 0.180 | 0.000 | 0.000 | 0.005 |  | 0.480 |  |
| mlb | probable_home | Cleveland Guardians | Shawn Armstrong | 10-17 01:24 | 1,355 | False | 0.185 | 0.000 | 0.000 | 0.000 |  | 0.520 |  |
| mlb | probable_home | Cleveland Guardians | Shawn Armstrong | 10-17 01:24 | 1,355 | True | 0.195 | 0.000 | 0.000 | 0.000 |  | 0.480 |  |
| mlb | probable_home | Cleveland Guardians | Shawn Armstrong | 10-17 01:24 | 1,355 | False | 0.195 | 0.000 | 0.000 | 0.000 |  | 0.520 |  |
| mlb | probable_home | Cleveland Guardians | Shawn Armstrong | 10-17 01:24 | 1,355 | False | 0.205 | 0.000 | 0.000 | 0.000 |  | 0.520 |  |
| mlb | probable_home | Cleveland Guardians | Shawn Armstrong | 10-17 01:24 | 1,355 | False | 0.615 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | probable_home | Cleveland Guardians | Shawn Armstrong | 10-17 01:24 | 1,355 | True | 0.205 | 0.000 | 0.000 | 0.000 |  | 0.480 |  |
| mlb | probable_home | Cleveland Guardians | Shawn Armstrong | 10-17 01:24 | 1,355 | False | 0.175 | 0.000 | 0.000 | 0.000 |  | 0.520 |  |
| mlb | probable_home | Cleveland Guardians | Shawn Armstrong | 10-17 01:24 | 1,355 | False | 0.655 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | probable_home | Cleveland Guardians | Shawn Armstrong | 10-17 01:24 | 1,355 | True | 0.185 | 0.000 | 0.000 | 0.000 |  | 0.480 |  |
| mlb | probable_home | Cleveland Guardians | Shawn Armstrong | 10-17 01:24 | 1,355 | False | 0.195 | 0.000 | -0.085 | -0.085 |  | 0.520 |  |
| mlb | probable_home | Cleveland Guardians | Shawn Armstrong | 10-17 01:24 | 1,355 | False | 0.455 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | probable_home | Cleveland Guardians | Shawn Armstrong | 10-17 01:24 | 1,355 | True | 0.185 | 0.000 | 0.275 | 0.270 |  | 0.480 |  |
| mlb | probable_home | Cleveland Guardians | Shawn Armstrong | 10-17 01:24 | 1,355 | False | 0.405 | 0.010 | 0.040 | 0.000 |  | 0.520 |  |
| mlb | probable_home | Cleveland Guardians | Shawn Armstrong | 10-17 01:24 | 1,355 | False | 0.195 | 0.000 | 0.000 | 0.005 |  |  |  |
| mlb | probable_home | Cleveland Guardians | Shawn Armstrong | 10-17 01:24 | 1,355 | True | 0.395 | 0.000 | -0.025 | -0.020 |  | 0.480 |  |
| mlb | probable_home | Cleveland Guardians | Shawn Armstrong | 10-17 01:24 | 1,355 | False | 0.512 | 0.000 | 0.000 | 0.000 |  | 0.520 | 0.083 |
| mlb | probable_home | Cleveland Guardians | Shawn Armstrong | 10-17 01:24 | 1,355 | False | 0.685 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | probable_home | Cleveland Guardians | Shawn Armstrong | 10-17 01:24 | 1,355 | False | 0.675 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | probable_away | Tampa Bay Rays | Nick Martinez | 10-17 01:24 | 1,355 | True | 0.512 | 0.000 | 0.000 | 0.000 |  | 0.520 | 0.083 |
| mlb | probable_away | Tampa Bay Rays | Nick Martinez | 10-17 01:24 | 1,355 | True | 0.185 | 0.000 | 0.000 | 0.000 |  | 0.520 |  |
| mlb | probable_away | Tampa Bay Rays | Nick Martinez | 10-17 01:24 | 1,355 | False | 0.685 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | probable_away | Tampa Bay Rays | Nick Martinez | 10-17 01:24 | 1,355 | False | 0.115 | 0.000 | 0.000 | 0.000 |  | 0.480 |  |
| mlb | probable_away | Tampa Bay Rays | Nick Martinez | 10-17 01:24 | 1,355 | True | 0.175 | 0.000 | 0.000 | 0.000 |  | 0.520 |  |
| mlb | probable_away | Tampa Bay Rays | Nick Martinez | 10-17 01:24 | 1,355 | False | 0.665 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | probable_away | Tampa Bay Rays | Nick Martinez | 10-17 01:24 | 1,355 | False | 0.185 | 0.000 | 0.000 | 0.000 |  | 0.480 |  |
| mlb | probable_away | Tampa Bay Rays | Nick Martinez | 10-17 01:24 | 1,355 | True | 0.140 | 0.000 | 0.000 | 0.000 |  | 0.520 |  |

Generated by method/analysis/report.py from the data branch.
