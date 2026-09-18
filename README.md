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


## Version 2.1

### Nytt
- Programmet identifierar vilka VM:ar som är stoppade.
- Exporterar stopped_vm_list till summary.json.
- Ger bättre underlag för felsökning och kostnadsoptimering.

## Version 2.2

### Nytt
- Programmet validerar inläst data.
- Kontrollerar att VM har namn, status och kostnad.
- Identifierar negativa kostnader.
- Förbättrar datakvalitet och tillförlitlighet.

## Version 2.3

### Nytt
- Programmet registrerar valideringsfel.
- Valideringsfel exporteras till summary.json.
- Identifierar negativa kostnader i resursdatan.
- Förbereder visning av datakvalitet i en framtida dashboard.



## Version 3.0

### Nytt
- Azure SDK installerad.
- Azure-autentisering verifierad.
- Python kan hämta Azure-token.
- Förbereder hämtning av Azure-resurser.


## Version 3.1

### Nytt
- Python hämtar VM-information från Azure via Azure CLI.
- Verifierad åtkomst till riktiga Azure-resurser.
- Kan läsa VM-namn, resursgrupp och region.
- Förbereder integration med analysmotorn.


## Version 3.2

### Nytt
- Python hämtar Azure-prenumerationsinformation.
- Resultatet exporteras till azure_subscription.json.
- Förbereder vidare integration med Azure-resurser och SharePoint.


## Version 3.3

### Nytt
- Python exporterar VM-information från Azure till azure_vms.json.
- Azure-data lagras lokalt i JSON-format.
- Förbereder integration mellan Azure-data och analysmotorn.


## Version 3.4

### Nytt
- Azure VM-data omvandlas till projektets interna resursmodell.
- Skapar en resources-lista från azure_vms.json.
- Förbereder integration med den befintliga analysmotorn.



## Version 3.5

### Nytt
- Analysmotorn använder Azure-data som datakälla.
- summary.json skapas från Azure VM-data.
- Första analysen körs på riktiga Azure-resurser.


## Version 3.6

### Nytt
- Python hämtar VM-status från Azure.
- Identifierar Running och Stopped VM.
- Konverterar Azure-status till projektets interna datamodell.
- Förbereder integration med analysmotorn.


## Version 3.7

### Nytt
- Python hämtar VM-status från Azure via Azure CLI.
- Azure-status konverteras till projektets interna resursmodell.
- Analysmotorn använder nu verklig Azure-data istället för testdata.
- summary.json skapas baserat på Azure VM-status.
- Beräknar antal Running och Stopped VM direkt från Azure.


## Version 3.8

### Nytt
- Health Status beräknas från Azure VM-status.
- Miljön markeras som Healthy eller Warning.
- Resultatet exporteras till summary.json.
- Använder verklig Azure-data som underlag.


## Version 3.9

### Nytt
- Environment Score beräknas från Azure-data.
- Miljön får ett poängvärde mellan 0 och 100.
- Resultatet exporteras till summary.json.


## Version 4.0

### Nytt
- Identifierar vilka Azure VM:ar som är stoppade.
- Exporterar stopped_vm_list till summary.json.
- Förbättrar beslutsunderlaget i dashboarden.


## Version 4.1

### Nytt
- Hämtar VM-region från Azure.
- Hämtar DeviceType från Azure-taggar.
- Utökar projektets interna resursmodell.
- Förbereder publicering till dashboard och SharePoint.


## Version 4.2

### Nytt
- Exporterar detaljerad VM-information till summary.json.
- Inkluderar namn, status, region och enhetstyp.
- Förbereder framtida dashboard och SharePoint-integration.


## Version 4.3

### Nytt
- Verifierat autentisering mot SharePoint från Python.
- Python kan hämta en giltig SharePoint access token.
- Bekräftar att Microsoft 365-identiteten fungerar mot SharePoint.
- Förbereder framtida integration mellan Python och SharePoint.
- Test utfört utan att påverka befintliga SharePoint-listor.


## Version 4.4

### Nytt
- Genererar rekommendationer baserat på Azure-data.
- Identifierar stoppade VM:ar som bör granskas.
- Exporterar rekommendationer till summary.json.
- Bygger vidare på Health Status och Environment Score.
- Förbereder beslutsstöd för framtida SharePoint-dashboard.


## Version 4.5

### Nytt
- Identifierar kritiska resurser från Azure-data.
- Exporterar critical_resources till summary.json.
- Förbättrar beslutsstödet genom att markera resurser som kräver uppmärksamhet.
- Förbereder framtida Environment Status-dashboard.


## Version 4.6

### Nytt
- Introducerar environment_status i summary.json.
- Samlar Health Status, Environment Score och VM-status i en gemensam struktur.
- Tydligare separation mellan inventeringsdata och analysdata.
- Förbereder framtida integration med SharePoint-dashboard.


## Version 4.7

### Nytt
- Lägger till last_updated i environment_status.
- Visar när Azure-analysen senast kördes.
- Förbättrar spårbarhet och dashboard-stöd.
- Förbereder framtida SharePoint-integration.


## Version 4.8

### Nytt
- Introducerar environment_summary.
- Sammanfattar miljöstatus i ett läsbart format.
- Inkluderar Health Status, Environment Score och VM-status.
- Förbereder publicering i SharePoint-dashboard.


## Version 4.9

### Nytt
- Introducerar alert_level för miljön.
- Klassificerar miljön som Green, Yellow eller Red.
- Baseras på Azure VM-status.
- Förbereder visualisering i SharePoint-dashboard.


## Version 5.0

### Nytt
- Omstrukturerar summary.json till dashboard-, actions- och inventory-sektioner.
- Skapar tydligare separation mellan analysdata och inventeringsdata.
- Förbereder framtida SharePoint-dashboard.
- Förbättrar återanvändning av data i flera dashboard-komponenter.


## Version 5.1

### Nytt
- Introducerar sharepoint_payload.json.
- Exporterar miljöstatus i ett SharePoint-anpassat format.
- Inkluderar Health Status, Environment Score, Alert Level och VM-status.
- Lägger till rekommendationer baserade på Azure-data.
- Förbereder framtida integration med SharePoint-dashboard.


## Version 5.2

### Nytt
- Verifierar autentisering mot Microsoft Graph från Python.
- Bekräftar åtkomst till Microsoft 365-tjänster via Azure CLI.
- Hämtar giltig Microsoft Graph-token.
- Förbereder framtida integration mellan Python och SharePoint.
- Verifierar teknisk kommunikationsväg mellan Azure, Python och Microsoft 365.


## Version 5.3

### Nytt
- Verifierar åtkomst till SharePoint-webbplats via Microsoft Graph.
- Läser information om SharePoint-sajten från Python.
- Bekräftar att Graph API fungerar mot SharePoint.
- Förbereder framtida läsning och skrivning av SharePoint-listor.


## Version 5.4

### Nytt
- Läser SharePoint-webbplats via Microsoft Graph.
- Hämtar och verifierar Site ID.
- Bekräftar åtkomst mellan Python och SharePoint.
- Undersöker SharePoint-listor via Graph API.
- Förbereder framtida läsning av SharePoint-innehåll.
