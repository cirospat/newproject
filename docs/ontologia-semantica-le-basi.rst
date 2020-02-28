
.. _h743223d41055f26406145e21744:

Ontologia semantica: le basi
############################


.. admonition:: Fonte dati

    La fonte di questo documento tradotto in italiano (traduttore Google e verificato da Ciro Spataro) è: \ |LINK1|\ .
    
    Il link a questo documento in lingua inglese è stato pubblicato da Giovanni Pirrotta sul gruppo FB di OpendataSicilia: \ |LINK2|\ 
    
    \ |STYLE0|\ : si ritiene utile pubblicare la traduzione di questo documento in quanto vengono spiegati concetti di semantica e ontologia in maniera facile e comprensibile anche ai non addetti ai lavori.

|

.. _h1c4337285af1d3316785b23465415:

Che cos'è la semantica?
***********************

La semantica è lo studio del significato. Creando una comprensione comune del significato delle cose, la semantica aiuta a capirci meglio. Il significato comune aiuta le persone a capirsi a vicenda nonostante esperienze o punti di vista diversi. Il significato comune aiuta i sistemi informatici a interpretare più accuratamente ciò che le persone intendono. Il significato comune consente a sistemi IT diversi - fonti di dati e applicazioni - di interfacciarsi in modo più efficiente e produttivo.

|

.. _h672737a5607367d664b511b5f69f:

Che cos'è un'ontologia?
***********************

Un'ontologia definisce tutti gli elementi coinvolti in un ecosistema aziendale e li organizza in base alla loro relazione reciproca. I vantaggi della costruzione di un'ontologia sono:

* Tutti concordano su un insieme comune di termini usati per descrivere le cose

* Sistemi diversi - database e applicazioni - possono comunicare tra loro senza dover connettersi direttamente tra loro.

|

.. _h212c334016737b19182140453d2c6e1e:

Ontologia di impresa
********************

Un'ontologia è un insieme di definizioni di concetti formali.

Una Enterprise Ontology è un'ontologia dei concetti chiave che organizzano e strutturano i sistemi informativi di un'organizzazione. Avere una Enterprise Ontology fornisce un insieme unificante che rende sopportabile l'integrazione del sistema.

Una Enterprise Ontology è come un dizionario di dati o un vocabolario controllato, tuttavia è diverso per un paio di aspetti chiave. Un dizionario di dati, o un vocabolario controllato, o persino una tassonomia, si basano sugli umani per leggere le definizioni e posizionare gli oggetti nelle giuste categorie. Un'ontologia è una serie di regole sull'appartenenza alla classe (concetto) che utilizza le relazioni per impostare i criteri di inclusione. Ciò ha diversi vantaggi, uno dei quali è che un sistema (un motore di inferenza) può assegnare gli individui alle classi in modo coerente e automatico.

Costruendo l'ontologia nella terminologia neutrale dell'applicazione, può ricoprire il ruolo di "comune denominatore" tra le numerose fonti di dati esistenti e potenziali che hai all'interno della tua azienda. Le migliori pratiche nella costruzione di ontologie favoriscono la costruzione di un'ontologia aziendale con il minor numero di concetti necessari per promuovere l'interoperabilità, e questo a sua volta gli consente di ricoprire il ruolo di "minimo comune denominatore".

Costruire un'ontologia aziendale è il punto di partenza per una serie di iniziative di tecnologia semantica. Riteniamo che la tecnologia semantica cambierà il modo in cui implementiamo i sistemi in tre aree principali:

* \ |STYLE1|\ : la maggior parte delle informazioni utilizzate per gestire le organizzazioni più grandi proviene dalle loro "applicazioni" (ERP o EHR o Case Management o qualunque applicazione interna). Ottenere nuove informazioni è una questione di costruire schermate in queste applicazioni e (di solito) pagare i dipendenti per inserire i dati, in modo da poterli successivamente estrarre per altri scopi. La tecnologia semantica introduce approcci per raccogliere dati non solo dalle app interne, ma dai social media, dai dati non strutturati e dai vasti e crescenti set di dati disponibili al pubblico in attesa di essere integrati.

* \ |STYLE2|\ : la tecnologia relazionale e persino orientata agli oggetti impone una struttura rigida e predefinita e un insieme di vincoli su quali dati possono essere archiviati e su come sono organizzati. La tecnologia semantica lo sostituisce con una struttura dati flessibile che può essere modificata senza convertire i dati sottostanti. È così flessibile che non tutti gli utenti di un set di dati devono condividere lo stesso schema (devono condividere una parte dello schema, altrimenti non vi sono basi per la condivisione, ma non devono essere in fase di blocco, ognuno può estendere il modello in modo indipendente). Inoltre, l'approccio semantico promuove l'idea che le informazioni siano almeno parzialmente "auto-organizzabili". L'uso di URI (identificatori di risorse uniformi basati sul Web) e database basati su grafici consente a questi sistemi di dedurre nuove informazioni dalle informazioni esistenti e quindi utilizzare quelle nuove informazioni nell'assemblaggio dinamico di strutture dati.

* \ |STYLE3|\ : Finalmente pensiamo che la tecnologia semantica cambierà il modo in cui consumiamo le informazioni. Sta già cambiando la natura dei sistemi orientati al flusso di lavoro (chiedici informazioni su BeInformed). Sta cambiando l'analisi dei dati. È la terza "V" nei Big Data ("Varietà"). I mashup basati su semantica stanno cambiando la natura della presentazione. L'ottimizzazione dei motori di ricerca semantica (SEO) sta cambiando la ricerca interna ed esterna.

|

.. _h2f184339505a7323927463b18a16a:

In che modo la tecnologia semantica è diversa dall'intelligenza artificiale?
****************************************************************************

L'intelligenza artificiale (AI) è una disciplina accademica di oltre 50 anni che ha fornito molte tecnologie che sono ora in uso commerciale. Due cose comprendono il nucleo della tecnologia semantica. Il primo deriva dalla ricerca sull'IA nella rappresentazione della conoscenza e nel ragionamento svolto negli anni '70 e '80 e comprende linguaggi di rappresentazione ontologica come OWL e motori di inferenza come Fact ++. 

Il secondo riguarda la rappresentazione e l'interrogazione dei dati utilizzando triple store, RDF e SPARQL, che sono in gran parte estranei all'intelligenza artificiale. Un'ampia definizione di tecnologia semantica include una varietà di altre tecnologie emerse dall'intelligenza artificiale. Questi includono l'apprendimento automatico, l'elaborazione del linguaggio naturale, agenti intelligenti e, in misura minore, il riconoscimento e la pianificazione del parlato. Le aree di intelligenza artificiale di solito non associate alla tecnologia semantica includono creatività, visione e robotica.

|

.. _h575f6c5d373975c79312702a3f7f4b:

In che modo la semantica usa l'inferenza per costruire la conoscenza?
*********************************************************************

La semantica organizza i dati in categorie ben definite con relazioni chiaramente definite. La classificazione delle informazioni in questo modo consente agli umani e alle macchine di leggere, comprendere e dedurre le conoscenze in base alla sua classificazione. Ad esempio, se vediamo un uccello dal petto rosso fuori dalla nostra finestra in aprile, le nostre conoscenze generali ci portano a identificarlo come un pettirosso. Una volta classificato correttamente, possiamo dedurre molte più informazioni sul pettirosso e solo il suo nome.

Sappiamo ad esempio che è un uccello; vola; canta una canzone; trascorre il suo inverno da qualche altra parte e il fatto che si sia presentato significa che il bel tempo è in arrivo.

Conosciamo queste altre informazioni perché il pettirosso è stato correttamente identificato nello schema delle nostre conoscenze generali sugli uccelli, una classificazione più elevata; stagioni, una relativa classificazione, ecc.

Questo è un semplice esempio di una corretta classificazione delle informazioni in una struttura predefinita che possiamo dedurre nuove conoscenze. In un modello semantico, una volta impostate le relazioni, un computer può classificare i dati in modo appropriato, analizzarli in base alle relazioni predeterminate e quindi dedurre nuove conoscenze basate su questa analisi.

|

.. _h36667695a611639d726d475206115:

Che cos'è l'accordo semantico?
******************************

La sfida principale nella costruzione di un'ontologia è far sì che le persone siano d'accordo su cosa realmente significano quando descrivono i concetti che definiscono la loro attività. Ottenere un accordo semantico è il processo per aiutare le persone a capire esattamente cosa significano quando si esprimono.

I tecnologi semantici realizzano questo perché definiscono termini e relazioni indipendenti dal contesto di come vengono applicati o dai sistemi IT che memorizzano le informazioni, in modo da poter costruire definizioni pure e coerenti tra le discipline.

|

.. _h596a7b276a1159434a377e496b243122:

Perché è importante l'accordo semantico?
****************************************

L'accordo semantico è importante perché consente a diversi sistemi informatici di comunicare direttamente tra loro. Se un'applicazione definisce un cliente come qualcuno che ha effettuato un ordine e un'altra applicazione definisce il cliente come qualcuno che potrebbe effettuare un ordine, le due applicazioni non possono passare informazioni avanti e indietro perché parlano di due persone diverse. In un approccio IT tradizionale, l'unico modo in cui le due applicazioni saranno in grado di trasmettere informazioni avanti e indietro è attraverso una patch di integrazione dei sistemi. Costruire queste patch costa tempo e denaro perché richiede che i proprietari dei due sistemi debbano negoziare un significato comune e scrivere un codice incrementale per garantire che le informazioni vengano passate avanti e indietro correttamente. In un ambiente IT abilitato semantico, tutti i concetti che significano la stessa cosa sono definiti da un significato comune, quindi le diverse applicazioni sono in grado di comunicare tra loro senza dover scrivere codice di integrazione dei sistemi.

|

.. _h232d1e255e4113697511c1537461f:

Qual è la differenza tra tassonomia e ontologia?
************************************************

Una tassonomia è un insieme di definizioni organizzate da una gerarchia che parte dalla descrizione più generale di qualcosa e diventa più definita e specifica man mano che si scende nella gerarchia dei termini. Ad esempio, un falco dalla coda rossa potrebbe essere rappresentato in una tassonomia del linguaggio comune come segue:

* Uccello

    * Rapace

        * Falco

            * Falco coda rossa

Un'ontologia descrive un concetto sia per la sua posizione in una gerarchia di fattori comuni come la descrizione sopra del falco dalla coda rossa, sia per le sue relazioni con altri concetti. Ad esempio, il falco coda rossa sarebbe anche associato al concetto di predatori o animali che vivono sugli alberi.

La ricchezza delle relazioni descritte in un'ontologia è ciò che la rende uno strumento potente per modellare ecosistemi aziendali complessi.

|

.. _h4556623b4d2f353e74b582e712e545a:

Qual'è la differenza tra un modello di dati logici e l'ontologia?
*****************************************************************

Lo scopo di un'ontologia è quello di modellare il business. È indipendente dai sistemi informatici, ad es. applicazioni e database legacy o futuri. Il suo scopo è quello di utilizzare la logica formale e termini comuni per descrivere il business, in modo che sia gli umani che le macchine possano capire. Le ontologie usano gli assiomi OWL per descrivere classi e proprietà condivise tra più linee di business in modo che i concetti possano essere definiti dalle loro relazioni, rendendoli estendibili a livelli di dettaglio crescenti come richiesto. Le buone ontologie sono "frattali" in natura, il che significa che le astrazioni comuni creano una struttura organizzativa che si espande facilmente per soddisfare le complesse esigenze di gestione delle informazioni dell'azienda. Lo scopo di un modello logico è descrivere la struttura dei dati richiesti per una particolare applicazione o servizio. In genere, un modello logico mostra tutte le entità, relazioni e attributi richiesti per un'applicazione proposta. Include solo i dati relativi alla particolare applicazione in questione. Idealmente i modelli logici derivano dall'ontologia che garantisce significato e denominazione coerenti nei futuri sistemi di informazione.

|

.. _h3285b81473506839685073244b2f6:

Come può un Ontologia collegare insieme i sistemi informatici?
**************************************************************

Poiché un'ontologia è separata da qualsiasi struttura IT, non è limitata dai vincoli richiesti da software o hardware specifici. L'ontologia esiste come punto di riferimento comune per l'accesso a qualsiasi sistema IT. Grazie a questa indipendenza, può servire come terreno comune per diversi:

* strutture di database, come relazionali e gerarchiche,

* applicazioni, come un sistema ERP SAP e un e-market ospitato su cloud,

* dispositivi, come un iPad o un telefono cellulare.

Il vantaggio dell'approccio semantico è che puoi collegare i sistemi IT legacy che sono la spina dorsale della maggior parte delle aziende a nuove entusiasmanti soluzioni IT, come il cloud computing e la consegna mobile.

|

.. _h39476f1361257a50216a7f5c544f337c:

Quali sono i 5 vantaggi commerciali delle soluzioni tecnologiche semantiche?
****************************************************************************

La tecnologia semantica ci aiuta a:

#. Trova informazioni più pertinenti e utili 

    * Perché ci consente di cercare informazioni da fonti disparate (ricerca federata) e perfezionare automaticamente le nostre ricerche (ricerca sfaccettata).

#. Comprendere meglio cosa sta succedendo 

    * Perché ci consente di utilizzare le relazioni tra concetti per prevedere e interpretare il cambiamento.

#. Costruisci sistemi e comunicazioni più trasparenti 

    * Perché si basa su significati comuni e comprensione reciproca dei concetti chiave e delle relazioni che governano i nostri ecosistemi aziendali.

#. Aumenta la nostra efficacia, efficienza e vantaggio strategico 

    * Perché ci consente di apportare modifiche ai nostri sistemi di informazione in modo più rapido e semplice.

#. Diventa più percettivo, intelligente e collaborativo 

    * Perché ci consente di porre domande che prima non potevamo fare.

|

.. _h73ea51535f537a6d55197048753412:

Come può la tecnologia semantica abilitare il flusso di lavoro dinamico?
************************************************************************

I sistemi di flusso di lavoro dinamico semantico sono un nuovo modo di organizzare, documentare e supportare la gestione della conoscenza. Includono due cose chiave:

#. Una definizione coerente, completa e rigorosa di un ecosistema che definisce tutti i suoi elementi e le relazioni tra gli elementi. È come una mappa.

#. Un set di strumenti che utilizzano questo modello per:

    * Raccogliere e fornire dati pertinenti e ad hoc.

    * Generare un elenco di azioni (attività, decisioni, comunicazioni, ecc.) basate sulla situazione attuale.

    * Facilitare e documentare le interazioni nell'ecosistema.

Questi strumenti funzionano come un sistema GPS che utilizza la mappa per adattare le sue raccomandazioni in base alle interazioni umane Questo nuovo approccio alla gestione del flusso di lavoro consente alle organizzazioni di rispondere più rapidamente, prendere decisioni migliori e aumentare la produttività.

|

.. _h263c6c5a55f12223319b22811447f:

Perché le organizzazioni necessitano di sistemi di flusso di lavoro dinamici e semantici?
*****************************************************************************************

Un ecosistema aziendale è una serie di sistemi interconnessi in continua evoluzione. Le persone hanno bisogno di informazioni e strumenti flessibili, precisi e tempestivi per avere un impatto positivo sui loro ecosistemi. Quindi devono vedere come le loro azioni incidono sull'energia e sul flusso dei sistemi. I sistemi di flusso di lavoro dinamico semantico-guidato consentono agli utenti di accedere alle informazioni da fonti non integrate, impostare regole per monitorare queste informazioni e avviare procedure di flusso di lavoro quando cambiano le dinamiche della relazione tra due concetti. Supporta inoltre la definizione, i ruoli e le responsabilità per garantire che questo processo automatizzato sia gestito in modo appropriato e sicuro. I vantaggi organizzativi per l'implementazione di sistemi di flusso di lavoro dinamici e semantici includono:

* Migliore gestione della complessità

* Migliore accesso a informazioni accurate e tempestive

* Migliore comprensione e processo decisionale

* Gestione proattiva del rischio e delle opportunità

* Maggiore reattività organizzativa al cambiamento

* Migliore comprensione dei sistemi di interblocco che influenzano la salute dell'ecosistema aziendale.

|

--------

|

.. _h4442311b48334c481f016e39684b63:

Verso la definizione di "Grafo di Conoscenza"
*********************************************

\ |LINK3|\  

\ |STYLE4|\ : Un grafo della conoscenza descrive principalmente le entità del mondo reale e le loro interrelazioni, organizzate in un grafico, definisce possibili classi e relazioni di entità in uno schema, consente l'interconnessione potenziale di entità arbitrarie tra loro e copre vari domini di argomento. \ |STYLE5|\ : H. Paulheim. Knowledge Graph Refinement: A Survey of Approaches and Evaluation Methods. Semantic Web Journal, (Preprint):1–20, 2016.

\ |STYLE6|\ : i grafici della conoscenza sono grandi reti di entità, i loro tipi semantici, proprietà e relazioni tra entità. \ |STYLE7|\ : M. Kroetsch and G. Weikum. \ |LINK4|\ . [August, 2016]. 

\ |STYLE8|\ : I grafici della conoscenza potrebbero essere immaginati come una rete di tutti i tipi di cose che sono rilevanti per un dominio specifico o per un'organizzazione. Non si limitano a concetti e relazioni astratti, ma possono anche contenere istanze di cose come documenti e set di dati. \ |STYLE9|\ : A. Blumauer. \ |LINK5|\  \ |LINK6|\ , July 2014. [August, 2016].

\ |STYLE10|\ : Definiamo un grafo della conoscenza come un grafo RDF. Un grafo RDF è costituito da un insieme di triple RDF in cui ogni tripla (s, p, o) RDF è un insieme ordinato dei seguenti termini RDF: asubjects∈U∪B, predicatep∈U e objectU∪B∪L. Un termine RDF è oURIu∈U, un nodo vuoto b∈B o letteralmente ∈L. \ |STYLE11|\ : M. Farber, B. Ell, C. Menne, A. Rettinger, and F. Bartscherer. Linked Data Quality of DBpedia, Freebase, OpenCyc, Wikidata, and YAGO. \ |LINK7|\ .  [August, 2016] (revised version, under review).

\ |STYLE12|\ : [...] esistono sistemi che [...] utilizzano una varietà di tecniche per estrarre nuove conoscenze, sotto forma di fatti, dal web. Questi fatti sono correlati, e quindi recentemente questa conoscenza estratta è stata definita un grafo della conoscenza. \ |STYLE13|\ : J. Pujara, H. Miao, L. Getoor, and W. Cohen. Knowledge Graph Identification. In Proceedings of the

12th International Semantic Web Conference - Part I, ISWC ’13, pages 542–557, New York, USA, 2013. Springer.

|

.. _h6c4369422b212d22625a35337ab844:

Un elenco dettagliato di come costruire un grafo della conoscenza.
==================================================================

\ |LINK8|\ .


|REPLACE1|


|REPLACE2|


|REPLACE3|

#. \ |STYLE14|\ . Stabilire l'obiettivo alla base della raccolta dei dati e definire a quali domande si desidera rispondere.

#. \ |STYLE15|\ . Scopri quali set di dati (sia aperti che proprietari) ti servirebbero meglio per raggiungere il tuo obiettivo in termini di dominio, ambito, provenienza, manutenzione, ecc.

#. \ |STYLE16|\ . Correggere eventuali problemi di qualità dei dati per rendere i dati più applicabili alla propria attività. Ciò include la rimozione di voci non valide o prive di significato, la regolazione dei campi di dati per adattarsi a più valori, la correzione di incoerenze, ecc.

#. \ |STYLE17|\ . Analizzare a fondo i diversi schemi di dati per preparare l'armonizzazione dei dati. Ciò include il riutilizzo o la progettazione di ontologie, profili applicativi, forme RDF o altri meccanismi su come utilizzarli insieme. Formalizza il tuo modello di dati usando gli standard W3C per la definizione dello schema, come RDF Schema e OWL.

#. \ |STYLE18|\ . Applica gli strumenti ETL per convertire i tuoi dati in RDF o usa la virtualizzazione dei dati per accedervi tramite tecnologie armonizzate come NoETL, OBDA, GraphQL Federation, ecc.

#. \ |STYLE19|\ . Abbina le descrizioni di una stessa entità a tutti i set di dati con ambito sovrapposto, gestisci i loro attributi per unire campi di dati singoli e multipli e mappa manualmente le loro diverse tassonomie, il che avrà un grande impatto sulle tue analisi.

#. \ |STYLE20|\ . Scegli dove archiviare i dati convertiti in base alla tua attività poiché diversi negozi hanno scopi diversi. Un triplestore RDF (come GraphDB di Ontotext) esporrà e applicherà correttamente la semantica del modello di dati semantici tramite inferenza, controllo di coerenza e validazione.

#. \ |STYLE21|\ . Arricchisci i tuoi dati con dati semantici esterni ed esegui deduzioni per scoprire nuove informazioni da fatti esistenti. Di conseguenza, il Grafo di Conoscenza diventa più della somma dei suoi set di dati costitutivi.

#. \ |STYLE22|\ . Inizia a fornire le risposte alle tue domande originali attraverso diversi strumenti di scoperta della conoscenza come potenti query SPARQL, interfaccia GraphQL facile da usare, ricerca semantica, ricerca sfaccettata, visualizzazione dei dati, ecc. Inoltre, assicurati che i tuoi dati seguano i principi dei dati FAIR e siano facilmente reperibile, accessibile, interoperabile e riutilizzabile.

#. \ |STYLE23|\ . Infine, dopo aver realizzato il Grafo di Conoscenza in modo semantico e le persone hanno iniziato a usarlo, mantienilo attivo impostando le procedure di manutenzione del Grafo di Conoscenza: il modo in cui si evolverebbe, aggiornerà le modifiche dei dati nelle fonti, ecc.

|


+---------------------------------+
|➽ Ritorna alla pagina \ |LINK9|\ |
+---------------------------------+


.. bottom of content


.. |STYLE0| replace:: **Nota**

.. |STYLE1| replace:: **Raccolta**

.. |STYLE2| replace:: **Organizza**

.. |STYLE3| replace:: **Consumo**

.. |STYLE4| replace:: **Definition**

.. |STYLE5| replace:: **Source**

.. |STYLE6| replace:: **Definition**

.. |STYLE7| replace:: **Source**

.. |STYLE8| replace:: **Definition**

.. |STYLE9| replace:: **Source**

.. |STYLE10| replace:: **Definition**

.. |STYLE11| replace:: **Source**

.. |STYLE12| replace:: **Definition**

.. |STYLE13| replace:: **Source**

.. |STYLE14| replace:: **Chiarire i requisiti aziendali / dei dati**

.. |STYLE15| replace:: **Raccogliere e analizzare dati e ontologie pertinenti**

.. |STYLE16| replace:: **Pulisci i tuoi dati per garantire la qualità dei dati**

.. |STYLE17| replace:: **Crea il tuo modello di dati semantici**

.. |STYLE18| replace:: **Integra i tuoi dati con strumenti ETL intelligenti o approcci di virtualizzazione**

.. |STYLE19| replace:: **Armonizza i tuoi dati tramite riconciliazione, fusione dei dati e armonizzazione della tassonomia**

.. |STYLE20| replace:: **Scegli dove conservare i tuoi dati**

.. |STYLE21| replace:: **Aumenta il tuo Grafo di Conoscenza con arricchimento e inferenza semantici (testo e dati)**

.. |STYLE22| replace:: **Massimizza l'usabilità dei tuoi dati**

.. |STYLE23| replace:: **Rendi il tuo Grafo di Conoscenza facile da mantenere**


.. |REPLACE1| raw:: html

    <img src="https://www.ontotext.com/wp-content/uploads/2020/02/Knowledge-Graph_Step1-Step3.png" width="650" />
.. |REPLACE2| raw:: html

    <img src="https://www.ontotext.com/wp-content/uploads/2020/02/Knowledge-Graph_Step4-Step6.png" width="650" />
.. |REPLACE3| raw:: html

    <img src="https://www.ontotext.com/wp-content/uploads/2020/02/Knowledge-Graph_Step7-Step10.png" width="650" />

.. |LINK1| raw:: html

    <a href="https://www.semanticarts.com/semantic-ontology-the-basics/" target="_blank">https://www.semanticarts.com/semantic-ontology-the-basics</a>

.. |LINK2| raw:: html

    <a href="https://www.facebook.com/groups/opendatasicilia/permalink/2491670394284934/" target="_blank">www.facebook.com/groups/opendatasicilia/permalink/2491670394284934</a>

.. |LINK3| raw:: html

    <a href="http://ceur-ws.org/Vol-1695/paper4.pdf" target="_blank">http://ceur-ws.org/Vol-1695/paper4.pdf</a>

.. |LINK4| raw:: html

    <a href="http://www.websemanticsjournal.org/index.php/ps/announcement/view/19" target="_blank">Journal of Web Semantics:  Special Issue on Knowledge Graphs</a>

.. |LINK5| raw:: html

    <a href="https://blog.semantic-web.at/2014/07/15/from-taxonomies-over-ontologies-to-knowledge-graphs" target="_blank">From Taxonomies over Ontologies to</a>

.. |LINK6| raw:: html

    <a href="https://blog.semantic-web.at/2014/07/15/from-taxonomies-over-ontologies-to-knowledge-graphs" target="_blank">Knowledge Graphs</a>

.. |LINK7| raw:: html

    <a href="http://www.semantic-web-journal.net/content/linked-data-quality-dbpedia-freebase-opencyc-wikidata-and-yago" target="_blank">Semantic Web Journal, 2016</a>

.. |LINK8| raw:: html

    <a href="https://www.ontotext.com/blog/knowledge-graph-with-semantic-data-modeling/" target="_blank">Link all'articolo</a>

.. |LINK9| raw:: html

    <a href="https://cirospat.readthedocs.io/it/latest/vocabolari-controllati.html" target="_blank">Vocabolari controllati e ontologie per l’interoperabilità semantica</a>

