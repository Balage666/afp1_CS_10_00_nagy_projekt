Projekt teszt jegyzőkönyv
=========================================
Tesztelést végezte:    Tóth Dorina Ildikó (FYA26Y) 
Operációs rendszer:	     WIN11
Böngésző:     Firefox verzió: 120.0.1 (64 bites)
Dátum:   2023.12.12.
Talált hibák száma:     12

# Bejelentkezés felület

## Funkcionális tesztek

### Felhasználói adatok ellenőrzése

+ **Helyes belépési adatok esetén:** A rendszerben szereplő megfelelő felhasználónév és jelszó kombináció megadásakor a rendszer nem dob fel párbeszédablakot vagy hibaüzenetet, hanem egyből átirányítja a felhasználót a főoldalra vagy a megfelelő céloldalra.
+ **Különböző jogosultságú felhasználók esetén:** Különböző jogosultságokkal rendelkező felhasználóknál a rendszer nem tájékoztat különbségekről vagy eltérésekről, hanem egységes reakciót ad.
+ **Hibás belépési adatok esetén:** Amennyiben a rendszerben nem szereplő felhasználónév és jelszó kombinációt ad meg a látogató, a rendszer megfelelő módon jelez, általában párbeszédablakot használva, amelyben kiírja, hogy 'Hibás felhasználónév vagy jelszó!'. Ezután nem engedi tovább a látogatót.
+ **Üres mezők esetén:** Amennyiben az egyik vagy mindkét beviteli mező üres, és a felhasználó kattint a 'Bejelentkezés' gombra, a rendszer nem dob hibát, de a figyelmet a felhasználónév mezőbe irányítja.
+ **Kihagyott jelszó mező esetén:** Ha a felhasználó kitölti a felhasználónév mezőt, de nem ad meg jelszót, a rendszer a kurzort automatikusan a jelszó mezőbe irányítja és megjeleníti a felhasználónak az üzenetet: 'Töltse ki ezt a mezőt.'
+ **Helyes jelszó, de helytelen felhasználónév esetén:** Ha a látogató helyes jelszót ad meg, de a felhasználónév rossz, a rendszer nem enged tovább a bejelentkezési folyamatban.
+ **A kurzort üres mező fölé mozgatva:** A mező fölé helyezve a kurzort jelzi, hogy 'Töltse ki ezt a mezőt.'.
+ **Navigáció a bejelentkező felületre:** A linkre kattintás átnavigál a regisztrációs felületre.

### Hibás bejelentkezés kezelése

+ **Sikertelen bejelentkezési kísérletek értesítése:** A rendszer nem értesít a felhasználót arról, ha túl sokszor próbálkozik valaki rossz jelszót megadni egy adott fiókhoz. Ez azt jelenti, hogy nincs specifikus figyelmeztetés vagy zárolás azoknál a felhasználóknál, akik sok sikertelen próbálkozást végeznek.
+ **Oldal újratöltése sikertelen bejelentkezés esetén:** Minden egyes rossz bejelentkezési próbálkozás után a rendszer újratölti az oldalt. Ez a működés azt jelenti, hogy a rendszer nem tárolja el az egyes sikertelen próbálkozások számát, ami lehetővé teszi a felhasználóknak többszörös próbálkozást anélkül, hogy bármilyen korlátozásba ütköznének.
+ **Böngészősáv korlátozása bejelentkezés nélkül:** Ha a felhasználó nincs bejelentkezve, a rendszer nem engedi hozzáférni a böngészősávban írt más oldalakhoz, ehelyett a rendszer hozzáférési próbálkozásokat módosítja. Például, beilleszti a '?bejelentkezes_szukseges=/index/' parancsot az oldal eléréséhez, ami azt jelzi, hogy be kell jelentkeznie az oldal további használatához.

### Újraterelés funkció

+ **Helyes adatok megadása esetén történő újraterelés:** Amikor a felhasználó helyes belépési adatokat (felhasználónév és jelszó) ad meg a bejelentkezési oldalon, a rendszer azonnal átirányítja a felhasználót a Főoldalra. Ezen kívül más oldalakhoz való hozzáférést nem engedélyez, és a felhasználó nem érheti el a rendszer egyéb funkcióit vagy oldalait. Az újraterelés kizárólag a Főoldal elérésére szolgál.

## Biztonsági tesztek

### SQL Injection ellenőrzése

+ **Tesztadatok bemutatása:** A táblázat tartalmaz olyan felhasználónév és jelszó kombinációkat, amelyek tipikusan felhasználhatóak SQL Injection támadás során.

Felhasználónév | Jelszó | Eredmény |
---|---|---|
105 OR 1=1 | 105 OR 1=1 | 'Hibás felhasználónév vagy jelszó!'
105 OR 1=1 | password | 'Hibás felhasználónév vagy jelszó!'
" or ""=" | " or ""=" | 'Hibás felhasználónév vagy jelszó!'
105; DROP TABLE Suppliers | password | 'Hibás felhasználónév vagy jelszó!'
' or 1 # | password | 'Hibás felhasználónév vagy jelszó!'
" or 1 # | password | 'Hibás felhasználónév vagy jelszó!'

+ **Az adatok hatása a rendszerre:** Az itt feltüntetett felhasználónév és jelszó kombinációk olyan adatokat tartalmaznak, amelyeket gyakran használnak SQL Injection támadásokban. Azonban a rendszer helyesen kezeli ezeket az adatokat, nem engedi a belépést ezekkel az adatokkal.

+ **Tesztelt SQL Injection kifejezések:** A következőkben szereplő példák (pl. 105 OR 1=1, 105; DROP TABLE Suppliers, stb.) olyan tipikus SQL Injection kifejezések, melyekkel a támadók általában próbálkoznak a rendszerbe való illetéktelen behatolásra. Az ilyen típusú adatok kezelését a rendszer megfelelően kivédi, és nem engedi a belépést ezekkel az adatokkal.

Ezen tesztesetek célja annak biztosítása, hogy a rendszer megfelelően reagáljon az SQL Injection támadásokra jellemző adatokra, és megakadályozza az ilyen típusú behatolási kísérleteket. Fontos, hogy a rendszer megfelelő védelmi mechanizmusokkal rendelkezzen, amelyek megakadályozzák az ilyen támadások sikeres végrehajtását.

### Cross-Site Scripting (XSS) ellenőrzése

+ **Tesztadatok bemutatása:** Az itt felsorolt HTML/JavaScript kódok példái azoknak a típusú kódoknak, melyek általában Cross-Site Scripting (XSS) támadásokhoz használhatóak fel.

``` ‘;alert(String.fromCharCode(88,83,83))//’;alert(String.fromCharCode(88,83,83))//”; ```
``` alert(String.fromCharCode(88,83,83))//”;alert(String.fromCharCode(88,83,83))//– ```
``` ></SCRIPT>”>’><SCRIPT>alert(String.fromCharCode(88,83,83))</SCRIPT> ```

+ **Az adatok hatása a rendszerre:** Ezeket a speciális karaktereket és kódokat szokták kipróbálni a támadók, hogy beilleszthessenek kártékony kódot egy weboldalba vagy alkalmazásba azáltal, hogy kihasználják a felhasználói bemeneti mezőket. Azonban a rendszer helyesen kezeli ezeket az adatokat, nem engedi tovább a felhasználót, és egy 'Hibás felhasználónév vagy jelszó!' üzenettel tájékoztatja.

+ **Tesztelt XSS kódok:** Az itt bemutatott XSS kódok olyan példák, amelyeket általában az XSS támadásokban használnak. Ezek a kódok lehetnek HTML/JavaScript részletek, melyek célja, hogy kártékonyan befolyásolják a weboldal vagy alkalmazás viselkedését, adatokat lopjanak vagy a felhasználókat megtévesztve bizalmas információkhoz jussanak hozzá.

Ezen tesztesetek célja annak biztosítása, hogy a rendszer megfelelően reagáljon és megakadályozza az XSS támadásokat, valamint a felhasználói bemenetek biztonságos kezelését. Fontos, hogy az ilyen típusú támadások ellen hatékony védelmi mechanizmusok legyenek beépítve a rendszerbe annak érdekében, hogy megakadályozzák az ilyen típusú támadások sikerességét.

## Kompatibilitási tesztek

### Mobil eszközök ellenőrzése

+ **Kisebb képernyőn való megjelenés:** Az oldal megfelelően jelenik meg kisebb képernyővel rendelkező eszközökön, mint mobiltelefonok vagy tabletek. A felület responszív és jól skálázódik úgy, hogy egyik része sem legyen elfedve vagy láthatatlan a kisebb kijelzőkhöz képest.
+ A hibaüzenet rossz adatok megadása esetén hibásan jelenik meg.

## Felhasználói élmény (UX) tesztek

### Felhasználói barát bejelentkezési folyamat

+ **Könnyen követhető bejelentkezési folyamat:** A bejelentkezési folyamat lépései és a felhasználó által elvégzendő teendők egyértelműen és könnyen követhetőek. A felhasználó számára világosak és érthetőek az instrukciók, amelyeket követnie kell a sikeres bejelentkezéshez.
+ A felhasználónév kihagyásakor nem tájékoztat megfelelően annak hiányáról.
+ **Jelszómező kiemelése üresen hagyás esetén:** Amikor a felhasználó megfeledkezik a jelszó megadásáról, a rendszer világosan jelzi számára, hogy a jelszó mezőt kötelező kitölteni a bejelentkezéshez. Ez általában egy egyértelmű üzenet formájában történik 'Töltse ki a mezőt.'.

### Hibaüzenetek megfelelő megjelenése 

+ **Világos és segítőkész hibaüzenetek:** Amikor a felhasználó hibás adatokat ad meg a bejelentkezési folyamat során, a rendszer által megjelenített hibaüzenetek világosak és érthetőek. Az üzenetek segítséget nyújtanak a felhasználónak az adatok hibás volta tekintetében, hogy megértsék és helyesbítsék azokat.
+ **Egységes hibaüzenetek kezelése:** Csak egyféle hibaüzenet jelenik meg, függetlenül attól, hogy a felhasználónév vagy a jelszó hibás-e. Azaz, a rendszer egységes üzenetet jelenít meg minden helytelen adatmegadás esetén, nem tesz különbséget a felhasználónév és a jelszó hibája között.
+ **Együtt kezelt felhasználónév és jelszó hibák:** A felhasználónév és a jelszó esetleges hibás megadásakor ugyanazt az üzenetet jeleníti meg a rendszer. Tehát, bármelyik mező esetén is történik hiba, a felhasználó ugyanazt a segítőkész és egységes hibaüzenetet kapja meg, ami lehetővé teszi számára a helyes adatok beírását.

## Teljesítménytesztek

### Betöltési idők ellenőrzése

Kérés | Átküldve | Befejezés | DOMContentLoaded | Load |
---|---|---|---|---|
6 | 6,57 kB / 5,02 kB | 1,14 mp | 156 ms | 605 ms
7 | 10,86 kB / 9,62 kB | 868 ms | 236 ms | 294 ms
6 | 6,57 kB / 5,02 kB | 1 mp | 224 ms | 255 ms
6 | 6,57 kB / 5,02 kB | 1,02 mp | 163 ms | 288 ms
6 | 6,57 kB / 5,02 kB | 574 ms | 125 ms | 681 ms

+ **Átlagos kérések és visszatérések száma:** Az átlagos kérések száma betöltéskor 6. Ezek közül 4 kérés sikeresen tér vissza, 1 hibás, és 1 esetben hiányzik a válasz.
+ **Hiányzó lap azonosítása:** A betöltés során a hiányzó lap azonosítása történt, ami a stíluslap hiányát jelenti. Ezt a lapot a rendszer nem éri el, amikor a weboldal betöltődik.
+ **Kéréses átirányítás esete:** Amikor a / oldalról a /login oldalra kell átnavigálni a betöltéskor, ez a folyamat 7 kérést eredményez.

## További javasolt tesztek
+ **Jelszópolitika vizsgálata**: Ellenőrizni a jelszókomplexitást és a megfelelő jelszó hosszúságot. Meg kell győződni arról, hogy a rendszer megfelelően reagál-e a megfelelő és nem megfelelő jelszókra, valamint megköveteli-e a jelszó erősségének megfelelő szintű biztonságot.
+ További vizsgálatra szorul a rendszer stabilitása nagy terhelés vagy váratlan forgalmi csúcsok esetén. Tesztelésre szorul, hogy a rendszer képes-e megfelelően kezelni a nagy terhelést, és nem vezet-e összeomláshoz vagy lassuláshoz.

## Javaslatok a fejlesztése
+ **Tiltott hozzáférés kezelése**: Ha túl sok sikertelen bejelentkezési kísérlet történik egy adott fiókhoz, a rendszer ne csak az oldal újratöltésével reagáljon, hanem zárolja le ideiglenesen a fiókot biztonsági okokból.
+ Vizsgálata annak, hogyan kezeli a rendszer a munkameneteket (session), ellenőrizni, hogy ne maradjon aktív munkamenet semmilyen inaktív időszak után.
+ Továbbfejlesztésre szorul a hibaüzenetek differenciált kezelése. Különbséget kell tenni a felhasználónév és jelszó hibás megadása között, hogy segítsen a felhasználóknak a pontos hiba azonosításában.

# Regisztrációs felület

## Funkcionális tesztek

### Felhasználói adatok ellenőrzése

+ **Üres mezők ellenőrzése:**
    + Ha a gombra kattintva üres mezők vannak, a kurzort a felhasználónév mezőre irányítja, de nem ad külön értesítést a hiányzó mezőkről.
    + A kurzor pozícióját nem igazítja az adatok megfelelő kitöltöttségéhez. Például, ha az email mező hiányzik, a kurzor visszavezet a felhasználónév mezőre, és nem jeleníti meg a 'Töltse ki ezt a mezőt.' üzenetet.
    + **Felhasználónév mező kitöltve:** A kurzor átirányítása a Keresztnév mezőbe történik, és kiírja, hogy 'Töltse ki ezt a mezőt.'.
    + **Felhasználónév és Keresztnév mezők kitöltve:** A kurzor a Vezetéknév mezőbe irányítódik, és megjeleníti a 'Töltse ki ezt a mezőt.' üzenetet.
    + **Felhasználónév, Keresztnév és Vezetéknév mezők kitöltve:** A kurzor az Email-cím mezőbe kerül, és megjelenik a 'Töltse ki ezt a mezőt.' szöveg.
    + **Felhasználónév, Keresztnév, Vezetéknév és Email-cím mezők kitöltve:** A kurzor a Jelszó mezőbe helyezkedik, és kiírja, hogy 'Töltse ki ezt a mezőt.'.
    + **Felhasználónév, Keresztnév, Vezetéknév, Email-cím és Jelszó mezők kitöltve:** A kurzor a Jelszó újra mezőbe irányítódik és megjelenik a 'Töltse ki ezt a mezőt.' üzenet.
    + **Kitöltött mezők esetén:** A kurzor lépésről lépésre követi a kitöltött mezőket, de mindig a következő szabad mezőbe irányít, és megjeleníti a 'Töltse ki ezt a mezőt.' üzenetet, ha szükséges.
+ **Input validáció és hibaüzenetek:**
    + Validáció hiányában nem jelez azonnali hibákat, ha valamelyik feltétel nem teljesül.
    + Az email input validálása helyes és működik.
    + Hibás adatok megadása után a jelszómezőket törli.
    + Rosszul megadott jelszavak esetén nem ad konkrét hibaüzenetet, csak törli azokat és visszatér a felhasználónév mezőhöz.
    + Ha már a rendszerben létező felhasználónevet ad meg, nem jelzi külön a hibát, csak törli a jelszó mezők tartalmát és a kurzort a felhasználónév mezőbe irányítja.
    + A rendszer hiányos vagy hibás adatok esetén nem jelenít meg azonnali hibajelzést, csak a validációs hiányosságok után kezdi el üríteni a jelszómezőket.
+ **Sikeres adatmegadás esetén:** Sikeres adatmegadás esetén nincs specifikus üzenet, csak átirányítás a bejelentkezési oldalra.
+ **A kurzort üres mező fölé mozgatva:** A mező fölé helyezve a kurzort, a rendszer azonnal jelzi, hogy 'Töltse ki ezt a mezőt.'.
+ **Navigáció a bejelentkező felületre:** A linkre kattintás nem engedi azonnal belépni a rendszerbe, hanem átnavigál a bejelentkező felületre.

### Hibás bejelentkezés kezelése

+ **Sikertelen regisztrációs kísérletek értesítése:** A hiányzó figyelmeztetések és a zárolás nélküli rendszer lehetővé teszi, hogy a támadók végtelen próbálkozást végezzenek anélkül, hogy korlátozásba ütköznének. Ennek következtében nincs automatikus értesítés vagy tevékenységi korlátozás azon felhasználók számára, akik ismételt sikertelen próbálkozásokat hajtanak végre. Ennek következtében a rendszer sebezhető lehet a bruteforce-támadásokkal szemben, mivel nincsenek korlátozások az ismételt próbálkozásokra.
+ **Oldal újratöltése sikertelen regisztráció esetén:** A hiányzó oldal újratöltési mechanizmus csökkenti a biztonságot, mivel a rendszer nem frissíti az oldalt, hanem csak az éppen kitöltött jelszómezőket üríti ki. Ennek eredményeképpen a rendszer nem nyomon követi és nem tárolja az egyes sikertelen bejelentkezési kísérleteket vagy regisztrációkat, ami egy hatékonyabb biztonsági protokoll hiányában növeli a rendszer sebezhetőségét.
+ **Böngészősáv korlátozása bejelentkezés nélkül:** Ha a felhasználó nincs bejelentkezve, a rendszer nem engedi hozzáférni a böngészősávban írt más oldalakhoz, ehelyett a rendszer hozzáférési próbálkozásokat módosítja. Például, beilleszti a '?bejelentkezes_szukseges=/index/' parancsot az oldal eléréséhez, ami azt jelzi, hogy be kell jelentkeznie az oldal további használatához. Ezen kívül átnavigál a bejelentkezés oldalra.

### Újraterelés funkció

+ **Helyes adatok megadása esetén történő újraterelés:** Amikor a felhasználó a regisztrációs folyamat során helyes adatokat ad meg, a rendszer azonnal továbbítja őt a Bejelentkezési felületre. Ez a művelet azonban korlátozza a felhasználó hozzáférését más oldalakhoz vagy a rendszer egyéb funkcióihoz. Az újraterelés kizárólag a Bejelentkező oldal elérésére szolgál. Ez azt jelenti, hogy a sikeres regisztrációt követően a felhasználót a Bejelentkezési felületre irányítja a rendszer, és nem engedi meg a hozzáférést más oldalakhoz vagy funkciókhoz. Ezzel a korlátozással megakadályozza, hogy a felhasználó azonnal más területekre navigáljon vagy funkciókat használjon a regisztráció után. Ezzel biztosítva a felhasználók számára, hogy a rendszerbe csak a megfelelő jogosultságokkal és a regisztráció utáni lépéseket követve léphessenek be.

## Kompatibilitási tesztek

### Mobil eszközök ellenőrzése

+ **Kisebb képernyőn való megjelenés:** Jelenleg az oldal nem teljesíti megfelelően a mobilbarát elvárásokat. Bár az oldal responszív, azaz alkalmazkodik az eszköz képernyőméretéhez, az elemek elrendeződése nem megfelelő. Ez azt jelenti, hogy bár az űrlap és a felület mérete alkalmazkodik az ablak méretéhez, az elrendezés nem megfelelő. Bizonyos részek vagy funkciók hiányosan jelennek meg, és az űrlap kicsiny méretben jelenik meg a kisebb képernyőn. 

## Felhasználói élmény (UX) tesztek

### Felhasználói barát regisztrációs folyamat

+ **Nem könnyen követhető regisztrációs folyamat:** Fontos, hogy az új felhasználók számára könnyen követhető és érthető legyen a regisztráció lépéseinek folyamata. Jelenleg azonban a regisztrációs folyamat nem megfelelően strukturált és nem biztosít kellő világosságot és eligazítást a felhasználók számára. Az instrukciók vagy a teendők nem kerültek pontosításra vagy részletezésre a felhasználók számára. Ez azt eredményezi, hogy a felhasználók számára nem egyértelmű, hogy mely lépéseket kell követniük, vagy ha hibásan adják meg az adatokat, nem kapnak egyértelmű visszajelzést arról, hogy mely mezők tartalmaznak hibát. A hibás adatok jelzése hiányzik vagy csak részben jelenik meg a folyamatban, például az email mező esetében, de más esetekben nem kap visszajelzést a felhasználó arról, hogy mely adatokat adta meg rosszul vagy hibásan. Ez a hiányosságokat magában hordozza, és negatívan befolyásolhatja a felhasználói élményt, mivel a regisztrációs folyamat nem egyértelmű és felhasználóbarát. A pontos és érthető instrukciók, valamint a hibás adatok világos visszajelzése a regisztrációs folyamat során elengedhetetlenek a sikeres és zökkenőmentes felhasználói élmény érdekében.

### Hibaüzenetek nem megfelelő megjelenése 

+ **Nincsenek világos és segítőkész hibaüzenetek:** Amikor a felhasználó hibás adatokat ad meg a bejelentkezési folyamat során, a rendszer által megjelenített hibaüzenetek hiányosak. Az üzenetek sok esetben nem nyújtanak segítséget a felhasználónak az adatok hibás volta tekintetében, hogy megértsék és helyesbítsék azokat. A hiányosságok közé tartozik, hogy a hibaüzenetek nem világosak és nem segítik a felhasználót abban, hogy pontosan értsék meg, mely adatok hibásak vagy hiányosak. Az üzenetek tartalma általában általános és nem különíti el, melyik mező hibás. Például, ha az email mező rosszul van kitöltve, az üzenetben található információ nem pontosítja vagy nem jelez egyértelműen erre rámutatva.
+ **Egységes hibaüzenetek kezelése:** Csak egyféle hibaüzenet jelenik meg, függetlenül attól, hogy melyik adat hibás. Azaz, a rendszer egységes üzenetet jelenít meg minden helytelen adatmegadás esetén, nem tesz különbséget csak az email mező hibás kitöltésekor. Ezen kívül az is problémát okoz, hogy csak egyféle hibaüzenet jelenik meg minden helytelen adatmegadás esetén. Például, ha a felhasználó hibásan tölti ki a felhasználónevet vagy a jelszót, a rendszer ugyanazt az üzenetet jeleníti meg mindkét esetben, amely nem segít a felhasználónak azonosítani és helyesbíteni a konkrét hibát.
+ **Együtt kezelt adat hibák:** Minden mező hibás megadásakor ugyanazt az üzenetet jeleníti meg a rendszer, viszont jelzi melyik mező üres. Ezen hibaüzenetek egységesítése nem különbözteti meg az egyes adatok helytelenségét vagy hiányát. Fontos lenne, hogy a rendszer pontosan jelezze, melyik mező tartalmazza a hibás vagy hiányzó adatot, hogy a felhasználó könnyen azonosíthassa és javíthassa azt. Ezáltal növelhető lenne a felhasználói élmény és a hatékonyabb hibaelhárítás lehetősége.

## Teljesítménytesztek

### Betöltési idők ellenőrzése

Kérés | Átküldve | Befejezés | DOMContentLoaded | Load |
---|---|---|---|---|
2 | 7,00 kB / 5,16 kB | 149 ms | 67 ms | 77 ms
2 | 7,00 kB / 5,16 kB  | 81 ms | 45 ms | 56 ms
2 | 7,00 kB / 5,16 kB  | 127 ms | 56 ms | 78 ms
2 | 7,00 kB / 5,16 kB  | 235 ms | 54 ms | 74 ms
2 | 7,00 kB / 5,16 kB  | 194 ms | 54 ms | 71 ms
+ **Átlagos kérések és visszatérések száma:** Az átlagos kérések száma betöltéskor 2. Ezek közül 1 kérés sikeresen tér vissza, 1 esetben hiányzik a válasz.
+ **Hiányzó lap azonosítása:** A betöltés során a hiányzó lap azonosítása történt, ami az ikon hiányát jelenti. Ezt a rendszer nem éri el, amikor a weboldal betöltődik.

## További javasolt tesztek
+ **Teljesítménytesztek:**
    + **Terheléses (Load) tesztek:** Annak vozsgálata, hogy az oldal hogyan reagál nagy terhelésre, sok látogató esetén. Az oldal teljesítményének tesztelése olyan esetekben, amikor nagy a forgalom vagy váratlan terhelés jelentkezik.
    + **Stabilitási tesztek:** Ellenőrizni az alkalmazás stabilitását hosszabb ideig történő használat során. Hosszabb ideig tartó tesztek futtatása annak érdekében, hogy kiderüljöm nincsenek hosszú távú problémák, pl. memóriakezelési problémák, folyamatok lefagyása.
+ **Biztonsági tesztek:**
    + **Penetrációs tesztek:** Ellenőrzések végzése, hogy az oldal ellenáll-e biztonsági fenyegetéseknek, például SQL injection, Cross-Site Scripting (XSS) vagy egyéb támadásoknak.
    + **Jelszópolitika vizsgálata:** Ellenőriznni a jelszókomplexitást, hosszúságot, és a rendszer reakcióját helyes és helytelen jelszavakra.
+ **Kompatibilitási tesztek:**
    + **Különböző böngészőkben és eszközökön való tesztelés:** Megvizsgálni az oldal kompatibilitását különböző böngészőkkel és eszközökkel, például mobiltelefonok, tabletek, különböző operációs rendszerek.

## Javaslatok a fejlesztése
+ **Mobilbarát felület optimalizálása:** Az oldal jelenlegi felületének alkalmazkodása nem megfelelő a mobiltelefonok vagy tabletek használatához. Ennek következtében az oldal felhasználói élménye szenvedhet, és az esetleges nehezen kezelhető felületek vagy elérhetetlen funkciók megnehezítik a navigációt. A javasolt fejlesztés során fontos, hogy az oldal minden képernyőméret esetén biztosítsa a felhasználóbarát elrendezést és az összes funkcionalitást.
+ **Regisztrációs folyamat javítása:** Az instrukciók világosságának és az egyértelmű hibaüzeneteknek kiemelt jelentősége van a regisztrációs folyamat során. A pontos és érthető instrukciók segítik a felhasználókat a helyes adatok megadásában, míg a hibás adatok világos visszajelzése lehetővé teszi számukra a helyesítést és a folyamat sikeres lezárását.

# Főoldal

## Funkcionális tesztelés:
+ **Bejelentkezési és regisztrációs oldal elérésének tiltása bejelentkezett felhasználók számára:**
    + Ellenőrizni, hogy bejelentkezett felhasználóként nem lehet-e elérni a bejelentkezési vagy regisztrációs oldalakat.
    + A böngészősávba írt login vagy register oldalak elérése le van tiltva, emellett megjelenik egy felugró ablak, ami tájékoztatja a felhasználót az oldal elérhetetlenségéről: 'A bejelentkezési felület nem elérhető bejelentkezett felhasználóknak!'
+ **Főoldal funkcionalitásának ellenőrzése:**
    + A főoldalon megjelenik a bemutatkozó szöveg, a logó és a 'Kezdj bele!' gomb.
    + A 'Kezdj bele!' gomb nem működik megfelelően (kattintásra nem indít el semmilyen tevékenységet).
+ **Menüsáv működése bejelentkezés után:** 
    + Kattintásra megnyitódó menüpontok (pl. 'Főoldal', 'Dokumentáció', 'Trello kártyák', 'Kód', 'Profil', 'Kijelentkezés') funkcionalitásának ellenőrzésekor a rendszer helyesen működik.
    + A 'Főoldal' elemre kattintva frissíti az oldalt, mert az index-re irányít ami a jelenlegi oldal.
+ **Admin jogosultsággal rendelkező felhasználó menüjének vizsgálata:** Ha admin jogosultsággal jelentkezik be valaki, megjelenik egy plusz menüpont 'Felhasználók' címmel, amit kizárólag egy admin érhet el, a többi felhasználó számára ez az oldal elérhetetlen. 
+ **Kijelentkezés funkcionalitása:** Van egy kijelentkezés gomb ami kijelentkezteti a felhasználót és visszairányít a login oldalra, de külön értesítést nem ad.

## Felhasználói élmény ellenőrzése:

+ **Felhasználói értesítések és visszajelzések vizsgálata:** A felhasználói értesítések megfelelően jelennek meg, például a bejelentkezett felhasználók számára tiltott oldalak elérésekor.

## Teljesítménytesztek

### Betöltési idők ellenőrzése

Kérés | Átküldve | Befejezés | DOMContentLoaded | Load |
---|---|---|---|---|
2 | 7,67 kB / 5,69 kB | 139 mp | 50 ms | 71 ms
2 | 7,67 kB / 5,69 kB | 106 mp | 51 ms | 59 ms
2 | 7,67 kB / 5,69 kB | 126 mp | 64 ms | 70 ms
2 | 7,67 kB / 5,69 kB | 106 mp | 50 ms | 62 ms
2 | 7,67 kB / 5,69 kB | 117 mp | 59 ms | 76 ms

+ **Átlagos kérések és visszatérések száma:** Az átlagos kérések száma betöltéskor 2. Ezek közül 1 kérés sikeresen tér vissza és 1 esetben hiányzik a válasz.
+ **Hiányzó lap azonosítása:** A betöltés során a hiányzó lap azonosítása történt, ami az ikon hiányát jelenti. Ezt a rendszer nem éri el, amikor a weboldal betöltődik.

# Dokumentáció

*Nincs implementálva!*

# Trelló Kártyák

*Nincs implementálva!*

# Profil

*Nincs implementálva!*

# Felhasználók

+ **Admin jogosultsággal rendelkezők hozzáférésének ellenőrzése:**
    + A rendszer ellenőrzi, hogy csak admin jogosultsággal rendelkező felhasználók érhetik el ezt az oldalt a főoldalon található megfelelő menüpont kattintásával.
    + Biztosítja, hogy a funkció működik-e megfelelően, és csak az adminoknak van-e hozzáférése az oldalhoz.
+ **Rendszerbe regisztrált felhasználók adatainak megjelenítése:**
    + Az oldalon megjelenő adatok (felhasználónév, teljes név, email, utolsó bejelentkezés dátuma) helyesen és aktuálisan jelennek meg.
+ **Menüsáv hiánya:**
    + Az oldalon nem található menüsáv, amivel el lehetne érni a rendszer többi oldalát.
    + A visszanavigálás gombra kattintáskor sszavezet a főoldalra.
+ **Superuser státusz rendelkező felhasználók gombjának megjelenítése:**
    + Ha az admin rendelkezik superuser státusszal megjelenik a megfelelő gomb a felhasználók módosításához, egy külön oldal megnyitásával.
    + A gomb funkciója megfelelő és csak superuser státusszal rendelkező felhasználók használhatják.