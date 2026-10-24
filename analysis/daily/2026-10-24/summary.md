# Daily analysis 2026-10-24

## Coverage

| source | sport | rows | events | passes | window_rows | first | last |
|---|---|---|---|---|---|---|---|
| polymarket_bbo | bundesliga | 32,466 | 18 | 868 | 5,004 | 10-15 06:34 | 10-24 10:22 |
| polymarket_bbo | cs2 | 194,553 | 618 | 5,150 | 49,301 | 10-14 19:27 | 10-24 10:22 |
| polymarket_bbo | epl | 35,867 | 20 | 968 | 5,280 | 10-15 23:32 | 10-24 10:22 |
| polymarket_bbo | laliga | 35,507 | 20 | 1,267 | 5,976 | 10-15 07:34 | 10-24 10:22 |
| polymarket_bbo | ligue1 | 29,880 | 17 | 947 | 5,592 | 10-15 06:55 | 10-24 10:22 |
| polymarket_bbo | lol | 3,079 | 25 | 1,337 | 620 | 10-14 19:27 | 10-24 10:22 |
| polymarket_bbo | mlb | 54,303 | 8 | 1,194 | 12,004 | 10-14 19:27 | 10-24 10:22 |
| polymarket_bbo | nba | 86,339 | 59 | 1,546 | 29,042 | 10-14 19:27 | 10-24 10:22 |
| polymarket_bbo | nfl | 28,231 | 26 | 971 | 5,103 | 10-14 19:27 | 10-24 10:22 |
| polymarket_bbo | nhl | 245,672 | 76 | 2,213 | 42,663 | 10-14 19:27 | 10-24 10:22 |
| polymarket_bbo | seriea | 36,201 | 20 | 1,231 | 6,132 | 10-15 06:55 | 10-24 10:22 |
| pinnacle | mlb | 1,854 | 9 | 396 |  | 10-14 21:29 | 10-24 09:56 |
| pinnacle | nba | 25,988 | 36 | 529 |  | 10-14 21:29 | 10-24 09:56 |
| pinnacle | nfl | 20,732 | 28 | 413 |  | 10-14 21:29 | 10-24 09:56 |
| pinnacle | nhl | 25,174 | 73 | 620 |  | 10-14 21:29 | 10-24 09:56 |
| polymarket_history | bundesliga | 181 | 181 | 195,661 |  | NaT | NaT |
| polymarket_history | cs2 | 1,715 | 1,647 | 1,417,088 |  | NaT | NaT |
| polymarket_history | epl | 197 | 197 | 212,957 |  | NaT | NaT |
| polymarket_history | laliga | 214 | 214 | 231,334 |  | NaT | NaT |
| polymarket_history | ligue1 | 185 | 185 | 199,985 |  | NaT | NaT |
| polymarket_history | lol | 17 | 17 | 18,377 |  | NaT | NaT |
| polymarket_history | mlb | 397 | 337 | 429,157 |  | NaT | NaT |
| polymarket_history | nba | 2,368 | 2,368 | 2,075,548 |  | NaT | NaT |
| polymarket_history | nfl | 595 | 595 | 643,195 |  | NaT | NaT |
| polymarket_history | nhl | 2,032 | 2,032 | 2,196,592 |  | NaT | NaT |
| polymarket_history | seriea | 195 | 195 | 210,795 |  | NaT | NaT |
| news_mlb | mlb | 420 |  |  |  | NaT | NaT |
| news_nhl | nhl | 472 |  |  |  | NaT | NaT |
| news_nhl_schedule | nhl | 523 |  |  |  | NaT | NaT |

Odds API quota at last pass: used 5044.0, remaining 14956.0 (741 Pinnacle passes recorded).

## Event matching (Polymarket US vs Pinnacle)

907 Polymarket events, 146 Pinnacle events, 143 matched (34 by full name, 109 by nickname).

Unmatched Polymarket events (764): bundesliga Eintracht Frankfurt vs. 1. FC Koln; bundesliga 1. FC Union Berlin vs. BV Borussia 09 Dortmund; bundesliga Hamburger SV vs. VfB Stuttgart; bundesliga SV Werder Bremen vs. SC Paderborn 07; bundesliga FC Schalke 04 vs. 1. FSV Mainz 05; bundesliga SV 07 Elversberg vs. FC Augsburg; bundesliga FC Bayern Munchen vs. RB Leipzig; bundesliga Bayer 04 Leverkusen vs. SC Freiburg; bundesliga Borussia Monchengladbach vs. TSG 1899 Hoffenheim; bundesliga VfB Stuttgart vs. Borussia Monchengladbach; bundesliga RB Leipzig vs. SV 07 Elversberg; bundesliga FC Augsburg vs. 1. FC Union Berlin; bundesliga 1. FSV Mainz 05 vs. SV Werder Bremen; bundesliga 1. FC Koln vs. FC Schalke 04; bundesliga SC Paderborn 07 vs. Hamburger SV

## Polymarket mid vs Pinnacle fair, main winner contracts

mid_minus_fair > 0 means Polymarket prices the team higher than Pinnacle's de-vigged price. taker_edge_at_ask = fair − ask − fee: what a taker would expect if Pinnacle were exactly right.

| sport | bucket | n | mean_diff | mean_abs_diff | within_1c | within_2c | mean_spread | median_bid_shares | taker_edge_mean | taker_edge_pos_share |
|---|---|---|---|---|---|---|---|---|---|---|
| mlb | 0-15 min | 452 | -0.252 | 0.271 | 8% | 9% | 0.024 | 5,900 | 0.229 | 81% |
| mlb | 15-60 min | 611 | -0.269 | 0.270 | 8% | 8% | 0.010 | 30,000 | 0.253 | 92% |
| mlb | 1-3 h | 692 | -0.272 | 0.273 | 7% | 8% | 0.010 | 27,000 | 0.256 | 92% |
| mlb | 3-12 h | 970 | -0.272 | 0.272 | 6% | 7% | 0.049 | 26,000 | 0.235 | 90% |
| mlb | 12 h+ | 1,184 | -0.245 | 0.247 | 4% | 7% | 0.188 | 24,000 | 0.137 | 75% |
| nba | 0-15 min | 3,484 | -0.019 | 0.154 | 7% | 12% | 0.372 | 26,000 | -0.178 | 24% |
| nba | 15-60 min | 1,540 | -0.028 | 0.084 | 17% | 25% | 0.304 | 25,000 | -0.138 | 22% |
| nba | 1-3 h | 2,807 | -0.040 | 0.097 | 15% | 22% | 0.323 | 25,000 | -0.135 | 20% |
| nba | 3-12 h | 3,956 | -0.022 | 0.073 | 18% | 27% | 0.138 | 26,000 | -0.063 | 25% |
| nba | 12 h+ | 1,568 | 0.000 | 0.010 | 79% | 95% | 0.025 | 270,000 | -0.028 | 1% |
| nhl | 0-15 min | 6,178 | -0.107 | 0.144 | 10% | 14% | 0.089 | 28,000 | 0.049 | 61% |
| nhl | 15-60 min | 2,861 | -0.115 | 0.115 | 13% | 15% | 0.012 | 32,000 | 0.093 | 84% |
| nhl | 1-3 h | 5,696 | -0.116 | 0.117 | 12% | 15% | 0.012 | 32,000 | 0.094 | 85% |
| nhl | 3-12 h | 9,487 | -0.112 | 0.113 | 11% | 14% | 0.045 | 31,000 | 0.073 | 82% |
| nhl | 12 h+ | 20,335 | -0.124 | 0.125 | 12% | 15% | 0.126 | 29,000 | 0.044 | 71% |

Largest gaps seen:

| sport | team | pin_ts | minutes_to_start | fair | pm_mid | pm_spread | mid_minus_fair | taker_edge_at_ask |
|---|---|---|---|---|---|---|---|---|
| mlb | Milwaukee Brewers | 10-24 02:58 | -179 | 0.938 | 0.025 | 0.010 | -0.913 | 0.906 |
| mlb | Tampa Bay Rays | 10-18 23:46 | -159 | 0.941 | 0.040 | 0.020 | -0.901 | 0.888 |
| nba | Mavericks | 10-24 01:18 | -139 | 0.899 | 0.020 | 0.020 | -0.879 | 0.867 |
| nba | Pacers | 10-24 01:18 | -139 | 0.101 | 0.965 | 0.050 | 0.864 | -0.890 |
| nba | Mavericks | 10-24 01:25 | -151 | 0.899 | 0.045 | 0.050 | -0.854 | 0.825 |
| nba | Pacers | 10-24 01:25 | -151 | 0.101 | 0.950 | 0.080 | 0.849 | -0.890 |
| nba | Cavaliers | 10-23 00:36 | -97 | 0.940 | 0.115 | 0.030 | -0.825 | 0.802 |
| nba | Cavaliers | 10-23 00:31 | -97 | 0.940 | 0.115 | 0.030 | -0.825 | 0.802 |
| nhl | Kings | 10-23 01:22 | -105 | 0.848 | 0.025 | 0.030 | -0.823 | 0.805 |
| nhl | Kings | 10-23 01:15 | -105 | 0.848 | 0.025 | 0.030 | -0.823 | 0.805 |
| nba | Cavaliers | 10-23 00:31 | -97 | 0.940 | 0.120 | 0.020 | -0.820 | 0.802 |
| nba | Cavaliers | 10-23 00:36 | -97 | 0.940 | 0.120 | 0.020 | -0.820 | 0.802 |

## Test (b): calibration of last pre-game mids (settled games)

| sport | n | mean_mid | win_rate | brier_pm | log_loss_pm | slope | slope_se | intercept | n_with_pinnacle | brier_pm_matched | brier_pinnacle |
|---|---|---|---|---|---|---|---|---|---|---|---|
| bundesliga | 90 | 0.334 | 0.333 | 0.217 | 0.624 | 0.605 | 0.326 | -0.262 |  |  |  |
| cs2 | 1,226 | 0.527 | 0.564 | 0.223 | 0.634 | 0.924 | 0.097 | 0.172 |  |  |  |
| epl | 99 | 0.337 | 0.333 | 0.190 | 0.560 | 1.358 | 0.385 | 0.201 |  |  |  |
| laliga | 108 | 0.345 | 0.333 | 0.197 | 0.577 | 1.096 | 0.328 | -0.002 |  |  |  |
| ligue1 | 90 | 0.342 | 0.333 | 0.209 | 0.608 | 1.007 | 0.456 | -0.039 |  |  |  |
| lol | 17 | 0.620 | 0.529 |  |  |  |  |  |  |  |  |
| mlb | 127 | 0.346 | 0.346 | 0.206 | 0.599 | 0.727 | 0.205 | -0.155 | 87 | 0.183 | 0.244 |
| nba | 483 | 0.367 | 0.342 | 0.195 | 0.557 | 0.964 | 0.140 | -0.143 | 312 | 0.248 | 0.240 |
| nhl | 650 | 0.348 | 0.332 | 0.219 | 0.629 | 0.679 | 0.197 | -0.269 | 454 | 0.226 | 0.246 |
| seriea | 99 | 0.351 | 0.333 | 0.227 | 0.650 | 0.326 | 0.364 | -0.483 |  |  |  |

2989 settled main winner contracts so far; calibration is reported from 30 per sport.

## Test (a): news events and price reaction

215 news events recorded; 2951 joined to a Polymarket contract with a price path.

| sport | kind | n |
|---|---|---|
| mlb | lineup_away | 17 |
| mlb | lineup_home | 9 |
| mlb | probable_away | 6 |
| mlb | probable_home | 4 |
| nhl | goalie_confirmed | 124 |
| nhl | goalie_likely | 55 |

Most recent joined events:

| sport | kind | team | detail | news_ts | minutes_to_start | contract_is_news_team | mid_before | move_plus5 | move_plus15 | move_plus30 | pin_fair_before | pin_fair_after | minutes_to_within_1c |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-23 22:25 | 95 | True | 0.215 | 0.000 | 0.000 | 0.000 | 0.368 | 0.366 | 296.983 |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-23 22:25 | 95 | True | 0.155 | 0.000 | 0.000 | 0.000 | 0.368 | 0.366 |  |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-23 22:25 | 95 | True | 0.372 | 0.000 | 0.000 | 0.000 | 0.368 | 0.366 | 0.983 |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-23 22:25 | 95 | False | 0.185 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-23 22:25 | 95 | False | 0.545 | 0.000 | 0.000 | 0.000 | 0.632 | 0.634 | 119.983 |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-23 22:25 | 95 | True | 0.285 | 0.000 | 0.000 | 0.000 | 0.368 | 0.366 | 114.983 |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-23 22:25 | 95 | False | 0.625 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-23 22:25 | 95 | False | 0.255 | 0.000 | 0.000 | 0.000 | 0.632 | 0.634 |  |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-23 22:25 | 95 | True | 0.155 | 0.000 | 0.000 | 0.000 | 0.368 | 0.366 |  |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-23 22:25 | 95 | False | 0.665 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-23 22:25 | 95 | True | 0.145 | 0.000 | 0.000 | 0.000 | 0.368 | 0.366 |  |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-23 22:25 | 95 | False | 0.635 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-23 22:25 | 95 | False | 0.245 | 0.000 | 0.000 | 0.000 | 0.632 | 0.634 |  |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-23 22:25 | 95 | True | 0.145 | 0.000 | 0.000 | 0.000 | 0.368 | 0.366 |  |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-23 22:25 | 95 | False | 0.625 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-23 22:25 | 95 | False | 0.235 | 0.000 | 0.000 | 0.000 | 0.632 | 0.634 |  |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-23 22:25 | 95 | False | 0.225 | 0.000 | 0.000 | 0.000 | 0.632 | 0.634 |  |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-23 22:25 | 95 | False | 0.635 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-23 22:25 | 95 | False | 0.205 | 0.000 | 0.000 | 0.000 | 0.632 | 0.634 |  |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-23 22:25 | 95 | False | 0.225 | 0.000 | 0.000 | 0.000 | 0.632 | 0.634 |  |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-23 22:25 | 95 | False | 0.065 | 0.000 | 0.000 | 0.000 | 0.632 | 0.634 |  |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-23 22:25 | 95 | False | 0.685 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-23 22:25 | 95 | True | 0.145 | 0.000 | 0.000 | 0.000 | 0.368 | 0.366 |  |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-23 22:25 | 95 | False | 0.175 | 0.000 | 0.000 | 0.000 | 0.632 | 0.634 |  |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-23 22:25 | 95 | True | 0.135 | 0.000 | 0.000 | 0.000 | 0.368 | 0.366 |  |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-23 22:25 | 95 | False | 0.655 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-23 22:25 | 95 | False | 0.625 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-23 22:25 | 95 | True | 0.165 | 0.000 | 0.000 | 0.000 | 0.368 | 0.366 |  |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-23 22:25 | 95 | False | 0.225 | 0.000 | 0.000 | 0.000 | 0.632 | 0.634 |  |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-23 22:25 | 95 | False | 0.625 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-23 22:25 | 95 | True | 0.155 | 0.000 | 0.000 | 0.000 | 0.368 | 0.366 | 187.983 |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-23 21:11 | 168 | False | 0.665 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-23 21:11 | 168 | False | 0.645 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-23 21:11 | 168 | True | 0.145 | 0.000 | 0.000 | 0.000 | 0.365 | 0.365 |  |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-23 21:11 | 168 | False | 0.245 | 0.000 | 0.000 | 0.000 | 0.635 | 0.635 |  |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-23 21:11 | 168 | False | 0.635 | 0.000 | 0.000 | 0.000 |  |  |  |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-23 21:11 | 168 | True | 0.155 | 0.000 | 0.000 | 0.000 | 0.365 | 0.365 |  |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-23 21:11 | 168 | False | 0.215 | 0.000 | 0.000 | 0.000 | 0.635 | 0.635 |  |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-23 21:11 | 168 | True | 0.372 | 0.000 | 0.000 | 0.000 | 0.365 | 0.365 | 0.350 |
| mlb | lineup_away | Tampa Bay Rays | 9 players | 10-23 21:11 | 168 | True | 0.155 | 0.000 | 0.020 | 0.000 | 0.365 | 0.365 |  |

Generated by method/analysis/report.py from the data branch.
