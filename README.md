# SQL Analisi Serie A

Analisi delle statistiche delle squadre di Serie A tramite query SQL su database SQLite, sviluppata con Python e Pandas.

## Descrizione

Questo progetto carica i dati di Serie A in un database SQLite ed esegue query SQL per estrarre statistiche interessanti.

## Tecnologie utilizzate

- Python 3
- Pandas
- SQLite3

## Query eseguite

- Squadre ordinate per gol segnati
- Top 3 squadre per possesso palla
- Squadre più indisciplinate (cartellini gialli > 80)

## File

| File | Descrizione |
|------|-------------|
| `sql_serie_a.py` | Script principale |
| `Football teams.csv` | Dataset originale |
| `risultati_sql.csv` | Output query finale |

## Come eseguire

```bash
python sql_serie_a.py
```
