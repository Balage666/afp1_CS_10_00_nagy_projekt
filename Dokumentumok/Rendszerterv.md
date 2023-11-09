# Rendszerterv

## 1.Bevezetés
Az Applikációfejlesztési folyamat-támogató alkalmazás rendszerterve egy olyan dokumentum, amely az alkalmazás fejlesztését, telepítését és működését részletezi. A célja, hogy elősegítse a cégeket és fejlesztőcsapatokat a hatékonyabb és strukturáltabb alkalmazásfejlesztési folyamatokban.

A modern vállalkozások számára az alkalmazások kritikus szerepet játszanak az üzleti sikerben. Az alkalmazások segíthetnek az ügyfélkapcsolatok erősítésében, az üzleti folyamatok optimalizálásában és az innováció elősegítésében. Az alkalmazásfejlesztés azonban gyakran összetett és időigényes folyamat, amely számos kihívást és nehézséget hordoz magában. Az Applikációfejlesztési folyamat-támogató alkalmazás célja a fejlesztőknek és vállalatoknak segítséget nyújtani ezen kihívások kezelésében.

Ebben a rendszertervben bemutatjuk az alkalmazás tervezését és működését, valamint a főbb funkciókat és előnyöket, amelyeket az alkalmazás nyújthat. Az alkalmazás tervezése és fejlesztése során számos tényezőt vettünk figyelembe, beleértve a felhasználói igényeket, a biztonsági szempontokat és az alkalmazás teljesítményét.

Az alkalmazás átfogó funkcionalitást kínál a fejlesztési folyamat minden szakaszához, beleértve a tervezést, kódolást, tesztelést és telepítést. Emellett eszközökkel és jelentésekkel is rendelkezik, amelyek segítik a fejlesztőket a folyamat hatékonyabb irányításában.

Ez a rendszerterv az alkalmazás tervezésének kiindulópontja, és iránymutatást nyújt a fejlesztési csapatnak az alkalmazás létrehozásához és a végrehajtáshoz. Az alkalmazás várhatóan hozzájárul a vállalatok sikeréhez és hatékonyságához az alkalmazásfejlesztési folyamatok optimalizálásával. A következő fejezetekben részletesen bemutatjuk az alkalmazás tervezését és funkcióit.

## 2. Architektúra
Az alkalmazás a következő fő komponensekből áll:

- Felhasználói felület (Frontend): Ez az alkalmazás azon része, amelyet a végfelhasználók látnak és használnak. Itt találhatóak a különböző funkcionalitásokhoz szükséges felületek, mint például az adatbeviteli űrlapok, jelentések, grafikonok stb. Mivel a Django egy teljes körű webfejlesztési keretrendszer, képes a frontend funkciók kezelésére is a template rendszerén keresztül.

- Backend: Itt található az alkalmazás logikája, az adatok feldolgozása és a felhasználói kérések kezelése. A Django ezen az oldalon is erős, mivel a Python nyelven íródott, és kifejezetten webalkalmazások back-end fejlesztésére lett tervezve. Az ORM (Object-Relational Mapping) funkcióval képes az adatbázissal való könnyű kommunikációra is.

- Adatbázis: Az alkalmazás adatainak tárolására szolgál. Django támogatja a legnépszerűbb adatbázis-rendszereket, mint például a PostgreSQL, MySQL, SQLite és Oracle. Az ORM révén a fejlesztőknek nem kell közvetlenül SQL kódokkal dolgozniuk, mivel a Django képes az adatmodellek alapján automatikusan generálni az adatbázis-sémát.

## 3. Implementáció
Az alkalmazás implementációja a következő technológiákon alapul:

- Felhasználói felület: A frontend fejlesztéséhez a Django template rendszerét fogjuk használni, mely lehetővé teszi dinamikus weboldalak készítését Python alapú logika és adatok felhasználásával.

- Backend: A backend logikájának megvalósításához Django-t fogunk használni. Ez a keretrendszer számos beépített funkciót kínál, mint például az autentikáció, az űrlapok kezelése, az adatbázis migrációk és az adminisztrációs interfész.

- Adatbázis: Django ORM-je lehetővé teszi az adatbázis-séma automatikus létrehozását a Python modellek alapján. Az adatbázis-kapcsolat beállításához a Django settings.py fájljában konfiguráljuk az adatbázis hitelesítési adatait és típusát.

## 4. Tesztelés

Az alkalmazást a következő tesztelési módszerekkel fogják tesztelni:
 - Unit tesztelés: Az alkalmazás egységeit fogják tesztelni.
 - Egység tesztelés: Az alkalmazás összetevőit fogják tesztelni.
 - Teljesítmény tesztelés: Az alkalmazás teljesítményét fogják tesztelni.
 - Támogatottsági tesztelés: Az alkalmazást különböző böngészőkben és operációs rendszerekben fogják tesztelni.

## 5. Karbantartás

Az alkalmazást rendszeresen karban fogják tartani, hogy biztosítsa a megfelelő működését. A karbantartás magában fogja foglalni a következőket:

Hibajavítások: Az alkalmazás hibáinak javítása.
Új funkciók hozzáadása: Az alkalmazás új funkcióinak hozzáadása.
Teljesítmény javítása: Az alkalmazás teljesítményének javítása.

## 7. Dokumentáció

Az alkalmazásnak megfelelő dokumentációval kell rendelkeznie, hogy a felhasználók könnyen meg tudják tanulni a használatát. 
Az alkalmazás dokumentációjának rendelkezésre állása elengedhetetlen a felhasználók számára a hatékony és helyes használat, valamint az alkalmazás megértése szempontjából. 
A dokumentáció segít a felhasználóknak az alkalmazás használatának elsajátításában, valamint a fejlesztőknek az alkalmazás architektúrájának és implementációjának megértésében. 
A dokumentáció a következőket fogja tartalmazni:
+ Használati útmutató: Az alkalmazás használatára vonatkozó utasításokat tartalmazza.
    - Telepítési útmutató: A felhasználók számára részletes lépéseket ad a telepítési folyamat során. Ez magában foglalja az alkalmazás letöltését, telepítését, és a szükséges konfigurációkat.
    - Felhasználói felület leírása: Az alkalmazás felhasználói felületét részletesen bemutatja, és bemutatja az összes funkciót és műveletet, amelyeket a felhasználók használhatnak.
    - Műveletek leírása: Az alkalmazás használatához szükséges műveleteket lépésről lépésre részletezi. Ide tartozik például az új projekt létrehozása, feladatok hozzáadása, és egyéb gyakori tevékenységek.
    - Hibaelhárítás: Az esetleges hibák és problémák elhárítására szolgáló útmutatót tartalmaz, valamint ajánlásokat ad a felmerülő problémák megoldására.
+ Technikai dokumentáció: Az alkalmazás architektúráját és implementációját írja le.
    - Architektúra leírása: Az alkalmazás architektúráját és komponenseit részletesen ismerteti. Ide tartozik az alkalmazás rétegeinek és komponenseinek leírása, valamint a kapcsolatok közöttük.
    - Implementáció részletei: A technikai dokumentáció bemutatja az alkalmazás fejlesztési környezetét, a használt programozási nyelveket, keretrendszereket és adatbázisokat. Az implementáció részletezésével a fejlesztők könnyebben megérthetik az alkalmazás kódját és struktúráját.
    - API dokumentáció: Ha az alkalmazásnak nyilvános vagy belső API-k vannak, a dokumentáció tartalmazza ezeknek a funkcióknak a leírását és használati útmutatóját.
    - Adatmodell leírása: Az alkalmazás adatmodelljét és az adatbázissémáját részletesen ismerteti. Ide tartoznak az adatok tárolására és kezelésére vonatkozó információk.

## 8. Tervezett idővonal

+ Projekt kezdet: A projekt kezdetén meghatározzuk a projektet, kijelöljük az erőforrásokat, elvégezzük a szükséges kutatásokat és adatgyűjtést, valamint kidolgozzuk a projekttervet. (Kezdet: 2023-07-01)

+ Követelménygyűjtés: Ebben a szakaszban gyűjtjük és elemzünk felhasználói és üzleti követelményeket, majd dokumentáljuk ezeket. (Időszak: 2023-07-15 - 2023-08-15)

+ Követelményspecifikáció: Elkészítjük a követelményspecifikációt a gyűjtött követelmények alapján. (Időszak: 2023-08-16 - 2023-09-15)

+ Funkcionális specifikáció: Ebben a fázisban készítjük el a funkcionális specifikációt a követelményspecifikáció alapján. (Időszak: 2023-09-16 - 2023-10-15)

+ Rendszerterv: Kidolgozzuk a rendszertervet a funkcionális specifikáció alapján, és elkészítjük az adatbázis tervezését és implementálását. (Időszak: 2023-10-16 - 2023-11-30)

+ Tesztelés: A rendszertervet validáljuk és teszteljük, javítjuk az esetleges hibákat, és finomítjuk a rendszert. (Időszak: 2023-12-01 - 2023-12-15)

+ Dokumentáció és befejezés: Véglegesítjük a rendszertervet, dokumentáljuk a projektet, és lezárjuk a projektet, majd átadjuk a felhasználóknak vagy fejlesztő csapatnak. (Időszak: 2023-12-16 - 2024-01-01)

## 11. Tervezett piac

+ Az alkalmazást elsősorban Magyarországon és a környező országokban fogják értékesíteni, de ezen kívül nemzetközi értékesítésre is alkalmas.

+ A tervezett felhasználópiacot fejlesztő csapatok alkotják, akik szeretnék megkönnyíteni a fejlesztéssel járó munkálataikat a mesterséges inteligenciák használatának segítségével.

# 12. Fenntarthatóság

Az alkalmazást úgy tervezték, hogy hosszútávon fenntartható legyen. A következő intézkedések szükségesek a fenntarthatóság biztosítására:

+ Energiahatékonyság: Az alkalmazást energiahatékonyan fogják megtervezni és implementálni energiaforrások tekintetében.
+ Felhasználói támogatás: Az alkalmazást felhasználóbarát módon készítik el, hogy a felhasználók könnyen kezelhessék azt, szükség esetén pedig segítséget is kérhetnek.
+ Frissítések: Az alkalmazást rendszeresen frissíteni fogják, hogy biztosítsák a megfelelő működését. Naprakészen tartják a harmadik felektől származó, működéshez elengedhetetlenül szükséges feltételeket. Esetleges módszertani változások bekövetkeztében igazítják az alkalmazás működését a megváltozott formai követelményekhez

