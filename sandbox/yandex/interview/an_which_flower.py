import pandas as pd

df_count = pd.read_csv("detection_count.csv")
df_quality = pd.read_csv("detection_quality.csv")

df_correct = df_quality[df_quality['detected_name'] == df_quality['human_name']]
correct_counts = df_correct['detected_name'].value_counts()
popular_flowers = set(correct_counts[correct_counts >= 10].index)

df_errors = df_quality[df_quality['detected_name'] != df_quality['human_name']]
not_flower_probs = df_errors.groupby('detected_name').apply(
    lambda g: (g['human_name'] == 'not_a_flower').mean()
)

default_not_flower_prob = (df_quality['human_name'] == 'not_a_flower').mean()
correct_probs = df_quality.groupby('detected_name').apply(
    lambda g: (g['detected_name'] == g['human_name']).mean()
)

all_detected = set(df_count['detected_name'])
rare_flowers = all_detected - popular_flowers - {'not_a_flower'}

rare_not_flower_prob = not_flower_probs.get(rare_flowers).mean()
rare_correct_prob = correct_probs.get(rare_flowers).mean()

naf_quality = df_quality[df_quality['detected_name'] == 'not_a_flower']
naf_accuracy = (naf_quality['human_name'] == 'not_a_flower').mean()
naf_count = df_count[df_count['detected_name'] == 'not_a_flower']['count'].sum()

total_weight = 0
weighted_quality = 0

for _, row in df_count.iterrows():
    name = row['detected_name']
    count = row['count']
    if name == 'not_a_flower':
        prob = 1 - default_not_flower_prob
        quality = naf_accuracy
    elif name in popular_flowers:
        prob = 1 - not_flower_probs.get(name, default_not_flower_prob)
        quality = correct_probs.get(name, 0)
    else:
        prob = 1 - not_flower_probs.get(name, default_not_flower_prob)
        quality = correct_probs.get(name, 0)
    weighted_quality += count * prob * quality
    total_weight += count

final_score = weighted_quality / total_weight
print(f"{final_score:.4f}")
