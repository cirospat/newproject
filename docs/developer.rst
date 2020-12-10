
.. _h5e72237b1d2f21437415232c67367c3d:

developer
*********

\ |LINK1|\   una pagina dove colleziono utilità per fini di sviluppo e creatività digitale -


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

\ |LINK2|\  

--------

.. _h7a604f4c23602b76e6f6e5c11765e7:

MAPPE PALERMO
=============

* \ |LINK3|\  my google maps

* \ |LINK4|\  (pagina FB con mappe su Palermo)

* \ |LINK5|\  (mappe varie di Ciro)

* \ |LINK6|\  (contenitore di oltre 100 mappe su Palermo, su Petrusino)

* \ |LINK7|\  (sito mappe di Palermo utili a turisti)

* \ |LINK8|\  (OMIRA su Umap cirospat) 

* \ |LINK9|\  elezioni2017_Palermo da Guenter Richter

* \ |LINK10|\  e relativo bot telegram #rifiutocivico

* \ |LINK11|\  mapillary cirospat

* \ |LINK12|\  Palermo su mapillary

* \ |LINK13|\  Palermo airbnb gen_2018 (Gianni Vitrano)

--------

.. _h305075b623d460273c1b71225e4959:

MAPPE PALERMO STORICA EFFETTO LENTE INGRANDIMENTO E ALTRE MAPPE INTERESSANTI
============================================================================

* \ |LINK14|\  (GBVitrano Palermo IGM 1:25000)

* \ |LINK15|\  carta tecnica comune Palermo

* \ |LINK16|\  (GBVitrano Omira 1:5000)

* \ |LINK17|\   PRG2025 (su Petrusino)

* \ |LINK18|\  (elenco mappe 2-3D di GBVitrano su Github SiciliaHub)

* \ |LINK19|\   (Hubsicilia - Omira Irta e Sas con OSM e RealVista su Gitub SiciliaHub, con metadati mappa su barra laterale)

* \ |LINK20|\  (variante general eal PRG 2004 con cerchio)

* \ |LINK21|\  (catasto centro storico 1887 con cerchio)

* \ |LINK22|\  (PRG scehma masima su PRG 2004 con cerchio)

* \ |LINK23|\    \ |LINK24|\    (Piano protezione civile Palermo)

* \ |LINK25|\   (stile petrusino)

* \ |LINK26|\   (stile petrusino, ultimo gen 2018) - hub di diverse mappe di Palermo a cura di GBVitrano iniziato gli ultimi giorni di dic. del 2017

--------

.. _h565872655f43734d6095583123c76:

SERVIZI DI WEBMAPPING ALTERNATIVI A UMAP
========================================

\ |LINK27|\  (che preferisco) 

\ |LINK28|\  (intramontabile) 

\ |LINK29|\  (questo però è un plugin per wordpress) 

\ |LINK30|\  (a pagamento)

--------

.. _h1e2c374df4a3014336ba536e5e5e6c:

FILTRI CON "DATE" NELLE FUNZIONI DI RICERCA (QUERY) DA USARE NEI GOOGLE SPREADSHEET
===================================================================================

\ |LINK31|\ 

Usare il formato YYYY-MM-DD.

The \ |LINK32|\  function converts it to the required format for the Query formula by specifying a format of "yyyy-mm-dd":

.. code:: 

    =TEXT(DATEVALUE("1/1/2000"),"yyyy-mm-dd")


.. code:: 

    = TEXT( NOW() , "hh:mm am/pm" )
    
    The formula:    = TEXT( NOW() , "hh:mm am/pm" )    will output the time just fine!

The output of this formula is a date in the desired format:

.. code:: 

    2000-01-01

\ |STYLE0|\ 

Substitute the TODAY() function into our formula:

.. code:: 

    =QUERY(Data!$A$1:$H$136,"select C, B where B > date '"&TEXT(TODAY(),"yyyy-mm-dd")&"'",1)

\ |STYLE1|\ 

\ |LINK33|\ 

.. _h5979383b6f422d6f1a3f404a4258253f:

Query di Andrea Borruso
-----------------------


+---+------------+--------------------------------------------------+-------------------------------------------------------------------------------------+
|   |A           |B                                                 |C                                                                                    |
+---+------------+--------------------------------------------------+-------------------------------------------------------------------------------------+
|1  |\ |STYLE2|\ |\ |STYLE3|\                                       |\ |STYLE4|\                                                                          |
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

* lista di tiles per sfondi   \ |LINK34|\  

* tiles vari da usare  \ |LINK35|\  

* satellite tile ESRI - World Imagery \ |LINK36|\  

* satellite tile Google \ |LINK37|\  

* tile con sfondo satellite da mapbox/satellite-v9 con API: \ |LINK38|\   (senza nomi strade)

* \ |LINK39|\  (con nomi strade)

* SERVIZIO ONLINE CREAZIONE DI TILES DA IMMAGINI  Mapwarper \ |LINK40|\  

* \ |LINK41|\  tile: https://api.mapbox.com/styles/v1/rplln/cjix2cv5l83yz2rmne9icvusx/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoicnBsbG4iLCJhIjoiY2ppeDI5ZTByMDVtMzN1cDRxZWlzamwzcyJ9.Yn6OjT0SStL2tffNloZrdg

--------

.. _h607b3a763222151e4a1c121b50313b6c:

CODICE DA USARE PER MAPPE UMAP
==============================

video embedding = {{{\ |LINK42|\ }}}

link con testo = [[\ |LINK43|\ |testo del link]] 

immagine = {{\ |LINK44|\ |larghezza}} Immagine 

link a url con icona cliccabile = [[\ |LINK45|\ }}]]

ICONE MAPPE = \ |LINK46|\  

GOOGLEMAPS = <iframe width='100%' height='500' src="http....   "></iframe>

URL ENCODER E DECODER = \ |LINK47|\  

POST IMAGE DA LINKARE SU UMAP: \ |LINK48|\  

Icone mappe \ |LINK49|\  ccbysa

.. _h1c7b5b1f64462a201813244135465568:

GOOGLE DRIVE SPREADSHEET TO UMAP
--------------------------------

Video breve per alimentare in modo facile uMap da un foglio elettronico su Google Drive, by Andrea Borruso \ |LINK50|\ 

Tutorial per fare mappe alimentate da google spreadsheet = \ |LINK51|\  

DB x UMAP con output in csv =

.. code:: 

    https://spreadsheets.google.com/tq?tqx=out:csv&tq=SELECT%20B%2CC%2CD%2CE%2CF%2CG%2CH%20WHERE%20G%20Contains%20%27.%27&key=

| 

.. _h595e66241d682068337c187a521a3c48:

\ |LINK52|\  e \ |LINK53|\  UMAP AVVISI POLIZIA MUNICIPALE PA
-------------------------------------------------------------

\ |STYLE5|\ .


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

⇒ \ |LINK54|\  plug in come componente aggiuntivo da installare su spreadsheet di Google. Sfrutta API di Google e quindi i dati delle coordinate geografiche sono riusabili solo su mappe Google.

\ |STYLE6|\  API che usa la seguente formula: 

.. code:: 

    =JOIN(",", ImportXML(CONCATENATE("http://nominatim.openstreetmap.org/search/?format=xml&q=",A2), "//place[1]/@lat | //place[1]/@lon"))

dove A2 è la colonna dove è contenuto l'indirizzo. \ |LINK55|\ .


|REPLACE5|

* \ |LINK56|\  con Openstreetmap tramite OnData

* \ |LINK57|\   con Openstreetmap

* \ |LINK58|\  con Openstreetmap

* \ |LINK59|\  con Openstreetmap

* \ |LINK60|\  con Googlemap

* \ |LINK61|\  by GBVitrano con API Google

* \ |LINK62|\  by GBVitrano con API Google

* \ |LINK63|\  con le API di Google

    * \ |LINK64|\  con API Google

* \ |LINK65|\  (google e bing) 

* \ |LINK66|\  con API di Mapquest

* \ |LINK67|\  API Mapquest per geocoding (cirospat - caneclaudia2volte)

* \ |LINK68|\  location helper in versione demo di Mapbox

--------

.. _h59432417563a5658746a24186d4d63c:

SENSORE POLVERI SOTTILI COLLEGATO AD UNA RETE ONLINE E DATI SU MAPPA
====================================================================

* \ |LINK69|\  (tutorial) - 

* \ |LINK70|\  (mappa con grafici e dati su sensore mio)

--------

.. _h631d7b1e4d1e68301d55423b256d212:

GIT GUIDE
=========

just a simple guide for getting started with git. \ |LINK71|\ 

--------

.. _h5a573672d621f4a3b656f28542c01a:

REPOSITORY DATA CIRO SPATARO
============================

\ |LINK72|\  

\ |LINK73|\  

--------

.. _h2778167b752037aa551c4b182d05:

MACHINE LEARNING E ARTIFICIAL INTELLIGENCE
==========================================

\ |LINK74|\  un articolo per capire un po

--------

.. _h2d6b469794e1c284e67294b2f4a5b52:

RICHIESTA FOIA ONLINE
=====================

\ |LINK75|\  generatore di richieste di accesso civico generalizzato (FOIA) a cura di Giovanni Pirrotta e Giuseppe Ragusa

--------

.. _h597d5e521a157c477c7371454c784711:

CSV EDITOR
==========

* \ |LINK76|\   download

* \ |LINK77|\  editor online sulla falsa riga di Google spreadsheet

--------

.. _h4c6c275e14302f40783e423111543c68:

EDITOR ONLINE PER LAVORI CONDIVISI
==================================

* \ |LINK78|\  

* \ |LINK79|\ 

* \ |LINK80|\ 

* \ |LINK81|\  

* \ |LINK82|\  

--------

.. _h111216149473f7510705c312977184a:

QUERY PER XML (RSS FEED) E FEEDBURNER
=====================================

.xml?query=cad&newscount=25

cad= parola da cercare

newscount= il numero delle news da visualizzare come output della query

\ |LINK83|\ 

\ |STYLE7|\  

* \ |LINK84|\  il mio genratore di feed RSS

* \ |LINK85|\  - \ |LINK86|\  per costruire Feed per gli eventi Feltrinelli di Palermo

--------

.. _h231f6c11635e136146664a627213879:

Badge img shields
=================

\ |LINK87|\ 

--------

.. _h3d4153661183e671395d2c4b706f3b:

web service per creare loghi e icone 
=====================================

\ |LINK88|\  

--------

.. _h337f7b59693822377f7601745347c:

Cards
=====

\ |LINK89|\ 

--------

.. _h174c79c39577e65293f6b5738726d5c:

Unire PDF
=========

\ |LINK90|\ 

* PDFTK Builder \ |LINK91|\  

* Online2PDF \ |LINK92|\  

* \ |LINK93|\  — servizio Web gratuito e che non richiede registrazioni. Permette di unire e modificare i file PDF in vari modi. Da notare che non consente di caricare file aventi un peso superiore ai 100 MB. Eventualmente, però, è possibile aggirare questa limitazione passando a uno dei piani a pagamento (con costi a partire da 6 euro/mese), i quali consentono di sbloccare anche altre funzionalità extra.

* \ |LINK94|\  — si tratta di un altro servizio Web gratuito e che non necessita di registrazione e permette di intervenire sui documenti PDF unendoli, oltre che convertendoli, dividendoli, alleggerendoli, sbloccandoli ecc. Non applica limitazioni per quel che concerne il peso massimo dei file.

* \ |LINK95|\  — è un’altra soluzione per unire i file PDF via Web e tramite la quale è eventualmente possibile apportare varie ulteriori modifiche ai documenti caricati. È gratis, non richiede registrazione e non pone limiti per l’upload.

\ |STYLE8|\ 

\ |STYLE9|\ . Si tratta, infatti, di un’app che consente di visualizzare i file PDF e intervenire su di essi in vari modi, andandoli a convertire, unire ecc. È gratuita e facile da usare. Per effettuarne il download sul tuo dispositivo, accedi alla \ |LINK96|\ 

--------

.. _h225bd2729b5f536b2e442259197a52:

Carousel
========

https://getbootstrap.com/docs/4.0/components/carousel/

|REPLACE6|

|

.. _h3d5e7e425c116114e331b3e663c3b47:

Directives in Read the Docs
===========================


.. class:: importante

    una prova di contenuto dentro una generic ``directive``.
    Questa è la renderizzazione su pagine web a seguito del commit su Github

:download:`Questo link è per il download del logo di FPA<https://readthedocs.org/projects/libro-bianco-cantiere-smartcity-fpa-2020/builds/>`.

.. centered:: Questo è un testo centrato. Questo è un testo centrato. Questo è un testo centrato

    


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
|:Link utili: \ |LINK97|\ , \ |LINK98|\                                                                                                                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

:Author: David Goodger

:Address: 123 Example Street, Example, EX  Canada, A1B 2C3, 123 Example Street, Example, EX  Canada, A1B 2C3

:Contact: docutils-develop@lists.sourceforge.net

:Authors: Me; Myself; I

:Author: David Goodger

:Address: 123 Example Street, Example, EX  Canada, A1B 2C3

:Contact: docutils-develop@lists.sourceforge.net

:Authors: Me; Myself; I

:guilabel:`Qualche azione`  viene renderizzata così come la leggi, ma la devi scrivere così: ``:guilabel:`Qualche azione```

Assuming you have Python already, install Sphinx locally::

    $ pip install sphinx sphinx-autobuild

|

Directives can be used within aliases::

    .. |logo| image:: img/logo_comune_Palermo.png

        :width: 20pt

        :height: 20pt

Using this image alias, you can insert it easily in the text `|logo|`, like this |logo|. This is especially useful when dealing with complicated code.

--------


.. method:: io (prova)

    This method is called for each request that goes through the download middleware. This method is called for each request that goes through the download middleware.
    
       :meth:`nero` e return ``rosso``, return a :class:`prova` object,


.. classe:: io 

    This method is called for each request that goes through the download middleware. 
    
       This method is called for each request that goes through the download middleware.
    
       return ``rosso``, return a :class:`nero` object,


.. bottom of content


.. |STYLE0| replace:: **Using today’s date as a filter**

.. |STYLE1| replace:: **Vedi anche le Query**

.. |STYLE2| replace:: **data**

.. |STYLE3| replace:: **standardDate**

.. |STYLE4| replace:: **query per esporre le celle con date ancora da venire e le celle con valore "null" (celle vuote senza valori)**

.. |STYLE5| replace:: **Da un foglio Google ad una mappa uMap in cui vengono visualizzati solo gli avvisi della data odierna**

.. |STYLE6| replace:: **⇒ Nominatim Openstreetmap**

.. |STYLE7| replace:: **Generatore di Feed:**

.. |STYLE8| replace:: **Su Android**

.. |STYLE9| replace:: **PDFelement**


.. |REPLACE1| raw:: html

    <div style="width: 650px; height: 500px;" data-wordart-src="//cdn.wordart.com/json/e9h2wyb41pzf"></div>
.. |REPLACE2| raw:: html

    <div style="width: 400px; height: 400px;" data-wordart-src="//cdn.wordart.com/json/v4ejjx85ti99"></div>
.. |REPLACE3| raw:: html

    <img src="https://images.unsplash.com/photo-1529666759085-741eefcd3371?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=925&q=80" /> Art by Lønfeldt
.. |REPLACE4| raw:: html

    <p><span style="background-color: #6462d1; color: #ffffff; display: inline-block; padding: 3px 8px; border-radius: 10px;">Su fogli google spreadsheet</span></p>
.. |REPLACE5| raw:: html

    <p><span style="background-color: #105618; color: #ffffff; display: inline-block; padding: 3px 8px; border-radius: 10px;">Altri Geocoder</span></p>
.. |REPLACE6| raw:: html

    <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
      <ol class="carousel-indicators">
        <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
        <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
        <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
      </ol>
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img class="d-block w-100" src="..." alt="First slide">
        </div>
        <div class="carousel-item">
          <img class="d-block w-100" src="..." alt="Second slide">
        </div>
        <div class="carousel-item">
          <img class="d-block w-100" src="..." alt="Third slide">
        </div>
      </div>
      <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="sr-only">Previous</span>
      </a>
      <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="sr-only">Next</span>
      </a>
    </div>
    

.. |LINK1| raw:: html

    <a href="http://cirospat.readthedocs.io/it/latest/developer.html" target="_blank">cirospat.readthedocs.io/it/latest/developer.html</a>

.. |LINK2| raw:: html

    <a href="https://docs.google.com/spreadsheets/d/1auVqTh1aeJ1c2DuYUWI1UX0p8OHtupApFEjCXWsmxbA" target="_blank">https://docs.google.com/spreadsheets/d/1auVqTh1aeJ1c2DuYUWI1UX0p8OHtupApFEjCXWsmxbA</a>

.. |LINK3| raw:: html

    <a href="https://www.google.com/maps/d/u/0/?hl=it&authuser=0&action=open" target="_blank">https://www.google.com/maps/d/u/0/?hl=it&authuser=0&action=open</a>

.. |LINK4| raw:: html

    <a href="https://www.facebook.com/mappedipalermo/" target="_blank">https://www.facebook.com/mappedipalermo/</a>

.. |LINK5| raw:: html

    <a href="http://umap.openstreetmap.fr/it/user/cirospat/" target="_blank">http://umap.openstreetmap.fr/it/user/cirospat/</a>

.. |LINK6| raw:: html

    <a href="http://bit.ly/palermomaps" target="_blank">http://bit.ly/palermomaps</a>

.. |LINK7| raw:: html

    <a href="http://bit.ly/palermo_maps" target="_blank">http://bit.ly/palermo_maps</a>

.. |LINK8| raw:: html

    <a href="http://u.osmfr.org/m/136197" target="_blank">u.osmfr.org/m/136197</a>

.. |LINK9| raw:: html

    <a href="http://projects.ixmaps.com.s3-website-eu-west-1.amazonaws.com/Palermo_Elezioni/app/Palermo_Elezioni/index_2017_full.html" target="_blank">http://projects.ixmaps.com.s3-website-eu-west-1.amazonaws.com/Palermo_Elezioni/app/Palermo_Elezioni/index_2017_full.html</a>

.. |LINK10| raw:: html

    <a href="http://lrssvt.ns0.it/rifiutocivico/#11/38.1375/13.5733" target="_blank">http://lrssvt.ns0.it/rifiutocivico/#11/38.1375/13.5733</a>

.. |LINK11| raw:: html

    <a href="https://www.mapillary.com/app/user/cirospat?lat=36.82147841468249&lng=15.104561915917657&z=15.017458713501235" target="_blank">https://www.mapillary.com/app/user/cirospat?lat=36.82147841468249&lng=15.104561915917657&z=15.017458713501235</a>

.. |LINK12| raw:: html

    <a href="https://www.mapillary.com/app/?lat=38.12949822320789&lng=13.368035190329692&z=13.561628216364625&menu=false&mapStyle=mapbox_satellite" target="_blank">https://www.mapillary.com/app/?lat=38.12949822320789&lng=13.368035190329692&z=13.561628216364625</a>

.. |LINK13| raw:: html

    <a href="http://u.osmfr.org/m/198624/" target="_blank">http://u.osmfr.org/m/198624/</a>

.. |LINK14| raw:: html

    <a href="http://gbvitrano.it/qgis/pa_carto/" target="_blank">http://gbvitrano.it/qgis/pa_carto/</a>

.. |LINK15| raw:: html

    <a href="http://github.gbvitrano.it/atlante_ctc_pa/index.html" target="_blank">http://github.gbvitrano.it/atlante_ctc_pa/index.html</a>

.. |LINK16| raw:: html

    <a href="http://gbvitrano.it/qgis/carto_storica" target="_blank">http://gbvitrano.it/qgis/carto_storica</a>

.. |LINK17| raw:: html

    <a href="http://gbvitrano.it/qgis/pa_carto/prg_2015.php" target="_blank">http://gbvitrano.it/qgis/pa_carto/prg_2015.php</a>

.. |LINK18| raw:: html

    <a href="https://github.com/SiciliaHub/mappe" target="_blank">https://github.com/SiciliaHub/mappe</a>

.. |LINK19| raw:: html

    <a href="http://siciliahub.github.io/mappe/atlante_carto_pa/" target="_blank">http://siciliahub.github.io/mappe/atlante_carto_pa/</a>

.. |LINK20| raw:: html

    <a href="http://egdisegno.studiovitrano.it/variante_generale/Zonizzazione.html" target="_blank">http://egdisegno.studiovitrano.it/variante_generale/Zonizzazione.html</a>

.. |LINK21| raw:: html

    <a href="http://egdisegno.studiovitrano.it/catasto_pa_1887" target="_blank">http://egdisegno.studiovitrano.it/catasto_pa_1887</a>

.. |LINK22| raw:: html

    <a href="http://egdisegno.studiovitrano.it/variante_generale/prg_2015.html" target="_blank">http://egdisegno.studiovitrano.it/variante_generale/prg_2015.html</a>

.. |LINK23| raw:: html

    <a href="http://github.gbvitrano.it/ppc" target="_blank">http://github.gbvitrano.it/ppc</a>

.. |LINK24| raw:: html

    <a href="http://siciliahub.github.io/mappe/ppc" target="_blank">http://siciliahub.github.io/mappe/ppc</a>

.. |LINK25| raw:: html

    <a href="https://siciliahub.github.io/mappe/palermo_hub/index.html" target="_blank">https://siciliahub.github.io/mappe/palermo_hub/index.html</a>

.. |LINK26| raw:: html

    <a href="https://siciliahub.github.io/palermohub/index.html" target="_blank">https://siciliahub.github.io/palermohub/index.html</a>

.. |LINK27| raw:: html

    <a href="https://l.facebook.com/l.php?u=https%3A%2F%2Fmaphub.net%2F&h=ATNg797_CAp5QX8MdtGE2t5QmsZ4zCHG2T6FXg3PFgptOklmzkPnVWpvAhUj6J_DatUI2UTyOL0IFdbo5lPnKtZ8KmtpnHmJUjSgRaflW44uMERy5ZR_RWyvClQEIEJnV1Dmr7IS" target="_blank">https://maphub.net/</a>

.. |LINK28| raw:: html

    <a href="https://l.facebook.com/l.php?u=https%3A%2F%2Fcrowdmap.com%2F&h=ATPxCiw6g584R_YPauk3WAaUXxblQ4If-KRQxUpzp1sOELRXRgZuD4mgqqJHJvTNWGzBDJ3x-Q-iwQpKDdjq4fCC8JIjWft_F4JUE5Y23UpSLJ55YxOIi7EMHMV2g3pKAASCHOjN" target="_blank">https://crowdmap.com/</a>

.. |LINK29| raw:: html

    <a href="https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.mapsmarker.com%2F&h=ATPouIz1_8mZonVbTHhYY9OwCeTfZmXSD-9hdJOjGNRfZroByLW72KZ3niNiREDAGi3lLTWW8LG-cCr3R3d3zTQB2QUIJIU2ldiPtc7frt75xiTK56So9_K906Bi_008XjlTFI3S" target="_blank">https://www.mapsmarker.com/</a>

.. |LINK30| raw:: html

    <a href="https://l.facebook.com/l.php?u=http%3A%2F%2Fwww.maptiler.com%2Fgeoeditor%2F&h=ATOIEGdaqbjrDIB4OnZk4GRogoAV7FbenrYuwjgPw3Z10gquAPZYyeXp7DhsN6uqevc_Q_qJjKOXVqhpT2WsM7jiJgCAwZ17llK4NceigsM6vYQjuJ0ObYICn2JHQsujpveAB_3F" target="_blank">http://www.maptiler.com/geoeditor/</a>

.. |LINK31| raw:: html

    <a href="https://www.benlcollins.com/spreadsheets/query-dates/" target="_blank">https://www.benlcollins.com/spreadsheets/query-dates/</a>

.. |LINK32| raw:: html

    <a href="https://support.google.com/docs/answer/3094139?hl=en" target="_blank">TEXT()</a>

.. |LINK33| raw:: html

    <a href="https://www.benlcollins.com/spreadsheets/google-sheets-query-sql/" target="_blank">https://www.benlcollins.com/spreadsheets/google-sheets-query-sql/</a>

.. |LINK34| raw:: html

    <a href="http://geomappando.com/maps/OL3_map_tile_provider.html" target="_blank">http://geomappando.com/maps/OL3_map_tile_provider.html</a>

.. |LINK35| raw:: html

    <a href="https://leaflet-extras.github.io/leaflet-providers/preview/" target="_blank">https://leaflet-extras.github.io/leaflet-providers/preview/</a>

.. |LINK36| raw:: html

    <a href="http://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}" target="_blank">http://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}</a>

.. |LINK37| raw:: html

    <a href="https://mt1.google.com/vt/lyrs=s&x=%7Bx%7D&y=%7By%7D&z=%7Bz%7D" target="_blank">https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}</a>

.. |LINK38| raw:: html

    <a href="http://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx" target="_blank">http://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx</a>

.. |LINK39| raw:: html

    <a href="https://api.mapbox.com/styles/v1/mapbox/satellite-streets-v9/tiles/{z}/{x}/{y}?access_token=pk.eyJ1Ijoibm9yZGFpIiwiYSI6ImtCWWpvY00ifQ.E9g3YhLqDFGkdXx7pKnCWw" target="_blank">https://api.mapbox.com/styles/v1/mapbox/satellite-streets-v9/tiles/{z}/{x}/{y}?access_token=pk.eyJ1Ijoibm9yZGFpIiwiYSI6ImtCWWpvY00ifQ.E9g3YhLqDFGkdXx7pKnCWw</a>

.. |LINK40| raw:: html

    <a href="http://mapwarper.net/" target="_blank">http://mapwarper.net/</a>

.. |LINK41| raw:: html

    <a href="http://umap.openstreetmap.fr/it/map/lete-numerique-de-louis-chadourne_228928#6/41.714/9.426" target="_blank">mappa antica del mondo</a>

.. |LINK42| raw:: html

    <a href="https://www.youtube.com/embed/_______|250" target="_blank">https://www.youtube.com/embed/_______|250</a>

.. |LINK43| raw:: html

    <a href="http://example.com/" target="_blank">http://example.com</a>

.. |LINK44| raw:: html

    <a href="http://immagine.url.it/" target="_blank">http://immagine.url.it</a>

.. |LINK45| raw:: html

    <a href="http://opendatasicilia.it|{{http://hexb.in/hexagons/opendatasicilia.png|90" target="_blank">http://opendatasicilia.it|{{http://hexb.in/hexagons/opendatasicilia.png|90</a>

.. |LINK46| raw:: html

    <a href="http://www.cityplanner.it/supply/icon_web/mapbox-maki-51d4f10/src/" target="_blank">http://www.cityplanner.it/supply/icon_web/mapbox-maki-51d4f10/src/</a>

.. |LINK47| raw:: html

    <a href="http://meyerweb.com/eric/tools/dencoder/" target="_blank">http://meyerweb.com/eric/tools/dencoder/</a>

.. |LINK48| raw:: html

    <a href="http://postimages.org/" target="_blank">http://postimages.org/</a>

.. |LINK49| raw:: html

    <a href="https://mapicons.mapsmarker.com" target="_blank">https://mapicons.mapsmarker.com</a>

.. |LINK50| raw:: html

    <a href="https://www.youtube.com/watch?v=YKZc84WtTd4" target="_blank">https://www.youtube.com/watch?v=YKZc84WtTd4</a>

.. |LINK51| raw:: html

    <a href="https://docs.google.com/document/d/1NARnTh4orNbIHEe8uROLYbWoc40nS3cGBpZqxBYFe5I" target="_blank">https://docs.google.com/document/d/1NARnTh4orNbIHEe8uROLYbWoc40nS3cGBpZqxBYFe5I</a>

.. |LINK52| raw:: html

    <a href="https://docs.google.com/spreadsheets/d/1laR9p_Ua0BPCJee5BbHvV7S-tjbmHxhLksUdKnZEW0M/edit#gid=0" target="_blank">DATASET XML</a>

.. |LINK53| raw:: html

    <a href="http://umap.openstreetmap.fr/it/map/avvisi-polizia-municipale-sulla-mobilita-di-palerm_135416" target="_blank">MAPPA</a>

.. |LINK54| raw:: html

    <a href="https://chrome.google.com/webstore/detail/geocode-by-awesome-table/cnhboknahecjdnlkjnlodacdjelippfg" target="_blank">Awesome Table</a>

.. |LINK55| raw:: html

    <a href="https://docs.google.com/spreadsheets/d/1y01HJEl5RQeSKbzA9TRyNdmHCaac7kNRjYgj3nH7oHo/edit#gid=652519043" target="_blank">Un esempio è qui</a>

.. |LINK56| raw:: html

    <a href="http://geocoder.ondata.it/" target="_blank">http://geocoder.ondata.it/</a>

.. |LINK57| raw:: html

    <a href="http://dati.comune.galatone.le.it/geocoder/" target="_blank">http://dati.comune.galatone.le.it/geocoder/</a>

.. |LINK58| raw:: html

    <a href="http://school.dataninja.it/tools/geocoder-trova-le-coordinate/" target="_blank">http://school.dataninja.it/tools/geocoder-trova-le-coordinate/</a>

.. |LINK59| raw:: html

    <a href="http://www.apposta.biz/prove/geocoder.php" target="_blank">http://www.apposta.biz/prove/geocoder.php</a>

.. |LINK60| raw:: html

    <a href="http://it.mygeoposition.com/" target="_blank">http://it.mygeoposition.com/</a>

.. |LINK61| raw:: html

    <a href="https://coseerobe.gbvitrano.it/geocodifica-il-tuo-indirizzo-utility.html" target="_blank">https://coseerobe.gbvitrano.it/geocodifica-il-tuo-indirizzo-utility.html</a>

.. |LINK62| raw:: html

    <a href="https://siciliahub.github.io/mappe/geolocation/geolocation.html" target="_blank">https://siciliahub.github.io/mappe/geolocation/geolocation.html</a>

.. |LINK63| raw:: html

    <a href="https://developers.google.com/maps/documentation/geocoding/start" target="_blank">https://developers.google.com/maps/documentation/geocoding/start</a>

.. |LINK64| raw:: html

    <a href="https://docs.google.com/spreadsheets/d/1_MH8u1JESQ_Qls5YBcZvlCLKvMmAsiV46b-w3kZQL8Y/edit#gid=0" target="_blank">Foglio mio prova geocode</a>

.. |LINK65| raw:: html

    <a href="http://www.gpsvisualizer.com/geocode" target="_blank">http://www.gpsvisualizer.com/geocode</a>

.. |LINK66| raw:: html

    <a href="http://www.gpsvisualizer.com/geocoder/" target="_blank">http://www.gpsvisualizer.com/geocoder/</a>

.. |LINK67| raw:: html

    <a href="https://developer.mapquest.com/user/me/apps" target="_blank">https://developer.mapquest.com/user/me/apps</a>

.. |LINK68| raw:: html

    <a href="https://demos.mapbox.com/location-helper/" target="_blank">https://demos.mapbox.com/location-helper/</a>

.. |LINK69| raw:: html

    <a href="http://bit.ly/tutorialkitpolverisottili" target="_blank">http://bit.ly/tutorialkitpolverisottili</a>

.. |LINK70| raw:: html

    <a href="http://bit.ly/pm10pa" target="_blank">http://bit.ly/pm10pa</a>

.. |LINK71| raw:: html

    <a href="http://rogerdudler.github.io/git-guide/" target="_blank">http://rogerdudler.github.io/git-guide</a>

.. |LINK72| raw:: html

    <a href="https://data.world/cirospat/" target="_blank">data.world/cirospat</a>

.. |LINK73| raw:: html

    <a href="https://archive.org/details/@ciro_spataro" target="_blank">archive.org/details/@ciro_spataro</a>

.. |LINK74| raw:: html

    <a href="https://google.qwiklabs.com/quests/32" target="_blank">https://google.qwiklabs.com/quests/32</a>

.. |LINK75| raw:: html

    <a href="http://www.foiapop.it/" target="_blank">www.foiapop.it</a>

.. |LINK76| raw:: html

    <a href="http://comma-chameleon.io/" target="_blank">http://comma-chameleon.io/</a>

.. |LINK77| raw:: html

    <a href="https://ethercalc.org/" target="_blank">https://ethercalc.org/</a>

.. |LINK78| raw:: html

    <a href="https://htmlg.com/html-editor/" target="_blank">https://htmlg.com/html-editor/</a>

.. |LINK79| raw:: html

    <a href="https://www.editpad.org/" target="_blank">https://www.editpad.org/</a>

.. |LINK80| raw:: html

    <a href="https://html-online.com/editor/" target="_blank">https://html-online.com/editor/</a>

.. |LINK81| raw:: html

    <a href="http://collabedit.com" target="_blank">http://collabedit.com</a>

.. |LINK82| raw:: html

    <a href="https://hackmd.io/AwEwHALAbBCGBmBaAnDAzIiBWZwUFMBjCRIgdjPlmpACZDkg?both" target="_blank">https://hackmd.io/AwEwHALAbBCGBmBaAnDAzIiBWZwUFMBjCRIgdjPlmpACZDkg?both</a>

.. |LINK83| raw:: html

    <a href="http://www.ilquotidianodellapa.it/_aree/feed_advanced.html" target="_blank">http://www.ilquotidianodellapa.it/_aree/feed_advanced.html</a>

.. |LINK84| raw:: html

    <a href="https://feedburner.google.com/fb/a/myfeeds" target="_blank">https://feedburner.google.com/fb/a/myfeeds</a>

.. |LINK85| raw:: html

    <a href="https://feed43.com/" target="_blank">Feed43</a>

.. |LINK86| raw:: html

    <a href="https://groups.google.com/forum/#!topic/opendatasicilia/mj4rOt3VUNg" target="_blank">vedi tutorial di Andrea Borruso</a>

.. |LINK87| raw:: html

    <a href="https://img.shields.io/badge/fondamentali-amministrazione_digitale-red?style=popout&logo=Read%20the%20Docs" target="_blank">https://img.shields.io/badge/fondamentali-amministrazione_digitale-red?style=popout&logo=Read%20the%20Docs</a>

.. |LINK88| raw:: html

    <a href="https://www.canva.com/" target="_blank">https://www.canva.com/</a>

.. |LINK89| raw:: html

    <a href="https://getbootstrap.com/docs/4.0/components/card/#border" target="_blank">https://getbootstrap.com/docs/4.0/components/card/#border</a>

.. |LINK90| raw:: html

    <a href="https://www.aranzulla.it/come-unire-due-pdf-923476.html" target="_blank">https://www.aranzulla.it/come-unire-due-pdf-923476.html</a>

.. |LINK91| raw:: html

    <a href="http://angusj.com/pdftkb/#pdftkbuilder" target="_blank">http://angusj.com/pdftkb/#pdftkbuilder</a>

.. |LINK92| raw:: html

    <a href="http://online2pdf.com/" target="_blank">http://online2pdf.com/</a>

.. |LINK93| raw:: html

    <a href="https://www.ilovepdf.com/it/unire_pdf" target="_blank">iLovePDF</a>

.. |LINK94| raw:: html

    <a href="https://pdfcandy.com/it/merge-pdf.html" target="_blank">PDF Candy</a>

.. |LINK95| raw:: html

    <a href="https://tools.pdf24.org/it/unire-pdf" target="_blank">PDF24</a>

.. |LINK96| raw:: html

    <a href="https://play.google.com/store/apps/details?id=com.wondershare.pdfelement&hl=it" target="_blank">relativa sezione del Play Store</a>

.. |LINK97| raw:: html

    <a href="https://www.comune.palermo.it/unita.php?apt=4&uo=2188&serv=1056&sett=230" target="_blank">link 1</a>

.. |LINK98| raw:: html

    <a href="https://www.comune.palermo.it/" target="_blank">link 2</a>

