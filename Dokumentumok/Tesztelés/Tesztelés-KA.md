### Bejelentkezés / regisztráció tesztelése:

**Tesztelő:** Kinczel Ádám Gergő

**Tesztelés dátuma:** 2023.12.13

| Teszteset azonosító | Teszteset | Elvárt eredmény | Tényleges eredmény | Megjegyzés |
| ------------------- | --------- | --------------- | ------------------ | ---------- |
| __KA_t001__| Bejelentkezés __mezők kitöltése nélkül__: | Az oldal jelzi, hogy nem adtunk megadatot. | Minden az elvárt szerint működik. | Minden rendben. |
| __KA_t002__ | Regisztráció __adatok megadása nélkül__: | A rendszer felhívja a figyelmet, hogy **minden adatot meg kell adni** | Minden az elvárt szerint működik. | Minden rendben. |
| __KA_t003__ | __Sikeretelen regisztráció__: | Sikertelen regisztráció esetén hibaüzenet jelez a felhasználónak. | Ha a jelszó és annak megerősítése nem egyezik, a regisztráció sikertelenségéről hibaüzenetet nem kapunk. | Javítás szügséges. |
| __KA_t004__ | Bejelentkezés __hibás adatokkal__: | Hibás adatok megadása esetén a **a belépést a rendszer megtagadja.** a hibás adatok hibaüzenet megjelenítésével | Minden az elvárt szerint működik. | Minden rendben. |
| __KA_t005__ | Regisztárciónál használt __jelszó erősségének ellenőrzése__: | 8 karakternél kisebb jelszó használatakor **a rendszer a regisztrációt megtagadja.** vagy ha nem tartalmaz nagybetűt illetve számot | Minden az elvárt szerint működik. | Minden rendben. |
| __KA_t006__ | Sikeres bejelentkezés | Sikeres bejelentkezést követően **a rendszer a főoldalra navigálja a felhasználót** és már képes lesz belépni az oldalra, megtekinteni a funkciókat | Minden az elvárt szerint működik. | Minden rendben. |
| __KA_t007__ | Bejelentkezés nélküli belépés az oldalra | Ha nincs a felhasználó bejelentkezve, **a rendszer a bejelentkezési oldalra navigálja a felhasználót**, bármilyen URL-t beírva mindig a bejelentkezési oldal jelenik meg addig, amíg be nem jelentkezik. A hibaüzenet is megjelenik mellé. | Minden az elvárt szerint működik. | Minden rendben. |
| __KA_t008__ | Az admin és a sima user szétválasztása. | A rendszer **megkülönbözteti a két jogosultágot** | Minden az elvárt szerint működik. | Minden rendben. |

### Kijelentkezés tesztelése:

**Tesztelő:** Kinczel Ádám Gergő

**Tesztelés dátuma:** 2023.12.13

| Teszteset azonosító | Teszteset | Elvárt eredmény | Tényleges eredmény | Megjegyzés |
| ------------------- | --------- | --------------- | ------------------ | ---------- |
| __KA_t009__ | Kijelentezési __gomb-ra való kattintás__: | Az oldal sikeresen **kijelentkezteti a felhasználót egy üzenettel jelezve** azt és átnavigálja a bejelentkezési oldalra. | Minden az elvárt szerint működik. | Minden rendben. |
| __KA_t010__ | Kijelentezés __után__: | Bármilyen URL-t beírva **a felhasználónak csak a bejelentkezési oldal jelenik meg**, hiszen sikeresen kijelentkezett. | Minden az elvárt szerint működik. | Minden rendben. |
| __KA_t011__ | Kijelentezés után __újra bejelentkezés__: | **A felhasználó újra be tud lépni**, és újra eléri az oldal funkcióit.                                                   | Minden az elvárt szerint működik. | Minden rendben. |
| __KA_t012__ | Kijelentezés __után__: | Bármilyen URL-t beírva **a felhasználónak csak a bejelentkezési oldal jelenik meg**, hiszen sikeresen kijelentkezett. | Minden az elvárt szerint működik. | Minden rendben. |

### Navigálás tesztelése:

**Tesztelő:** Kinczel Ádám Gergő

**Tesztelés dátuma:** 2023.12.13

| Teszteset azonosító | Teszteset | Elvárt eredmény | Tényleges eredmény | Megjegyzés |
| ------------------- | --------- | --------------- | ------------------ | ---------- |
| __KA_t013__ | __"Kezdj bele" gomb__ kezelése a főoldalon | A gomb átirányít arra az oldalra, ahol lehetőségünk lesz elkezdeni a 'munkát'. | A gomb nem visz sehova. | Javítás szügséges. |
| __KA_t014__ | __"Főoldal" gomb__ kezelése a navbaron | A gomb elvisz a főoldalra. | Minden az elvárt szerint működik. | Minden rendben. |
| __KA_t015__ | __"Dokumentáció" gomb__ kezelése a navbaron | A gomb elvisz a "documentation" oldalra. | Minden az elvárt szerint működik. | Minden rendben. |
| __KA_t016__ | __"Trello kártyák" gomb__ kezelése a navbaron | A gomb elvisz a "trello_cards" oldalra. | Minden az elvárt szerint működik. | Minden rendben. |
| __KA_t017__ | __"Kód" gomb__ kezelése a navbaron | A gomb elvisz a code oldalra. | Minden az elvárt szerint működik. | Minden rendben. |
| __KA_t018__ | __"Profil" gomb__ kezelése a navbaron | A gomb elvisz a trello_cards oldalra. | Minden az elvárt szerint működik. | Minden rendben. |
| __KA_t019__ | __"Felhasználók" gomb__ kezelése a navbaron | A gomb elvisz a "users" oldalra. | Minden az elvárt szerint működik. | Minden rendben. |
| __KA_t020__ | __"Visszatérés a főoldalra!" gomb__ kezelése a felhasználók oldalon | A gomb visszavisszavisz a főoldalra. | Minden az elvárt szerint működik. | Minden rendben. |

### Funkciók tesztelése:

**Tesztelő:** Kinczel Ádám Gergő

**Tesztelés dátuma:** 2023.12.13

| Teszteset azonosító | Teszteset | Elvárt eredmény | Tényleges eredmény | Megjegyzés |
| ------------------- | --------- | --------------- | ------------------ | ---------- |
| __KA_t021__ | __"Kezdj bele" gomb__ működése | A gomb átirányít a munka kezdő oldalra | A gomb nem működik, nem lett elkészítve. | Javítás szügséges. |
| __KA_t022__ | __"Trello kártyák"__ megjelenése és kezelése | A Trello kártyák megjelennek és lehet őket kezelni. | Nem jellennek meg a kártyák. | Javítás szügséges. |
| __KA_t023__ | __"Kód"__ oldal megjelenése és kezelése | A kód oldalon kezelhetjük és megtekinthetjük a Csapattagok által megírt kódokat | Nem jelenik meg semmi. | Javítás szügséges. |
| __KA_t024__ | __"Profil"__ oldal megjelenése és adatok kezelése | A profil olalon látható a jelenleg bejelentkezett profil adatai és módosíthatóak ezek. | Az oldalon nem jelenik meg semmi. | Javítás szügséges. |
| __KA_t025__ | __"Felhasználók"__ oldal megjelenése | Megjelennek az oldalra regisztrált felhasználók általános adatai. | Minden az elvárt szerint jelenik meg. | Minden rendben. |