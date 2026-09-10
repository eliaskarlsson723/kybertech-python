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

## Version 1.5 

### Nytt
- Programmet identifierar nu VM:ar med hög kostnad.
- VM:ar som kostar över 1000 kr markeras.
- Resultatet sparas i summary.json.
- Ger underlag för kostnadsoptimering i en framtida dashboard.

## Version 1.6

### Nytt

- Programmet bedömer miljöns hälsostatus.
- Om en eller flera VM:ar är stoppade markeras miljön som Warning.
- Status exporteras till summary.json.



## Version 1.7

### Nytt
- Beräknar kostnad för Running VM.
- Beräknar kostnad för Stopped VM.
- Exporterar kostnadsfördelningen till summary.json.
- Ger bättre underlag för kostnadsanalys och optimering.



## Version 1.8

### Nytt
- Programmet beräknar ett Environment Score mellan 0 och 100.
- Poängen påverkas av stoppade VM:ar och högkostnadsresurser.
- Resultatet visas i terminalen och exporteras till summary.json.


## Version 1.9

### Nytt
- Programmet beräknar potentiell kostnadsbesparing.
- Kostnaden för stoppade VM:ar redovisas som möjlig besparing.
- Exporteras till summary.json.


## Version 2.0

### Nytt
- Programmet genererar rekommendationer baserat på analysresultatet.
- Rekommendationerna visas i terminalen.
- Rekommendationerna exporteras till summary.json.
- Förbereder beslutsstöd i framtida dashboard.
