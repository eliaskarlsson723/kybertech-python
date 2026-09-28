# KyberTech Hosting AB - Python Middleware & Analysis

## Syfte

Python-programmet är utvecklat som en del av skolprojektet KyberTech Hosting AB.

Python-komponenten fungerar som ett middleware- och analyslager mellan Azure
och SharePoint. Programmet hämtar riktig information om virtuella maskiner
från Azure, bearbetar informationen i en separat analysmotor och publicerar
resultatet till SharePoint via Microsoft Graph.

I lösningen har komponenterna olika roller:

- Azure är datakällan för den aktuella VM-miljön.
- Python fungerar som middleware och kopplar samman Azure-data med analys och vidare publicering.
- analysis.py fungerar som analysmotor och skapar beslutsunderlag.
- Microsoft Graph används för kommunikationen mellan Python och SharePoint.
- SharePoint används för att lagra och presentera analysresultatet för gruppens dashboard.

Python-programmet kompletterar därför SharePoint istället för att duplicera
dess funktion. SharePoint används för presentation och inventering medan
Python bearbetar aktuell Azure-data och skapar Health Status, Environment
Score, Alert Level och Recommendations.

## Lösningsarkitektur

Python-komponenten fungerar som middleware mellan projektets Azure-miljö
och SharePoint samt som ett analyslager för den data som hämtas.

Dataflödet i den färdiga prototypen är:

Azure
↓
Azure SDK for Python
↓
azure_vm_status.py
↓
analysis.py
↓
Health Status
Environment Score
Alert Level
Recommendations
Critical Resources
↓
sharepoint.py
↓
Microsoft Graph
↓
SharePoint
↓
KyberTech-Python-Analysis

## Python som middleware

I projektet fungerar Python som middleware mellan Azure och SharePoint.

Middleware innebär här att Python-komponenten ligger mellan olika delar av
lösningen och ansvarar för att hämta, bearbeta och föra vidare information.

I KyberTech-lösningen sker detta genom att Python:

1. Hämtar aktuell VM-data från Azure via Azure SDK.
2. Omvandlar Azure-informationen till projektets interna resursmodell.
3. Skickar informationen till analysis.py.
4. Beräknar Health Status, Environment Score, Alert Level och Recommendations.
5. Förbereder resultatet för SharePoint.
6. Autentiserar mot Microsoft Graph.
7. Publicerar analysresultatet till KyberTech-Python-Analysis.

Python fungerar därför både som integrationslager mellan systemen och som
analysmotor för den data som passerar genom lösningen.

## Funktioner

Den färdiga Python-lösningen kan:

- Hämta riktig VM-information från Azure.
- Läsa aktuell Power State för virtuella maskiner.
- Läsa region och DeviceType från Azure-data och taggar.
- Identifiera Running och Stopped VM.
- Beräkna Environment Score mellan 0 och 100.
- Beräkna Health Status.
- Klassificera Alert Level som Green, Yellow eller Red.
- Generera rekommendationer baserat på VM-status.
- Identifiera kritiska resurser.
- Generera summary.json.
- Generera sharepoint_payload.json.
- Autentisera mot Microsoft Graph med MSAL.
- Publicera analysresultatet till SharePoint-listan KyberTech-Python-Analysis.
- Hantera vanliga Azure-fel på ett kontrollerat sätt.
- Testa analysmotorn automatiskt med pytest.


## Projektstruktur

Python/
├── Archive/
│   └── äldre utvecklings- och integrationstester
├── Tests/
│   └── test_analysis.py
├── .gitignore
├── analysis.py
├── azure_vm_status.py
├── README.md
├── sharepoint.py
├── sharepoint_payload.json
└── summary.json

### Viktiga filer

**azure_vm_status.py**
Huvudprogrammet. Hämtar VM-data från Azure och startar analys- och 
publiceringsflödet.

**analysis.py**
Innehåller den separerade analyslogiken och funktionen analyze_environment().

**sharepoint.py**
Ansvarar för autentisering mot Microsoft Graph och publicering av 
analysresultatet till SharePoint.

**Tests/test_analysis.py**
Innehåller automatiserade tester för analysmotorn.

**summary.json**
Innehåller programmets fullständiga analysresultat.

**sharepoint_payload.json**
Innehåller den analysdata som används för SharePoint-integrationen.


## Konfiguration

Känsliga konfigurationsvärden hårdkodas inte i källkoden.

Programmet använder följande miljövariabler:

AZURE_SUBSCRIPTION_ID
KYBERTECH_CLIENT_ID
KYBERTECH_TENANT_ID

Azure-autentisering sker med AzureCliCredential.

Microsoft Graph-autentisering sker med MSAL och public client/device flow. 
Ingen client secret används.


## Automatiserade tester

Analyslogiken testas med pytest.

Testerna körs med:

python -m pytest Tests/test_analysis.py -v --tb=short

Följande scenarier testas:

1. Alla VM är Running.
2. En VM är Stopped.
3. Alla VM är Stopped.

Testerna verifierar bland annat:

- Environment Score
- Health Status
- Alert Level
- Running VMs
- Stopped VMs
- Recommendations

Nuvarande resultat:

3 passed


## Felhantering

Programmet innehåller strukturerad felhantering för bland annat:

- Saknad AZURE_SUBSCRIPTION_ID.
- Problem med Azure-autentisering.
- Saknad eller felaktig Resource Group.
- Nätverks- och Azure-fel.
- Problem med att läsa status för en individuell VM.
- Resource Group utan virtuella maskiner.

Målet är att användaren ska få ett begripligt felmeddelande istället för 
ett långt Python-traceback vid förväntade fel.


## SharePoint och Microsoft Graph

Analysresultatet publiceras till SharePoint-listan:

KyberTech-Python-Analysis

Följande analysvärden publiceras:

- ResourceName
- HealthStatus
- EnvironmentScore
- AlertLevel
- RunningVMs
- StoppedVMs
- LastUpdated
- Recommendations

Integrationen har verifierats end-to-end med riktig Azure-data.

VM-status har jämförts mot Azure och motsvarande analysresultat har verifierats 
i SharePoint.


## Säkerhet

Autentiseringsuppgifter och secrets ska inte lagras i källkoden.

Azure Subscription ID, Client ID och Tenant ID hanteras genom miljövariabler.

Microsoft Graph-integrationen använder för närvarande bredare behörigheter än 
vad som är önskvärt i en framtida produktionslösning. Under utvecklingen har 
Graph-operationerna därför begränsats till den avsedda SharePoint-listan.

En framtida lösning bör använda principen om minsta möjliga behörighet 
(least privilege) och begränsa applikationens åtkomst till de resurser som 
faktiskt behöver användas.


## AI som utvecklingsstöd

Jag hade ingen tidigare erfarenhet av Python när projektet startade och har 
använt AI som stöd under utvecklingen.

AI har bland annat använts för att förstå Python-struktur, felsöka problem, 
diskutera API:er, Azure SDK, Microsoft Graph, autentisering, Git och automatiserade tester.

Arbetssättet har varit iterativt:

Idé
↓
AI-stöd
↓
Kod
↓
Test
↓
Fel och felsökning
↓
Ökad förståelse
↓
Feedback
↓
Refaktorering

Ett konkret exempel är Azure-integrationen. En tidigare version använde Azure CLI 
på ett sätt som innehöll en hårdkodad sökväg. Efter feedback refaktorerades 
lösningen till Azure SDK for Python med AzureCliCredential.

AI har därför fungerat som ett utvecklings- och lärandestöd samtidigt som 
lösningen kontinuerligt har testats mot den riktiga projektmiljön.


## Avgränsning och framtida utveckling

Målet med projektet har varit att skapa en fungerande end-to-end-prototyp.

Nuvarande lösning körs manuellt och omfattar VM-resurser. Projektet har medvetet 
avgränsats för att prioritera en fungerande och testbar kärnlösning framför 
ytterligare funktioner.

Möjlig framtida utveckling skulle kunna vara:

- Schemalagd körning.
- Azure Functions eller annan Azure-hosting.
- Managed Identity.
- Mer begränsade Microsoft Graph-behörigheter enligt least privilege.
- Analys av fler Azure-resurstyper.
- Ytterligare automatiserade tester.

Dessa funktioner ingår inte i den nuvarande prototypen.


## Slutresultat

Den färdiga Python-prototypen uppfyller projektets huvudsakliga tekniska mål:

Azure
↓
Python
↓
analysis.py
↓
Microsoft Graph
↓
SharePoint

Programmet hämtar riktig VM-data från Azure, analyserar miljön och publicerar 
resultatet till KyberTech-Python-Analysis i SharePoint.

Analysmotorn är separerad från Azure-integrationen och verifieras med 
automatiserade pytest-tester.

Det färdiga resultatet visar ett komplett dataflöde från molnresurs till 
analys och vidare till presentation i gruppens lösning.


# Versionshistorik

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


## Version 5.5

### Nytt
- Undersöker SharePoint-listor via Microsoft Graph.
- Verifierar åtkomst till SharePoint Site via Graph API.
- Hämtar Site ID från SharePoint-webbplatsen.
- Bekräftar att Graph-anrop mot SharePoint fungerar.
- Identifierar att listor inte returneras via nuvarande Graph-behörigheter eller endpoint.


## Version 5.6

### Nytt
- Undersöker Microsoft Graph-behörigheter från Python.
- Läser scopes från aktuell Graph-token.
- Identifierar att nuvarande token saknar Sites-behörighet.
- Förklarar varför SharePoint-listor inte kan läsas med nuvarande behörigheter.
- Förbereder nästa steg med Microsoft Entra ID App Registration.


## Version 5.7

### Nytt
- Refaktoriserar Azure-integrationen till Azure SDK för Python.
- Tar bort hårdkodad sökväg till Azure CLI.
- Tar bort beroendet av subprocess för hämtning av VM-data.
- Hämtar VM-information och aktuell Power State direkt via Azure Compute SDK.
- Behåller befintlig analyslogik och dashboard-output.
- Förbättrar programmets portabilitet och struktur.


## Version 5.8

### Nytt
- Förbättrar konfigurationshanteringen för Azure SDK.
- Flyttar Azure Subscription ID till extern miljökonfiguration.
- Gör programmet möjligt att köra direkt från VS Code.
- Behåller Azure-autentisering utanför källkoden.
- Förbättrar programmets portabilitet mellan utvecklingsmiljöer.


## Version 5.9

### Nytt
- Registrerar KyberTech-Python i Microsoft Entra ID.
- Introducerar en separat applikationsidentitet för Python-lösningen.
- Förbereder säker autentisering mot Microsoft Graph.
- Använder en single-tenant-konfiguration för skolans organisation.
- Skapar inga client secrets eller breda Graph-behörigheter.
- Förbereder framtida integration med SharePoint-testlistan.


## Version 5.10

### Nytt
- Konfigurerar Microsoft Graph-behörighet för KyberTech-Python.
- Använder delegerad läsbehörighet för SharePoint.
- Följer principen om minsta nödvändiga behörighet.
- Skapar inga client secrets eller skrivbehörigheter.
- Förbereder säker läsning av SharePoint-testlistan.


## Version 5.11

### Nytt
- Implementerar autentisering för KyberTech-Python med MSAL.
- Använder public client flow utan client secret.
- Testar delegerad autentisering mot Microsoft Graph.
- Identifierar krav på administratörsgodkännande för SharePoint-behörighet.
- Behåller autentiseringsuppgifter utanför källkoden.


## Version 5.12

### Nytt
- Introducerar strukturerad felhantering för Azure SDK.
- Hanterar saknad Azure-konfiguration.
- Hanterar autentiserings- och anslutningsfel.
- Hanterar saknade Azure-resurser på ett kontrollerat sätt.
- Förbättrar programmets stabilitet och användarvänlighet.


## Version 5.13

### Nytt
- Separerar analyslogiken från Azure-integrationen.
- Introducerar en återanvändbar analysfunktion i analysis.py.
- Lägger till automatiserade tester med pytest.
- Testar scenarier där alla VM körs, en VM är stoppad och alla VM är stoppade.
- Verifierar Environment Score, Health Status, Alert Level och Recommendations.
- Tar bort duplicerad analyslogik från huvudprogrammet.
- Lägger till .gitignore för Python- och pytest-cache.
- Förbättrar programmets struktur, testbarhet och versionshantering.


## Version 5.14

### Nytt
- Verifierar läsning av SharePoint-listan KyberTech-Python-Analysis via Microsoft Graph.
- Verifierar listans kolumner och interna kolumnnamn.
- Verifierar skrivning till SharePoint från Python via Microsoft Graph.
- Genomför ett kontrollerat POST-test mot KyberTech-Python-Analysis.
- Använder korrekta SharePoint-datatyper för Environment Score, Running VMs, Stopped VMs och Last Updated.
- Verifierar att numeriska analysvärden kan skickas som Number-värden.
- Verifierar att Last Updated kan lagras och visas som Date and Time.
- Bekräftar hela kommunikationsvägen Python → MSAL → Microsoft Graph → SharePoint.


## Version 5.15

### Nytt
- Integrerar Azure-analysen med SharePoint via Microsoft Graph.
- Publicerar riktiga analysresultat från Azure VM-data till KyberTech-Python-Analysis.
- Skickar Health Status, Environment Score och Alert Level till SharePoint.
- Skickar antal Running och Stopped VM från den riktiga Azure-miljön.
- Publicerar rekommendationer baserade på analysresultatet.
- Skickar Last Updated som datum och tid.
- Verifierar att SharePoint-data överensstämmer med aktuell VM-status i Azure.
- Behåller automatiserade tester för analysmotorn med 3 godkända pytest-tester.
- Fullbordar dataflödet Azure → Python → analysis.py → Microsoft Graph → SharePoint.
