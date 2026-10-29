# Daily analysis 2026-10-29

## Coverage

| source | sport | rows | events | passes | window_rows | first | last |
|---|---|---|---|---|---|---|---|
| polymarket_bbo | bundesliga | 41,850 | 19 | 1,203 | 8,724 | 10-15 06:34 | 10-29 10:03 |
| polymarket_bbo | cs2 | 251,055 | 728 | 7,079 | 64,900 | 10-14 19:27 | 10-29 10:07 |
| polymarket_bbo | epl | 49,643 | 20 | 1,314 | 8,844 | 10-15 23:32 | 10-25 18:22 |
| polymarket_bbo | laliga | 51,203 | 22 | 1,900 | 10,416 | 10-15 07:34 | 10-29 10:03 |
| polymarket_bbo | ligue1 | 47,760 | 21 | 1,362 | 9,384 | 10-15 06:55 | 10-29 10:03 |
| polymarket_bbo | lol | 5,551 | 38 | 2,248 | 1,265 | 10-14 19:27 | 10-29 10:03 |
| polymarket_bbo | mlb | 77,669 | 11 | 1,682 | 16,580 | 10-14 19:27 | 10-29 03:01 |
| polymarket_bbo | nba | 207,581 | 92 | 2,545 | 70,259 | 10-14 19:27 | 10-29 10:03 |
| polymarket_bbo | nfl | 48,321 | 29 | 1,543 | 8,946 | 10-14 19:27 | 10-29 10:03 |
| polymarket_bbo | nhl | 370,034 | 109 | 3,240 | 64,923 | 10-14 19:27 | 10-29 10:03 |
| polymarket_bbo | seriea | 66,777 | 30 | 2,047 | 12,960 | 10-15 06:55 | 10-29 10:03 |
| pinnacle | mlb | 2,522 | 12 | 564 |  | 10-14 21:29 | 10-29 02:39 |
| pinnacle | nba | 35,018 | 71 | 822 |  | 10-14 21:29 | 10-29 09:40 |
| pinnacle | nfl | 30,166 | 42 | 622 |  | 10-14 21:29 | 10-29 09:40 |
| pinnacle | nhl | 36,696 | 108 | 918 |  | 10-14 21:29 | 10-29 09:40 |
| polymarket_history | bundesliga | 337 | 337 | 364,297 |  | NaT | NaT |
| polymarket_history | cs2 | 2,249 | 2,186 | 1,915,234 |  | NaT | NaT |
| polymarket_history | epl | 360 | 360 | 389,160 |  | NaT | NaT |
| polymarket_history | laliga | 382 | 382 | 412,942 |  | NaT | NaT |
| polymarket_history | ligue1 | 343 | 331 | 370,783 |  | NaT | NaT |
| polymarket_history | lol | 35 | 35 | 37,835 |  | NaT | NaT |
| polymarket_history | mlb | 640 | 580 | 691,840 |  | NaT | NaT |
| polymarket_history | nba | 5,514 | 5,514 | 5,100,673 |  | NaT | NaT |
| polymarket_history | nfl | 1,132 | 1,132 | 1,223,692 |  | NaT | NaT |
| polymarket_history | nhl | 3,282 | 3,282 | 3,547,842 |  | NaT | NaT |
| polymarket_history | seriea | 508 | 508 | 549,148 |  | NaT | NaT |
| news_mlb | mlb | 593 |  |  |  | NaT | NaT |
| news_nhl | nhl | 691 |  |  |  | NaT | NaT |
| news_nhl_schedule | nhl | 763 |  |  |  | NaT | NaT |

Odds API quota at last pass: used 8223.0, remaining 11777.0 (1097 Pinnacle passes recorded).

## Event matching (Polymarket US vs Pinnacle)

1119 Polymarket events, 233 Pinnacle events, 219 matched (68 by full name, 151 by nickname).

Unmatched Polymarket events (900): bundesliga Eintracht Frankfurt vs. 1. FC Koln; bundesliga 1. FC Union Berlin vs. BV Borussia 09 Dortmund; bundesliga Hamburger SV vs. VfB Stuttgart; bundesliga SV Werder Bremen vs. SC Paderborn 07; bundesliga FC Schalke 04 vs. 1. FSV Mainz 05; bundesliga SV 07 Elversberg vs. FC Augsburg; bundesliga FC Bayern Munchen vs. RB Leipzig; bundesliga Bayer 04 Leverkusen vs. SC Freiburg; bundesliga Borussia Monchengladbach vs. TSG 1899 Hoffenheim; bundesliga VfB Stuttgart vs. Borussia Monchengladbach; bundesliga RB Leipzig vs. SV 07 Elversberg; bundesliga FC Augsburg vs. 1. FC Union Berlin; bundesliga 1. FSV Mainz 05 vs. SV Werder Bremen; bundesliga 1. FC Koln vs. FC Schalke 04; bundesliga SC Paderborn 07 vs. Hamburger SV

## Polymarket mid vs Pinnacle fair, main winner contracts

mid_minus_fair > 0 means Polymarket prices the team higher than Pinnacle's de-vigged price. taker_edge_at_ask = fair − ask − fee: what a taker would expect if Pinnacle were exactly right.

| sport | bucket | n | mean_diff | mean_abs_diff | within_1c | within_2c | mean_spread | median_bid_shares | taker_edge_mean | taker_edge_pos_share |
|---|---|---|---|---|---|---|---|---|---|---|
| mlb | 0-15 min | 762 | -0.254 | 0.271 | 6% | 7% | 0.021 | 6,000 | 0.233 | 85% |
| mlb | 15-60 min | 1,115 | -0.270 | 0.270 | 7% | 7% | 0.010 | 48,000 | 0.253 | 93% |
| mlb | 1-3 h | 1,091 | -0.272 | 0.272 | 6% | 7% | 0.010 | 29,000 | 0.255 | 93% |
| mlb | 3-12 h | 1,852 | -0.274 | 0.274 | 6% | 6% | 0.047 | 26,000 | 0.238 | 92% |
| mlb | 12 h+ | 2,150 | -0.255 | 0.257 | 4% | 6% | 0.140 | 20,000 | 0.172 | 83% |
| nba | 0-15 min | 8,911 | -0.025 | 0.164 | 6% | 11% | 0.287 | 26,000 | -0.131 | 30% |
| nba | 15-60 min | 4,504 | -0.035 | 0.103 | 14% | 20% | 0.306 | 26,000 | -0.131 | 24% |
| nba | 1-3 h | 8,566 | -0.051 | 0.126 | 14% | 22% | 0.410 | 25,000 | -0.166 | 19% |
| nba | 3-12 h | 11,168 | -0.045 | 0.120 | 16% | 23% | 0.428 | 25,000 | -0.181 | 15% |
| nba | 12 h+ | 2,087 | -0.003 | 0.015 | 75% | 92% | 0.046 | 330,000 | -0.036 | 1% |
| nhl | 0-15 min | 9,302 | -0.109 | 0.148 | 9% | 13% | 0.087 | 28,000 | 0.051 | 62% |
| nhl | 15-60 min | 4,616 | -0.117 | 0.118 | 12% | 14% | 0.012 | 32,000 | 0.095 | 86% |
| nhl | 1-3 h | 8,666 | -0.117 | 0.117 | 12% | 14% | 0.012 | 32,000 | 0.095 | 86% |
| nhl | 3-12 h | 16,327 | -0.113 | 0.114 | 10% | 13% | 0.044 | 31,000 | 0.075 | 83% |
| nhl | 12 h+ | 30,748 | -0.131 | 0.132 | 12% | 13% | 0.144 | 29,000 | 0.043 | 71% |

Largest gaps seen:

| sport | team | pin_ts | minutes_to_start | fair | pm_mid | pm_spread | mid_minus_fair | taker_edge_at_ask |
|---|---|---|---|---|---|---|---|---|
| nhl | Panthers | 10-28 01:46 | -106 | 0.959 | 0.025 | 0.030 | -0.934 | 0.916 |
| mlb | Milwaukee Brewers | 10-24 02:58 | -179 | 0.938 | 0.025 | 0.010 | -0.913 | 0.906 |
| mlb | Tampa Bay Rays | 10-18 23:46 | -159 | 0.941 | 0.040 | 0.020 | -0.901 | 0.888 |
| nba | Mavericks | 10-24 01:18 | -139 | 0.899 | 0.020 | 0.020 | -0.879 | 0.867 |
| nba | Pacers | 10-24 01:18 | -139 | 0.101 | 0.965 | 0.050 | 0.864 | -0.890 |
| nba | Mavericks | 10-24 01:25 | -151 | 0.899 | 0.045 | 0.050 | -0.854 | 0.825 |
| nba | Pacers | 10-24 01:25 | -151 | 0.101 | 0.950 | 0.080 | 0.849 | -0.890 |
| nhl | Blue Jackets | 10-28 00:42 | -94 | 0.902 | 0.065 | 0.010 | -0.837 | 0.827 |
| nba | Pistons | 10-26 02:07 | -157 | 0.950 | 0.115 | 0.210 | -0.835 | 0.718 |
| nba | Denver Nuggets | 10-29 00:57 | -62 | 0.939 | 0.110 | 0.180 | -0.829 | 0.728 |
| nba | Raptors | 10-26 00:44 | -109 | 0.157 | 0.985 | 0.010 | 0.828 | -0.834 |
| nba | Raptors | 10-26 00:39 | -109 | 0.157 | 0.985 | 0.010 | 0.828 | -0.834 |

## Test (b): calibration of last pre-game mids (settled games)

| sport | n | mean_mid | win_rate | brier_pm | log_loss_pm | slope | slope_se | intercept | n_with_pinnacle | brier_pm_matched | brier_pinnacle |
|---|---|---|---|---|---|---|---|---|---|---|---|
| bundesliga | 162 | 0.335 | 0.333 | 0.214 | 0.615 | 0.708 | 0.254 | -0.198 |  |  |  |
| cs2 | 1,588 | 0.530 | 0.548 | 0.224 | 0.635 | 0.896 | 0.083 | 0.093 |  |  |  |
| epl | 180 | 0.337 | 0.333 | 0.204 | 0.594 | 1.006 | 0.274 | -0.014 |  |  |  |
| laliga | 189 | 0.341 | 0.333 | 0.201 | 0.585 | 1.023 | 0.249 | -0.025 |  |  |  |
| ligue1 | 162 | 0.344 | 0.333 | 0.207 | 0.601 | 1.001 | 0.307 | -0.051 |  |  |  |
| lol | 35 | 0.583 | 0.400 | 0.233 | 0.656 | 0.999 | 0.441 | -0.924 |  |  |  |
| mlb | 251 | 0.346 | 0.343 | 0.197 | 0.583 | 0.812 | 0.150 | -0.122 | 171 | 0.174 | 0.245 |
| nba | 1,161 | 0.339 | 0.331 | 0.184 | 0.534 | 0.907 | 0.074 | -0.081 | 750 | 0.243 | 0.244 |
| nhl | 1,105 | 0.349 | 0.338 | 0.217 | 0.626 | 0.867 | 0.158 | -0.134 | 769 | 0.227 | 0.241 |
| seriea | 252 | 0.353 | 0.333 | 0.206 | 0.599 | 0.921 | 0.220 | -0.138 |  |  |  |

5085 settled main winner contracts so far; calibration is reported from 30 per sport.

## Test (a): news events and price reaction

325 news events recorded; 4633 joined to a Polymarket contract with a price path.

| sport | kind | n |
|---|---|---|
| mlb | lineup_away | 23 |
| mlb | lineup_home | 13 |
| mlb | probable_away | 8 |
| mlb | probable_home | 6 |
| nhl | goalie_confirmed | 194 |
| nhl | goalie_likely | 80 |
| nhl | goalie_unknown | 1 |

Most recent joined events:

| sport | kind | team | detail | news_ts | minutes_to_start | contract_is_news_team | mid_before | move_plus5 | move_plus15 | move_plus30 | pin_fair_before | pin_fair_after | minutes_to_within_1c |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| nhl | goalie_confirmed | Seattle Kraken | Philipp Grubauer | 10-29 01:33 | 27 | False | 0.445 | 0.000 | 0.015 | 0.015 | 0.540 | 0.543 |  |
| nhl | goalie_confirmed | Seattle Kraken | Philipp Grubauer | 10-29 01:33 | 27 | False | 0.355 | 0.000 | 0.000 | 0.000 | 0.540 | 0.543 |  |
| nhl | goalie_confirmed | Seattle Kraken | Philipp Grubauer | 10-29 01:33 | 27 | False | 0.545 | 0.000 | 0.000 | 0.000 | 0.540 | 0.543 | 0.683 |
| nhl | goalie_confirmed | Seattle Kraken | Philipp Grubauer | 10-29 01:33 | 27 | False | 0.295 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Seattle Kraken | Philipp Grubauer | 10-29 01:33 | 27 | True | 0.355 | 0.000 | 0.000 | 0.000 | 0.460 | 0.457 | 39.683 |
| nhl | goalie_confirmed | Seattle Kraken | Philipp Grubauer | 10-29 01:33 | 27 | False | 0.305 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Seattle Kraken | Philipp Grubauer | 10-29 01:33 | 27 | True | 0.305 | 0.000 | 0.000 | 0.000 | 0.460 | 0.457 |  |
| nhl | goalie_confirmed | Seattle Kraken | Philipp Grubauer | 10-29 01:33 | 27 | False | 0.365 | 0.000 | 0.000 | 0.000 | 0.540 | 0.543 |  |
| nhl | goalie_confirmed | Seattle Kraken | Philipp Grubauer | 10-29 01:33 | 27 | False | 0.255 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Seattle Kraken | Philipp Grubauer | 10-29 01:33 | 27 | True | 0.325 | 0.000 | 0.000 | 0.000 | 0.460 | 0.457 | 147.683 |
| nhl | goalie_confirmed | Seattle Kraken | Philipp Grubauer | 10-29 01:33 | 27 | False | 0.415 | 0.000 | 0.000 | 0.000 | 0.540 | 0.543 | 179.683 |
| nhl | goalie_confirmed | Seattle Kraken | Philipp Grubauer | 10-29 01:33 | 27 | False | 0.225 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Seattle Kraken | Philipp Grubauer | 10-29 01:33 | 27 | True | 0.365 | -0.005 | -0.005 | -0.005 | 0.460 | 0.457 | 54.683 |
| nhl | goalie_confirmed | Washington Capitals | Logan Thompson | 10-28 23:02 | 28 | True | 0.425 | 0.000 | 0.000 | 0.000 | 0.690 | 0.695 |  |
| nhl | goalie_confirmed | Washington Capitals | Logan Thompson | 10-28 23:02 | 28 | False | 0.305 | 0.000 | 0.000 | 0.000 | 0.310 | 0.305 | 0.771 |
| nhl | goalie_confirmed | Washington Capitals | Logan Thompson | 10-28 23:02 | 28 | False | 0.355 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Washington Capitals | Logan Thompson | 10-28 23:02 | 28 | False | 0.255 | 0.000 | 0.000 | 0.000 | 0.310 | 0.305 |  |
| nhl | goalie_confirmed | Washington Capitals | Logan Thompson | 10-28 23:02 | 28 | True | 0.405 | 0.000 | 0.000 | 0.015 | 0.690 | 0.695 | 37.771 |
| nhl | goalie_confirmed | Washington Capitals | Logan Thompson | 10-28 23:02 | 28 | False | 0.325 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Washington Capitals | Logan Thompson | 10-28 23:02 | 28 | False | 0.285 | 0.000 | 0.000 | 0.000 | 0.310 | 0.305 | 111.771 |
| nhl | goalie_confirmed | Washington Capitals | Logan Thompson | 10-28 23:02 | 28 | False | 0.205 | 0.000 | 0.000 | -0.065 |  |  |  |
| nhl | goalie_confirmed | Washington Capitals | Logan Thompson | 10-28 23:02 | 28 | False | 0.275 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Washington Capitals | Logan Thompson | 10-28 23:02 | 28 | False | 0.285 | -0.020 | -0.020 | -0.020 | 0.310 | 0.305 |  |
| nhl | goalie_confirmed | Washington Capitals | Logan Thompson | 10-28 23:02 | 28 | True | 0.495 | 0.000 | 0.000 | 0.000 | 0.690 | 0.695 |  |
| nhl | goalie_confirmed | Washington Capitals | Logan Thompson | 10-28 23:02 | 28 | False | 0.240 | -0.005 | -0.005 | -0.005 | 0.310 | 0.305 |  |
| nhl | goalie_confirmed | Washington Capitals | Logan Thompson | 10-28 23:02 | 28 | True | 0.585 | 0.000 | -0.005 | -0.005 | 0.690 | 0.695 | 118.771 |
| nhl | goalie_confirmed | Philadelphia Flyers | Joseph Woll | 10-28 21:52 | 98 | False | 0.425 | 0.000 | 0.000 | 0.000 | 0.686 | 0.685 |  |
| nhl | goalie_confirmed | Philadelphia Flyers | Joseph Woll | 10-28 21:52 | 98 | True | 0.315 | 0.000 | 0.000 | 0.000 | 0.314 | 0.315 | 0.541 |
| nhl | goalie_confirmed | Philadelphia Flyers | Joseph Woll | 10-28 21:52 | 98 | False | 0.355 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Philadelphia Flyers | Joseph Woll | 10-28 21:52 | 98 | True | 0.255 | 0.000 | 0.000 | 0.000 | 0.314 | 0.315 |  |
| nhl | goalie_confirmed | Philadelphia Flyers | Joseph Woll | 10-28 21:52 | 98 | False | 0.405 | 0.000 | 0.000 | 0.000 | 0.686 | 0.685 | 107.541 |
| nhl | goalie_confirmed | Philadelphia Flyers | Joseph Woll | 10-28 21:52 | 98 | False | 0.325 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Philadelphia Flyers | Joseph Woll | 10-28 21:52 | 98 | True | 0.285 | 0.000 | 0.000 | 0.000 | 0.314 | 0.315 | 181.541 |
| nhl | goalie_confirmed | Philadelphia Flyers | Joseph Woll | 10-28 21:52 | 98 | False | 0.595 | 0.000 | -0.005 | -0.005 | 0.686 | 0.685 | 187.541 |
| nhl | goalie_confirmed | Philadelphia Flyers | Joseph Woll | 10-28 21:52 | 98 | False | 0.275 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Philadelphia Flyers | Joseph Woll | 10-28 21:52 | 98 | False | 0.495 | 0.000 | 0.000 | 0.000 | 0.686 | 0.685 |  |
| nhl | goalie_confirmed | Philadelphia Flyers | Joseph Woll | 10-28 21:52 | 98 | False | 0.205 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Philadelphia Flyers | Joseph Woll | 10-28 21:52 | 98 | True | 0.240 | 0.000 | 0.000 | 0.000 | 0.314 | 0.315 |  |
| nhl | goalie_confirmed | Philadelphia Flyers | Joseph Woll | 10-28 21:52 | 98 | True | 0.285 | 0.000 | 0.000 | 0.000 | 0.314 | 0.315 |  |
| mlb | lineup_away | Milwaukee Brewers | 9 players | 10-28 20:31 | 209 | False | 0.625 | 0.000 | 0.000 | 0.000 |  |  |  |

Generated by method/analysis/report.py from the data branch.
