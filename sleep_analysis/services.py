# sudo apt-get install python3.7-dev to get numpy to install
import pandas as pd

class SleepDuration:
    fly_has_been_sleeping = 0

    def __init__(self, fly, interval, min_bout, duration, start_day, start_hour, start_minute):
        self.fly = fly
        self.interval = interval
        self.min_bout = min_bout
        self.duration = duration
        self.start_day = start_day
        self.start_hour = start_hour
        self.start_minute = start_minute

    def calculate(self):
        # for the fly get all data where activity is 0

        pass

    def is_sleeping_at(self, start_day, start_hour, start_minute):
        pass

    def fly_starting_sleeping(self):
        pass

"""
>>> df['changed'] = (df['fly5'] > 0).astype(int).diff().fillna(1).astype(int)
>>> df
      id       date      time  control  control2  something  huh fly1  fly2  fly3  fly4  fly5  fly6            datetime  changed
0  27242  13 Mar 19  11:16:00        1         0         37    0   Ct     0     1     3     0     4 2019-03-13 11:16:00        1
1  27243  13 Mar 19  11:17:00        1         0         37    0   Ct     0     1     3     0     0 2019-03-13 11:17:00        0
2  27244  13 Mar 19  11:18:00        1         0         37    0   Ct     0     1     2     0     4 2019-03-13 11:18:00        0
3  27245  13 Mar 19  11:19:00        1         0         37    0   Ct     0     1     5     6     1 2019-03-13 11:19:00        1
4  27246  13 Mar 19  11:20:00        1         0         37    0   Ct     0     1     0     0     0 2019-03-13 11:20:00       -1
5  27247  13 Mar 19  11:21:00        1         0         37    0   Ct     0     1     1     1     1 2019-03-13 11:21:00        1
6  27248  13 Mar 19  11:22:00        1         0         37    0   Ct     0     1     0     0     2 2019-03-13 11:22:00       -1
7  27249  13 Mar 19  11:23:00        1         0         37    0   Ct     0     1     1     0     3 2019-03-13 11:23:00        0
8  27250  13 Mar 19  11:24:00        1         0         37    0   Ct     0     1     1     0     2 2019-03-13 11:24:00        0
9  27251  13 Mar 19  11:25:00        1         0         37    0   Ct     0     1     3     0     1 2019-03-13 11:25:00        0

>>> df['changed'] = (df['fly5'] > 0).astype(int).diff().fillna(0).astype(int)
>>> df
      id       date      time  control  control2  something  huh fly1  fly2  fly3  fly4  fly5  fly6            datetime  changed
0  27242  13 Mar 19  11:16:00        1         0         37    0   Ct     0     1     3     0     4 2019-03-13 11:16:00        0
1  27243  13 Mar 19  11:17:00        1         0         37    0   Ct     0     1     3     0     0 2019-03-13 11:17:00        0
2  27244  13 Mar 19  11:18:00        1         0         37    0   Ct     0     1     2     0     4 2019-03-13 11:18:00        0
3  27245  13 Mar 19  11:19:00        1         0         37    0   Ct     0     1     5     6     1 2019-03-13 11:19:00        1
4  27246  13 Mar 19  11:20:00        1         0         37    0   Ct     0     1     0     0     0 2019-03-13 11:20:00       -1
5  27247  13 Mar 19  11:21:00        1         0         37    0   Ct     0     1     1     1     1 2019-03-13 11:21:00        1
6  27248  13 Mar 19  11:22:00        1         0         37    0   Ct     0     1     0     0     2 2019-03-13 11:22:00       -1
7  27249  13 Mar 19  11:23:00        1         0         37    0   Ct     0     1     1     0     3 2019-03-13 11:23:00        0
8  27250  13 Mar 19  11:24:00        1         0         37    0   Ct     0     1     1     0     2 2019-03-13 11:24:00        0
9  27251  13 Mar 19  11:25:00        1         0         37    0   Ct     0     1     3     0     1 2019-03-13 11:25:00        0
>>> df['changed'] = (df['fly5'] > 0).astype(int).diff().fillna(-1).astype(int)
>>> df
      id       date      time  control  control2  something  huh fly1  fly2  fly3  fly4  fly5  fly6            datetime  changed
0  27242  13 Mar 19  11:16:00        1         0         37    0   Ct     0     1     3     0     4 2019-03-13 11:16:00       -1
1  27243  13 Mar 19  11:17:00        1         0         37    0   Ct     0     1     3     0     0 2019-03-13 11:17:00        0
2  27244  13 Mar 19  11:18:00        1         0         37    0   Ct     0     1     2     0     4 2019-03-13 11:18:00        0
3  27245  13 Mar 19  11:19:00        1         0         37    0   Ct     0     1     5     6     1 2019-03-13 11:19:00        1
4  27246  13 Mar 19  11:20:00        1         0         37    0   Ct     0     1     0     0     0 2019-03-13 11:20:00       -1
5  27247  13 Mar 19  11:21:00        1         0         37    0   Ct     0     1     1     1     1 2019-03-13 11:21:00        1
6  27248  13 Mar 19  11:22:00        1         0         37    0   Ct     0     1     0     0     2 2019-03-13 11:22:00       -1
7  27249  13 Mar 19  11:23:00        1         0         37    0   Ct     0     1     1     0     3 2019-03-13 11:23:00        0
8  27250  13 Mar 19  11:24:00        1         0         37    0   Ct     0     1     1     0     2 2019-03-13 11:24:00        0
9  27251  13 Mar 19  11:25:00        1         0         37    0   Ct     0     1     3     0     1 2019-03-13 11:25:00        0
>>> df['changed'] = (df['fly5'] > 0).astype(int).diff().fillna(-1).astype(int)
>>> df
      id       date      time  control  control2  something  huh fly1  fly2  fly3  fly4  fly5  fly6            datetime  changed
0  27242  13 Mar 19  11:16:00        1         0         37    0   Ct     0     1     3     0     4 2019-03-13 11:16:00       -1
1  27243  13 Mar 19  11:17:00        1         0         37    0   Ct     0     1     3     0     0 2019-03-13 11:17:00        0
2  27244  13 Mar 19  11:18:00        1         0         37    0   Ct     0     1     2     0     4 2019-03-13 11:18:00        0
3  27245  13 Mar 19  11:19:00        1         0         37    0   Ct     0     1     5     6     1 2019-03-13 11:19:00        1
4  27246  13 Mar 19  11:20:00        1         0         37    0   Ct     0     1     0     0     0 2019-03-13 11:20:00       -1
5  27247  13 Mar 19  11:21:00        1         0         37    0   Ct     0     1     1     1     1 2019-03-13 11:21:00        1
6  27248  13 Mar 19  11:22:00        1         0         37    0   Ct     0     1     0     0     2 2019-03-13 11:22:00       -1
7  27249  13 Mar 19  11:23:00        1         0         37    0   Ct     0     1     1     0     3 2019-03-13 11:23:00        0
8  27250  13 Mar 19  11:24:00        1         0         37    0   Ct     0     1     1     0     2 2019-03-13 11:24:00        0
9  27251  13 Mar 19  11:25:00        1         0         37    0   Ct     0     1     3     0     1 2019-03-13 11:25:00        0
>>> df2 = pd.DataFrame({'start': df.loc[df.changed == -1 , 'datetime'].reset_index(drop=True), 'end': df.loc[df.changed == 1, 'datetime'].reset_index(drop=True)})

>>> df2
                start                 end
0 2019-03-13 11:16:00 2019-03-13 11:19:00
1 2019-03-13 11:20:00 2019-03-13 11:21:00
2 2019-03-13 11:22:00                 NaT
>>> df2['diff'] = df2['end'] - df2['start']
>>> df2
                start                 end     diff
0 2019-03-13 11:16:00 2019-03-13 11:19:00 00:03:00
1 2019-03-13 11:20:00 2019-03-13 11:21:00 00:01:00
2 2019-03-13 11:22:00                 NaT      NaT

>>> df2[df2['diff'] > pd.Timedelta('1 min')]
                start                 end     diff
0 2019-03-13 11:16:00 2019-03-13 11:19:00 00:03:00
>>> df2
                start                 end     diff
0 2019-03-13 11:16:00 2019-03-13 11:19:00 00:03:00
1 2019-03-13 11:20:00 2019-03-13 11:21:00 00:01:00
2 2019-03-13 11:22:00                 NaT      NaT
>>> df2[df2['diff'] >= pd.Timedelta('1 min')]
                start                 end     diff
0 2019-03-13 11:16:00 2019-03-13 11:19:00 00:03:00
1 2019-03-13 11:20:00 2019-03-13 11:21:00 00:01:00
>>> df2[df2['diff'] >= pd.Timedelta('1 min')].sum()
Series([], dtype: float64)
>>> df2[df2['diff'] >= pd.Timedelta('1 min')]['diff']
0   00:03:00
1   00:01:00
Name: diff, dtype: timedelta64[ns]
>>> df2[df2['diff'] >= pd.Timedelta('1 min')]['diff'].sum()
Timedelta('0 days 00:04:00')
"""