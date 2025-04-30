import os
import pandas as pd
import psycopg2
# import time
# from flask import Flask, jsonify


# app = Flask(__name__)
# Configuration de la base de données PostgreSQL
DB_NAME = "mydatabase"
DB_USER = "user"
DB_PASSWORD = "password"
DB_HOST = "db"  # Nom du service Docker
DB_PORT = "5432"

# Nom du fichier CSV
CSV_FILE = "data.csv"

# Vérifier si le fichier CSV existe, sinon le créer avec des données fictives
if not os.path.exists(CSV_FILE):
    print("📂 Fichier data.csv introuvable, création en cours...")
    
    # Génération des données fictives
    data = {
        "nom": ["Alice", "Bob", "Charlie", "David"],
        "age": [25, 30, 35, 40],
        "salaire": [45000, 55000, 60000, 70000]
    }
    
    df = pd.DataFrame(data)
    df.to_csv(CSV_FILE, index=False)
    
    print("✅ Fichier data.csv créé avec succès !")

# Charger le fichier CSV
df = pd.read_csv(CSV_FILE)
print("\n📊 Statistiques du dataset :")
print(df.describe())  # Affiche les stats sur les colonnes numériques
print("\n🔍 Valeurs manquantes :")
print(df.isnull().sum())

# Connexion à PostgreSQL
try:
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    print("✅ Connexion réussie à PostgreSQL !")
except Exception as e:
    print(f"❌ Erreur de connexion : {e}")
    exit()

# Création de la table dans PostgreSQL
table_name = "dataset"
with conn.cursor() as cur:
    cur.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id SERIAL PRIMARY KEY,
            {", ".join([f"{col} TEXT" for col in df.columns])}
        );
    """)
    conn.commit()
    print(f"📌 Table '{table_name}' prête dans PostgreSQL !")

# Insertion des données
with conn.cursor() as cur:
    for _, row in df.iterrows():
        cur.execute(f"""
            INSERT INTO {table_name} ({", ".join(df.columns)})
            VALUES ({", ".join(['%s' for _ in row])});
        """, tuple(row))
    conn.commit()
    print(f"✅ Données insérées dans '{table_name}' avec succès !")


# @app.route("/")
# def home():
#     return "<h1>Bienvenue sur l'API de Science des Données ! 🚀</h1>"

# @app.route("/stats")
# def stats():
#     df = pd.read_csv(CSV_FILE)
#     stats = df.describe().to_dict()
#     return jsonify(stats)

# @app.route("/data")
# def get_data():
#     df = pd.read_csv(CSV_FILE)
#     return jsonify(df.to_dict(orient="records"))

# @app.route("/db")
# def db_data():
#     conn = get_db_connection()
#     if not conn:
#         return jsonify({"error": "Impossible de se connecter à la base de données"}), 500

#     cur = conn.cursor()
#     cur.execute("SELECT * FROM dataset;")
#     rows = cur.fetchall()

# Fermer la connexion
conn.close()
print("🔌 Connexion PostgreSQL fermée.")

# return jsonify(rows)

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=80, debug=True)
