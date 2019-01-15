# Trivia

----
## Wat is trivia?

> Trivia is een meerkeuze spel waarbij spelers antwoord moeten geven op vragen uit verschillende categorieën.

----
## Samenvatting

Het doel van de trivia is op een leuke en competitieve manier kennis bij te brengen. Onze trivia heeft als uniek element dat er muziek- en filmfragmenten worden afgespeeld waarbij de speler de bijbehorende titel moet invullen. Aangezien dit element moeilijk te vinden is bij de online databases hebben wij een back up bedacht als dit niet gerealiseerd kan worden. Bezoekers kunnen via een inlogpagina de eerder behaalde scores opslaan en later terugkijken. Op deze manier is de persoonlijke voortgang ten alle tijden in te zien. Daarnaast is het mogelijk de score te vergelijken met andere spelers waardoor de trivia erg competitief kan worden.

----
## Het spel
In trivia zijn een aantal regels, maar het gaat vooral om winnen en natuurlijk kennis verkrijgen. Om te winnen moet de speler antwoorden goed hebben en de speler met de meest goede antwoorden wint. Bij gelijk spel zal het element tijd de winnaar bekend maken. De speler die het snelst de meeste vragen goed beantwoord wint de game. Dus gelijkspel is niet helemaal mogelijk. 

De game heeft verder een simpele opbouw. De speler kan kiezen voor quickplay waarin vragen uit verschillende categorieën komen om door een speler beantwoord te worden. Daarnaast is het mogelijk voor de speler om per categorie een game te spelen. Hierdoor kan de speler goed trainen per categorie voordat het de quickplay ingaat. 

----
## Score
- De score wordt op verschillende manieren weergegeven. 
- Als spelers ingelogd en online zijn, zal de behaalde score in de wereldranglijst terecht komen. 
Wanneer een speler is ingelogd en local multiplayer speelt, zal de tussenstand ook local blijven. Hierdoor is het mogelijk voor de spelers om te kunnen zien wie de vorige keer gewonnen heeft. 
- De speler heeft de optie om trivia te spelen zonder in te loggen, de score van deze speler wordt niet opgeslagen. 

----
## Schetsen

## Schets 1: Homepagina
In de bovenstaande schets verwijzen in de nav-bar Speel, Scorelijst, Regels en Login naar de respectievelijke pagina. Ook in de onderste balk verwijst facebook naar de facebookpagina van onze trivia. Dit is elke keer zo bij elke pagina.

![](https://github.com/misskoekie/Webik/blob/master/Def_images/Schermafbeelding%202019-01-15%20om%2010.48.35.png)


## Schets 2: Login pagina
In de bovenstaande schets verwijst ‘log in’ naar de inlogpagina en ‘registreer’ verwijst naar de registratiepagina.

![](https://github.com/misskoekie/Webik/blob/master/Def_images/Schermafbeelding%202019-01-15%20om%2010.48.56.png)


## Schets 3: Registreer pagina
In de bovenstaande schets wordt er als er op ‘registreer’ wordt gedrukt geregistreerd en ingelogd en ‘Log in’ in verwijst naar de log in pagina.

![](https://github.com/misskoekie/Webik/blob/master/Def_images/Schermafbeelding%202019-01-15%20om%2010.49.06.png)


## Schets 4: Speelpagina
Hier kan er gekozen worden tussen local of online. Bij local wordt het spel gestart waarbij twee mensen op 1 computer spelen en bij online wordt het spel gestart waarbij je in je eentje speelt, en vervolgens je score in een lijst zet. Alle scores van alle spelers op elke computer worden hier laten zien.

![](https://github.com/misskoekie/Webik/blob/master/Def_images/Schermafbeelding%202019-01-15%20om%2012.32.34.png)

## Schets 5: Local game
Hier wordt er bij het klikken op een van de antwoorden naar de volgende vraag gegaan. Eerst beantwoord speler 1 een vraag en vervolgens speler 2. 

![](https://github.com/misskoekie/Webik/blob/master/Def_images/Schermafbeelding%202019-01-15%20om%2012.32.45.png)


## Schets 6: Multiplayer game
Hier speel je in je eentje en wordt je score vervolgens toegevoegd aan de scorelijst. Ook hierbij wordt er bij het klikken op een van de antwoorden naar de volgende vraag gegaan.

![](https://github.com/misskoekie/Webik/blob/master/Def_images/Schermafbeelding%202019-01-15%20om%2012.35.01.png)


## Schets 7: Scorepagina
Hier worden alle scores genoemd van hoog naar laag. Je inlognaam wordt gekoppeld aan je score

![](https://github.com/misskoekie/Webik/blob/master/Def_images/Schermafbeelding%202019-01-15%20om%2012.35.20.png)


## Features
 - Onze trivia beschikt minimaal over twee homepages (voor niet ingelogde gebruiker en ingelogde gebruiker), inlogpagina, leaderboard en de trivia pagina zelf. 
 - Er wordt gebruik gemaakt van local multiplayer. Het multiplayer element is turn-based: Op één platform zullen twee spelers achtereenvolgens vragen beantwoorden. 
  *Alternatief*: Speler maakt trivia alleen, vervolgens worden scores op de leaderboard gezet om te concurreren. De behaalde scores opgeslagen op een online leaderboard. 
 - Trivia heeft vijf categorieën: Sport, Videogames, Beroemdheden, Muziekfragmenten, Filmfragmenten. 
 - Als er gekozen wordt voor het alternatief: Eventueel een notificatie versturen: “Speler x heeft u hi-score verbroken, speel nu verder!” om het competitieve element te versterken.

## Minimum viable product (MVP)
De features die nodig zijn om het eindproduct te laten kloppen zijn:

- Er moet gebruik worden gemaakt van local multiplayer

- Er moet een mogelijkheid zijn om trivia te spelen zonder in te loggen

- Er moet een online mogelijkheid zijn voor spelers

- Er moet ingelogd kunnen worden om de scores op te slaan

- Er moeten vragen met kloppende antwoorden bestaan en na het beantwoorden hiervan moet score bijgehouden worden

- De score moet opgeteld worden aan het eind van de quiz en deze score moet worden laten zien en opgeslagen kunnen worden.

# Afhankelijkheden
De trivia site is afhankelijk van verschillende aspecten. Deze aspecten worden hieronder genoemd.


 - Databronnen: [Trivia database](https://opentdb.com/api_config.php)

   Het aanbod voor trivia vragen is ruim, alleen ons unieke element is lastig te implementeren. Er zijn geen databases met beeld- en geluidsfragmenten, waardoor wij dit zelf moeten toevoegen. Gezien onze huidige programmeerkennis kan dit een lastige opdracht worden.

 - Externe componenten:

     - Bootstrap
     - [Basis Git commando's](https://confluence.atlassian.com/bitbucketserver/basic-git-commands-776639767.html)
     - [HTML tags](https://www.w3schools.com/tags/)


 - Concurrerende bestaande websites


     - [Trivia Crack](http://www.triviacrack.com)

       Trivia Crack is een van de bekendste trivia apps op dit moment. Trivia Crack is concurrerend omdat deze verschillende categorieën heeft. De kracht van deze website is het draaiende rad. Elke ronde wordt er aan een rad gedraaid om te zien over welke categorie je een vraag moet beantwoorden. Dit maakt het spel leuk en spannend. 

     - [Sporcle](https://www.sporcle.com/) 

       Sporcle is een van de grootste trivia sites die er is. Hierdoor is het ook een concurrent. De site bevat bijna alle categorieën die er te bedenken zijn waardoor iedereen vragen heeft die diegene ligt. De site is dus aantrekkelijk voor heel hele grote groep mensen. 

     - [Triviaplaza](https://www.triviaplaza.com/) 

       Triviaplaza is een website met verschillende korte quizes van 10 vragen. De site bevat per categorie subcategorieën. Bijvoorbeeld bij de categorie muziek kan er vervolgens worden tussen jaren 70, jaren 80, pop enz. Deze website is concurrentie omdat ze meerdere dezelfde categorieën bevatten als onze website, namelijk: film, muziek en games. 


## Moeilijkste delen van de applicatie

Er zijn een paar moeilijke onderdelen die gedaan moeten worden voor onze website. Ten eerste de beeld en geluidsfragmenten. Het is niet duidelijk hoe dit geïmplementeerd kan worden. Tot nu toe is er geen dataset gevonden hiervan en het is ook niet duidelijk of dit zelf gemaakt kan worden. Ten tweede is het multiplayer component een moeilijk deel. Het is niet bekend of het idee met twee spelers op een computer toegestaan is. Als dit niet is toegestaan is het idee van de scorelijst ook ingewikkeld. Het is niet bekend hoe er op twee computers hetzelfde spel gespeeld kan worden. Bij beiden is er uitzoekwerk nodig om erachter te komen hoe dit opgelost kan worden. 
