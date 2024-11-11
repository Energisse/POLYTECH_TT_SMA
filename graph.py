import pandas as pd
import matplotlib.pyplot as plt

# Charger le fichier CSV
df = pd.read_csv('data.csv', sep=';')

# Calculer la moyenne des valeurs pour chaque combinaison de 'nbrPas', 'nbrPatrouilleurs', 'cognitif' et 'step'
moyennes_df = df.groupby(['nbrPas', 'nbrPatrouilleurs', 'cognitif', 'step','reactif'], as_index=False)['value'].mean()

# Récupérer les combinaisons uniques de 'nbrPas', 'nbrPatrouilleurs' et 'cognitif' pour créer un graphique pour chaque groupe
groupes_uniques = moyennes_df[['nbrPas', 'nbrPatrouilleurs', 'cognitif','reactif']].drop_duplicates()

# Créer un graphique pour chaque combinaison de 'nbrPas', 'nbrPatrouilleurs' et 'cognitif'
for _, row in groupes_uniques.iterrows():
    nbrPas = row['nbrPas']
    nbrPatrouilleurs = row['nbrPatrouilleurs']
    cognitif = row['cognitif']
    reactif = row['reactif']
    
    # Filtrer les données pour ce groupe
    subset = moyennes_df[(moyennes_df['nbrPas'] == nbrPas) & 
                         (moyennes_df['nbrPatrouilleurs'] == nbrPatrouilleurs) & 
                         (moyennes_df['cognitif'] == cognitif)& (moyennes_df['reactif'] == reactif)
                         ]
    plt.figure()
    plt.plot(subset['step'], subset['value'], marker='o')
    plt.xlabel('Step')
    plt.ylabel('Valeur Moyenne')
    plt.title(f'Moyenne pour nbrPatrouilleurs={nbrPatrouilleurs}, {"cognitif" if cognitif else ("reactif" if reactif else "aléatoire")}')
    plt.grid(True)
    plt.savefig(f'graphique_{nbrPatrouilleurs}_{"cognitif" if cognitif else ("reactif" if reactif else "aléatoire")}.png')
