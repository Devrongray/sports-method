# Daily analysis 2026-10-28

## Coverage

| source | sport | rows | events | passes | window_rows | first | last |
|---|---|---|---|---|---|---|---|
| polymarket_bbo | bundesliga | 41,742 | 18 | 1,194 | 8,724 | 10-15 06:34 | 10-25 18:22 |
| polymarket_bbo | cs2 | 241,330 | 698 | 6,748 | 61,775 | 10-14 19:27 | 10-28 10:04 |
| polymarket_bbo | epl | 49,643 | 20 | 1,314 | 8,844 | 10-15 23:32 | 10-25 18:22 |
| polymarket_bbo | laliga | 51,107 | 21 | 1,892 | 10,416 | 10-15 07:34 | 10-26 21:24 |
| polymarket_bbo | ligue1 | 47,388 | 18 | 1,350 | 9,384 | 10-15 06:55 | 10-26 21:13 |
| polymarket_bbo | lol | 5,282 | 36 | 2,137 | 1,229 | 10-14 19:27 | 10-28 10:00 |
| polymarket_bbo | mlb | 74,633 | 11 | 1,613 | 15,920 | 10-14 19:27 | 10-28 10:00 |
| polymarket_bbo | nba | 181,134 | 89 | 2,397 | 62,471 | 10-14 19:27 | 10-28 10:00 |
| polymarket_bbo | nfl | 47,838 | 28 | 1,474 | 8,946 | 10-14 19:27 | 10-27 03:15 |
| polymarket_bbo | nhl | 347,753 | 97 | 3,108 | 63,159 | 10-14 19:27 | 10-28 10:00 |
| polymarket_bbo | seriea | 61,881 | 30 | 1,929 | 11,652 | 10-15 06:55 | 10-28 10:00 |
| pinnacle | mlb | 2,430 | 12 | 541 |  | 10-14 21:29 | 10-28 09:38 |
| pinnacle | nba | 33,212 | 68 | 777 |  | 10-14 21:29 | 10-28 09:38 |
| pinnacle | nfl | 28,766 | 42 | 597 |  | 10-14 21:29 | 10-28 09:38 |
| pinnacle | nhl | 34,964 | 97 | 878 |  | 10-14 21:29 | 10-28 09:38 |
| polymarket_history | bundesliga | 337 | 337 | 364,297 |  | NaT | NaT |
| polymarket_history | cs2 | 2,149 | 2,096 | 1,827,882 |  | NaT | NaT |
| polymarket_history | epl | 360 | 360 | 389,160 |  | NaT | NaT |
| polymarket_history | laliga | 382 | 382 | 412,942 |  | NaT | NaT |
| polymarket_history | ligue1 | 343 | 331 | 370,783 |  | NaT | NaT |
| polymarket_history | lol | 33 | 33 | 35,673 |  | NaT | NaT |
| polymarket_history | mlb | 579 | 519 | 625,899 |  | NaT | NaT |
| polymarket_history | nba | 4,623 | 4,623 | 4,186,946 |  | NaT | NaT |
| polymarket_history | nfl | 1,132 | 1,132 | 1,223,692 |  | NaT | NaT |
| polymarket_history | nhl | 3,146 | 3,146 | 3,400,826 |  | NaT | NaT |
| polymarket_history | seriea | 414 | 414 | 447,534 |  | NaT | NaT |
| news_mlb | mlb | 566 |  |  |  | NaT | NaT |
| news_nhl | nhl | 660 |  |  |  | NaT | NaT |
| news_nhl_schedule | nhl | 728 |  |  |  | NaT | NaT |

Odds API quota at last pass: used 7734.0, remaining 12266.0 (1052 Pinnacle passes recorded).

## Event matching (Polymarket US vs Pinnacle)

1066 Polymarket events, 219 Pinnacle events, 204 matched (64 by full name, 140 by nickname).

Unmatched Polymarket events (862): bundesliga Eintracht Frankfurt vs. 1. FC Koln; bundesliga 1. FC Union Berlin vs. BV Borussia 09 Dortmund; bundesliga Hamburger SV vs. VfB Stuttgart; bundesliga SV Werder Bremen vs. SC Paderborn 07; bundesliga FC Schalke 04 vs. 1. FSV Mainz 05; bundesliga SV 07 Elversberg vs. FC Augsburg; bundesliga FC Bayern Munchen vs. RB Leipzig; bundesliga Bayer 04 Leverkusen vs. SC Freiburg; bundesliga Borussia Monchengladbach vs. TSG 1899 Hoffenheim; bundesliga VfB Stuttgart vs. Borussia Monchengladbach; bundesliga RB Leipzig vs. SV 07 Elversberg; bundesliga FC Augsburg vs. 1. FC Union Berlin; bundesliga 1. FSV Mainz 05 vs. SV Werder Bremen; bundesliga 1. FC Koln vs. FC Schalke 04; bundesliga SC Paderborn 07 vs. Hamburger SV

## Polymarket mid vs Pinnacle fair, main winner contracts

mid_minus_fair > 0 means Polymarket prices the team higher than Pinnacle's de-vigged price. taker_edge_at_ask = fair − ask − fee: what a taker would expect if Pinnacle were exactly right.

| sport | bucket | n | mean_diff | mean_abs_diff | within_1c | within_2c | mean_spread | median_bid_shares | taker_edge_mean | taker_edge_pos_share |
|---|---|---|---|---|---|---|---|---|---|---|
| mlb | 0-15 min | 710 | -0.255 | 0.271 | 6% | 7% | 0.021 | 6,000 | 0.233 | 85% |
| mlb | 15-60 min | 1,031 | -0.269 | 0.269 | 7% | 7% | 0.010 | 37,000 | 0.252 | 93% |
| mlb | 1-3 h | 1,007 | -0.271 | 0.272 | 6% | 7% | 0.010 | 28,000 | 0.255 | 93% |
| mlb | 3-12 h | 1,663 | -0.272 | 0.272 | 6% | 6% | 0.050 | 26,000 | 0.234 | 92% |
| mlb | 12 h+ | 2,108 | -0.254 | 0.256 | 4% | 6% | 0.142 | 20,000 | 0.169 | 83% |
| nba | 0-15 min | 7,621 | -0.025 | 0.160 | 7% | 11% | 0.307 | 26,000 | -0.141 | 29% |
| nba | 15-60 min | 3,841 | -0.036 | 0.107 | 15% | 20% | 0.342 | 25,000 | -0.148 | 22% |
| nba | 1-3 h | 7,474 | -0.048 | 0.128 | 14% | 22% | 0.437 | 25,000 | -0.182 | 17% |
| nba | 3-12 h | 9,615 | -0.042 | 0.121 | 17% | 25% | 0.440 | 25,000 | -0.190 | 15% |
| nba | 12 h+ | 2,025 | -0.003 | 0.015 | 76% | 93% | 0.045 | 320,000 | -0.035 | 1% |
| nhl | 0-15 min | 9,051 | -0.109 | 0.148 | 9% | 14% | 0.088 | 28,000 | 0.051 | 62% |
| nhl | 15-60 min | 4,508 | -0.117 | 0.118 | 12% | 14% | 0.012 | 32,000 | 0.095 | 86% |
| nhl | 1-3 h | 8,360 | -0.117 | 0.117 | 12% | 14% | 0.012 | 32,000 | 0.095 | 86% |
| nhl | 3-12 h | 15,958 | -0.113 | 0.114 | 10% | 13% | 0.044 | 31,000 | 0.075 | 83% |
| nhl | 12 h+ | 27,940 | -0.126 | 0.127 | 12% | 14% | 0.133 | 29,000 | 0.043 | 71% |

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
| nba | Raptors | 10-26 00:44 | -109 | 0.157 | 0.985 | 0.010 | 0.828 | -0.834 |
| nba | Raptors | 10-26 00:39 | -109 | 0.157 | 0.985 | 0.010 | 0.828 | -0.834 |
| nba | Cavaliers | 10-23 00:36 | -97 | 0.940 | 0.115 | 0.030 | -0.825 | 0.802 |

## Test (b): calibration of last pre-game mids (settled games)

| sport | n | mean_mid | win_rate | brier_pm | log_loss_pm | slope | slope_se | intercept | n_with_pinnacle | brier_pm_matched | brier_pinnacle |
|---|---|---|---|---|---|---|---|---|---|---|---|
| bundesliga | 162 | 0.335 | 0.333 | 0.214 | 0.615 | 0.708 | 0.254 | -0.198 |  |  |  |
| cs2 | 1,530 | 0.531 | 0.558 | 0.223 | 0.634 | 0.909 | 0.085 | 0.132 |  |  |  |
| epl | 180 | 0.337 | 0.333 | 0.204 | 0.594 | 1.006 | 0.274 | -0.014 |  |  |  |
| laliga | 189 | 0.341 | 0.333 | 0.201 | 0.585 | 1.023 | 0.249 | -0.025 |  |  |  |
| ligue1 | 162 | 0.344 | 0.333 | 0.207 | 0.601 | 1.001 | 0.307 | -0.051 |  |  |  |
| lol | 33 | 0.572 | 0.364 | 0.243 | 0.678 | 0.933 | 0.447 | -1.020 |  |  |  |
| mlb | 220 | 0.345 | 0.341 | 0.197 | 0.582 | 0.816 | 0.161 | -0.127 | 150 | 0.173 | 0.247 |
| nba | 933 | 0.338 | 0.326 | 0.184 | 0.534 | 0.911 | 0.084 | -0.102 | 594 | 0.243 | 0.244 |
| nhl | 1,053 | 0.349 | 0.339 | 0.219 | 0.631 | 0.763 | 0.160 | -0.190 | 733 | 0.228 | 0.245 |
| seriea | 207 | 0.353 | 0.333 | 0.202 | 0.589 | 1.076 | 0.257 | -0.058 |  |  |  |

4669 settled main winner contracts so far; calibration is reported from 30 per sport.

## Test (a): news events and price reaction

311 news events recorded; 4366 joined to a Polymarket contract with a price path.

| sport | kind | n |
|---|---|---|
| mlb | lineup_away | 22 |
| mlb | lineup_home | 12 |
| mlb | probable_away | 8 |
| mlb | probable_home | 5 |
| nhl | goalie_confirmed | 186 |
| nhl | goalie_likely | 78 |

Most recent joined events:

| sport | kind | team | detail | news_ts | minutes_to_start | contract_is_news_team | mid_before | move_plus5 | move_plus15 | move_plus30 | pin_fair_before | pin_fair_after | minutes_to_within_1c |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| nhl | goalie_confirmed | Buffalo Sabres | Colten Ellis | 10-28 02:07 | 22 | False | 0.355 | 0.000 | 0.000 | 0.000 | 0.422 | 0.418 |  |
| nhl | goalie_confirmed | Buffalo Sabres | Colten Ellis | 10-28 02:07 | 22 | False | 0.315 | 0.000 | 0.000 | 0.000 | 0.422 | 0.418 |  |
| nhl | goalie_confirmed | Buffalo Sabres | Colten Ellis | 10-28 02:07 | 22 | True | 0.575 | 0.000 | 0.000 | 0.000 | 0.578 | 0.582 | 0.129 |
| nhl | goalie_confirmed | Buffalo Sabres | Colten Ellis | 10-28 02:07 | 22 | True | 0.405 | 0.000 | 0.000 | 0.000 | 0.578 | 0.582 |  |
| nhl | goalie_confirmed | Buffalo Sabres | Colten Ellis | 10-28 02:07 | 22 | False | 0.305 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Buffalo Sabres | Colten Ellis | 10-28 02:07 | 22 | False | 0.315 | 0.000 | 0.000 | 0.025 | 0.422 | 0.418 |  |
| nhl | goalie_confirmed | Buffalo Sabres | Colten Ellis | 10-28 02:07 | 22 | False | 0.275 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Buffalo Sabres | Colten Ellis | 10-28 02:07 | 22 | True | 0.405 | 0.000 | 0.000 | 0.000 | 0.578 | 0.582 |  |
| nhl | goalie_confirmed | Buffalo Sabres | Colten Ellis | 10-28 02:07 | 22 | True | 0.435 | 0.000 | 0.000 | 0.000 | 0.578 | 0.582 |  |
| nhl | goalie_confirmed | Buffalo Sabres | Colten Ellis | 10-28 02:07 | 22 | False | 0.275 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Buffalo Sabres | Colten Ellis | 10-28 02:07 | 22 | False | 0.345 | 0.000 | 0.000 | 0.000 | 0.422 | 0.418 |  |
| nhl | goalie_confirmed | Buffalo Sabres | Colten Ellis | 10-28 02:07 | 22 | True | 0.455 | 0.000 | 0.000 | 0.000 | 0.578 | 0.582 | 112.129 |
| nhl | goalie_confirmed | Buffalo Sabres | Colten Ellis | 10-28 02:07 | 22 | False | 0.205 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-28 01:30 | 29 | True | 0.255 | 0.000 | 0.000 | 0.000 | 0.333 | 0.334 | 79.307 |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-28 01:30 | 29 | True | 0.335 | 0.000 | 0.000 | 0.000 | 0.333 | 0.334 | 0.307 |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-28 01:30 | 29 | False | 0.415 | 0.000 | 0.000 | 0.000 | 0.667 | 0.666 |  |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-28 01:30 | 29 | False | 0.300 | 0.015 | 0.015 | 0.015 |  |  |  |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-28 01:30 | 29 | True | 0.285 | 0.000 | 0.000 | 0.000 | 0.333 | 0.334 |  |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-28 01:30 | 29 | False | 0.315 | 0.000 | -0.035 | -0.020 |  |  |  |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-28 01:30 | 29 | False | 0.465 | 0.000 | 0.000 | 0.000 | 0.667 | 0.666 |  |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-28 01:30 | 29 | False | 0.455 | 0.000 | 0.000 | 0.000 | 0.667 | 0.666 |  |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-28 01:30 | 29 | True | 0.270 | 0.000 | -0.005 | -0.005 | 0.333 | 0.334 |  |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-28 01:30 | 29 | False | 0.575 | 0.000 | 0.000 | 0.000 | 0.667 | 0.666 | 64.307 |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-28 01:30 | 29 | False | 0.185 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-28 01:30 | 29 | True | 0.275 | 0.000 | 0.000 | 0.000 | 0.333 | 0.334 |  |
| nhl | goalie_confirmed | Vancouver Canucks | Leevi Merilainen | 10-28 01:30 | 29 | False | 0.265 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Los Angeles Kings | Anton Forsberg | 10-27 23:32 | 28 | True | 0.365 | 0.000 | 0.000 | 0.000 | 0.495 | 0.493 |  |
| nhl | goalie_confirmed | Los Angeles Kings | Anton Forsberg | 10-27 23:32 | 28 | True | 0.495 | 0.000 | 0.000 | -0.010 | 0.495 | 0.493 | 0.814 |
| nhl | goalie_confirmed | Los Angeles Kings | Anton Forsberg | 10-27 23:32 | 28 | False | 0.335 | 0.000 | 0.000 | 0.000 | 0.505 | 0.507 |  |
| nhl | goalie_confirmed | Los Angeles Kings | Anton Forsberg | 10-27 23:32 | 28 | False | 0.365 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Los Angeles Kings | Anton Forsberg | 10-27 23:32 | 28 | True | 0.345 | 0.000 | 0.000 | 0.000 | 0.495 | 0.493 | 46.814 |
| nhl | goalie_confirmed | Los Angeles Kings | Anton Forsberg | 10-27 23:32 | 28 | False | 0.365 | 0.000 | 0.000 | 0.000 | 0.505 | 0.507 |  |
| nhl | goalie_confirmed | Los Angeles Kings | Anton Forsberg | 10-27 23:32 | 28 | False | 0.285 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Los Angeles Kings | Anton Forsberg | 10-27 23:32 | 28 | False | 0.345 | 0.000 | 0.000 | 0.000 | 0.505 | 0.507 |  |
| nhl | goalie_confirmed | Los Angeles Kings | Anton Forsberg | 10-27 23:32 | 28 | False | 0.295 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Los Angeles Kings | Anton Forsberg | 10-27 23:32 | 28 | True | 0.375 | 0.000 | 0.000 | 0.000 | 0.495 | 0.493 | 162.814 |
| nhl | goalie_confirmed | Los Angeles Kings | Anton Forsberg | 10-27 23:32 | 28 | False | 0.345 | 0.020 | 0.020 | 0.020 | 0.505 | 0.507 | 167.814 |
| nhl | goalie_confirmed | Los Angeles Kings | Anton Forsberg | 10-27 23:32 | 28 | False | 0.215 | 0.000 | 0.000 | 0.000 |  |  |  |
| nhl | goalie_confirmed | Los Angeles Kings | Anton Forsberg | 10-27 23:32 | 28 | True | 0.365 | 0.000 | 0.000 | 0.000 | 0.495 | 0.493 |  |
| nhl | goalie_confirmed | Carolina Hurricanes | Pyotr Kochetkov | 10-27 23:31 | 28 | False | 0.315 | 0.000 | 0.000 | 0.000 |  |  |  |

Generated by method/analysis/report.py from the data branch.
