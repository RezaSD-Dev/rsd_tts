# rsd_tts · [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Libreria Python per sintesi vocale in italiano** con pulizia avanzata del testo per un output chiaro e naturale.

✨ **Funzionalità**:
- Pulisce automaticamente testo da markdown, emoji e caratteri speciali
- Ottimizzato per la lingua italiana
- Semplice integrazione con Windows SAPI
- Regolazione di velocità e volume

```python
from rsd_tts import parla

parla("Ciao mondo! :)")  # Pronuncia "Ciao mondo sorriso"
