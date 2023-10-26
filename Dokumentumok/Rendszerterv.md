# Rendszerterv

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
