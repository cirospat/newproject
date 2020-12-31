
.. _h5e72237b1d2f21437415232c67367c3d:

developer
*********


+-------------------------------------------------------------------------------------------------------------------------------------------+
|\ |LINK1|\  è una pagina dove colleziono utilità per fini di sviluppo e creatività digitale. La pagina doc sorgente è a questo \ |LINK2|\ .|
+-------------------------------------------------------------------------------------------------------------------------------------------+


.. toctree::  
    :maxdepth: 3
    :caption: dev

    developer


|REPLACE1|


|REPLACE2|


|REPLACE3|

|

.. _ha4a69c15721f287c7e3f4245326:

CATALOGO DI TUTTE LE MAPPE DI CIRO SPATARO E DI GB VITRANO
==========================================================

\ |LINK3|\  

--------

.. _h7a604f4c23602b76e6f6e5c11765e7:

MAPPE PALERMO
=============

* \ |LINK4|\  my google maps

* \ |LINK5|\  (pagina FB con mappe su Palermo)

* \ |LINK6|\  (mappe varie di Ciro)

* \ |LINK7|\  (contenitore di oltre 100 mappe su Palermo, su Petrusino)

* \ |LINK8|\  (sito mappe di Palermo utili a turisti)

* \ |LINK9|\  (OMIRA su Umap cirospat) 

* \ |LINK10|\  elezioni2017_Palermo da Guenter Richter

* \ |LINK11|\  e relativo bot telegram #rifiutocivico

* \ |LINK12|\  mapillary cirospat

* \ |LINK13|\  Palermo su mapillary

* \ |LINK14|\  Palermo airbnb gen_2018 (Gianni Vitrano)

--------

.. _h305075b623d460273c1b71225e4959:

MAPPE PALERMO STORICA EFFETTO LENTE INGRANDIMENTO E ALTRE MAPPE INTERESSANTI
============================================================================

* \ |LINK15|\  (GBVitrano Palermo IGM 1:25000)

* \ |LINK16|\  carta tecnica comune Palermo

* \ |LINK17|\  (GBVitrano Omira 1:5000)

* \ |LINK18|\   PRG2025 (su Petrusino)

* \ |LINK19|\  (elenco mappe 2-3D di GBVitrano su Github SiciliaHub)

* \ |LINK20|\   (Hubsicilia - Omira Irta e Sas con OSM e RealVista su Gitub SiciliaHub, con metadati mappa su barra laterale)

* \ |LINK21|\  (variante general eal PRG 2004 con cerchio)

* \ |LINK22|\  (catasto centro storico 1887 con cerchio)

* \ |LINK23|\  (PRG scehma masima su PRG 2004 con cerchio)

* \ |LINK24|\    \ |LINK25|\    (Piano protezione civile Palermo)

* \ |LINK26|\   (stile petrusino)

* \ |LINK27|\   (stile petrusino, ultimo gen 2018) - hub di diverse mappe di Palermo a cura di GBVitrano iniziato gli ultimi giorni di dic. del 2017

--------

.. _h565872655f43734d6095583123c76:

SERVIZI DI WEBMAPPING ALTERNATIVI A UMAP
========================================

\ |LINK28|\  (che preferisco) 

\ |LINK29|\  (intramontabile) 

\ |LINK30|\  (questo però è un plugin per wordpress) 

\ |LINK31|\  (a pagamento)

\ |LINK32|\  \ |STYLE0|\ 

* Enter a latitude/longitude

* Lat/lng in deg min sec

* Enter a UK grid reference

* UK Northing/Easting

* Plus code

* what3words

--------

.. _h1e2c374df4a3014336ba536e5e5e6c:

FILTRI CON "DATE" NELLE FUNZIONI DI RICERCA (QUERY) DA USARE NEI GOOGLE SPREADSHEET
===================================================================================

\ |LINK33|\ 

Usare il formato YYYY-MM-DD.

The \ |LINK34|\  function converts it to the required format for the Query formula by specifying a format of "yyyy-mm-dd":

.. code:: 

    =TEXT(DATEVALUE("1/1/2000"),"yyyy-mm-dd")


.. code:: 

    = TEXT( NOW() , "hh:mm am/pm" )
    
    The formula:    = TEXT( NOW() , "hh:mm am/pm" )    will output the time just fine!

The output of this formula is a date in the desired format:

.. code:: 

    2000-01-01

\ |STYLE1|\ 

Substitute the TODAY() function into our formula:

.. code:: 

    =QUERY(Data!$A$1:$H$136,"select C, B where B > date '"&TEXT(TODAY(),"yyyy-mm-dd")&"'",1)

\ |STYLE2|\ 

\ |LINK35|\ 

.. _h5979383b6f422d6f1a3f404a4258253f:

Query di Andrea Borruso
-----------------------


+---+------------+--------------------------------------------------+-------------------------------------------------------------------------------------+
|   |A           |B                                                 |C                                                                                    |
+---+------------+--------------------------------------------------+-------------------------------------------------------------------------------------+
|1  |\ |STYLE3|\ |\ |STYLE4|\                                       |\ |STYLE5|\                                                                          |
+---+------------+--------------------------------------------------+-------------------------------------------------------------------------------------+
|2  |05/12/2019  |``=if(A2="";"";TEXT(DATEVALUE(A2);"yyyy-mm-dd"))``|``=query("select * where (B > date '"&text(TODAY();"yyyy-mm-dd")&"' OR R = '') ";1)``|
+---+------------+--------------------------------------------------+-------------------------------------------------------------------------------------+

--------

.. _h386c10261440441c2374124f3d34445:

IMMAGINI DENTRO GOOGLE DRIVE SPREADSHEET
========================================

Combine the IMAGE and HYPERLINK functions to create clickable images

.. code:: 

    =HYPERLINK( "https://www.google.com/" , IMAGE( "https://www.google.com/favicon.ico" ) )

--------

.. _h2a5254404e7a6b2c7131e3066704d6d:

SFONDI TILES PER MAPPE UMAP
===========================

* lista di tiles per sfondi   \ |LINK36|\  

* tiles vari da usare  \ |LINK37|\  

* satellite tile ESRI - World Imagery \ |LINK38|\  

* satellite tile Google \ |LINK39|\  

* tile con sfondo satellite da mapbox/satellite-v9 con API: \ |LINK40|\   (senza nomi strade)

* \ |LINK41|\  (con nomi strade)

* SERVIZIO ONLINE CREAZIONE DI TILES DA IMMAGINI  Mapwarper \ |LINK42|\  

* \ |LINK43|\  tile: https://api.mapbox.com/styles/v1/rplln/cjix2cv5l83yz2rmne9icvusx/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoicnBsbG4iLCJhIjoiY2ppeDI5ZTByMDVtMzN1cDRxZWlzamwzcyJ9.Yn6OjT0SStL2tffNloZrdg

--------

.. _h607b3a763222151e4a1c121b50313b6c:

CODICE DA USARE PER MAPPE UMAP
==============================

video embedding = {{{\ |LINK44|\ }}}

link con testo = [[\ |LINK45|\ |testo del link]] 

immagine = {{\ |LINK46|\ |larghezza}} Immagine 

link a url con icona cliccabile = [[\ |LINK47|\ }}]]

ICONE MAPPE = \ |LINK48|\  

GOOGLEMAPS = <iframe width='100%' height='500' src="http....   "></iframe>

URL ENCODER E DECODER = \ |LINK49|\  

POST IMAGE DA LINKARE SU UMAP: \ |LINK50|\  

Icone mappe \ |LINK51|\  ccbysa

.. _h1c7b5b1f64462a201813244135465568:

GOOGLE DRIVE SPREADSHEET TO UMAP
--------------------------------

Video breve per alimentare in modo facile uMap da un foglio elettronico su Google Drive, by Andrea Borruso \ |LINK52|\ 

Tutorial per fare mappe alimentate da google spreadsheet = \ |LINK53|\  

DB x UMAP con output in csv =

.. code:: 

    https://spreadsheets.google.com/tq?tqx=out:csv&tq=SELECT%20B%2CC%2CD%2CE%2CF%2CG%2CH%20WHERE%20G%20Contains%20%27.%27&key=

| 

.. _h63332d1c432651713b441e586e2e476d:

\ |LINK54|\  e \ |LINK55|\  UMAP AVVISI POLIZIA MUNICIPALE PA
-------------------------------------------------------------

\ |STYLE6|\ .


.. code:: 

    =IMPORTXML("https://www.comune.palermo.it/feed/rss_pm.xml","//item") 
    TRUE:   =if(G2="","",REGEXMATCH(G2,"[a-zA-Z]{3}, "&TEXT(DAY(TODAY()),"00")))

La query per Umap è =


.. code:: 

    https://spreadsheets.google.com/tq?tqx=out:csv&tq=SELECT%20A%2CB%2CC%2CG%2CH%2CI%20WHERE%20H%20Contains%20%27.%27%20AND%20K%20Contains%20%27true%27&key=1nalX173WMBzIl7kWrMb52CG5MvRuyLqhvR7hCMk7CIM  
    
    (db GBVitrano)


.. code:: 

    https://spreadsheets.google.com/tq?tqx=out:csv&tq=SELECT%20A%2CB%2CC%2CG%2CH%2CI%20WHERE%20H%20Contains%20%27.%27%20AND%20K%20Contains%20%27true%27&key=1laR9p_Ua0BPCJee5BbHvV7S-tjbmHxhLksUdKnZEW0M 
    
    (db Andrea Borruso)

--------

.. _h5443d5022373b132c3257d5e6e546:

GEOCODER PER TROVARE COORDINATE LATITUDINE E LONGITUDINE 
=========================================================


|REPLACE4|

⇒ \ |LINK56|\  plug in come componente aggiuntivo da installare su spreadsheet di Google. Sfrutta API di Google e quindi i dati delle coordinate geografiche sono riusabili solo su mappe Google.

\ |STYLE7|\  API che usa la seguente formula: 

.. code:: 

    =JOIN(",", ImportXML(CONCATENATE("http://nominatim.openstreetmap.org/search/?format=xml&q=",A2), "//place[1]/@lat | //place[1]/@lon"))

dove A2 è la colonna dove è contenuto l'indirizzo. \ |LINK57|\ .


|REPLACE5|

* \ |LINK58|\  con Openstreetmap tramite OnData

* \ |LINK59|\   con Openstreetmap

* \ |LINK60|\  con Openstreetmap

* \ |LINK61|\  con Openstreetmap

* \ |LINK62|\  con Googlemap

* \ |LINK63|\  by GBVitrano con API Google

* \ |LINK64|\  by GBVitrano con API Google

* \ |LINK65|\  con le API di Google

    * \ |LINK66|\  con API Google

* \ |LINK67|\  (google e bing) 

* \ |LINK68|\  con API di Mapquest

* \ |LINK69|\  API Mapquest per geocoding (cirospat - caneclaudia2volte)

* \ |LINK70|\  location helper in versione demo di Mapbox

--------

.. _h59432417563a5658746a24186d4d63c:

SENSORE POLVERI SOTTILI COLLEGATO AD UNA RETE ONLINE E DATI SU MAPPA
====================================================================

* \ |LINK71|\  (tutorial) - 

* \ |LINK72|\  (mappa con grafici e dati su sensore mio)

--------

.. _h631d7b1e4d1e68301d55423b256d212:

GIT GUIDE
=========

just a simple guide for getting started with git. \ |LINK73|\ 

--------

.. _h5a573672d621f4a3b656f28542c01a:

REPOSITORY DATA CIRO SPATARO
============================

\ |LINK74|\  

\ |LINK75|\  

--------

.. _h2778167b752037aa551c4b182d05:

MACHINE LEARNING E ARTIFICIAL INTELLIGENCE
==========================================

\ |LINK76|\  un articolo per capire un po

--------

.. _h2d6b469794e1c284e67294b2f4a5b52:

RICHIESTA FOIA ONLINE
=====================

\ |LINK77|\  generatore di richieste di accesso civico generalizzato (FOIA) a cura di Giovanni Pirrotta e Giuseppe Ragusa

--------

.. _h597d5e521a157c477c7371454c784711:

CSV EDITOR
==========

* \ |LINK78|\   download

* \ |LINK79|\  editor online sulla falsa riga di Google spreadsheet

--------

.. _h4c6c275e14302f40783e423111543c68:

EDITOR ONLINE PER LAVORI CONDIVISI
==================================

* \ |LINK80|\  

* \ |LINK81|\ 

* \ |LINK82|\ 

* \ |LINK83|\  

* \ |LINK84|\  

--------

.. _h111216149473f7510705c312977184a:

QUERY PER XML (RSS FEED) E FEEDBURNER
=====================================

.xml?query=cad&newscount=25

cad= parola da cercare

newscount= il numero delle news da visualizzare come output della query

\ |LINK85|\ 

\ |STYLE8|\  

* \ |LINK86|\  il mio genratore di feed RSS

* \ |LINK87|\  - \ |LINK88|\  per costruire Feed per gli eventi Feltrinelli di Palermo

--------

.. _h231f6c11635e136146664a627213879:

Badge img shields
=================

\ |LINK89|\ 

--------

.. _h3d4153661183e671395d2c4b706f3b:

web service per creare loghi e icone 
=====================================

\ |LINK90|\  

--------

.. _h337f7b59693822377f7601745347c:

Cards
=====

\ |LINK91|\ 

--------

.. _h174c79c39577e65293f6b5738726d5c:

Unire PDF
=========

\ |LINK92|\ 

* PDFTK Builder \ |LINK93|\  

* Online2PDF \ |LINK94|\  

* \ |LINK95|\  — servizio Web gratuito e che non richiede registrazioni. Permette di unire e modificare i file PDF in vari modi. Da notare che non consente di caricare file aventi un peso superiore ai 100 MB. Eventualmente, però, è possibile aggirare questa limitazione passando a uno dei piani a pagamento (con costi a partire da 6 euro/mese), i quali consentono di sbloccare anche altre funzionalità extra.

* \ |LINK96|\  — si tratta di un altro servizio Web gratuito e che non necessita di registrazione e permette di intervenire sui documenti PDF unendoli, oltre che convertendoli, dividendoli, alleggerendoli, sbloccandoli ecc. Non applica limitazioni per quel che concerne il peso massimo dei file.

* \ |LINK97|\  — è un’altra soluzione per unire i file PDF via Web e tramite la quale è eventualmente possibile apportare varie ulteriori modifiche ai documenti caricati. È gratis, non richiede registrazione e non pone limiti per l’upload.

\ |STYLE9|\ 

\ |STYLE10|\ . Si tratta, infatti, di un’app che consente di visualizzare i file PDF e intervenire su di essi in vari modi, andandoli a convertire, unire ecc. È gratuita e facile da usare. Per effettuarne il download sul tuo dispositivo, accedi alla \ |LINK98|\ 

--------

.. _h225bd2729b5f536b2e442259197a52:

Carousel
========

\ |LINK99|\ 

|

←  ↑  →  ↓  ↖   ↗   ↘   ↙ 

.. _h3d5e7e425c116114e331b3e663c3b47:

Directives in Read the Docs
===========================

:guilabel:`Queste ed altre indicazioni per Read the Docs si tovano anche a` \ |LINK100|\  


.. class:: importante

    una prova di contenuto dentro una generic ``directive``.
    Questa è la renderizzazione su pagine web a seguito del commit su Github

:download:\`Questo link è per il download <\ |LINK101|\ >\`.

si scrive così: ``:download:`Questo link è per il download <\ |LINK102|\ >```


.. centered:: Questo è un testo centrato.

si scrive così: ``.. centered:: Questo è un testo centrato.``

\ |STYLE11|\ 


+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|:Author: David Goodger                                                                                                                                                                                          |
|                                                                                                                                                                                                                |
|:Address: 123 Example Street, Example, EX  Canada, A1B 2C3, 123 Example Street, Example, EX  Canada, A1B 2C3, 123 Example Street, Example, EX  Canada, A1B 2C3, 123 Example Street, Example, EX  Canada, A1B 2C3|
|                                                                                                                                                                                                                |
|:Contact: docutils-develop@lists.sourceforge.net                                                                                                                                                                |
|                                                                                                                                                                                                                |
|:Authors: Me; Myself; I                                                                                                                                                                                         |
|                                                                                                                                                                                                                |
|:Author: David Goodger                                                                                                                                                                                          |
|                                                                                                                                                                                                                |
|:Address: 123 Example Street, Example, EX  Canada, A1B 2C3                                                                                                                                                      |
|                                                                                                                                                                                                                |
|:Contact: docutils-develop@lists.sourceforge.net                                                                                                                                                                |
|                                                                                                                                                                                                                |
|:Authors: Me; Myself; I                                                                                                                                                                                         |
|                                                                                                                                                                                                                |
|:Authors: Me; Myself; I                                                                                                                                                                                         |
|                                                                                                                                                                                                                |
|:Authors: Me; Myself; I                                                                                                                                                                                         |
|                                                                                                                                                                                                                |
|:Author: David Goodger                                                                                                                                                                                          |
|                                                                                                                                                                                                                |
|:Link utili: \ |LINK103|\ , \ |LINK104|\                                                                                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

\ |STYLE12|\ 

:Author: David Goodger

:Address: 123 Example Street, Example, EX  Canada, A1B 2C3, 123 Example Street, Example, EX  Canada, A1B 2C3

:Contact: docutils-develop@lists.sourceforge.net

:Authors: Me; Myself; I

:Author: David Goodger

:Address: 123 Example Street, Example, EX  Canada, A1B 2C3

:Contact: docutils-develop@lists.sourceforge.net

:Authors: Me; Myself; I

\ |STYLE13|\ 


.. sidebar:: Argomento
    :subtitle: Sotto argomento

    Questo è il ``sidebar``.  \ |STYLE14|\  il testo al di fuori del flusso del testo principale. Questa è una casella. laterale. Si usa per il testo al di fuori del flusso del testo principale. Questa è una casella.
    
    .. rubric:: Questa è una rubrica dentro il ``sidebar``
    Le barre laterali vengono spesso visualizzate accanto al testo principale con un bordo e un colore grigio chiaro (solitamente) di sfondo.

:guilabel:`Qualche azione`  viene renderizzata così come la leggi, ma la devi scrivere così: ``:guilabel:`Qualche azione```

:class:`nero` viene renderizzata così come la leggi, ma la devi scrivere così: ``:class:`nero```

:kbd:`nero` viene renderizzata così come la leggi, ma la devi scrivere così: ``:kbd:`nero```

:data:`prova3` viene renderizzata così come la leggi, ma la devi scrivere così: ``:data:`prova3```

--------


.. glossary::   
    :class:`Documentation`
       Provides users with the knowledge they need to use something.
    
    :class:`Reading`
       The process of taking information into ones mind through the use of eyes.
    
    :class:`Writing`
       The process of putting thoughts into a medium for other people to :term:`read <Reading>`.

--------


.. method:: (questa è una prova)

    This method is called for each request that goes through the download middleware. 
    
       This method is called for each request that goes through the download middleware.
    
       :meth:`nero` e return ``rosso``, return a :class:`prova` object,
    
    


.. class:: io 

    This method is called for each request that goes through the download middleware. 
    
       This method is called for each request that goes through the download middleware.
    
       return ``rosso``, return a :class:`nero` object,

--------


.. bottom of content


.. |STYLE0| replace:: **Lat/long finderSearch for an address**

.. |STYLE1| replace:: **Using today’s date as a filter**

.. |STYLE2| replace:: **Vedi anche le Query**

.. |STYLE3| replace:: **data**

.. |STYLE4| replace:: **standardDate**

.. |STYLE5| replace:: **query per esporre le celle con date ancora da venire e le celle con valore "null" (celle vuote senza valori)**

.. |STYLE6| replace:: **Da un foglio Google ad una mappa uMap in cui vengono visualizzati solo gli avvisi della data odierna**

.. |STYLE7| replace:: **⇒ Nominatim Openstreetmap**

.. |STYLE8| replace:: **Generatore di Feed:**

.. |STYLE9| replace:: **Su Android**

.. |STYLE10| replace:: **PDFelement**

.. |STYLE11| replace:: **Lista di elementi dentro un riquadro ↓**

.. |STYLE12| replace:: **Lista di elementi senza riquadro ↓**

.. |STYLE13| replace:: **Sidebar**

.. |STYLE14| replace:: **Si usa per**


.. |REPLACE1| raw:: html

    <div style="width: 550px; height: 400px;" data-wordart-src="//cdn.wordart.com/json/e9h2wyb41pzf"></div>
.. |REPLACE2| raw:: html

    <div style="width: 400px; height: 400px;" data-wordart-src="//cdn.wordart.com/json/v4ejjx85ti99"></div>
.. |REPLACE3| raw:: html

    <img src="https://images.unsplash.com/photo-1529666759085-741eefcd3371?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=700" /> Art by Lønfeldt
.. |REPLACE4| raw:: html

    <p><span style="background-color: #6462d1; color: #ffffff; display: inline-block; padding: 3px 8px; border-radius: 10px;">Su fogli google spreadsheet</span></p>
.. |REPLACE5| raw:: html

    <p><span style="background-color: #105618; color: #ffffff; display: inline-block; padding: 3px 8px; border-radius: 10px;">Altri Geocoder</span></p>

.. |LINK1| raw:: html

    <a href="http://cirospat.readthedocs.io/it/latest/developer.html" target="_blank">cirospat.readthedocs.io/it/latest/developer.html</a>

.. |LINK2| raw:: html

    <a href="https://docs.google.com/document/d/1UBNgDirj7I4cCSZSSLqbygu3U4SM8IoeW0M22HcOBPI" target="_blank">link</a>

.. |LINK3| raw:: html

    <a href="https://docs.google.com/spreadsheets/d/1auVqTh1aeJ1c2DuYUWI1UX0p8OHtupApFEjCXWsmxbA" target="_blank">https://docs.google.com/spreadsheets/d/1auVqTh1aeJ1c2DuYUWI1UX0p8OHtupApFEjCXWsmxbA</a>

.. |LINK4| raw:: html

    <a href="https://www.google.com/maps/d/u/0/?hl=it&authuser=0&action=open" target="_blank">https://www.google.com/maps/d/u/0/?hl=it&authuser=0&action=open</a>

.. |LINK5| raw:: html

    <a href="https://www.facebook.com/mappedipalermo/" target="_blank">https://www.facebook.com/mappedipalermo/</a>

.. |LINK6| raw:: html

    <a href="http://umap.openstreetmap.fr/it/user/cirospat/" target="_blank">http://umap.openstreetmap.fr/it/user/cirospat/</a>

.. |LINK7| raw:: html

    <a href="http://bit.ly/palermomaps" target="_blank">http://bit.ly/palermomaps</a>

.. |LINK8| raw:: html

    <a href="http://bit.ly/palermo_maps" target="_blank">http://bit.ly/palermo_maps</a>

.. |LINK9| raw:: html

    <a href="http://u.osmfr.org/m/136197" target="_blank">u.osmfr.org/m/136197</a>

.. |LINK10| raw:: html

    <a href="http://projects.ixmaps.com.s3-website-eu-west-1.amazonaws.com/Palermo_Elezioni/app/Palermo_Elezioni/index_2017_full.html" target="_blank">http://projects.ixmaps.com.s3-website-eu-west-1.amazonaws.com/Palermo_Elezioni/app/Palermo_Elezioni/index_2017_full.html</a>

.. |LINK11| raw:: html

    <a href="http://lrssvt.ns0.it/rifiutocivico/#11/38.1375/13.5733" target="_blank">http://lrssvt.ns0.it/rifiutocivico/#11/38.1375/13.5733</a>

.. |LINK12| raw:: html

    <a href="https://www.mapillary.com/app/user/cirospat?lat=36.82147841468249&lng=15.104561915917657&z=15.017458713501235" target="_blank">https://www.mapillary.com/app/user/cirospat?lat=36.82147841468249&lng=15.104561915917657&z=15.017458713501235</a>

.. |LINK13| raw:: html

    <a href="https://www.mapillary.com/app/?lat=38.12949822320789&lng=13.368035190329692&z=13.561628216364625&menu=false&mapStyle=mapbox_satellite" target="_blank">https://www.mapillary.com/app/?lat=38.12949822320789&lng=13.368035190329692&z=13.561628216364625</a>

.. |LINK14| raw:: html

    <a href="http://u.osmfr.org/m/198624/" target="_blank">http://u.osmfr.org/m/198624/</a>

.. |LINK15| raw:: html

    <a href="http://gbvitrano.it/qgis/pa_carto/" target="_blank">http://gbvitrano.it/qgis/pa_carto/</a>

.. |LINK16| raw:: html

    <a href="http://github.gbvitrano.it/atlante_ctc_pa/index.html" target="_blank">http://github.gbvitrano.it/atlante_ctc_pa/index.html</a>

.. |LINK17| raw:: html

    <a href="http://gbvitrano.it/qgis/carto_storica" target="_blank">http://gbvitrano.it/qgis/carto_storica</a>

.. |LINK18| raw:: html

    <a href="http://gbvitrano.it/qgis/pa_carto/prg_2015.php" target="_blank">http://gbvitrano.it/qgis/pa_carto/prg_2015.php</a>

.. |LINK19| raw:: html

    <a href="https://github.com/SiciliaHub/mappe" target="_blank">https://github.com/SiciliaHub/mappe</a>

.. |LINK20| raw:: html

    <a href="http://siciliahub.github.io/mappe/atlante_carto_pa/" target="_blank">http://siciliahub.github.io/mappe/atlante_carto_pa/</a>

.. |LINK21| raw:: html

    <a href="http://egdisegno.studiovitrano.it/variante_generale/Zonizzazione.html" target="_blank">http://egdisegno.studiovitrano.it/variante_generale/Zonizzazione.html</a>

.. |LINK22| raw:: html

    <a href="http://egdisegno.studiovitrano.it/catasto_pa_1887" target="_blank">http://egdisegno.studiovitrano.it/catasto_pa_1887</a>

.. |LINK23| raw:: html

    <a href="http://egdisegno.studiovitrano.it/variante_generale/prg_2015.html" target="_blank">http://egdisegno.studiovitrano.it/variante_generale/prg_2015.html</a>

.. |LINK24| raw:: html

    <a href="http://github.gbvitrano.it/ppc" target="_blank">http://github.gbvitrano.it/ppc</a>

.. |LINK25| raw:: html

    <a href="http://siciliahub.github.io/mappe/ppc" target="_blank">http://siciliahub.github.io/mappe/ppc</a>

.. |LINK26| raw:: html

    <a href="https://siciliahub.github.io/mappe/palermo_hub/index.html" target="_blank">https://siciliahub.github.io/mappe/palermo_hub/index.html</a>

.. |LINK27| raw:: html

    <a href="https://siciliahub.github.io/palermohub/index.html" target="_blank">https://siciliahub.github.io/palermohub/index.html</a>

.. |LINK28| raw:: html

    <a href="https://l.facebook.com/l.php?u=https%3A%2F%2Fmaphub.net%2F&h=ATNg797_CAp5QX8MdtGE2t5QmsZ4zCHG2T6FXg3PFgptOklmzkPnVWpvAhUj6J_DatUI2UTyOL0IFdbo5lPnKtZ8KmtpnHmJUjSgRaflW44uMERy5ZR_RWyvClQEIEJnV1Dmr7IS" target="_blank">https://maphub.net/</a>

.. |LINK29| raw:: html

    <a href="https://l.facebook.com/l.php?u=https%3A%2F%2Fcrowdmap.com%2F&h=ATPxCiw6g584R_YPauk3WAaUXxblQ4If-KRQxUpzp1sOELRXRgZuD4mgqqJHJvTNWGzBDJ3x-Q-iwQpKDdjq4fCC8JIjWft_F4JUE5Y23UpSLJ55YxOIi7EMHMV2g3pKAASCHOjN" target="_blank">https://crowdmap.com/</a>

.. |LINK30| raw:: html

    <a href="https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.mapsmarker.com%2F&h=ATPouIz1_8mZonVbTHhYY9OwCeTfZmXSD-9hdJOjGNRfZroByLW72KZ3niNiREDAGi3lLTWW8LG-cCr3R3d3zTQB2QUIJIU2ldiPtc7frt75xiTK56So9_K906Bi_008XjlTFI3S" target="_blank">https://www.mapsmarker.com/</a>

.. |LINK31| raw:: html

    <a href="https://l.facebook.com/l.php?u=http%3A%2F%2Fwww.maptiler.com%2Fgeoeditor%2F&h=ATOIEGdaqbjrDIB4OnZk4GRogoAV7FbenrYuwjgPw3Z10gquAPZYyeXp7DhsN6uqevc_Q_qJjKOXVqhpT2WsM7jiJgCAwZ17llK4NceigsM6vYQjuJ0ObYICn2JHQsujpveAB_3F" target="_blank">http://www.maptiler.com/geoeditor/</a>

.. |LINK32| raw:: html

    <a href="https://www.doogal.co.uk/LatLong.php" target="_blank">https://www.doogal.co.uk/LatLong.php</a>

.. |LINK33| raw:: html

    <a href="https://www.benlcollins.com/spreadsheets/query-dates/" target="_blank">https://www.benlcollins.com/spreadsheets/query-dates/</a>

.. |LINK34| raw:: html

    <a href="https://support.google.com/docs/answer/3094139?hl=en" target="_blank">TEXT()</a>

.. |LINK35| raw:: html

    <a href="https://www.benlcollins.com/spreadsheets/google-sheets-query-sql/" target="_blank">https://www.benlcollins.com/spreadsheets/google-sheets-query-sql/</a>

.. |LINK36| raw:: html

    <a href="http://geomappando.com/maps/OL3_map_tile_provider.html" target="_blank">http://geomappando.com/maps/OL3_map_tile_provider.html</a>

.. |LINK37| raw:: html

    <a href="https://leaflet-extras.github.io/leaflet-providers/preview/" target="_blank">https://leaflet-extras.github.io/leaflet-providers/preview/</a>

.. |LINK38| raw:: html

    <a href="http://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}" target="_blank">http://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}</a>

.. |LINK39| raw:: html

    <a href="https://mt1.google.com/vt/lyrs=s&x=%7Bx%7D&y=%7By%7D&z=%7Bz%7D" target="_blank">https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}</a>

.. |LINK40| raw:: html

    <a href="http://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx" target="_blank">http://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx</a>

.. |LINK41| raw:: html

    <a href="https://api.mapbox.com/styles/v1/mapbox/satellite-streets-v9/tiles/{z}/{x}/{y}?access_token=pk.eyJ1Ijoibm9yZGFpIiwiYSI6ImtCWWpvY00ifQ.E9g3YhLqDFGkdXx7pKnCWw" target="_blank">https://api.mapbox.com/styles/v1/mapbox/satellite-streets-v9/tiles/{z}/{x}/{y}?access_token=pk.eyJ1Ijoibm9yZGFpIiwiYSI6ImtCWWpvY00ifQ.E9g3YhLqDFGkdXx7pKnCWw</a>

.. |LINK42| raw:: html

    <a href="http://mapwarper.net/" target="_blank">http://mapwarper.net/</a>

.. |LINK43| raw:: html

    <a href="http://umap.openstreetmap.fr/it/map/lete-numerique-de-louis-chadourne_228928#6/41.714/9.426" target="_blank">mappa antica del mondo</a>

.. |LINK44| raw:: html

    <a href="https://www.youtube.com/embed/_______|250" target="_blank">https://www.youtube.com/embed/_______|250</a>

.. |LINK45| raw:: html

    <a href="http://example.com/" target="_blank">http://example.com</a>

.. |LINK46| raw:: html

    <a href="http://immagine.url.it/" target="_blank">http://immagine.url.it</a>

.. |LINK47| raw:: html

    <a href="http://opendatasicilia.it|{{http://hexb.in/hexagons/opendatasicilia.png|90" target="_blank">http://opendatasicilia.it|{{http://hexb.in/hexagons/opendatasicilia.png|90</a>

.. |LINK48| raw:: html

    <a href="http://www.cityplanner.it/supply/icon_web/mapbox-maki-51d4f10/src/" target="_blank">http://www.cityplanner.it/supply/icon_web/mapbox-maki-51d4f10/src/</a>

.. |LINK49| raw:: html

    <a href="http://meyerweb.com/eric/tools/dencoder/" target="_blank">http://meyerweb.com/eric/tools/dencoder/</a>

.. |LINK50| raw:: html

    <a href="http://postimages.org/" target="_blank">http://postimages.org/</a>

.. |LINK51| raw:: html

    <a href="https://mapicons.mapsmarker.com" target="_blank">https://mapicons.mapsmarker.com</a>

.. |LINK52| raw:: html

    <a href="https://www.youtube.com/watch?v=YKZc84WtTd4" target="_blank">https://www.youtube.com/watch?v=YKZc84WtTd4</a>

.. |LINK53| raw:: html

    <a href="https://docs.google.com/document/d/1NARnTh4orNbIHEe8uROLYbWoc40nS3cGBpZqxBYFe5I" target="_blank">https://docs.google.com/document/d/1NARnTh4orNbIHEe8uROLYbWoc40nS3cGBpZqxBYFe5I</a>

.. |LINK54| raw:: html

    <a href="https://docs.google.com/spreadsheets/d/1laR9p_Ua0BPCJee5BbHvV7S-tjbmHxhLksUdKnZEW0M/edit#gid=0" target="_blank">DATASET XML</a>

.. |LINK55| raw:: html

    <a href="http://umap.openstreetmap.fr/it/map/avvisi-polizia-municipale-sulla-mobilita-di-palerm_135416" target="_blank">MAPPA</a>

.. |LINK56| raw:: html

    <a href="https://chrome.google.com/webstore/detail/geocode-by-awesome-table/cnhboknahecjdnlkjnlodacdjelippfg" target="_blank">Awesome Table</a>

.. |LINK57| raw:: html

    <a href="https://docs.google.com/spreadsheets/d/1y01HJEl5RQeSKbzA9TRyNdmHCaac7kNRjYgj3nH7oHo/edit#gid=652519043" target="_blank">Un esempio è qui</a>

.. |LINK58| raw:: html

    <a href="http://geocoder.ondata.it/" target="_blank">http://geocoder.ondata.it/</a>

.. |LINK59| raw:: html

    <a href="http://dati.comune.galatone.le.it/geocoder/" target="_blank">http://dati.comune.galatone.le.it/geocoder/</a>

.. |LINK60| raw:: html

    <a href="http://school.dataninja.it/tools/geocoder-trova-le-coordinate/" target="_blank">http://school.dataninja.it/tools/geocoder-trova-le-coordinate/</a>

.. |LINK61| raw:: html

    <a href="http://www.apposta.biz/prove/geocoder.php" target="_blank">http://www.apposta.biz/prove/geocoder.php</a>

.. |LINK62| raw:: html

    <a href="http://it.mygeoposition.com/" target="_blank">http://it.mygeoposition.com/</a>

.. |LINK63| raw:: html

    <a href="https://coseerobe.gbvitrano.it/geocodifica-il-tuo-indirizzo-utility.html" target="_blank">https://coseerobe.gbvitrano.it/geocodifica-il-tuo-indirizzo-utility.html</a>

.. |LINK64| raw:: html

    <a href="https://siciliahub.github.io/mappe/geolocation/geolocation.html" target="_blank">https://siciliahub.github.io/mappe/geolocation/geolocation.html</a>

.. |LINK65| raw:: html

    <a href="https://developers.google.com/maps/documentation/geocoding/start" target="_blank">https://developers.google.com/maps/documentation/geocoding/start</a>

.. |LINK66| raw:: html

    <a href="https://docs.google.com/spreadsheets/d/1_MH8u1JESQ_Qls5YBcZvlCLKvMmAsiV46b-w3kZQL8Y/edit#gid=0" target="_blank">Foglio mio prova geocode</a>

.. |LINK67| raw:: html

    <a href="http://www.gpsvisualizer.com/geocode" target="_blank">http://www.gpsvisualizer.com/geocode</a>

.. |LINK68| raw:: html

    <a href="http://www.gpsvisualizer.com/geocoder/" target="_blank">http://www.gpsvisualizer.com/geocoder/</a>

.. |LINK69| raw:: html

    <a href="https://developer.mapquest.com/user/me/apps" target="_blank">https://developer.mapquest.com/user/me/apps</a>

.. |LINK70| raw:: html

    <a href="https://demos.mapbox.com/location-helper/" target="_blank">https://demos.mapbox.com/location-helper/</a>

.. |LINK71| raw:: html

    <a href="http://bit.ly/tutorialkitpolverisottili" target="_blank">http://bit.ly/tutorialkitpolverisottili</a>

.. |LINK72| raw:: html

    <a href="http://bit.ly/pm10pa" target="_blank">http://bit.ly/pm10pa</a>

.. |LINK73| raw:: html

    <a href="http://rogerdudler.github.io/git-guide/" target="_blank">http://rogerdudler.github.io/git-guide</a>

.. |LINK74| raw:: html

    <a href="https://data.world/cirospat/" target="_blank">data.world/cirospat</a>

.. |LINK75| raw:: html

    <a href="https://archive.org/details/@ciro_spataro" target="_blank">archive.org/details/@ciro_spataro</a>

.. |LINK76| raw:: html

    <a href="https://google.qwiklabs.com/quests/32" target="_blank">https://google.qwiklabs.com/quests/32</a>

.. |LINK77| raw:: html

    <a href="http://www.foiapop.it/" target="_blank">www.foiapop.it</a>

.. |LINK78| raw:: html

    <a href="http://comma-chameleon.io/" target="_blank">http://comma-chameleon.io/</a>

.. |LINK79| raw:: html

    <a href="https://ethercalc.org/" target="_blank">https://ethercalc.org/</a>

.. |LINK80| raw:: html

    <a href="https://htmlg.com/html-editor/" target="_blank">https://htmlg.com/html-editor/</a>

.. |LINK81| raw:: html

    <a href="https://www.editpad.org/" target="_blank">https://www.editpad.org/</a>

.. |LINK82| raw:: html

    <a href="https://html-online.com/editor/" target="_blank">https://html-online.com/editor/</a>

.. |LINK83| raw:: html

    <a href="http://collabedit.com" target="_blank">http://collabedit.com</a>

.. |LINK84| raw:: html

    <a href="https://hackmd.io/AwEwHALAbBCGBmBaAnDAzIiBWZwUFMBjCRIgdjPlmpACZDkg?both" target="_blank">https://hackmd.io/AwEwHALAbBCGBmBaAnDAzIiBWZwUFMBjCRIgdjPlmpACZDkg?both</a>

.. |LINK85| raw:: html

    <a href="http://www.ilquotidianodellapa.it/_aree/feed_advanced.html" target="_blank">http://www.ilquotidianodellapa.it/_aree/feed_advanced.html</a>

.. |LINK86| raw:: html

    <a href="https://feedburner.google.com/fb/a/myfeeds" target="_blank">https://feedburner.google.com/fb/a/myfeeds</a>

.. |LINK87| raw:: html

    <a href="https://feed43.com/" target="_blank">Feed43</a>

.. |LINK88| raw:: html

    <a href="https://groups.google.com/forum/#!topic/opendatasicilia/mj4rOt3VUNg" target="_blank">vedi tutorial di Andrea Borruso</a>

.. |LINK89| raw:: html

    <a href="https://img.shields.io/badge/fondamentali-amministrazione_digitale-red?style=popout&logo=Read%20the%20Docs" target="_blank">https://img.shields.io/badge/fondamentali-amministrazione_digitale-red?style=popout&logo=Read%20the%20Docs</a>

.. |LINK90| raw:: html

    <a href="https://www.canva.com/" target="_blank">https://www.canva.com/</a>

.. |LINK91| raw:: html

    <a href="https://getbootstrap.com/docs/4.0/components/card/#border" target="_blank">https://getbootstrap.com/docs/4.0/components/card/#border</a>

.. |LINK92| raw:: html

    <a href="https://www.aranzulla.it/come-unire-due-pdf-923476.html" target="_blank">https://www.aranzulla.it/come-unire-due-pdf-923476.html</a>

.. |LINK93| raw:: html

    <a href="http://angusj.com/pdftkb/#pdftkbuilder" target="_blank">http://angusj.com/pdftkb/#pdftkbuilder</a>

.. |LINK94| raw:: html

    <a href="http://online2pdf.com/" target="_blank">http://online2pdf.com/</a>

.. |LINK95| raw:: html

    <a href="https://www.ilovepdf.com/it/unire_pdf" target="_blank">iLovePDF</a>

.. |LINK96| raw:: html

    <a href="https://pdfcandy.com/it/merge-pdf.html" target="_blank">PDF Candy</a>

.. |LINK97| raw:: html

    <a href="https://tools.pdf24.org/it/unire-pdf" target="_blank">PDF24</a>

.. |LINK98| raw:: html

    <a href="https://play.google.com/store/apps/details?id=com.wondershare.pdfelement&hl=it" target="_blank">relativa sezione del Play Store</a>

.. |LINK99| raw:: html

    <a href="https://getbootstrap.com/docs/4.0/components/carousel/" target="_blank">https://getbootstrap.com/docs/4.0/components/carousel/</a>

.. |LINK100| raw:: html

    <a href="https://schema-tipo.readthedocs.io/" target="_blank">https://schema-tipo.readthedocs.io/</a>

.. |LINK101| raw:: html

    <a href="https://readthedocs.org/projects/libro-bianco-cantiere-smartcity-fpa-2020/builds/" target="_blank">https://readthedocs.org/projects/libro-bianco-cantiere-smartcity-fpa-2020/builds/</a>

.. |LINK102| raw:: html

    <a href="https://readthedocs.org/projects/libro-bianco-cantiere-smartcity-fpa-2020/builds/" target="_blank">https://readthedocs.org/projects/libro-bianco-cantiere-smartcity-fpa-2020/builds/</a>

.. |LINK103| raw:: html

    <a href="https://www.comune.palermo.it/unita.php?apt=4&uo=2188&serv=1056&sett=230" target="_blank">link 1</a>

.. |LINK104| raw:: html

    <a href="https://www.comune.palermo.it/" target="_blank">link 2</a>

