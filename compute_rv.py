import pandas as pd

def compute_re24(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute the re24 and re24_change columns and add them to a given dataframe.
    
    Parameters:
    - df (pd.DataFrame): The input dataframe containing play-by-play baseball data.
    
    Returns:
    - pd.DataFrame: The dataframe with the added re24 and re24_change columns.
    """
    
    # Compute runs scored in a play
    df = df.loc[df['inning'] <= 9] # Remove extra innings      
    df = df.sort_values(by=['game_pk', 'at_bat_number', 'pitch_number'], ascending=True)
    df['runs_scored_play'] = df['post_bat_score'] - df['bat_score']
    
    # Compute runner columns and concatenate to form runners column
    df['runner_1b'] = df['on_1b'].notna().astype(int)
    df['runner_2b'] = df['on_2b'].notna().astype(int)
    df['runner_3b'] = df['on_3b'].notna().astype(int)
    df['runners'] = df['runner_1b'].astype(str) + df['runner_2b'].astype(str) + df['runner_3b'].astype(str)
    
    # Compute half_inning column
    df['half_inning'] = df['game_pk'].astype(str) + ' ' + df['inning'].astype(str) + ' ' + df['inning_topbot'].astype(str)
    
    # Group by half_inning to compute runs scored in the inning
    runs_scored = df.groupby('half_inning', as_index=False)[['bat_score', 'post_bat_score']].agg(['min', 'max'])
    runs_scored.columns = runs_scored.columns.map('_'.join)
    runs_scored['runs_scored_inning_total'] = runs_scored['post_bat_score_max'] - runs_scored['bat_score_min']
    
    # Merge runs_scored_inning_total with the original dataframe
    runs_scored_inning_total = runs_scored[['bat_score_min', 'runs_scored_inning_total']].reset_index()
    df = pd.merge(df, runs_scored_inning_total, on='half_inning', how='left')
    
    # Compute runs scored for the rest of the inning
    df['runs_scored_rest_of_inning'] = df['runs_scored_inning_total'] - (df['bat_score'] - df['bat_score_min'])
    
    # Compute re24 values
    re_24 = df.groupby(['outs_when_up', 'runners'])['runs_scored_rest_of_inning'].mean().round(2).reset_index().rename(columns={'runs_scored_rest_of_inning': 're24'})
    df = pd.merge(df, re_24, on=['outs_when_up', 'runners'], how='left')
    
    # Compute re24_change values
    df['re24_change'] = df.groupby('half_inning').re24.diff().shift(-1)
    df['re24_change'] = df['re24_change'] + df['runs_scored_play']
    
    return df