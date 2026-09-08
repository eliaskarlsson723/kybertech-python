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


## Version 1.4

### Nytt
- Programmet beräknar genomsnittlig kostnad per VM.
- Resultatet visas i terminalen.
- Genomsnittlig kostnad exporteras till summary.json.

### Exempel på resultat

```json
{
    "running_vms": 3,
    "stopped_vms": 2,
    "total_cost": 5100,
    "average_cost": 1020.0,
    "most_expensive_vm": "VM-03"
}


## Version 1.5

### Nytt
- Programmet identifierar VM:ar med hög kostnad.
- VM:ar som kostar över 1000 kr markeras.
- Resultatet sparas i summary.json.
- Ger underlag för kostnadsoptimering i en framtida dashboard.
