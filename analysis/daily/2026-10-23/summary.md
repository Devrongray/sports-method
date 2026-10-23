# Daily analysis 2026-10-23

## Coverage

| source | sport | rows | events | passes | window_rows | first | last |
|---|---|---|---|---|---|---|---|
| polymarket_bbo | bundesliga | 23,886 | 16 | 740 | 4,644 | 10-15 06:34 | 10-23 10:26 |
| polymarket_bbo | cs2 | 174,158 | 589 | 4,709 | 44,645 | 10-14 19:27 | 10-23 10:26 |
| polymarket_bbo | epl | 27,947 | 15 | 824 | 4,728 | 10-15 23:32 | 10-23 10:26 |
| polymarket_bbo | laliga | 28,667 | 16 | 1,139 | 5,616 | 10-15 07:34 | 10-23 10:26 |
| polymarket_bbo | ligue1 | 25,620 | 11 | 815 | 5,184 | 10-15 06:55 | 10-23 10:26 |
| polymarket_bbo | lol | 2,204 | 17 | 1,050 | 358 | 10-14 19:27 | 10-23 10:26 |
| polymarket_bbo | mlb | 45,738 | 7 | 1,056 | 10,244 | 10-14 19:27 | 10-23 10:26 |
| polymarket_bbo | nba | 50,515 | 50 | 1,309 | 15,879 | 10-14 19:27 | 10-23 10:26 |
| polymarket_bbo | nfl | 26,390 | 15 | 929 | 5,103 | 10-14 19:27 | 10-23 03:14 |
| polymarket_bbo | nhl | 216,986 | 64 | 2,047 | 40,941 | 10-14 19:27 | 10-23 10:26 |
| polymarket_bbo | seriea | 28,641 | 15 | 1,099 | 5,724 | 10-15 06:55 | 10-23 10:26 |
| pinnacle | mlb | 1,686 | 8 | 354 |  | 10-14 21:29 | 10-23 10:01 |
| pinnacle | nba | 22,988 | 28 | 458 |  | 10-14 21:29 | 10-23 10:01 |
| pinnacle | nfl | 18,860 | 28 | 377 |  | 10-14 21:29 | 10-23 10:01 |
| pinnacle | nhl | 22,916 | 62 | 566 |  | 10-14 21:29 | 10-23 10:01 |
| polymarket_history | bundesliga | 163 | 163 | 176,203 |  | NaT | NaT |
| polymarket_history | cs2 | 1,546 | 1,480 | 1,280,201 |  | NaT | NaT |
| polymarket_history | epl | 180 | 180 | 194,580 |  | NaT | NaT |
| polymarket_history | laliga | 197 | 197 | 212,957 |  | NaT | NaT |
| polymarket_history | ligue1 | 167 | 167 | 180,527 |  | NaT | NaT |
| polymarket_history | lol | 9 | 9 | 9,729 |  | NaT | NaT |
| polymarket_history | mlb | 339 | 279 | 366,459 |  | NaT | NaT |
| polymarket_history | nba | 1,354 | 1,354 | 1,222,266 |  | NaT | NaT |
| polymarket_history | nfl | 595 | 595 | 643,195 |  | NaT | NaT |
| polymarket_history | nhl | 1,961 | 1,961 | 2,119,841 |  | NaT | NaT |
| polymarket_history | seriea | 175 | 175 | 189,175 |  | NaT | NaT |
| news_mlb | mlb | 375 |  |  |  | NaT | NaT |
| news_nhl | nhl | 429 |  |  |  | NaT | NaT |
| news_nhl_schedule | nhl | 479 |  |  |  | NaT | NaT |

Odds API quota at last pass: used 4393.0, remaining 15607.0 (670 Pinnacle passes recorded).

## Event matching (Polymarket US vs Pinnacle)

815 Polymarket events, 126 Pinnacle events, 112 matched (22 by full name, 90 by nickname).

Unmatched Polymarket events (703): bundesliga Eintracht Frankfurt vs. 1. FC Koln; bundesliga 1. FC Union Berlin vs. BV Borussia 09 Dortmund; bundesliga Hamburger SV vs. VfB Stuttgart; bundesliga SV Werder Bremen vs. SC Paderborn 07; bundesliga FC Schalke 04 vs. 1. FSV Mainz 05; bundesliga SV 07 Elversberg vs. FC Augsburg; bundesliga FC Bayern Munchen vs. RB Leipzig; bundesliga Bayer 04 Leverkusen vs. SC Freiburg; bundesliga Borussia Monchengladbach vs. TSG 1899 Hoffenheim; bundesliga VfB Stuttgart vs. Borussia Monchengladbach; bundesliga RB Leipzig vs. SV 07 Elversberg; bundesliga FC Augsburg vs. 1. FC Union Berlin; bundesliga 1. FSV Mainz 05 vs. SV Werder Bremen; bundesliga 1. FC Koln vs. FC Schalke 04; bundesliga SC Paderborn 07 vs. Hamburger SV

## Polymarket mid vs Pinnacle fair, main winner contracts

mid_minus_fair > 0 means Polymarket prices the team higher than Pinnacle's de-vigged price. taker_edge_at_ask = fair − ask − fee: what a taker would expect if Pinnacle were exactly right.

| sport | bucket | n | mean_diff | mean_abs_diff | within_1c | within_2c | mean_spread | median_bid_shares | taker_edge_mean | taker_edge_pos_share |
|---|---|---|---|---|---|---|---|---|---|---|
| mlb | 0-15 min | 340 | -0.247 | 0.267 | 9% | 10% | 0.023 | 5,800 | 0.225 | 79% |
| mlb | 15-60 min | 506 | -0.267 | 0.267 | 9% | 9% | 0.010 | 29,000 | 0.251 | 91% |
| mlb | 1-3 h | 524 | -0.270 | 0.270 | 8% | 8% | 0.010 | 25,000 | 0.253 | 92% |
| mlb | 3-12 h | 718 | -0.270 | 0.270 | 8% | 8% | 0.047 | 24,000 | 0.234 | 88% |
| mlb | 12 h+ | 995 | -0.240 | 0.243 | 4% | 8% | 0.211 | 26,000 | 0.120 | 71% |
| nba | 0-15 min | 1,833 | -0.017 | 0.148 | 5% | 10% | 0.555 | 1,500 | -0.269 | 16% |
| nba | 15-60 min | 708 | -0.029 | 0.098 | 13% | 19% | 0.519 | 510 | -0.240 | 11% |
| nba | 1-3 h | 1,013 | -0.039 | 0.114 | 12% | 17% | 0.568 | 450 | -0.254 | 8% |
| nba | 3-12 h | 731 | -0.023 | 0.074 | 30% | 39% | 0.210 | 26,000 | -0.097 | 17% |
| nba | 12 h+ | 1,396 | 0.001 | 0.007 | 83% | 98% | 0.013 | 270,000 | -0.024 | 0% |
| nhl | 0-15 min | 6,014 | -0.107 | 0.144 | 10% | 14% | 0.090 | 28,000 | 0.048 | 61% |
| nhl | 15-60 min | 2,753 | -0.115 | 0.115 | 13% | 16% | 0.012 | 32,000 | 0.093 | 84% |
| nhl | 1-3 h | 5,489 | -0.116 | 0.117 | 12% | 15% | 0.012 | 32,000 | 0.094 | 85% |
| nhl | 3-12 h | 9,145 | -0.112 | 0.113 | 11% | 14% | 0.045 | 31,000 | 0.073 | 82% |
| nhl | 12 h+ | 16,096 | -0.123 | 0.125 | 13% | 15% | 0.123 | 29,000 | 0.046 | 71% |

Largest gaps seen:

| sport | team | pin_ts | minutes_to_start | fair | pm_mid | pm_spread | mid_minus_fair | taker_edge_at_ask |
|---|---|---|---|---|---|---|---|---|
| mlb | Tampa Bay Rays | 10-18 23:46 | -159 | 0.941 | 0.040 | 0.020 | -0.901 | 0.888 |
| nba | Cavaliers | 10-23 00:36 | -97 | 0.940 | 0.115 | 0.030 | -0.825 | 0.802 |
| nba | Cavaliers | 10-23 00:31 | -97 | 0.940 | 0.115 | 0.030 | -0.825 | 0.802 |
| nhl | Kings | 10-23 01:15 | -105 | 0.848 | 0.025 | 0.030 | -0.823 | 0.805 |
| nhl | Kings | 10-23 01:22 | -105 | 0.848 | 0.025 | 0.030 | -0.823 | 0.805 |
| nba | Cavaliers | 10-23 00:31 | -97 | 0.940 | 0.120 | 0.020 | -0.820 | 0.802 |
| nba | Cavaliers | 10-23 00:36 | -97 | 0.940 | 0.120 | 0.020 | -0.820 | 0.802 |
| mlb | Tampa Bay Rays | 10-20 01:12 | -64 | 0.881 | 0.075 | 0.010 | -0.806 | 0.796 |
| nba | 76ers | 10-23 00:31 | -97 | 0.060 | 0.865 | 0.050 | 0.805 | -0.837 |
| nba | 76ers | 10-23 00:36 | -97 | 0.060 | 0.865 | 0.050 | 0.805 | -0.837 |
| nhl | Oilers | 10-21 03:31 | -151 | 0.924 | 0.125 | 0.190 | -0.799 | 0.692 |
| nhl | Sharks | 10-23 01:22 | -147 | 0.964 | 0.165 | 0.010 | -0.799 | 0.784 |

## Test (b): calibration of last pre-game mids (settled games)

| sport | n | mean_mid | win_rate | brier_pm | log_loss_pm | slope | slope_se | intercept | n_with_pinnacle | brier_pm_matched | brier_pinnacle |
|---|---|---|---|---|---|---|---|---|---|---|---|
| bundesliga | 81 | 0.334 | 0.333 | 0.200 | 0.583 | 1.137 | 0.415 | 0.084 |  |  |  |
| cs2 | 1,111 | 0.530 | 0.562 | 0.221 | 0.630 | 0.963 | 0.102 | 0.147 |  |  |  |
| epl | 90 | 0.338 | 0.333 | 0.187 | 0.554 | 1.358 | 0.389 | 0.192 |  |  |  |
| laliga | 99 | 0.346 | 0.333 | 0.190 | 0.560 | 1.313 | 0.367 | 0.114 |  |  |  |
| ligue1 | 81 | 0.342 | 0.333 | 0.206 | 0.601 | 1.071 | 0.465 | 0.001 |  |  |  |
| lol | 9 | 0.704 | 0.667 |  |  |  |  |  |  |  |  |
| mlb | 96 | 0.348 | 0.354 | 0.214 | 0.617 | 0.660 | 0.233 | -0.163 | 66 | 0.191 | 0.242 |
| nba | 255 | 0.394 | 0.329 | 0.204 | 0.583 | 0.997 | 0.240 | -0.316 | 156 | 0.240 | 0.218 |
| nhl | 624 | 0.348 | 0.332 | 0.220 | 0.632 | 0.592 | 0.199 | -0.324 | 436 | 0.228 | 0.247 |
| seriea | 90 | 0.353 | 0.333 | 0.227 | 0.652 | 0.308 | 0.373 | -0.497 |  |  |  |

2536 settled main winner contracts so far; calibration is reported from 30 per sport.

## Test (a): news events and price reaction

205 news events recorded; 2731 joined to a Polymarket contract with a price path.

| sport | kind | n |
|---|---|---|
| mlb | lineup_away | 14 |
| mlb | lineup_home | 8 |
| mlb | probable_away | 6 |
| mlb | probable_home | 4 |
| nhl | goalie_confirmed | 119 |
| nhl | goalie_likely | 54 |

Most recent joined events:

| sport | kind | team | detail | news_ts | minutes_to_start | contract_is_news_team | mid_before | move_plus5 | move_plus15 | move_plus30 | pin_fair_before | pin_fair_after | minutes_to_within_1c |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| nhl | goalie_confirmed | Seattle Kraken | Philipp Grubauer | 10-23 01:35 | 25 | False | 0.550 | 0.000 | 0.000 | 0.070 | 0.620 | 0.628 | 25.624 |
| nhl | goalie_confirmed | Seattle Kraken | Philipp Grubauer | 10-23 01:35 | 25 | False | 0.415 | 0.000 | 0.000 | 0.000 | 0.620 | 0.628 |  |
| nhl | goalie_confirmed | Seattle Kraken | Philipp Grubauer | 10-23 01:35 | 25 | False | 0.635 | 0.000 | 0.000 | 0.000 | 0.620 | 0.628 | 0.624 |
| nhl | goalie_confirmed | Seattle Kraken | Philipp Grubauer | 10-23 01:35 | 25 | False | 0.325 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Seattle Kraken | Philipp Grubauer | 10-23 01:35 | 25 | True | 0.305 | 0.000 | 0.000 | 0.000 | 0.380 | 0.372 | 38.624 |
| nhl | goalie_confirmed | Seattle Kraken | Philipp Grubauer | 10-23 01:35 | 25 | False | 0.395 | 0.000 | 0.000 | 0.000 | 0.620 | 0.628 |  |
| nhl | goalie_confirmed | Seattle Kraken | Philipp Grubauer | 10-23 01:35 | 25 | True | 0.255 | 0.000 | 0.000 | 0.000 | 0.380 | 0.372 |  |
| nhl | goalie_confirmed | Seattle Kraken | Philipp Grubauer | 10-23 01:35 | 25 | False | 0.335 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Seattle Kraken | Philipp Grubauer | 10-23 01:35 | 25 | False | 0.245 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Seattle Kraken | Philipp Grubauer | 10-23 01:35 | 25 | True | 0.295 | 0.000 | 0.000 | 0.000 | 0.380 | 0.372 | 125.624 |
| nhl | goalie_confirmed | Seattle Kraken | Philipp Grubauer | 10-23 01:35 | 25 | False | 0.465 | 0.000 | 0.000 | 0.000 | 0.620 | 0.628 | 154.624 |
| nhl | goalie_confirmed | Seattle Kraken | Philipp Grubauer | 10-23 01:35 | 25 | False | 0.195 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Seattle Kraken | Philipp Grubauer | 10-23 01:35 | 25 | True | 0.275 | 0.000 | 0.000 | 0.000 | 0.380 | 0.372 | 39.624 |
| nhl | goalie_confirmed | Detroit Red Wings | John Gibson | 10-23 01:31 | 28 | False | 0.275 | 0.000 | 0.000 | 0.000 | 0.387 | 0.387 |  |
| nhl | goalie_confirmed | Detroit Red Wings | John Gibson | 10-23 01:31 | 28 | True | 0.615 | 0.000 | 0.000 | 0.000 | 0.613 | 0.613 | 0.422 |
| nhl | goalie_confirmed | Detroit Red Wings | John Gibson | 10-23 01:31 | 28 | True | 0.385 | 0.000 | 0.000 | 0.000 | 0.613 | 0.613 |  |
| nhl | goalie_confirmed | Detroit Red Wings | John Gibson | 10-23 01:31 | 28 | False | 0.355 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Detroit Red Wings | John Gibson | 10-23 01:31 | 28 | True | 0.385 | 0.000 | 0.000 | 0.000 | 0.613 | 0.613 |  |
| nhl | goalie_confirmed | Detroit Red Wings | John Gibson | 10-23 01:31 | 28 | False | 0.325 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Detroit Red Wings | John Gibson | 10-23 01:31 | 28 | False | 0.275 | 0.000 | 0.000 | 0.000 | 0.387 | 0.387 |  |
| nhl | goalie_confirmed | Detroit Red Wings | John Gibson | 10-23 01:31 | 28 | True | 0.415 | 0.000 | 0.000 | 0.000 | 0.613 | 0.613 |  |
| nhl | goalie_confirmed | Detroit Red Wings | John Gibson | 10-23 01:31 | 28 | False | 0.265 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Detroit Red Wings | John Gibson | 10-23 01:31 | 28 | False | 0.325 | 0.000 | 0.000 | 0.000 | 0.387 | 0.387 |  |
| nhl | goalie_confirmed | Detroit Red Wings | John Gibson | 10-23 01:31 | 28 | True | 0.465 | 0.000 | 0.000 | 0.000 | 0.613 | 0.613 | 41.422 |
| nhl | goalie_confirmed | Detroit Red Wings | John Gibson | 10-23 01:31 | 28 | False | 0.205 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Detroit Red Wings | John Gibson | 10-23 01:31 | 28 | False | 0.330 | 0.000 | -0.045 | -0.035 | 0.387 | 0.387 |  |
| nhl | goalie_confirmed | Utah Mammoth | Karel Vejmelka | 10-23 01:31 | 29 | True | 0.635 | 0.000 | 0.000 | 0.000 | 0.620 | 0.620 | 38.962 |
| nhl | goalie_confirmed | Utah Mammoth | Karel Vejmelka | 10-23 01:31 | 29 | False | 0.325 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Utah Mammoth | Karel Vejmelka | 10-23 01:31 | 29 | False | 0.305 | 0.000 | 0.000 | 0.000 | 0.380 | 0.380 | 42.962 |
| nhl | goalie_confirmed | Utah Mammoth | Karel Vejmelka | 10-23 01:31 | 29 | True | 0.395 | 0.000 | 0.000 | 0.000 | 0.620 | 0.620 |  |
| nhl | goalie_confirmed | Utah Mammoth | Karel Vejmelka | 10-23 01:31 | 29 | False | 0.335 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Utah Mammoth | Karel Vejmelka | 10-23 01:31 | 29 | False | 0.255 | 0.000 | 0.000 | 0.000 | 0.380 | 0.380 |  |
| nhl | goalie_confirmed | Utah Mammoth | Karel Vejmelka | 10-23 01:31 | 29 | True | 0.415 | 0.000 | 0.000 | 0.000 | 0.620 | 0.620 |  |
| nhl | goalie_confirmed | Utah Mammoth | Karel Vejmelka | 10-23 01:31 | 29 | False | 0.245 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Utah Mammoth | Karel Vejmelka | 10-23 01:31 | 29 | False | 0.295 | 0.000 | 0.000 | 0.000 | 0.380 | 0.380 | 129.962 |
| nhl | goalie_confirmed | Utah Mammoth | Karel Vejmelka | 10-23 01:31 | 29 | True | 0.465 | 0.000 | 0.000 | 0.000 | 0.620 | 0.620 | 158.962 |
| nhl | goalie_confirmed | Utah Mammoth | Karel Vejmelka | 10-23 01:31 | 29 | False | 0.195 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Utah Mammoth | Karel Vejmelka | 10-23 01:31 | 29 | False | 0.275 | 0.000 | 0.000 | 0.000 | 0.380 | 0.380 | 43.962 |
| nhl | goalie_confirmed | Utah Mammoth | Karel Vejmelka | 10-23 01:31 | 29 | True | 0.550 | 0.000 | 0.000 | 0.070 | 0.620 | 0.620 | 29.962 |
| nhl | goalie_confirmed | Vancouver Canucks | Kevin Lankinen | 10-23 01:30 | 29 | True | 0.275 | 0.000 | 0.000 | 0.000 | 0.387 | 0.387 |  |

Generated by method/analysis/report.py from the data branch.
