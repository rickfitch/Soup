from get_numbers import get_numbers
import numpy as np
import pandas as pd
import datetime


def main():
    today = np.array(get_numbers())
    draw_number = today[0]
    date = today[1] 
    print(date)   

    df_today = pd.DataFrame(today)

    try:
        df_existing = pd.read_excel('today.xlsx')
        df_final = pd.concat([df_existing, df_today])
    except FileNotFoundError:
        df_final = df_today

    df_final.to_excel('today.xlsx', index=False)

    print(df_today)
    df_today.to_csv('today.csv', index=False, header=False, mode='a')
    

if __name__ == "__main__":
    main()