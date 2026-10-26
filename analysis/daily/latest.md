# Daily analysis 2026-10-26

## Coverage

| source | sport | rows | events | passes | window_rows | first | last |
|---|---|---|---|---|---|---|---|
| polymarket_bbo | bundesliga | 41,742 | 18 | 1,194 | 8,724 | 10-15 06:34 | 10-25 18:22 |
| polymarket_bbo | cs2 | 225,114 | 663 | 6,132 | 57,684 | 10-14 19:27 | 10-26 09:39 |
| polymarket_bbo | epl | 49,643 | 20 | 1,314 | 8,844 | 10-15 23:32 | 10-25 18:22 |
| polymarket_bbo | laliga | 50,531 | 21 | 1,844 | 10,200 | 10-15 07:34 | 10-26 09:33 |
| polymarket_bbo | ligue1 | 46,704 | 18 | 1,293 | 9,048 | 10-15 06:55 | 10-26 09:33 |
| polymarket_bbo | lol | 4,912 | 33 | 1,937 | 1,130 | 10-14 19:27 | 10-26 09:33 |
| polymarket_bbo | mlb | 64,027 | 9 | 1,415 | 13,588 | 10-14 19:27 | 10-26 09:33 |
| polymarket_bbo | nba | 146,305 | 73 | 2,088 | 49,667 | 10-14 19:27 | 10-26 09:33 |
| polymarket_bbo | nfl | 47,229 | 28 | 1,387 | 8,708 | 10-14 19:27 | 10-26 09:33 |
| polymarket_bbo | nhl | 304,430 | 82 | 2,810 | 56,061 | 10-14 19:27 | 10-26 09:33 |
| polymarket_bbo | seriea | 51,777 | 23 | 1,726 | 10,644 | 10-15 06:55 | 10-26 09:33 |
| pinnacle | mlb | 2,206 | 10 | 484 |  | 10-14 21:29 | 10-26 09:12 |
| pinnacle | nba | 30,668 | 52 | 685 |  | 10-14 21:29 | 10-26 09:12 |
| pinnacle | nfl | 26,034 | 38 | 539 |  | 10-14 21:29 | 10-26 09:12 |
| pinnacle | nhl | 31,110 | 82 | 789 |  | 10-14 21:29 | 10-26 09:12 |
| polymarket_history | bundesliga | 337 | 337 | 364,297 |  | NaT | NaT |
| polymarket_history | cs2 | 1,961 | 1,904 | 1,652,034 |  | NaT | NaT |
| polymarket_history | epl | 360 | 360 | 389,160 |  | NaT | NaT |
| polymarket_history | laliga | 366 | 366 | 395,646 |  | NaT | NaT |
| polymarket_history | ligue1 | 325 | 313 | 351,325 |  | NaT | NaT |
| polymarket_history | lol | 29 | 29 | 31,349 |  | NaT | NaT |
| polymarket_history | mlb | 457 | 397 | 494,017 |  | NaT | NaT |
| polymarket_history | nba | 3,613 | 3,613 | 3,151,153 |  | NaT | NaT |
| polymarket_history | nfl | 1,099 | 1,099 | 1,188,019 |  | NaT | NaT |
| polymarket_history | nhl | 2,657 | 2,657 | 2,872,217 |  | NaT | NaT |
| polymarket_history | seriea | 362 | 362 | 391,322 |  | NaT | NaT |
| news_mlb | mlb | 509 |  |  |  | NaT | NaT |
| news_nhl | nhl | 591 |  |  |  | NaT | NaT |
| news_nhl_schedule | nhl | 652 |  |  |  | NaT | NaT |

Odds API quota at last pass: used 6714.0, remaining 13286.0 (957 Pinnacle passes recorded).

## Event matching (Polymarket US vs Pinnacle)

988 Polymarket events, 182 Pinnacle events, 171 matched (37 by full name, 134 by nickname).

Unmatched Polymarket events (817): bundesliga Eintracht Frankfurt vs. 1. FC Koln; bundesliga 1. FC Union Berlin vs. BV Borussia 09 Dortmund; bundesliga Hamburger SV vs. VfB Stuttgart; bundesliga SV Werder Bremen vs. SC Paderborn 07; bundesliga FC Schalke 04 vs. 1. FSV Mainz 05; bundesliga SV 07 Elversberg vs. FC Augsburg; bundesliga FC Bayern Munchen vs. RB Leipzig; bundesliga Bayer 04 Leverkusen vs. SC Freiburg; bundesliga Borussia Monchengladbach vs. TSG 1899 Hoffenheim; bundesliga VfB Stuttgart vs. Borussia Monchengladbach; bundesliga RB Leipzig vs. SV 07 Elversberg; bundesliga FC Augsburg vs. 1. FC Union Berlin; bundesliga 1. FSV Mainz 05 vs. SV Werder Bremen; bundesliga 1. FC Koln vs. FC Schalke 04; bundesliga SC Paderborn 07 vs. Hamburger SV

## Polymarket mid vs Pinnacle fair, main winner contracts

mid_minus_fair > 0 means Polymarket prices the team higher than Pinnacle's de-vigged price. taker_edge_at_ask = fair − ask − fee: what a taker would expect if Pinnacle were exactly right.

| sport | bucket | n | mean_diff | mean_abs_diff | within_1c | within_2c | mean_spread | median_bid_shares | taker_edge_mean | taker_edge_pos_share |
|---|---|---|---|---|---|---|---|---|---|---|
| mlb | 0-15 min | 557 | -0.253 | 0.272 | 6% | 8% | 0.022 | 5,800 | 0.231 | 83% |
| mlb | 15-60 min | 779 | -0.270 | 0.271 | 8% | 8% | 0.010 | 29,000 | 0.254 | 92% |
| mlb | 1-3 h | 818 | -0.272 | 0.273 | 7% | 7% | 0.010 | 28,000 | 0.256 | 93% |
| mlb | 3-12 h | 1,327 | -0.272 | 0.273 | 6% | 7% | 0.050 | 26,000 | 0.235 | 91% |
| mlb | 12 h+ | 1,961 | -0.253 | 0.254 | 4% | 7% | 0.147 | 15,000 | 0.165 | 83% |
| nba | 0-15 min | 6,002 | -0.024 | 0.162 | 7% | 11% | 0.353 | 26,000 | -0.164 | 26% |
| nba | 15-60 min | 2,918 | -0.040 | 0.115 | 15% | 21% | 0.429 | 25,000 | -0.186 | 16% |
| nba | 1-3 h | 6,135 | -0.051 | 0.136 | 15% | 23% | 0.512 | 1,500 | -0.216 | 13% |
| nba | 3-12 h | 8,050 | -0.036 | 0.122 | 18% | 26% | 0.474 | 1,550 | -0.212 | 13% |
| nba | 12 h+ | 1,815 | -0.000 | 0.013 | 78% | 94% | 0.035 | 300,000 | -0.033 | 1% |
| nhl | 0-15 min | 8,060 | -0.108 | 0.147 | 9% | 14% | 0.090 | 28,000 | 0.049 | 61% |
| nhl | 15-60 min | 3,815 | -0.116 | 0.116 | 12% | 15% | 0.012 | 32,000 | 0.094 | 85% |
| nhl | 1-3 h | 7,271 | -0.117 | 0.117 | 12% | 14% | 0.012 | 32,000 | 0.095 | 85% |
| nhl | 3-12 h | 14,671 | -0.113 | 0.114 | 11% | 13% | 0.045 | 31,000 | 0.075 | 82% |
| nhl | 12 h+ | 23,602 | -0.126 | 0.127 | 12% | 14% | 0.134 | 29,000 | 0.042 | 70% |

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
| nba | Cavaliers | 10-23 00:31 | -97 | 0.940 | 0.115 | 0.030 | -0.825 | 0.802 |
| nba | Cavaliers | 10-23 00:36 | -97 | 0.940 | 0.115 | 0.030 | -0.825 | 0.802 |
| nhl | Kings | 10-23 01:15 | -105 | 0.848 | 0.025 | 0.030 | -0.823 | 0.805 |

## Test (b): calibration of last pre-game mids (settled games)

| sport | n | mean_mid | win_rate | brier_pm | log_loss_pm | slope | slope_se | intercept | n_with_pinnacle | brier_pm_matched | brier_pinnacle |
|---|---|---|---|---|---|---|---|---|---|---|---|
| bundesliga | 162 | 0.335 | 0.333 | 0.214 | 0.615 | 0.708 | 0.254 | -0.198 |  |  |  |
| cs2 | 1,411 | 0.530 | 0.565 | 0.221 | 0.629 | 0.963 | 0.092 | 0.160 |  |  |  |
| epl | 180 | 0.337 | 0.333 | 0.204 | 0.594 | 1.006 | 0.274 | -0.014 |  |  |  |
| laliga | 180 | 0.341 | 0.333 | 0.203 | 0.589 | 0.967 | 0.250 | -0.060 |  |  |  |
| ligue1 | 153 | 0.344 | 0.333 | 0.212 | 0.612 | 0.898 | 0.332 | -0.115 |  |  |  |
| lol | 29 | 0.574 | 0.379 |  |  |  |  |  |  |  |  |
| mlb | 158 | 0.346 | 0.342 | 0.204 | 0.595 | 0.736 | 0.185 | -0.172 | 108 | 0.183 | 0.244 |
| nba | 686 | 0.340 | 0.324 | 0.182 | 0.529 | 0.978 | 0.106 | -0.097 | 425 | 0.244 | 0.237 |
| nhl | 871 | 0.349 | 0.334 | 0.218 | 0.628 | 0.729 | 0.171 | -0.234 | 607 | 0.227 | 0.245 |
| seriea | 180 | 0.358 | 0.333 | 0.209 | 0.607 | 0.877 | 0.271 | -0.185 |  |  |  |

4010 settled main winner contracts so far; calibration is reported from 30 per sport.

## Test (a): news events and price reaction

264 news events recorded; 3673 joined to a Polymarket contract with a price path.

| sport | kind | n |
|---|---|---|
| mlb | lineup_away | 20 |
| mlb | lineup_home | 10 |
| mlb | probable_away | 6 |
| mlb | probable_home | 4 |
| nhl | goalie_confirmed | 157 |
| nhl | goalie_likely | 67 |

Most recent joined events:

| sport | kind | team | detail | news_ts | minutes_to_start | contract_is_news_team | mid_before | move_plus5 | move_plus15 | move_plus30 | pin_fair_before | pin_fair_after | minutes_to_within_1c |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-26 01:38 | 21 | True | 0.255 | 0.000 | 0.000 | -0.060 | 0.350 | 0.350 |  |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-26 01:38 | 21 | True | 0.305 | 0.000 | 0.000 | 0.000 | 0.350 | 0.350 | 87.084 |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-26 01:38 | 21 | False | 0.645 | 0.000 | 0.000 | 0.010 | 0.650 | 0.650 | 0.084 |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-26 01:38 | 21 | False | 0.355 | 0.000 | 0.000 | -0.020 |  |  |  |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-26 01:38 | 21 | False | 0.375 | 0.000 | 0.000 | 0.035 | 0.650 | 0.650 |  |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-26 01:38 | 21 | False | 0.265 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-26 01:38 | 21 | False | 0.465 | 0.000 | 0.000 | 0.000 | 0.650 | 0.650 |  |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-26 01:38 | 21 | True | 0.305 | 0.000 | 0.000 | 0.000 | 0.350 | 0.350 |  |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-26 01:38 | 21 | False | 0.265 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-26 01:38 | 21 | False | 0.465 | 0.000 | 0.000 | 0.000 | 0.650 | 0.650 | 143.084 |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-26 01:38 | 21 | True | 0.275 | 0.000 | 0.000 | 0.000 | 0.350 | 0.350 |  |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-26 01:38 | 21 | False | 0.215 | 0.000 | 0.000 | -0.070 |  |  |  |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-26 01:38 | 21 | False | 0.555 | 0.000 | 0.040 | 0.150 | 0.650 | 0.650 |  |
| nhl | goalie_confirmed | Colorado Avalanche | Scott Wedgewood | 10-25 23:30 | 30 | False | 0.295 | 0.000 | 0.000 | 0.000 | 0.314 | 0.309 | 96.550 |
| nhl | goalie_confirmed | Colorado Avalanche | Scott Wedgewood | 10-25 23:30 | 30 | True | 0.685 | 0.000 | 0.000 | 0.000 | 0.686 | 0.691 | 0.550 |
| nhl | goalie_confirmed | Colorado Avalanche | Scott Wedgewood | 10-25 23:30 | 30 | True | 0.410 | -0.015 | -0.005 | -0.005 | 0.686 | 0.691 |  |
| nhl | goalie_confirmed | Colorado Avalanche | Scott Wedgewood | 10-25 23:30 | 30 | False | 0.345 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Colorado Avalanche | Scott Wedgewood | 10-25 23:30 | 30 | False | 0.295 | 0.000 | 0.000 | -0.050 | 0.314 | 0.309 |  |
| nhl | goalie_confirmed | Colorado Avalanche | Scott Wedgewood | 10-25 23:30 | 30 | True | 0.425 | 0.000 | 0.000 | 0.000 | 0.686 | 0.691 |  |
| nhl | goalie_confirmed | Colorado Avalanche | Scott Wedgewood | 10-25 23:30 | 30 | False | 0.315 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Colorado Avalanche | Scott Wedgewood | 10-25 23:30 | 30 | True | 0.575 | -0.005 | 0.070 | 0.080 | 0.686 | 0.691 |  |
| nhl | goalie_confirmed | Colorado Avalanche | Scott Wedgewood | 10-25 23:30 | 30 | True | 0.455 | 0.000 | 0.000 | 0.000 | 0.686 | 0.691 |  |
| nhl | goalie_confirmed | Colorado Avalanche | Scott Wedgewood | 10-25 23:30 | 30 | False | 0.275 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Colorado Avalanche | Scott Wedgewood | 10-25 23:30 | 30 | False | 0.245 | 0.000 | 0.000 | 0.000 | 0.314 | 0.309 | 115.550 |
| nhl | goalie_confirmed | Colorado Avalanche | Scott Wedgewood | 10-25 23:30 | 30 | False | 0.195 | -0.000 | -0.005 | -0.020 |  |  |  |
| nhl | goalie_confirmed | Colorado Avalanche | Scott Wedgewood | 10-25 23:30 | 30 | False | 0.265 | 0.000 | -0.010 | -0.030 | 0.314 | 0.309 |  |
| nhl | goalie_confirmed | Nashville Predators | Justus Annunen | 10-25 23:30 | 30 | True | 0.295 | 0.000 | 0.000 | 0.000 | 0.314 | 0.314 | 96.690 |
| nhl | goalie_confirmed | Nashville Predators | Justus Annunen | 10-25 23:30 | 30 | False | 0.685 | 0.000 | 0.000 | 0.000 | 0.686 | 0.686 | 0.690 |
| nhl | goalie_confirmed | Nashville Predators | Justus Annunen | 10-25 23:30 | 30 | False | 0.410 | -0.015 | -0.005 | -0.005 | 0.686 | 0.686 |  |
| nhl | goalie_confirmed | Nashville Predators | Justus Annunen | 10-25 23:30 | 30 | False | 0.345 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Nashville Predators | Justus Annunen | 10-25 23:30 | 30 | True | 0.295 | 0.000 | 0.000 | -0.050 | 0.314 | 0.314 |  |
| nhl | goalie_confirmed | Nashville Predators | Justus Annunen | 10-25 23:30 | 30 | False | 0.425 | 0.000 | 0.000 | 0.000 | 0.686 | 0.686 |  |
| nhl | goalie_confirmed | Nashville Predators | Justus Annunen | 10-25 23:30 | 30 | False | 0.315 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Nashville Predators | Justus Annunen | 10-25 23:30 | 30 | False | 0.575 | -0.005 | 0.070 | 0.080 | 0.686 | 0.686 |  |
| nhl | goalie_confirmed | Nashville Predators | Justus Annunen | 10-25 23:30 | 30 | False | 0.455 | 0.000 | 0.000 | 0.000 | 0.686 | 0.686 |  |
| nhl | goalie_confirmed | Nashville Predators | Justus Annunen | 10-25 23:30 | 30 | False | 0.275 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Nashville Predators | Justus Annunen | 10-25 23:30 | 30 | True | 0.245 | 0.000 | 0.000 | 0.000 | 0.314 | 0.314 | 115.690 |
| nhl | goalie_confirmed | Nashville Predators | Justus Annunen | 10-25 23:30 | 30 | False | 0.195 | -0.000 | -0.005 | -0.020 |  |  |  |
| nhl | goalie_confirmed | Nashville Predators | Justus Annunen | 10-25 23:30 | 30 | True | 0.265 | 0.000 | -0.010 | -0.030 | 0.314 | 0.314 |  |
| nhl | goalie_confirmed | Winnipeg Jets | Stuart Skinner | 10-25 22:42 | 18 | False | 0.525 | 0.000 | 0.000 | 0.000 | 0.514 | 0.514 | 69.657 |

Generated by method/analysis/report.py from the data branch.
