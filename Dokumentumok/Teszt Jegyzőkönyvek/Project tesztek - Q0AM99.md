Projekt teszt jegyzőkönyv
=========================================
Tesztelést végezte:    Kovácspál Bálint István - Q0AM99
Operációs rendszer:	     Windows 11
Böngésző:     Brave
Dátum:   2023.12.13.
Talált hibák száma:     7

# Login
+ A login felület ad visszajelzés hibás bejelentkezés után.
+ A felület nem ad visszajelzést a sikeres bejelntkezés után.
+ A felület rendeltetés szerűen működik, nincs lehetőség az oldal tartalmának elérésére bejelentkezés nélkül.
+ A bejelentkező felület nem elérhető a már bejelentkezett felhasználóknak.

# Register
+ A felület nem ad egyenes utasítást az adatokkal szemben való formai elvárásokról.
+ A felület nem ad visszajelzést a hibás adatokról, és hogy mi volt a sikertelen regisztráció oka.
+ A sikeres regisztráció után nincs visszajelzés, csak visszadob a bejelentkező felületre.
+ A Regisztráció nem elérhető a már bejelentkezett felhasználóknak.

# Főoldal
+ A felület felhasználó barát, szintén nem elérhető a bejelentkezés előtt.
+ A főoldalon a navigációs sávban elérhető az oldal összes funkciója.
+ A navigációs sáv megjelenik minden egyes oldalelemen, ezzel a főoldal felhasználó barát.

## Dokumentáció
+ A felület nincs implementálva.

## Trello kártyák
+ A navigációs sávon a "Trello kártyák"-ra kattintva, megjelenik a "Trello kártyák mozgatása" oldal.
+ Az oldal nem elérhető bejelentkezés nélkül.
+ Az oldal kilistázza az alapértelmezett Trello tábla összes listáját és kártyáit.
+ Az oldal nem ad visszajelzést, ha a kártya már ugyan abban a listában van.
+ A sikeres mozgatás után nincs visszajelzés, hanem az oldal ujratölt.
+ Az oldalon megjelenő gombok rendeltetés szerűen működnek.
+ Az oldalon megjelenő további Trello műveletek hiperhivatkozása működőképes.
+ Az oldal hiperhivatkozása megjelenik mind a "Trello kártyák létrehozása" és a "Trello lista létrehozása" felületen.

## Trello kártya létrehozása
+ Az oldal hiperhivatkozása megjelenik mind a "Trello kártyák mozgatása" és a "Trello lista létrehozása" felületen.
+ Az oldalon megjelenő szöveges input mezők adataival létrehoz egy új kártyát az alapértelmezett Trello táblában.
+ Az inputok kitöltése kötelező, ezzel elkerülve az üres kártyák létrehozását.
+ A felület felhasználó barát, szintén nem elérhető a bejelentkezés előtt.
+ A felület sikeresen létrehoz egy kártyát az alapértelmezett trello tálában.
+ sikeres létrehozás egy httpresponse-t ad vissza.

## Trello lista létrehozása
+ Lista nevének megadása kötelező.
+ Sikeres létrehozás után nem ad vissza választ, csak egy http respose-t.
+ A létrehozott lista mindig az első helyre kerül.

# Javasolt változtatások
+ GPT API implementáslása után összekötni a Trello API-val a folyékony felhsználói élményért.
+ A sikeres operációk után visszajelzés küldése a felhasználónak.
+ A HTTPResponse lecserélése MessageBox szerű megjelenésre.
+ A Regisztráció felületre több instrukció
+ A Főoldal bővítése egyébb elemekkel.
+ Egy Hibajelentés felület, hogy a felhasználók jelentést tudjanak küldeni a fejlesztőknek.
