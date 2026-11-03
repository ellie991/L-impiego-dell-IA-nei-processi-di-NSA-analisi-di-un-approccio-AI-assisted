#!/usr/bin/env python3
"""
Agente AI per la parte AI-assisted della tesi (Network Security Audit).

Architettura (AutoGen 0.4+, human-in-the-loop):
  - security_analyst (AssistantAgent): analista di sicurezza basato su LLM.
  - analista_umano   (UserProxyAgent): sei tu; ad ogni tuo turno il programma ti
    chiede input da tastiera. Premi solo Invio per far proseguire l'agente,
    oppure scrivi una correzione/domanda.

Sicurezza:
  - Nessun tool di esecuzione comandi/codice e' collegato all'agente: puo' solo
    generare testo, non eseguire nulla sul sistema.
  - Ogni turno dell'agente e' seguito da un turno "umano" obbligatorio
    (RoundRobinGroupChat a 2 partecipanti): nessuna azione senza il tuo input.
  - Opera solo su output gia' raccolti, in un laboratorio isolato di tua proprieta'.

Setup (una tantum):
  python -m venv .venv
  # Windows (PowerShell):
  .\\.venv\\Scripts\\Activate.ps1
  # macOS/Linux:
  source .venv/bin/activate
  pip install pyautogen "autogen-ext[openai,azure]"

Uso con Azure OpenAI:
  $env:AZURE_OPENAI_API_KEY = "..."                      # PowerShell
  $env:AZURE_OPENAI_ENDPOINT = "https://<risorsa>.openai.azure.com/"
  $env:AZURE_OPENAI_DEPLOYMENT = "<nome-deployment>"      # es. gpt-4.1
  $env:AZURE_OPENAI_API_VERSION = "2024-10-21"            # opzionale
  python agente.py

  # macOS/Linux/Kali (bash):
  export AZURE_OPENAI_API_KEY="..."
  export AZURE_OPENAI_ENDPOINT="https://<risorsa>.openai.azure.com/"
  export AZURE_OPENAI_DEPLOYMENT="<nome-deployment>"
  python agente.py

Uso con OpenAI (in alternativa ad Azure):
  export OPENAI_API_KEY="sk-..."
  export OPENAI_MODEL="gpt-4o"   # opzionale, default gpt-4o
  python agente.py
"""

import asyncio
import os
import sys
from datetime import datetime

try:
    from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
    from autogen_agentchat.conditions import TextMentionTermination
    from autogen_agentchat.teams import RoundRobinGroupChat
    from autogen_ext.models.openai import (
        AzureOpenAIChatCompletionClient,
        OpenAIChatCompletionClient,
    )
except ImportError:
    sys.exit(
        "Dipendenze mancanti. Esegui:\n"
        '  pip install pyautogen "autogen-ext[openai,azure]"'
    )

OUTPUT_DIR = "output"
TRANSCRIPT = os.path.join(OUTPUT_DIR, "08_agente_autogen.md")


def build_model_client():
    """Costruisce il client del modello: Azure OpenAI se configurato, altrimenti OpenAI."""
    if os.environ.get("AZURE_OPENAI_API_KEY"):
        endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT")
        deployment = os.environ.get("AZURE_OPENAI_DEPLOYMENT")
        if not endpoint or not deployment:
            sys.exit("Azure: imposta AZURE_OPENAI_ENDPOINT e AZURE_OPENAI_DEPLOYMENT.")
        return AzureOpenAIChatCompletionClient(
            azure_deployment=deployment,
            model=deployment,
            api_version=os.environ.get("AZURE_OPENAI_API_VERSION", "2024-10-21"),
            azure_endpoint=endpoint,
            api_key=os.environ["AZURE_OPENAI_API_KEY"],
        )
    if os.environ.get("OPENAI_API_KEY"):
        return OpenAIChatCompletionClient(
            model=os.environ.get("OPENAI_MODEL", "gpt-4o"),
            api_key=os.environ["OPENAI_API_KEY"],
        )
    sys.exit(
        "Manca la API key. Usa OpenAI (export OPENAI_API_KEY=...) "
        "oppure Azure (export AZURE_OPENAI_API_KEY=... + ENDPOINT + DEPLOYMENT)."
    )


def leggi(nome_file: str) -> str:
    """Legge un file di output se esiste, altrimenti restituisce un avviso."""
    percorso = os.path.join(OUTPUT_DIR, nome_file)
    if os.path.exists(percorso):
        with open(percorso, encoding="utf-8", errors="ignore") as f:
            return f.read().strip()
    return f"[FILE NON TROVATO: {percorso} - salta questa sezione]"


async def main() -> None:
    # Raccoglie gli output degli strumenti tradizionali (quelli presenti).
    nmap = leggi("02_nmap_full.txt")
    nikto = leggi("04_nikto.txt")
    gvm = leggi("07_gvm_report.csv")  # esporta il report GVM anche in CSV, se puoi

    model_client = build_model_client()

    system_message = (
        "Sei un analista esperto di network security. Ricevi gli output di strumenti di "
        "scanning (Nmap, Nikto, GVM/OpenVAS) eseguiti in un LABORATORIO ISOLATO sulla "
        "macchina didattica Metasploitable 2. Svolgi in ordine queste fasi:\n"
        "1) INTERPRETAZIONE: per ogni servizio indica porta, servizio, versione.\n"
        "2) CORRELAZIONE: associa vulnerabilita' note con CVE REALI e punteggio CVSS.\n"
        "3) PRIORITIZZAZIONE: classifica per rischio (Critica/Alta/Media/Bassa) motivando.\n"
        "4) REPORT: produci una bozza di report tecnico in italiano.\n"
        "Regole: NON fornire codice di exploit; segnala esplicitamente le incertezze; "
        "non inventare CVE. Dopo ogni fase, fermati e attendi il turno dell'utente umano "
        "prima di proseguire con la fase successiva. Quando hai completato il report finale "
        "scrivi da sola, su una riga, la parola TERMINATO."
    )

    analyst = AssistantAgent(
        name="security_analyst",
        model_client=model_client,
        system_message=system_message,
    )

    # input_func=input -> ad ogni turno umano il programma chiede input da tastiera:
    # premi Invio per approvare e proseguire, oppure scrivi una correzione.
    human = UserProxyAgent(
        name="analista_umano",
        input_func=input,
    )

    termination = TextMentionTermination("TERMINATO")

    team = RoundRobinGroupChat(
        [analyst, human],
        termination_condition=termination,
    )

    task = (
        "Analizza i seguenti output raccolti nel laboratorio e procedi con le 4 fasi.\n\n"
        f"=== OUTPUT NMAP ===\n{nmap}\n\n"
        f"=== OUTPUT NIKTO ===\n{nikto}\n\n"
        f"=== REPORT GVM (CSV) ===\n{gvm}\n"
    )

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    transcript_lines: list[str] = []

    # try/finally: salva sempre la trascrizione, anche se lo script viene
    # interrotto (Ctrl+C), va in errore di rete o la sessione si blocca a meta'.
    try:
        async for event in team.run_stream(task=task):
            source = getattr(event, "source", None)
            to_text = getattr(event, "to_text", None)
            if source is None or to_text is None:
                continue  # es. il TaskResult finale, non un messaggio di chat
            testo = to_text()
            print(f"\n--- {source} ---\n{testo}\n")
            transcript_lines.append(f"## {source}\n\n{testo}\n\n---\n\n")
    except (KeyboardInterrupt, Exception) as exc:
        print(f"\n[ATTENZIONE] Sessione interrotta ({exc!r}). Salvo comunque quanto raccolto finora.")
    finally:
        await model_client.close()
        with open(TRANSCRIPT, "w", encoding="utf-8") as f:
            f.write("# Trascrizione sessione agente AutoGen\n\n")
            f.write(f"Data: {datetime.now().isoformat(timespec='seconds')}\n\n")
            f.writelines(transcript_lines)
        print(f"\nTrascrizione salvata in: {TRANSCRIPT}")


if __name__ == "__main__":
    asyncio.run(main())
