# Daily analysis 2026-11-02

## Coverage

| source | sport | rows | events | passes | window_rows | first | last |
|---|---|---|---|---|---|---|---|
| polymarket_bbo | bundesliga | 57,234 | 27 | 1,586 | 11,304 | 10-15 06:34 | 11-01 18:22 |
| polymarket_bbo | cs2 | 279,829 | 797 | 8,326 | 73,250 | 10-14 19:27 | 11-02 10:18 |
| polymarket_bbo | epl | 66,683 | 30 | 1,724 | 11,928 | 10-15 23:32 | 11-02 10:15 |
| polymarket_bbo | laliga | 68,435 | 31 | 2,452 | 13,392 | 10-15 07:34 | 11-02 10:15 |
| polymarket_bbo | ligue1 | 62,532 | 27 | 1,810 | 11,772 | 10-15 06:55 | 11-02 10:15 |
| polymarket_bbo | lol | 6,162 | 43 | 2,560 | 1,389 | 10-14 19:27 | 11-02 10:15 |
| polymarket_bbo | mlb | 77,669 | 11 | 1,682 | 16,580 | 10-14 19:27 | 10-29 03:01 |
| polymarket_bbo | nba | 266,878 | 128 | 3,136 | 87,881 | 10-14 19:27 | 11-02 10:15 |
| polymarket_bbo | ncaab | 24,778 | 121 | 269 | 295 | 10-31 02:38 | 11-02 10:18 |
| polymarket_bbo | nfl | 63,483 | 42 | 1,895 | 11,788 | 10-14 19:27 | 11-02 10:15 |
| polymarket_bbo | nhl | 449,267 | 130 | 3,902 | 79,917 | 10-14 19:27 | 11-02 10:15 |
| polymarket_bbo | seriea | 84,681 | 40 | 2,565 | 15,972 | 10-15 06:55 | 11-02 10:15 |
| pinnacle | mlb | 2,522 | 12 | 564 |  | 10-14 21:29 | 10-29 02:39 |
| pinnacle | nba | 39,388 | 107 | 997 |  | 10-14 21:29 | 11-02 09:51 |
| pinnacle | ncaab | 3,390 | 72 | 65 |  | 10-31 15:59 | 11-02 10:15 |
| pinnacle | nfl | 36,784 | 50 | 761 |  | 10-14 21:29 | 11-02 09:51 |
| pinnacle | nhl | 43,382 | 130 | 1,114 |  | 10-14 21:29 | 11-02 09:51 |
| polymarket_history | bundesliga | 500 | 500 | 540,500 |  | NaT | NaT |
| polymarket_history | cs2 | 2,660 | 2,589 | 2,232,054 |  | NaT | NaT |
| polymarket_history | epl | 522 | 522 | 564,282 |  | NaT | NaT |
| polymarket_history | laliga | 541 | 541 | 584,821 |  | NaT | NaT |
| polymarket_history | ligue1 | 518 | 494 | 559,958 |  | NaT | NaT |
| polymarket_history | lol | 42 | 42 | 45,402 |  | NaT | NaT |
| polymarket_history | mlb | 640 | 580 | 691,840 |  | NaT | NaT |
| polymarket_history | nba | 7,608 | 7,608 | 7,192,184 |  | NaT | NaT |
| polymarket_history | ncaab | 52 | 25 | 47,590 |  | NaT | NaT |
| polymarket_history | nfl | 1,587 | 1,587 | 1,715,547 |  | NaT | NaT |
| polymarket_history | nhl | 4,315 | 4,315 | 4,664,515 |  | NaT | NaT |
| polymarket_history | seriea | 695 | 695 | 750,925 |  | NaT | NaT |
| news_mlb | mlb | 703 |  |  |  | NaT | NaT |
| news_nhl | nhl | 843 |  |  |  | NaT | NaT |
| news_nhl_schedule | nhl | 933 |  |  |  | NaT | NaT |

Odds API quota at last pass: used 676.0, remaining 19324.0 (1333 Pinnacle passes recorded).

## Event matching (Polymarket US vs Pinnacle)

1427 Polymarket events, 371 Pinnacle events, 290 matched (117 by full name, 173 by nickname).

Unmatched Polymarket events (1137): bundesliga Eintracht Frankfurt vs. 1. FC Koln; bundesliga 1. FC Union Berlin vs. BV Borussia 09 Dortmund; bundesliga Hamburger SV vs. VfB Stuttgart; bundesliga SV Werder Bremen vs. SC Paderborn 07; bundesliga FC Schalke 04 vs. 1. FSV Mainz 05; bundesliga SV 07 Elversberg vs. FC Augsburg; bundesliga FC Bayern Munchen vs. RB Leipzig; bundesliga Bayer 04 Leverkusen vs. SC Freiburg; bundesliga Borussia Monchengladbach vs. TSG 1899 Hoffenheim; bundesliga VfB Stuttgart vs. Borussia Monchengladbach; bundesliga RB Leipzig vs. SV 07 Elversberg; bundesliga FC Augsburg vs. 1. FC Union Berlin; bundesliga 1. FSV Mainz 05 vs. SV Werder Bremen; bundesliga 1. FC Koln vs. FC Schalke 04; bundesliga SC Paderborn 07 vs. Hamburger SV

## Polymarket mid vs Pinnacle fair, main winner contracts

mid_minus_fair > 0 means Polymarket prices the team higher than Pinnacle's de-vigged price. taker_edge_at_ask = fair − ask − fee: what a taker would expect if Pinnacle were exactly right.

| sport | bucket | n | mean_diff | mean_abs_diff | within_1c | within_2c | mean_spread | median_bid_shares | taker_edge_mean | taker_edge_pos_share |
|---|---|---|---|---|---|---|---|---|---|---|
| mlb | 0-15 min | 762 | -0.254 | 0.271 | 6% | 7% | 0.021 | 6,000 | 0.233 | 85% |
| mlb | 15-60 min | 1,115 | -0.270 | 0.270 | 7% | 7% | 0.010 | 48,000 | 0.253 | 93% |
| mlb | 1-3 h | 1,091 | -0.272 | 0.272 | 6% | 7% | 0.010 | 29,000 | 0.255 | 93% |
| mlb | 3-12 h | 1,852 | -0.274 | 0.274 | 6% | 6% | 0.047 | 26,000 | 0.238 | 92% |
| mlb | 12 h+ | 2,150 | -0.255 | 0.257 | 4% | 6% | 0.140 | 20,000 | 0.172 | 83% |
| nba | 0-15 min | 10,545 | -0.025 | 0.161 | 7% | 11% | 0.268 | 26,000 | -0.122 | 31% |
| nba | 15-60 min | 5,713 | -0.036 | 0.098 | 13% | 20% | 0.265 | 26,000 | -0.111 | 27% |
| nba | 1-3 h | 10,880 | -0.054 | 0.121 | 13% | 21% | 0.363 | 26,000 | -0.140 | 22% |
| nba | 3-12 h | 15,191 | -0.057 | 0.119 | 15% | 22% | 0.402 | 26,000 | -0.157 | 17% |
| nba | 12 h+ | 2,438 | -0.005 | 0.018 | 72% | 91% | 0.059 | 360,000 | -0.040 | 1% |
| nhl | 0-15 min | 11,056 | -0.111 | 0.149 | 9% | 13% | 0.085 | 28,000 | 0.054 | 63% |
| nhl | 15-60 min | 5,786 | -0.120 | 0.121 | 11% | 14% | 0.018 | 32,000 | 0.095 | 86% |
| nhl | 1-3 h | 10,610 | -0.120 | 0.121 | 12% | 14% | 0.018 | 32,000 | 0.095 | 86% |
| nhl | 3-12 h | 20,233 | -0.122 | 0.123 | 10% | 13% | 0.066 | 30,000 | 0.073 | 81% |
| nhl | 12 h+ | 36,139 | -0.138 | 0.139 | 12% | 13% | 0.163 | 29,000 | 0.040 | 70% |

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
| nhl | Stars | 11-01 01:09 | -74 | 0.885 | 0.015 | 0.010 | -0.870 | 0.864 |
| nhl | Stars | 11-01 01:01 | -62 | 0.885 | 0.015 | 0.010 | -0.870 | 0.864 |
| nba | Pacers | 10-24 01:18 | -139 | 0.101 | 0.965 | 0.050 | 0.864 | -0.890 |
| nba | Mavericks | 10-24 01:25 | -151 | 0.899 | 0.045 | 0.050 | -0.854 | 0.825 |
| nba | Pacers | 10-24 01:25 | -151 | 0.101 | 0.950 | 0.080 | 0.849 | -0.890 |

## Test (b): calibration of last pre-game mids (settled games)

| sport | n | mean_mid | win_rate | brier_pm | log_loss_pm | slope | slope_se | intercept | n_with_pinnacle | brier_pm_matched | brier_pinnacle |
|---|---|---|---|---|---|---|---|---|---|---|---|
| bundesliga | 243 | 0.341 | 0.333 | 0.219 | 0.628 | 0.588 | 0.212 | -0.294 |  |  |  |
| cs2 | 1,842 | 0.529 | 0.545 | 0.224 | 0.637 | 0.877 | 0.077 | 0.082 |  |  |  |
| epl | 261 | 0.335 | 0.333 | 0.207 | 0.601 | 1.007 | 0.249 | -0.002 |  |  |  |
| laliga | 270 | 0.339 | 0.333 | 0.199 | 0.580 | 0.947 | 0.187 | -0.063 |  |  |  |
| ligue1 | 243 | 0.341 | 0.333 | 0.188 | 0.552 | 1.422 | 0.280 | 0.217 |  |  |  |
| lol | 42 | 0.577 | 0.452 | 0.238 | 0.669 | 0.729 | 0.338 | -0.494 |  |  |  |
| mlb | 251 | 0.346 | 0.343 | 0.197 | 0.583 | 0.812 | 0.150 | -0.122 | 171 | 0.174 | 0.245 |
| nba | 1,617 | 0.339 | 0.332 | 0.181 | 0.527 | 0.943 | 0.064 | -0.058 | 1,062 | 0.241 | 0.244 |
| ncaab | 2 | 0.765 | 0.500 |  |  |  |  |  |  |  |  |
| nhl | 1,482 | 0.346 | 0.339 | 0.215 | 0.621 | 1.016 | 0.137 | -0.025 | 1,030 | 0.223 | 0.239 |
| seriea | 342 | 0.349 | 0.333 | 0.199 | 0.583 | 1.136 | 0.201 | -0.002 |  |  |  |

6595 settled main winner contracts so far; calibration is reported from 30 per sport.

## Test (a): news events and price reaction

394 news events recorded; 5543 joined to a Polymarket contract with a price path.

| sport | kind | n |
|---|---|---|
| mlb | lineup_away | 23 |
| mlb | lineup_home | 13 |
| mlb | probable_away | 8 |
| mlb | probable_home | 6 |
| nhl | goalie_confirmed | 251 |
| nhl | goalie_likely | 92 |
| nhl | goalie_unknown | 1 |

Most recent joined events:

| sport | kind | team | detail | news_ts | minutes_to_start | contract_is_news_team | mid_before | move_plus5 | move_plus15 | move_plus30 | pin_fair_before | pin_fair_after | minutes_to_within_1c |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| nhl | goalie_confirmed | Ottawa Senators | Jonas Johansson | 11-01 23:48 | 72 | True | 0.325 | 0.000 | 0.000 | 0.055 | 0.528 | 0.528 | 166.750 |
| nhl | goalie_confirmed | Ottawa Senators | Jonas Johansson | 11-01 23:48 | 72 | True | 0.395 | 0.000 | 0.000 | 0.000 | 0.528 | 0.528 |  |
| nhl | goalie_confirmed | Ottawa Senators | Jonas Johansson | 11-01 23:48 | 72 | True | 0.535 | 0.000 | 0.000 | 0.000 | 0.528 | 0.528 | 0.750 |
| nhl | goalie_confirmed | Ottawa Senators | Jonas Johansson | 11-01 23:48 | 72 | False | 0.315 | 0.000 | 0.000 | 0.000 | 0.472 | 0.472 |  |
| nhl | goalie_confirmed | Ottawa Senators | Jonas Johansson | 11-01 23:48 | 72 | False | 0.325 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Ottawa Senators | Jonas Johansson | 11-01 23:48 | 72 | True | 0.375 | 0.000 | 0.000 | 0.000 | 0.528 | 0.528 |  |
| nhl | goalie_confirmed | Ottawa Senators | Jonas Johansson | 11-01 23:48 | 72 | False | 0.325 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Ottawa Senators | Jonas Johansson | 11-01 23:48 | 72 | False | 0.315 | 0.000 | 0.000 | 0.000 | 0.472 | 0.472 |  |
| nhl | goalie_confirmed | Ottawa Senators | Jonas Johansson | 11-01 23:48 | 72 | False | 0.385 | 0.000 | 0.000 | 0.000 | 0.472 | 0.472 |  |
| nhl | goalie_confirmed | Ottawa Senators | Jonas Johansson | 11-01 23:48 | 72 | False | 0.235 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Ottawa Senators | Jonas Johansson | 11-01 23:48 | 72 | True | 0.385 | 0.000 | 0.000 | 0.000 | 0.528 | 0.528 |  |
| nhl | goalie_confirmed | Ottawa Senators | Jonas Johansson | 11-01 23:48 | 72 | False | 0.405 | 0.000 | 0.000 | -0.055 | 0.472 | 0.472 |  |
| nhl | goalie_confirmed | Ottawa Senators | Jonas Johansson | 11-01 23:48 | 72 | False | 0.225 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Utah Mammoth | Karel Vejmelka | 11-01 20:31 | 28 | True | 0.395 | 0.000 | 0.000 | 0.000 | 0.605 | 0.597 |  |
| nhl | goalie_confirmed | Utah Mammoth | Karel Vejmelka | 11-01 20:31 | 28 | True | 0.615 | 0.000 | 0.000 | -0.010 | 0.605 | 0.597 | 30.452 |
| nhl | goalie_confirmed | Utah Mammoth | Karel Vejmelka | 11-01 20:31 | 28 | False | 0.365 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Utah Mammoth | Karel Vejmelka | 11-01 20:31 | 28 | False | 0.295 | 0.000 | 0.000 | 0.000 | 0.395 | 0.403 |  |
| nhl | goalie_confirmed | Utah Mammoth | Karel Vejmelka | 11-01 20:31 | 28 | False | 0.325 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Utah Mammoth | Karel Vejmelka | 11-01 20:31 | 28 | False | 0.295 | 0.000 | 0.000 | 0.000 | 0.395 | 0.403 |  |
| nhl | goalie_confirmed | Utah Mammoth | Karel Vejmelka | 11-01 20:31 | 28 | True | 0.395 | 0.000 | 0.000 | 0.000 | 0.605 | 0.597 |  |
| nhl | goalie_confirmed | Utah Mammoth | Karel Vejmelka | 11-01 20:31 | 28 | False | 0.245 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Utah Mammoth | Karel Vejmelka | 11-01 20:31 | 28 | False | 0.335 | 0.000 | 0.000 | 0.000 | 0.395 | 0.403 | 134.452 |
| nhl | goalie_confirmed | Utah Mammoth | Karel Vejmelka | 11-01 20:31 | 28 | True | 0.445 | 0.000 | 0.000 | 0.000 | 0.605 | 0.597 |  |
| nhl | goalie_confirmed | Utah Mammoth | Karel Vejmelka | 11-01 20:31 | 28 | False | 0.190 | 0.015 | 0.065 | -0.025 |  |  |  |
| nhl | goalie_confirmed | Utah Mammoth | Karel Vejmelka | 11-01 20:31 | 28 | False | 0.195 | 0.010 | 0.080 | 0.010 | 0.395 | 0.403 |  |
| nhl | goalie_confirmed | Utah Mammoth | Karel Vejmelka | 11-01 20:31 | 28 | True | 0.530 | 0.000 | 0.025 | 0.020 | 0.605 | 0.597 | 47.452 |
| nhl | goalie_confirmed | Philadelphia Flyers | Dan Vladar | 11-01 18:46 | 134 | False | 0.615 | 0.000 | 0.000 | 0.000 | 0.620 | 0.620 | 0.650 |
| nhl | goalie_confirmed | Philadelphia Flyers | Dan Vladar | 11-01 18:46 | 134 | False | 0.365 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Philadelphia Flyers | Dan Vladar | 11-01 18:46 | 134 | True | 0.295 | 0.000 | 0.000 | 0.000 | 0.380 | 0.380 |  |
| nhl | goalie_confirmed | Philadelphia Flyers | Dan Vladar | 11-01 18:46 | 134 | False | 0.365 | 0.000 | 0.000 | 0.020 | 0.620 | 0.620 |  |
| nhl | goalie_confirmed | Philadelphia Flyers | Dan Vladar | 11-01 18:46 | 134 | False | 0.325 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Philadelphia Flyers | Dan Vladar | 11-01 18:46 | 134 | True | 0.295 | 0.000 | 0.000 | 0.000 | 0.380 | 0.380 |  |
| nhl | goalie_confirmed | Philadelphia Flyers | Dan Vladar | 11-01 18:46 | 134 | False | 0.395 | 0.000 | 0.000 | 0.000 | 0.620 | 0.620 |  |
| nhl | goalie_confirmed | Philadelphia Flyers | Dan Vladar | 11-01 18:46 | 134 | False | 0.245 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Philadelphia Flyers | Dan Vladar | 11-01 18:46 | 134 | True | 0.335 | 0.000 | 0.000 | 0.000 | 0.380 | 0.380 | 235.650 |
| nhl | goalie_confirmed | Philadelphia Flyers | Dan Vladar | 11-01 18:46 | 134 | False | 0.445 | 0.000 | 0.000 | 0.000 | 0.620 | 0.620 |  |
| nhl | goalie_confirmed | Philadelphia Flyers | Dan Vladar | 11-01 18:46 | 134 | False | 0.140 | 0.000 | 0.050 | 0.050 |  |  |  |
| nhl | goalie_confirmed | Philadelphia Flyers | Dan Vladar | 11-01 18:46 | 134 | True | 0.175 | 0.000 | 0.000 | 0.000 | 0.380 | 0.380 |  |
| nhl | goalie_confirmed | Philadelphia Flyers | Dan Vladar | 11-01 18:46 | 134 | False | 0.520 | 0.000 | -0.145 | -0.145 | 0.620 | 0.620 | 145.650 |
| nhl | goalie_confirmed | Washington Capitals | Logan Thompson | 11-01 18:41 | 108 | True | 0.325 | 0.000 | 0.000 | 0.000 | 0.491 | 0.487 |  |

Generated by method/analysis/report.py from the data branch.
