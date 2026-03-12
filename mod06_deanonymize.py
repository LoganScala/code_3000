import pandas as pd

def load_data(anonymized_path, auxiliary_path):
    """
    Load anonymized and auxiliary datasets.
    """
    anon = pd.read_csv(anonymized_path)
    aux = pd.read_csv(auxiliary_path)
    return anon, aux


def link_records(anon_df, aux_df):
    final_matches = []
    for i in range(len(anon_df)):
        current_anon = anon_df.iloc[i] 
        matches_found = []
        for j in range(len(aux_df)):
            current_aux = aux_df.iloc[j]
            if current_anon['age'] == current_aux['age']:
                if current_anon['gender'] == current_aux['gender']:
                    if current_anon['zip3'] == current_aux['zip3']:
                        matches_found.append(current_aux['name'])
        if len(matches_found) == 1:
            match_data = {
                'anon_id': current_anon['anon_id'],
                'matched_name': matches_found[0]
            }
            final_matches.append(match_data)
    return pd.DataFrame(final_matches)

def deanonymization_rate(matches_df, anon_df):
        
    return len(matches_df)/len(anon_df)