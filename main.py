import os
from bot import Bot

# Récupérer le port depuis l'environnement ou utiliser 8000 par défaut
port = int(os.getenv("PORT", 8000))

# Lancer le bot avec le port
Bot().run(port=port)
