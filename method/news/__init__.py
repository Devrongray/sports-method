"""News-timestamp recorders for test (a): when did the information arrive?

Each recorder polls a source and writes a timestamped record only when the
source's content changed since the previous poll in the same run (and always
on the first poll of a run). The analysis step later joins these change
times to the Polymarket US price paths and the Pinnacle snapshots.

    mlb.py   MLB StatsAPI: posted lineups and probable pitchers (official)
    nba.py   NBA official injury report PDFs (official; raw text kept)
    nhl.py   DailyFaceoff starting-goalie page (raw HTML kept; parsed later),
             only when robots.txt allows it
"""
