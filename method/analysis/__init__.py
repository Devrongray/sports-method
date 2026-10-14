"""Daily analysis of the recorded data (data branch) for the 90-day tests.

    load.py     read the gzipped NDJSON/JSON records into DataFrames
    match.py    pair Polymarket US events with Pinnacle (Odds API) events
    compare.py  Polymarket mid vs de-vigged Pinnacle fair, spreads and depth
    calib.py    test (b): calibration of last pre-game mids once games settle
    newsjoin.py test (a) preparation: price paths around news timestamps
    report.py   CLI: python -m method.analysis.report --data data --out analysis/daily
"""
