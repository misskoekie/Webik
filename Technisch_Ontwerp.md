# Trivia

----
## Controllers

![](https://github.com/misskoekie/Webik/blob/master/Images/activitydiagram.png)

## Routes, met functie:
## Registreer pagina. Functie hergebruiken van Finance opdracht (‘register.html’).
- Inloggegevens opslaan in een database.
- Gebruiker is direct ingelogd na registreren.
## Log in pagina. Functie hergebruiken van Finance opdracht (‘login.html’).
- Inloggegevens zoeken in database.
## Homepagina, gebruiker. Homepage voor bezoekers met inloggegevens. Eigen HTML pagina (‘homepagina_gebruiker.html’). Volgende opties zijn beschikbaar:
- Speel spel
- Scorelijst (algemeen, local, multiplayer)
- Regels
- Log uit
## Homepagina, gast. Homepage voor bezoekers zonder inloggegevens. Eigen HTML pagina (‘homepagina_gast.html’). Volgende opties zijn beschikbaar:
- Speel spel
- Scorelijst (algemeen)
- Regels
## Speelpagina, gebruiker. Het uiteindelijke spel voor bezoekers met inloggegevens. Heeft een HTML pagina nodig (‘speelpagina_gebruiker.html’).
- Local of multiplayer
- Quick play of categorieën
- Zie eigen score
- Post scores naar database
## Speelpagina, gast. Het uiteindelijke spel voor bezoekers zonder inloggegevens. Heeft een HTML pagina nodig (‘speelpagina_gast.html’).
- Quick play of categorieën
- Zie eigen score
## Scorelijst, gebruiker. Weergeven van high-scores van bezoekers met inloggegevens. Leaderboard pagina heeft een eigen HTML pagina nodig (‘scorelijst_gebruiker.html’). 
- Algemeen. Scores die ooit behaald zijn
- Local. Scores die op de lokale computer behaald zijn
- Multiplayer. Scores die vrienden op verschillende computers behaald zijn
- Scorelijst, gast. Weergeven van high-scores van bezoekers zonder (‘scorelijst_gast.html’) inloggegevens. Scorelijst pagina heeft een eigen HTML pagina nodig (GET-request).
- Algemeen. Scores die ooit behaald zijn
## Regels. Regels is dezelfde pagina voor zowel de gebruiker als gast gebruiker. (‘regels’)
## Log uit pagina. (‘loguit.html’)

----
## View

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


----
## Models/Helpers
-__**Layout**__: Algemene layout die wordt aangehouden op de gehele site. Kleine dingen zullen getweaked worden afhankelijk van de pagina. Layout van schetsen in “Views” zullen worden gebruikt als layout. 
-__**Functie: Apology**__. Deze functie treed op wanneer een gebruiker iets doet wat niet kan. Bijvoorbeeld inloggen zonder dat hij zichzelf geregistreerd heeft. 
-__**Functie: Login_required**__. Deze functie treed op wanneer een niet ingelogde gebruiker naar een pagina gaat waar hij eigenlijk ingelogd voor moet zijn. 
Het bestand met deze functies zal helpers genoemd worden. 
-__**Functie: Score**__. Deze functie berekend de behaalde score en verzend deze naar de database. Dit is een hulpfunctie omdat we 3 maal een soortgelijke functie moeten gebruiken voor het updaten van de score van algemeen, local en multiplayer.
-__**Functie: Retrieve_questions**__. Deze functie wordt aangeroepen als de vraag van een API moet worden opgehaald door middel van een GET-request. Deze functie zal per gestelde vraag aangeroepen worden. 

----
## Geavanceerde architectuur
Er is voor gekozen om niet met een geavanceerde architectuur te werken. 
Dit komt omdat de opbouw van de opdracht van Finance wat bekender is. 
Door met de opbouw van Finance te werken geeft dat een beter gevoel in plaats van een nieuwe methode die eventueel gebruikt kan worden. 

## Plugins en frameworks
__**Flask**__
- http://flask.pocoo.org 
- https://github.com/pallets/flask 
__**Jinja**__
- http://jinja.pocoo.org/docs/2.10/ 
__**Bootstrap**__
- https://getbootstrap.com 

