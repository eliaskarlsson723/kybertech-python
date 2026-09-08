# KyberTech Python

## Version 1.0

### Syfte
Programmet analyserar resursdata för virtuella servrar (VM:ar).

### Funktioner
- Visar VM-namn, status och kostnad
- Räknar antal VM:ar som är igång
- Beräknar total kostnad
- Identifierar den dyraste VM:n

### Exempel på resultat

VM-01 - Running - 1200 kr
VM-02 - Stopped - 800 kr
VM-03 - Running - 1500 kr

Antal VM som är igång: 2
Total kostnad: 3500 kr

Dyraste VM:
VM-03 - 1500 kr

### Kommande utveckling
- Importera data från fil (CSV eller JSON)
- Hämta data från Azure
- Presentera resultat i SharePoint-dashboard

## Version 1.1

### Nytt
- Flyttade resursdata till en JSON-fil.
- Programmet läser nu data från fil istället för hårdkodad information.
- Förbereder lösningen för framtida Azure-integration.

Kommande utveckling
- Importera data från fil (CSV eller JSON)
- Hämta data från Azure
- Presentera resultat i SharePoint-dashboard

## Version 1.2

### Nytt
- Programmet genererar en sammanfattningsfil.
- Analysresultat exporteras till summary.json.
- Förbereder integration med dashboard.

## Version 1.3

### Nytt
- Programmet räknar antal stoppade VM:ar.
- Resultatet visas i terminalen.
- Värdet exporteras även till summary.json.
