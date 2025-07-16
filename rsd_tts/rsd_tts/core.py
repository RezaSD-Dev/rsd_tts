import win32com.client
import re

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def pulisci_testo(testo):
    """Pulisce il testo da caratteri speciali e formattazioni indesiderate"""
    # Rimozione di markdown e formattazioni speciali
    testo = re.sub(r'\*\*([^*]+)\*\*', r'\1', testo)  # **grassetto**
    testo = re.sub(r'\*([^*]+)\*', r'\1', testo)      # *corsivo*
    testo = re.sub(r'`([^`]+)`', r'\1', testo)        # `codice`
    testo = re.sub(r'~~([^~]+)~~', r'\1', testo)      # ~~barrato~~
    
    # Rimozione di caratteri speciali isolati
    testo = re.sub(r'[^\w\s.,!?;:\'\"()\-—+&@#%$€£]', ' ', testo)
    
    # Sostituzione di sequenze speciali
    sostituzioni = {
        r'\.{3,}': ' punto punto punto ',   # ...
        r':-\)|:\)': ' sorriso ',            # :-) :)
        r':\(|:-\(': ' triste ',             # :( : -(
        r';\)|;-\)': ' occhiolino ',         # ;) ;-)
        r':D|:-D': ' risata ',               # :D :-D
        r'<3': ' cuore ',                    # <3
        r'->': ' diventa ',                  # ->
        r'<-': ' da ',                       # <-
        r'&': ' e ',                         # &
        r'@': ' chiocciola ',                # @
        r'#': ' hashtag ',                   # #
        r'\*': ' asterisco ',                # * isolato
        r'\/': ' barra ',                    # / isolato
    }
    
    for pattern, repl in sostituzioni.items():
        testo = re.sub(pattern, repl, testo)
    
    # Gestione di numeri e simboli combinati
    testo = re.sub(r'(\d+)\s*([x×])\s*(\d+)', r'\1 per \3', testo)  # 10x10 → 10 per 10
    testo = re.sub(r'(\d+)\s*%', r'\1 percento', testo)             # 50% → 50 percento
    
    # Normalizzazione spazi
    testo = re.sub(r'\s+', ' ', testo).strip()
    
    return testo

def parla(testo, is_ai_response=True):
    """Pronuncia il testo con controlli aggiuntivi"""
    if is_ai_response:
        # 1. Rimuovi domande dalla risposta AI
        testo = re.sub(r'\?.*$', '.', testo)
        
        # 2. Rimuovi prompt che potrebbero innescare nuove risposte
        testo = re.sub(r'(puoi|potresti|vorrei|per favore|grazie)', '', testo, flags=re.IGNORECASE)
        
        # 3. Tronca le risposte lunghe
        if len(testo) > 500:
            testo = testo[:497] + '...'
    
    testo_pulito = pulisci_testo(testo)
    
    if testo_pulito:
        speaker.Rate = 0
        speaker.Volume = 100
        speaker.Speak(testo_pulito)  # Rimosso il secondo parametro