    returns : pd.Series
        Returns for each day in the date range.
        - Example:
            2017-01-01   -0.017098
            2017-01-02    0.002683
            2017-01-03   -0.008669
    positions: pd.DataFrame
        Daily holdings (in dollars or percentages), indexed by date.
        Will be converted to percentages if positions are in dollars.
        Short positions show up as cash in the 'cash' column.
        - Examples:
                        AAPL  TLT  XOM  cash
            2017-01-01    34   58   10     0
            2017-01-02    22   77   18     0
            2017-01-03   -15   27   30    15
                            AAPL       TLT       XOM  cash
            2017-01-01  0.333333  0.568627  0.098039   0.0
            2017-01-02  0.188034  0.658120  0.153846   0.0
            2017-01-03  0.208333  0.375000  0.416667   0.0
    factor_returns : pd.DataFrame
        Returns by factor, with date as index and factors as columns
        - Example:
                        momentum  reversal
            2017-01-01  0.002779 -0.005453
            2017-01-02  0.001096  0.010290
    factor_loadings : pd.DataFrame
        Factor loadings for all days in the date range, with date and ticker as
        index, and factors as columns.
        - Example:
                               momentum  reversal
            dt         ticker
            2017-01-01 AAPL   -1.592914  0.852830
                       TLT     0.184864  0.895534
                       XOM     0.993160  1.149353
            2017-01-02 AAPL   -0.140009 -0.524952
                       TLT    -1.066978  0.185435
                       XOM    -1.798401  0.761549
    transactions : pd.DataFrame, optional
        Executed trade volumes and fill prices. Used to check the turnover of
        the algorithm. Default is None, in which case the turnover check is
        skipped.
        - One row per trade.
        - Trades on different names that occur at the
          same time will have identical indicies.
        - Example:
            index                  amount   price    symbol
            2004-01-09 12:18:01    483      324.12   'AAPL'
            2004-01-09 12:18:01    122      83.10    'MSFT'
            2004-01-13 14:12:23    -75      340.43   'AAPL'

