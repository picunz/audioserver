# Usa un'immagine ufficiale di Python
FROM python:3.11-slim

# Imposta la cartella di lavoro nel contenitore
WORKDIR /app

# Copia il file dei requisiti (se ce l'hai) e installa le dipendenze
# Se non hai un file requirements.txt, puoi commentare queste righe
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia tutto il resto del codice
COPY . .

# Comando per avviare l'applicazione
# Sostituisci 'main.py' con il nome del tuo file principale
# E assicurati che il tuo server ascolti sulla porta 8080 (richiesto da Cloud Run)
CMD ["python", "main.py"]
