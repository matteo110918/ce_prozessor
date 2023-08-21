import pandas as pd
import chardet
from datetime import datetime

# Definiere die Pfade
file_path_ceramic = 'data/Spare part catalog - Ceramics.txt'
file_path_corrugated = 'data/Spare part catalog - Corrugated Single Pass.txt'
file_path_habitat_varijet = 'data/Spare part catalog - Habitat and Varijet.txt'
file_path_label = 'data/Spare part catalog - Label.txt'
file_path_lfp_graphics = 'data/Spare part catalog - LFP and Graphics.txt'
file_path_lfp_peripherie = 'data/Spare part catalog_LFP_Peripherie.txt'

path_list = [file_path_corrugated, file_path_habitat_varijet, file_path_label, file_path_lfp_graphics, file_path_lfp_peripherie]


# Lese alle Files ein
df_ceramic = pd.read_csv(file_path_ceramic, delimiter='\t', encoding='utf-16', skiprows=0)
df_corrugated = pd.read_csv(file_path_corrugated, delimiter='\t', encoding='utf-16', skiprows=0)
df_habitat_varijet = pd.read_csv(file_path_habitat_varijet, delimiter='\t', encoding='utf-16', skiprows=0)
df_label = pd.read_csv(file_path_label, delimiter='\t', encoding='utf-16', skiprows=0)
df_lfp_graphics = pd.read_csv(file_path_lfp_graphics, delimiter='\t', encoding='utf-16', skiprows=0)
df_lfp_peripherie = pd.read_csv(file_path_lfp_peripherie, delimiter='\t', encoding='utf-16', skiprows=0)

# Struktur harmonisieren
df_ceramic_filtered = df_ceramic[['Code', 'TOC element name', 'Vertriebstext DE', 'Vertriebstext EN', 'Nota_Association_2', 'Nota_Association_1', 'SerialNumer_Association',
       'SerialNumer_Association.1', 'HTS Code', 'Herkunftsland', 'Gewicht', 'Gewicht Einheit', 'Path 2', 'Path 3', 'Path 4', 'Path 5']]
df_lfp_graphics_filtered = df_lfp_graphics[['Code', 'Hauptknoten Name', 'Vertriebstext DE', 'Vertriebstext EN', 'Nota_Association_2', 'Nota_Association_1', 'SerialNumer_Association',
       'SerialNumer_Association.1', 'HTS Code', 'Herkunftsland', 'Gewicht', 'Gewicht Einheit', 'Path 2', 'Path 3', 'Path 4', 'Path 5']]
df_label_filtered = df_label[['Code', 'TOC element name', 'Vertriebstext DE', 'Vertriebstext EN', 'Nota_Association_2', 'Nota_Association_1', 'SerialNumer_Association',
       'SerialNumer_Association.1', 'HTS Code', 'Herkunftsland', 'Gewicht', 'Gewicht Einheit', 'Path 2', 'Path 3', 'Path 4', 'Path 5']]
df_habitat_varijet_filtered = df_habitat_varijet[['Code', 'TOC element name', 'Vertriebstext DE', 'Vertriebstext EN', 'Nota_Association_2', 'Nota_Association_1', 'SerialNumer_Association',
       'SerialNumer_Association.1', 'HTS Code', 'Herkunftsland', 'Gewicht', 'Gewicht Einheit', 'Path 2', 'Path 3', 'Path 4', 'Path 5']]
df_lfp_peripherie_filtered = df_lfp_peripherie[['Code', 'Hauptknoten Name', 'Vertriebstext DE', 'Vertriebstext EN', 'Nota_Association_2', 'Nota_Association_1', 'SerialNumer_Association',
       'SerialNumer_Association.1', 'HTS Code', 'Herkunftsland', 'Gewicht', 'Gewicht Einheit']]

# Spalten Namen harmonisieren
df_ceramic_filtered.rename(columns={'TOC element name': 'Hauptknoten Name'}, inplace=True)
df_label_filtered.rename(columns={'TOC element name': 'Hauptknoten Name'}, inplace=True)
df_habitat_varijet_filtered.rename(columns={'TOC element name': 'Hauptknoten Name'}, inplace=True)

# Füge den Pfad zum Dataframe hinzu
df_ceramic_filtered['pfad'] = file_path_ceramic
df_lfp_graphics_filtered['pfad'] = file_path_lfp_graphics
df_label_filtered['pfad'] = file_path_label
df_habitat_varijet_filtered['pfad'] = file_path_habitat_varijet
df_lfp_peripherie_filtered['pfad'] = file_path_lfp_peripherie

# Die DataFrames zusammenführen
result_df = pd.concat([df_ceramic_filtered, df_lfp_graphics_filtered, df_label_filtered,
                      df_habitat_varijet_filtered, df_lfp_peripherie_filtered], ignore_index=True)

# Erstellung der Datei
## Generiere den aktuellen Zeitstempel
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
## Erstelle den Dateinamen mit Zeitstempel
file_name = f"ce_result_dataframe_{timestamp}.csv"
## Speichere das DataFrame als CSV-Datei im selben Ordner ab
result_df.to_csv(file_name, index=False)
print(f"Das DataFrame wurde im File '{file_name}' gespeichert.")