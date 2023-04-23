import pandas as pd 
codes = [70378 , 85540 , 14109 , 15236 ,14480 ]
volts  = [2400 , 3900 , 5100 ,11700]

for code in codes :
        
        for volt in volts :
                print(f'{code}+{volt}')