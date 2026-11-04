# Polymarket US discovery 2026-11-04T08:57:35+00:00

394 leagues listed.

| Sport | Slug | Listed | Events | Next 36h | Main lines to record (next 36h) | Unclassified types | Note |
|---|---|---|---|---|---|---|---|
| mlb | mlb | yes | 0 | 0 | 0 | - | candidates: mlb |
| nba | nba | yes | 115 | 14 | 42 | BASKETBALL_PLAYER_REBOUNDS, BASKETBALL_PLAYER_ASSISTS, BASKETBALL_PLAYER_POINTS, BASKETBALL_PLAYER_THREES, BASKETBALL_PLAYER_STEALS, BASKETBALL_PLAYER_POINTS_REBOUNDS_ASSISTS, BASKETBALL_PLAYER_BLOCKS, BASKETBALL_GAME_OVERTIME |  |
| ncaab | cbb | yes | 632 | 10 | 38 | BASKETBALL_TEAM_TOTAL_POINTS |  |
| nhl | nhl | yes | 36 | 4 | 84 | HOCKEY_TEAM_TOTAL_GOALS, HOCKEY_PLAYER_POINTS, HOCKEY_PLAYER_ASSISTS, HOCKEY_PLAYER_GOALS, HOCKEY_GAME_OVERTIME, HOCKEY_GAME_FIRST_TEAM_TO_SCORE |  |
| nfl | nfl | yes | 29 | 0 | 0 | - |  |
| cs2 | cs2 | yes | 73 | 53 | 169 | - |  |
| lol | lol | yes | 3 | 1 | 1 | ESPORTS_SERIES_GAME_HANDICAP, ESPORTS_GAME_WINNER_3, ESPORTS_GAME_WINNER_2, ESPORTS_GAME_WINNER_1, ESPORTS_SERIES_TOTAL_GAMES, ESPORTS_GAME_PLAYER_KILLS_1, ESPORTS_GAME_PLAYER_KILLS_2, ESPORTS_GAME_PLAYER_KILLS_3, ESPORTS_PLAYER_KILLS |  |
| epl | epl | yes | 10 | 0 | 0 | - |  |
| laliga | lal | yes | 10 | 0 | 0 | - |  |
| bundesliga | bun | yes | 9 | 0 | 0 | - |  |
| seriea | sea | yes | 10 | 0 | 0 | - |  |
| ligue1 | lg1 | yes | 9 | 0 | 0 | - |  |

## Market types seen, with one example each

| Sport | Raw type | Class/segment | Count | Example question | Line | Sides |
|---|---|---|---|---|---|---|
| nba | BASKETBALL_GAME_OVERTIME | OTHER/UNKNOWN | 1 | Will CHI Bulls vs. NY Knicks go to overtime? | 0.5 | astatc-nba-chi-ny-2026-11-04-ot @0.01; astatc-nba-chi-ny-2026-11-04-ot @0.04 |
| nba | BASKETBALL_PLAYER_ASSISTS | OTHER/UNKNOWN | 473 | Will Keyonte George record at least 6 assists in UTA Jazz vs | 6 | astatc-nba-uta-no-2026-11-04-ast-keygeo-gte6 (team 35) @0.39; astatc-nba-uta-no-2026-11-04 |
| nba | BASKETBALL_PLAYER_BLOCKS | OTHER/UNKNOWN | 140 | Will Paul Reed record at least 1 blocks in PHI 76ers vs. DET | 1 | astatc-nba-phi-det-2026-11-04-blk-pauree-gte1 (team 23) @0.48; astatc-nba-phi-det-2026-11- |
| nba | BASKETBALL_PLAYER_POINTS | OTHER/UNKNOWN | 724 | Will Jalen Brunson record at least 25 points in CHI Bulls vs | 25 | astatc-nba-chi-ny-2026-11-04-pts-jalbru-gte25 (team 43) @0.48; astatc-nba-chi-ny-2026-11-0 |
| nba | BASKETBALL_PLAYER_POINTS_REBOUNDS_ASSISTS | OTHER/UNKNOWN | 550 | Will Evan Mobley record at least 30 combined points, rebound | 30 | astatc-nba-cle-okc-2026-11-04-pra-evamob-gte30 (team 38) @0.49; astatc-nba-cle-okc-2026-11 |
| nba | BASKETBALL_PLAYER_REBOUNDS | OTHER/UNKNOWN | 746 | Will Tyrese Maxey record at least 4 total rebounds in PHI 76 | 4 | astatc-nba-phi-det-2026-11-04-reb-tyrmax-gte4 (team 29) @0.48; astatc-nba-phi-det-2026-11- |
| nba | BASKETBALL_PLAYER_STEALS | OTHER/UNKNOWN | 264 | Will Tyrese Maxey record at least 1 steals in PHI 76ers vs.  | 1 | astatc-nba-phi-det-2026-11-04-stl-tyrmax-gte1 (team 29) @0.42; astatc-nba-phi-det-2026-11- |
| nba | BASKETBALL_PLAYER_THREES | OTHER/UNKNOWN | 483 | Will Luguentz Dort record at least 2 three-point field goals | 2 | astatc-nba-atl-was-2026-11-04-3pm-lugdor-gte2 (team 25) @0.48; astatc-nba-atl-was-2026-11- |
| nba | BASKETBALL_TEAM_FULL_GAME_SPREAD | SPREAD/FULL_GAME | 468 | Will the PHI 76ers cover 2.5 vs the DET Pistons in PHI 76ers | 2.5 | asc-nba-phi-det-2026-11-04-pos-2pt5 (team 29) @0.50; asc-nba-phi-det-2026-11-04-pos-2pt5 ( |
| nba | BASKETBALL_TEAM_FULL_GAME_TOTAL | TOTAL/FULL_GAME | 423 | Will the total in PHI 76ers vs. DET Pistons be more than 217 | 217.5 | tsc-nba-phi-det-2026-11-04-217pt5 @0.51; tsc-nba-phi-det-2026-11-04-217pt5 @0.52 |
| nba | BASKETBALL_TEAM_FULL_GAME_WINNER | WINNER/FULL_GAME | 115 | Who will win in the upcoming basketball event PHI 76ers vs D |  | aec-nba-phi-det-2026-11-04 (team 29) @0.45; aec-nba-phi-det-2026-11-04 (team 23) @0.46 |
| ncaab | BASKETBALL_TEAM_FIRST_HALF_SPREAD | SPREAD/FIRST_HALF | 20 | Will Cal State Northridge cover +7.5 vs Wichita State in the | 7.5 | asc-cbb-csunr-wichst-2026-11-04-fh-pos-7pt5 (team 1780) @0.01; asc-cbb-csunr-wichst-2026-1 |
| ncaab | BASKETBALL_TEAM_FIRST_HALF_TOTAL | TOTAL/FIRST_HALF | 20 | Will the first half total in Cal State Northridge vs. Wichit | 77.5 | tsc-cbb-csunr-wichst-2026-11-04-fh-77pt5 @0.01; tsc-cbb-csunr-wichst-2026-11-04-fh-77pt5 @ |
| ncaab | BASKETBALL_TEAM_FULL_GAME_SPREAD | SPREAD/FULL_GAME | 259 | Will Longwood cover +9.5 vs Saint Joseph's in Longwood vs. S | 9.5 | asc-cbb-longwd-stjoe-2026-11-04-pos-9pt5 (team 1746) @0.49; asc-cbb-longwd-stjoe-2026-11-0 |
| ncaab | BASKETBALL_TEAM_FULL_GAME_TOTAL | TOTAL/FULL_GAME | 269 | Will the total in Longwood vs. Saint Joseph's be more than 1 | 149.5 | tsc-cbb-longwd-stjoe-2026-11-04-149pt5 @0.48; tsc-cbb-longwd-stjoe-2026-11-04-149pt5 @0.50 |
| ncaab | BASKETBALL_TEAM_FULL_GAME_WINNER | WINNER/FULL_GAME | 632 | Who will win in the upcoming basketball event Longwood vs Sa |  | aec-cbb-longwd-stjoe-2026-11-04 (team 1746) @0.18; aec-cbb-longwd-stjoe-2026-11-04 (team 1 |
| ncaab | BASKETBALL_TEAM_TOTAL_POINTS | OTHER/UNKNOWN | 60 | Will Saint Joseph's score more than 77.5 points in Longwood  | 77.5 | tsc-cbb-longwd-stjoe-2026-11-04-tt-stjoe-fg-77pt5 (team 1705) @0.29; tsc-cbb-longwd-stjoe- |
| nhl | HOCKEY_GAME_FIRST_TEAM_TO_SCORE | OTHER/UNKNOWN | 12 | Will OTT vs BUF see no goal in regulation or overtime? |  | astatc-nhl-ott-buf-2026-11-04-ftts-neither @0.01; astatc-nhl-ott-buf-2026-11-04-ftts-neith |
| nhl | HOCKEY_GAME_OVERTIME | OTHER/UNKNOWN | 4 | Will the NHL hockey game between Senators and Sabres on 2026 | 0.5 | astatc-nhl-ott-buf-2026-11-04-ot (team 1485) @0.20; astatc-nhl-ott-buf-2026-11-04-ot (team |
| nhl | HOCKEY_PLAYER_ASSISTS | OTHER/UNKNOWN | 94 | Will Rasmus Dahlin record at least 1 assists in OTT vs BUF? | 1 | astatc-nhl-ott-buf-2026-11-04-ast-rasdah-gte1 (team 1485) @0.50; astatc-nhl-ott-buf-2026-1 |
| nhl | HOCKEY_PLAYER_GOALS | OTHER/UNKNOWN | 146 | Will Tage Thompson record at least 1 goals in OTT vs BUF? | 1 | astatc-nhl-ott-buf-2026-11-04-goals-tagtho-gte1 (team 1485) @0.23; astatc-nhl-ott-buf-2026 |
| nhl | HOCKEY_PLAYER_POINTS | OTHER/UNKNOWN | 130 | Will Matvei Gridin record at least 1 points in CGY vs SEA? | 1 | astatc-nhl-cgy-sea-2026-11-04-pts-matgri-gte1 (team 1507) @0.46; astatc-nhl-cgy-sea-2026-1 |
| nhl | HOCKEY_TEAM_FIRST_PERIOD_SPREAD | SPREAD/FIRST_PERIOD | 8 | Will OTT Senators cover +1.5 vs BUF Sabres in the first peri | 1.5 | asc-nhl-ott-buf-2026-11-04-p1-pos-1pt5 (team 1488) @0.85; asc-nhl-ott-buf-2026-11-04-p1-po |
| nhl | HOCKEY_TEAM_FIRST_PERIOD_TOTAL | TOTAL/FIRST_PERIOD | 16 | Will OTT vs BUF have more than 1.5 goals in the first period | 1.5 | tsc-nhl-ott-buf-2026-11-04-p1-1pt5 @0.55; tsc-nhl-ott-buf-2026-11-04-p1-1pt5 @0.60 |
| nhl | HOCKEY_TEAM_FIRST_PERIOD_WINNER | WINNER/FIRST_PERIOD | 12 | Will BUF Sabres win the first period of OTT vs BUF? |  | atc-nhl-ott-buf-2026-11-04-p1-buf (team 1485) @0.33; atc-nhl-ott-buf-2026-11-04-p1-buf (te |
| nhl | HOCKEY_TEAM_FULL_GAME_SPREAD | SPREAD/FULL_GAME | 24 | Will the OTT Senators cover 1.5 vs the BUF Sabres in OTT vs  | 1.5 | asc-nhl-ott-buf-2026-11-04-pos-1pt5 (team 1488) @0.66; asc-nhl-ott-buf-2026-11-04-pos-1pt5 |
| nhl | HOCKEY_TEAM_FULL_GAME_TOTAL | TOTAL/FULL_GAME | 32 | Will the total in OTT vs BUF be more than 6.5? | 6.5 | tsc-nhl-ott-buf-2026-11-04-6pt5 @0.53; tsc-nhl-ott-buf-2026-11-04-6pt5 @0.54 |
| nhl | HOCKEY_TEAM_FULL_GAME_WINNER | WINNER/FULL_GAME | 36 | Who will win in the upcoming hockey event OTT Senators vs BU |  | aec-nhl-ott-buf-2026-11-04 (team 1488) @0.44; aec-nhl-ott-buf-2026-11-04 (team 1485) @0.45 |
| nhl | HOCKEY_TEAM_REGULATION_WINNER | WINNER/REGULATION | 12 | Will BUF Sabres lead after regulation of OTT vs BUF? |  | atc-nhl-ott-buf-2026-11-04-reg-buf (team 1485) @0.01; atc-nhl-ott-buf-2026-11-04-reg-buf ( |
| nhl | HOCKEY_TEAM_SECOND_PERIOD_SPREAD | SPREAD/SECOND_PERIOD | 8 | Will OTT Senators cover +1.5 vs BUF Sabres in the second per | 1.5 | asc-nhl-ott-buf-2026-11-04-p2-pos-1pt5 (team 1488) @0.73; asc-nhl-ott-buf-2026-11-04-p2-po |
| nhl | HOCKEY_TEAM_SECOND_PERIOD_TOTAL | TOTAL/SECOND_PERIOD | 16 | Will OTT vs BUF have more than 2.5 goals in the second perio | 2.5 | tsc-nhl-ott-buf-2026-11-04-p2-2pt5 @0.35; tsc-nhl-ott-buf-2026-11-04-p2-2pt5 @0.41 |
| nhl | HOCKEY_TEAM_SECOND_PERIOD_WINNER | WINNER/SECOND_PERIOD | 12 | Will BUF Sabres win the second period of OTT vs BUF? |  | atc-nhl-ott-buf-2026-11-04-p2-buf (team 1485) @0.36; atc-nhl-ott-buf-2026-11-04-p2-buf (te |
| nhl | HOCKEY_TEAM_THIRD_PERIOD_SPREAD | SPREAD/THIRD_PERIOD | 8 | Will OTT Senators cover +1.5 vs BUF Sabres in the third peri | 1.5 | asc-nhl-ott-buf-2026-11-04-p3-pos-1pt5 (team 1488) @0.64; asc-nhl-ott-buf-2026-11-04-p3-po |
| nhl | HOCKEY_TEAM_THIRD_PERIOD_TOTAL | TOTAL/THIRD_PERIOD | 16 | Will OTT vs BUF have more than 2.5 goals in the third period | 2.5 | tsc-nhl-ott-buf-2026-11-04-p3-2pt5 @0.38; tsc-nhl-ott-buf-2026-11-04-p3-2pt5 @0.45 |
| nhl | HOCKEY_TEAM_THIRD_PERIOD_WINNER | WINNER/THIRD_PERIOD | 12 | Will BUF Sabres win the third period of OTT vs BUF? |  | atc-nhl-ott-buf-2026-11-04-p3-buf (team 1485) @0.38; atc-nhl-ott-buf-2026-11-04-p3-buf (te |
| nhl | HOCKEY_TEAM_TOTAL_GOALS | OTHER/UNKNOWN | 48 | Will BUF Sabres score more than 0.5 goals in OTT vs BUF? | 0.5 | tsc-nhl-ott-buf-2026-11-04-tt-buf-0pt5 (team 1485) @0.82; tsc-nhl-ott-buf-2026-11-04-tt-bu |
| nfl | FOOTBALL_TEAM_FULL_GAME_WINNER | WINNER/FULL_GAME | 29 | Who will win in the upcoming football event Jacksonville Jag |  | aec-nfl-jax-bal-2026-11-05 (team 62) @0.81; aec-nfl-jax-bal-2026-11-05 (team 50) @0.81 |
| cs2 | ESPORTS_MAP_WINNER_1 | WINNER/MAP_1 | 42 | Will ILLYRIANS win Map 1 vs Bebop? |  | astatc-cs2-ill-bbp-2026-11-04-map1 (team 29616) @0.54; astatc-cs2-ill-bbp-2026-11-04-map1  |
| cs2 | ESPORTS_MAP_WINNER_2 | WINNER/MAP_2 | 42 | Will ILLYRIANS win Map 2 vs Bebop? |  | astatc-cs2-ill-bbp-2026-11-04-map2 (team 29616) @0.54; astatc-cs2-ill-bbp-2026-11-04-map2  |
| cs2 | ESPORTS_MATCH_WINNER | WINNER/MATCH | 73 | Who will win in the upcoming esports event Liquid vs BetBoom |  | aec-cs2-tl-bb-2026-11-04 (team 5162) @0.39; aec-cs2-tl-bb-2026-11-04 (team 5423) @0.40 |
| cs2 | ESPORTS_SERIES_MAP_HANDICAP | SPREAD/SERIES | 18 | Will the ILLYRIANS cover -1.5 vs the Bebop in ILLYRIANS vs.  | -1.5 | asc-cs2-ill-bbp-2026-11-04-hcap-neg-1pt5 (team 29616) @0.95; asc-cs2-ill-bbp-2026-11-04-hc |
| cs2 | ESPORTS_SERIES_TOTAL_MAPS | TOTAL/SERIES | 16 | Will the total in ILLYRIANS vs. Bebop be more than 2.5? | 2.5 | tsc-cs2-ill-bbp-2026-11-04-tot-2pt5 @0.01; tsc-cs2-ill-bbp-2026-11-04-tot-2pt5 @0.99 |
| lol | ESPORTS_GAME_PLAYER_KILLS_1 | OTHER/UNKNOWN | 9 | Will Berserker record 3 or more kills in Game 1 of Gen.G Esp | 3 | astatc-lol-gen-lyon-2026-11-04-g1-k-berser-gte3 (team 42093); astatc-lol-gen-lyon-2026-11- |
| lol | ESPORTS_GAME_PLAYER_KILLS_2 | OTHER/UNKNOWN | 9 | Will Berserker record 3 or more kills in Game 2 of Gen.G Esp | 3 | astatc-lol-gen-lyon-2026-11-04-g2-k-berser-gte3 (team 42093); astatc-lol-gen-lyon-2026-11- |
| lol | ESPORTS_GAME_PLAYER_KILLS_3 | OTHER/UNKNOWN | 9 | Will Berserker record 3 or more kills in Game 3 of Gen.G Esp | 3 | astatc-lol-gen-lyon-2026-11-04-g3-k-berser-gte3 (team 42093); astatc-lol-gen-lyon-2026-11- |
| lol | ESPORTS_GAME_WINNER_1 | OTHER/UNKNOWN | 1 | Will Gen.G Esports win Game 1 vs LYON? |  | astatc-lol-gen-lyon-2026-11-04-game1 (team 5134) @0.80; astatc-lol-gen-lyon-2026-11-04-gam |
| lol | ESPORTS_GAME_WINNER_2 | OTHER/UNKNOWN | 1 | Will Gen.G Esports win Game 2 vs LYON? |  | astatc-lol-gen-lyon-2026-11-04-game2 (team 5134) @0.78; astatc-lol-gen-lyon-2026-11-04-gam |
| lol | ESPORTS_GAME_WINNER_3 | OTHER/UNKNOWN | 1 | Will Gen.G Esports win Game 3 vs LYON? |  | astatc-lol-gen-lyon-2026-11-04-game3 (team 5134) @0.78; astatc-lol-gen-lyon-2026-11-04-gam |
| lol | ESPORTS_MATCH_WINNER | WINNER/MATCH | 3 | Who will win in the upcoming esports event Gen.G Esports vs  |  | aec-lol-gen-lyon-2026-11-04 (team 5134) @0.90; aec-lol-gen-lyon-2026-11-04 (team 42093) @0 |
| lol | ESPORTS_PLAYER_KILLS | OTHER/UNKNOWN | 9 | Will Berserker record 8 or more kills in Games 1, 2 and 3 of | 8 | astatc-lol-gen-lyon-2026-11-04-k-berser-gte8 (team 42093); astatc-lol-gen-lyon-2026-11-04- |
| lol | ESPORTS_SERIES_GAME_HANDICAP | OTHER/UNKNOWN | 3 | Will the Gen.G Esports cover 1.5 vs the LYON in Gen.G Esport | 1.5 | asc-lol-gen-lyon-2026-11-04-hcap-pos-1pt5 (team 5134) @0.86; asc-lol-gen-lyon-2026-11-04-h |
| lol | ESPORTS_SERIES_TOTAL_GAMES | OTHER/UNKNOWN | 2 | Will the total in Gen.G Esports vs. LYON be more than 3.5? | 3.5 | tsc-lol-gen-lyon-2026-11-04-tot-3pt5 @0.44; tsc-lol-gen-lyon-2026-11-04-tot-3pt5 @0.47 |
| epl | SOCCER_TEAM_FULL_TIME_WINNER | WINNER/FULL_TIME | 30 | Will Everton FC win against Coventry City FC in the Premier  |  | atc-epl-eve-cov-2026-11-06-eve (team 2690) @0.56; atc-epl-eve-cov-2026-11-06-eve (team 269 |
| laliga | SOCCER_TEAM_FULL_TIME_WINNER | WINNER/FULL_TIME | 30 | Will Sevilla FC win against Deportivo Alaves in the La Liga  |  | atc-lal-sev-ala-2026-11-06-sev (team 3443) @0.49; atc-lal-sev-ala-2026-11-06-sev (team 344 |
| bundesliga | SOCCER_TEAM_FULL_TIME_WINNER | WINNER/FULL_TIME | 27 | Will Hamburger SV win against Borussia Monchengladbach in th |  | atc-bun-hsv-bmg-2026-11-06-hsv (team 3410) @0.39; atc-bun-hsv-bmg-2026-11-06-hsv (team 341 |
| seriea | SOCCER_TEAM_FULL_TIME_WINNER | WINNER/FULL_TIME | 30 | Will Venezia FC win against Udinese Calcio in the Serie A ma |  | atc-sea-ven-udi-2026-11-06-ven (team 7127) @0.44; atc-sea-ven-udi-2026-11-06-ven (team 712 |
| ligue1 | SOCCER_TEAM_FULL_TIME_WINNER | WINNER/FULL_TIME | 27 | Will Toulouse FC win against RC Strasbourg Alsace in the Lig |  | atc-lg1-tou-str-2026-11-06-tou (team 25611) @0.46; atc-lg1-tou-str-2026-11-06-tou (team 25 |

## All leagues

| Slug | Name | Operational |
|---|---|---|
| mlb | MLB | True |
| f1 | Formula 1 | True |
| boxing | Boxing | True |
| poly-open | Polymarket Open | True |
| itfm | ITF Men | True |
| itfw | ITF Women | True |
| fwc | World Cup | True |
| masters | Golf | True |
| cjcupbyr | THE CJ CUP Byron Nelson | True |
| ucl | UCL | True |
| epl | EPL | True |
| nbasl | NBA Summer League | True |
| cbb | CBB | True |
| wnba | WNBA | True |
| uefa | UEFA | True |
| mls | MLS | True |
| cham | TOUR Championship | True |
| cycling | Cycling | True |
| nhl | NHL | True |
| nfl | NFL | True |
| lal | La Liga | True |
| cws | CWS | True |
| bun | Bundesliga | True |
| ufc | UFC | True |
| wcbb | WCBB | True |
| cadi | Cadillac Championship | True |
| lol | League of Legends | True |
| onefmyrtbeac | ONEflight Myrtle Beach Classic | True |
| trui | Truist Championship | True |
| atpcq | ATP Challenger Qualifiers | True |
| ipl | IPL | True |
| rbcheri | RBC Heritage | True |
| flc | Chance Liga | True |
| cs2 | CS2 | True |
| charschw | Charles Schwab Challenge | True |
| cod | Call of Duty | True |
| twc | Worst Cup | True |
| valetexa | Valero Texas Open | True |
| test | Test International | True |
| indy500 | Indy 500 | True |
| pgacham | PGA Championship | True |
| nb1 | Hungarian NB I | True |
| memotour | the Memorial Tournament pres. by Workday | True |
| t20blast | T20 Blast (M) | True |
| mlsas | MLS All-Star Game | True |
| sea | Serie A | True |
| blw | Big League Wiffle Ball | True |
| mlc | Major League Cricket | True |
| valorant | Valorant | True |
| dota2 | Dota 2 | True |
| etpl | European T20 Premier League | True |
| ncaams | NCAA Men's Soccer | True |
| icaa | ICAA | True |
| rbccana | RBC Canadian Open | True |
| intf | Friendlies | True |
| ittf | ITTF | True |
| ttelite | TT Elite Series | True |
| t20blastw | T20 Blast (W) | True |
| itfme | ITF Mens | True |
| itfwo | ITF Womens | True |
| rockclas | Rocket Classic | True |
| lmx | Liga MX | True |
| us | U.S. Open | True |
| mlp | Major League Pickleball | True |
| t20i | T20 International (M) | True |
| t20iw | T20 International (W) | True |
| kbo | KBO | True |
| 3m | 3M Open | True |
| pdcdarts | Professional Darts Corporation | True |
| ligpor | Liga Portugal | True |
| npb | NPB | True |
| wtt | WTT | True |
| travcham | Travelers Championship | True |
| t20worldcupw | Women's T20 World Cup | True |
| dodgeball | Dodgeball | True |
| cfb | CFB | True |
| cpl | Caribbean Premier League | True |
| spl | Saudi Pro League | True |
| motogp | MotoGP | True |
| corapunt | Corales Puntacana Championship | True |
| fibawcq | FIBA | True |
| usc | UEFA Super Cup | True |
| egpl | Egyptian Premier League | True |
| czechligapro | Czech Liga Pro | True |
| russialigapro | Russia Liga Pro | True |
| genescot | Genesis Scottish Open | True |
| ttcup | TT Cup | True |
| setkacup | Setka Cup | True |
| ttchallenger | Challenger Series | True |
| wincup | Win Cup | True |
| tsl | Süper Lig | True |
| iscocham | ISCO Championship | True |
| misc | Misc | True |
| sclc | Scottish League Cup | True |
| johndeer | John Deere Classic | True |
| ekst | Ekstraklasa | True |
| theopen | The Open | True |
| svnp | PrvaLiga | True |
| atbl | Austrian Bundesliga | True |
| uslc | USL Championship | True |
| alsv | Allsvenskan | True |
| bra | Brasileirão | True |
| brb | Série B | True |
| kl1 | K League 1 | True |
| cpbl | Chinese Professional Baseball League | True |
| els | Eliteserien | True |
| csl | CSL | True |
| nor1 | OBOS-ligaen | True |
| lpa | Liga Argentina | True |
| pl1 | Liga 1 | True |
| slr | SuperLiga | True |
| lco | Liga Colombia | True |
| rpl | RPL | True |
| pdc | Primera Chile | True |
| nls | Niké Liga | True |
| sld | Superliga | True |
| lng | Liga Nacional | True |
| lpc | Liga Promérica | True |
| ecu1 | LigaPro Ecuador | True |
| den1 | Danish 1. Division | True |
| irlp | LOI Premier Division | True |
| irl1 | LOI First Division | True |
| vkl | Veikkausliiga | True |
| dfb | DFB-Pokal | True |
| danigolf | Danish Golf Championship | True |
| cshield | Community Shield | True |
| wsl | WSL | True |
| dflsc | DFL-Supercup | True |
| scp | Scottish Prem | True |
| uel | UEL | True |
| uecl | UECL | True |
| sud | Sudamericana | True |
| auc | Australia Cup | True |
| ofb | ÖFB Cup | True |
| nwsl | NWSL | True |
| uwcl | UWCL | True |
| iplcr | IPL CR | True |
| mlccr | Major League Cricket CR | True |
| womessco | Women's Scottish Open | True |
| portclas | Portland Classic | True |
| t20worldcupwcr | Women's T20 World Cup CR | True |
| espnocho | The Ocho | True |
| polyclas | The Polymarket Classic | False |
| cplcr | Caribbean Premier League CR | True |
| swsl | Swiss Super League | True |
| pvl | Parva Liga | True |
| cfac | Chinese FA Cup | True |
| clbf | Club Friendlies | True |
| ykk | Ykkösliiga | True |
| uzb1 | Uzbekistan Superliga | True |
| swe2 | Superettan | True |
| testcr | Test Intl | True |
| swcl | Challenge League | True |
| uru1 | Primera Uruguay | True |
| lexp | Liga de Expansión MX | True |
| arg2 | Primera Nacional | True |
| t20blastwcr | T20 Blast (W) CR | True |
| t20iwcr | T20 Intl (W) | True |
| t20blastcr | T20 Blast (M) CR | True |
| odiwcr | ODI Intl (W) | True |
| t20icr | T20 Intl (M) | True |
| odicr | ODI (M) | True |
| setkameua | Setka Cup Ukraine Men | True |
| setkamemd | Setka Cup Moldova Men | True |
| setkamecz | Setka Cup Czechia Men | True |
| setkawoua | Setka Cup Ukraine Women | True |
| rl | Rocket League | True |
| ow | Overwatch | True |
| r6 | Rainbow Six Siege | True |
| isl1 | Besta deild | True |
| par2 | Paraguay Segunda | True |
| btla | Botola Pro | True |
| nascar | NASCAR | True |
| hundred | The Hundred | True |
| hundredw | The Hundred Women | True |
| t20gsl | T20 Global Super League | True |
| odcup | One-Day Cup | True |
| acle | AFC Champions League Elite | True |
| cop | Coppa Italia | True |
| usoc | US Open Cup | True |
| ere | Eredivisie | True |
| lig2 | Ligue 2 | True |
| womes | Women's Open | True |
| cdb | Copa do Brasil | True |
| eflc | EFL Cup | True |
| lgscup | Leagues Cup | True |
| wyndcham | Wyndham Championship | True |
| ncaaws | NCAA Women's Soccer | True |
| bmwcham | BMW Championship | True |
| unitking | United Kingdom Individual | True |
| lpb | Liga Boliviana | True |
| newyorki | New York Individual | True |
| tdc | Trophée des Champions | True |
| lg1 | Ligue 1 | True |
| lib | Copa Libertadores | True |
| eflch | EFL Championship | True |
| lal2 | LaLiga 2 | True |
| srb | Serie B | True |
| tdp | Taça de Portugal | True |
| fedestju | FedEx St. Jude Championship | True |
| prescup | Presidents Cup | True |
| bmwpgach | BMW PGA Championship | True |
| uaepl | UAE Pro League | True |
| euromast | European Masters | True |
| wtadb | WTA Doubles | True |
| fmcham | FM Championship | True |
| atpdb | ATP Doubles | True |
| iris | Irish Open | True |
| britmast | British Masters | True |
| utr | UTR | True |
| bbl | Basketball Bundesliga | True |
| county | County Championship | True |
| dwcs | Dana White's Contender Series | True |
| indiindi | Indianapolis Individual | True |
| cpkcwome | CPKC Women's Open | True |
| modus | MODUS Super Series | True |
| fibawwc | FIBA Women's World Cup | True |
| baycclas | Baycurrent Classic | True |
| nexocham | Nexo Championship | True |
| bankutah | Bank of Utah Championship | True |
| cmpcup | Campeones Cup | True |
| nbl | Australia NBL | True |
| nwarkach | NW Arkansas Championship | True |
| defran | Open de France | True |
| polandmasters | Poland Masters | True |
| liv | LIV Golf | True |
| lpga | LPGA | True |
| dpwt | DP World Tour | True |
| natichil | Nationwide Children's Hospital Championship | True |
| pureinsu | Pure Insurance Championship | True |
| biltcham | Biltmore Championship Asheville | True |
| acb | Spain Liga ACB | True |
| wta | WTA | True |
| atp | ATP | True |
| alfrdunh | Alfred Dunhill Links Championship | True |
| lnbp | LNBP | True |
| bcl | Basketball Champions League | True |
| ahl | AHL | True |
| lnb | France LNB Elite | True |
| eurolg | EuroLeague | True |
| pll | Premier Lacrosse League | True |
| ppa | The Pro Tour of Pickleball | True |
| khl | KHL | True |
| compsolu | Compliance Solutions Championship | True |
| del | DEL | True |
| buiclpga | Buick LPGA Shanghai | True |
| indicham | India Championship | True |
| sascham | SAS Championship | True |
| deespa | Open de Espana | True |
| kornferr | Korn Ferry Tour Championship | True |
| consfury | Constellation Furyk & Friends | True |
| ebattlesefia | eBattles: International A | True |
| ebattlesefib | eBattles: International B | True |
| ebattlesefcwc | eBattles: Club World Cup | True |
| ebattlesefwca | eBattles: World Cup A | True |
| ebattlesefwcb | eBattles: World Cup B | True |
| ebattlesefpl | eBattles: Premier League | True |
| ebattlesefsa | eBattles: Serie A | True |
| vtb | VTB United League | True |
| daviscup | Davis Cup | True |
| lavercup | Laver Cup | True |
| gbl | Greece GBL | True |
| denbl | Denmark Basketligaen | True |
| slnbl | Slovenia Liga OTP banka | True |
| svkbl | Slovakia SBL | True |
| hunbl | Hungary NB I/A | True |
| fra2 | France Elite 2 | True |
| unl | UEFA Nations League | True |
| grcup | Greek Cup | True |
| bsl | Turkey BSL | True |
| lba | Italy LBA Serie A | True |
| lkl | Lithuania LKL | True |
| buttberm | Butterfield Bermuda Championship | True |
| lottcham | LOTTE Championship | True |
| lehivall | Lehigh Valley Classic | True |
| cnl | CONCACAF Nations League | True |
| shl | SHL | True |
| snhl | National League | True |
| cehl | Czech Extraliga | True |
| j1 | J1 League | True |
| j2 | J2 League | True |
| par1 | Paraguay Primera División | True |
| bun2 | 2. Bundesliga | True |
| tff1 | TFF 1. Lig | True |
| bel1 | Belgian Pro League | True |
| fnl | Czech National Football League | True |
| grsl | Super League Greece | True |
| idnsl | Indonesia Super League | True |
| hnl | Croatian HNL | True |
| efl1 | EFL League One | True |
| efl2 | EFL League Two | True |
| engnl | English National League | True |
| thai1 | Thai League 1 | True |
| mysl | Malaysia Super League | True |
| serca | Serie C Girone A | True |
| sercb | Serie C Girone B | True |
| sercc | Serie C Girone C | True |
| brc | Brasileirão Série C | True |
| ligaf | Liga F | True |
| sapl | South African Premiership | True |
| cyp1 | Cyprus First Division | True |
| fbl | Frauen-Bundesliga | True |
| cba | China CBA | True |
| eurocup | EuroCup | True |
| kbl | Korean Basketball League | True |
| bjkcup | Billie Jean King Cup | True |
| jpbl | Japan B.League Premier | True |
| slb | British Super League Basketball | True |
| ita2 | Italian Serie A2 | True |
| autbl | Austrian Superliga | True |
| sixkings | Six Kings Slam | True |
| uslcp | USL Cup | True |
| afcq | Africa Cup of Nations Qualification | True |
| czcup | Czech Cup | True |
| nrl | NRL | True |
| nrlw | NRLW | True |
| superleague | Super League | True |
| urc | United Rugby Championship | True |
| bolcup | Copa Bolivia | True |
| bmwladic | BMW Ladies Championship | True |
| svk2 | Slovak 2. Liga | True |
| prem | PREM Rugby | True |
| top14 | TOP 14 | True |
| liiga | Liiga | True |
| arfa | Torneo Regional Federal Amateur | False |
| urupda | Uruguay Primera Divisional C | False |
| nscup | North of Scotland Cup | False |
| maybcham | Maybank Championship | True |
| vidamexi | VidantaWorld Mexico Open | True |
| asgames | Asian Games Men's Football | True |
| aseanc | ASEAN Cup Challenge Division | True |
| genecham | Genesis Championship | True |
| stifchar | Stifel Charity Classic | True |
| u19f | U19 International Friendlies | True |
| ilaln | Israel Liga Alef North | True |
| ilals | Israel Liga Alef South | True |
| caru20 | Carioca U20 | True |
| mne2 | Montenegro Second League | True |
| nmcup | Norwegian Cup | True |
| wecq | UEFA Women's Europa Cup Qualifying | True |
| norw1 | Norway Women's First Division | True |
| ngnpfl | Nigeria NPFL | True |
| ghpl | Ghana Premier League | True |
| cpreina | Copa de la Reina | True |
| u21eq | UEFA U21 European Championship Qualifying | True |
| svn3e | Slovenia Third League East | True |
| cpafed | Copa Federación | True |
| be1acff | Belgium Nationale 1 ACFF | True |
| be1vv | Belgium Nationale 1 VV | True |
| fawlc | FA Women's League Cup | True |
| minw | Campeonato Mineiro Women | True |
| peu20 | Pernambucano U20 | True |
| gaub | Gaúcho Série B U23 | True |
| ch1cl | Swiss 1. Liga Classic | True |
| cpauy | Copa Uruguay | True |
| slps | Southern League Premier South | True |
| isthp | Isthmian League Premier | True |
| ven2 | Venezuela Segunda División | True |
| cpapy | Copa Paraguay | True |
| gtasc | Guatemala Primera División de Ascenso | True |
| cpach | Copa Chile | True |
| one | ONE Championship | True |
| pfl | Professional Fighters League | True |
| bledisloe | Bledisloe Cup | True |
| uwwcq | UEFA Women's World Cup Qualifying | True |
| powerslap | Power Slap | True |
| aba | Adriatic ABA League | True |
| cznbl | Czech NBL | True |
| koris | Korisliiga | True |
| nba | NBA | True |
| bsktcua | BSKT Cup | True |
| bsktcin | BSKT Cup International | True |
| lfa | LFA | True |
| rsmclas | The RSM Classic | True |
| rlwc | RLWC | True |
| bkfc | BKFC | True |
| bskt3x3 | BSKT Cup 3x3 | True |
| acw | Astra Cup Women | True |
| abudhabc | Abu Dhabi Championship | True |
| dpworlch | DP World Tour Championship | True |
| anni | ANNIKA | True |
| ebattlesebb | eBattles: eBasketball | True |
| austcham | Austin Championship | True |
| ebattlesebbec | eBattles: eBasketball European Conference | True |
| worlwide | World Wide Technology Championship | True |
| totojapa | Toto Japan Classic | True |
| cmegrouc | CME Group Tour Championship | True |
| simmbank | Simmons Bank Championship | True |
| pga | PGA Tour | True |
| heroworl | Hero World Challenge | True |
| masttour | Masters Tournament | True |
| austpgac | Australian PGA Championship | True |
| aust | Australian Open | True |
| nedbgolf | Nedbank Golf Challenge | True |
