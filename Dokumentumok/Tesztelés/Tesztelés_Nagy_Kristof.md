### Bejelentkezés / regisztráció tesztelése:

**Tesztelő:** Nagy Kristóf

**Tesztelés dátuma:** 2023.12.13

| Teszteset azonosító | Teszteset                                                    | Elvárt eredmény                                                                                                                                                                                                                            | Tényleges eredmény                                                                                       | Megjegyzés                         |
| ------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| __NK_t001__         | Bejelentkezés __input kitöltés nélkül__:                    | Az oldal jelez hogy adjuk meg az  elvárt adatokat.                                                                                                                                                                                                | Ugyanaz, mint az Elvárt eredmény szekcióban.                                                             | Nem találtam hibára utaló jeleket. |
| __NK_t002__         | Regisztráció __adatok hiányos megadásával__:                     | A rendszer üzenet: **minden adatot meg kell adni.**                                                                                                                                                                     | Ugyanaz, mint az Elvárt eredmény szekcióban.                                                             | Nem találtam hibára utaló jeleket. |
| __NK_t003__         | __Sikeretelen regisztráció__:                                | Hibaüzenet formájában jelezzük a felhasználónak.                                                                                                                                                                          | Nincs hiba üzenet. | Javítani szükséges.                |
| __NK_t004__         | Bejelentkezés __hibás adatokkal__:                           |  **A belépést a rendszer megtagadja.**                                                                                                                           | Ugyanaz, mint az Elvárt eredmény szekcióban.                                                             | Nem találtam hibára utaló jeleket. |
| __NK_t005__         | __Jelszavak input validaciója__: | 8 karakter minimum,kis és nagy betű                                                                                                    | Ugyanaz, mint az Elvárt eredmény szekcióban.                                                             | Nem találtam hibára utaló jeleket. |
| __NK_t006__         | Sikeres bejelentkezés                                        |  **A rendszer a főoldalra léptet**                                                                                          | Ugyanaz, mint az Elvárt eredmény szekcióban.                                                             | Nem találtam hibára utaló jeleket. |
| __NK_t007__         | Bejelentkezés nélküli belépés az oldalra                     | Ha nincs a felhasználó bejelentkezve, **a rendszer a bejelentkezési oldalra navigálja a felhasználót**, bármilyen URL-t beírva sem lehet megkerülni | Ugyanaz, mint az Elvárt eredmény szekcióban.                                                             | Nem találtam hibára utaló jeleket. |


### Kijelentkezés tesztelése:

**Tesztelő:** Nagy Kristóf

**Tesztelés dátuma:** 2023.12.13

| Teszteset azonosító | Teszteset                                 | Elvárt eredmény                                                                                                          | Tényleges eredmény                           | Megjegyzés                         |
| ------------------- | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------- | ---------------------------------- |
| __NK_t008__         | Kijelentezési __gomb-ra való kattintás__: | Az oldal sikeresen **kijelentkezteti a felhasználót**  | Ugyanaz, mint az Elvárt eredmény szekcióban. | Nem találtam hibára utaló jeleket. |


### Navigálás tesztelése:

**Tesztelő:** Nagy Kristóf

**Tesztelés dátuma:** 2023.12.13

| Teszteset azonosító | Teszteset                                                           | Elvárt eredmény                                                                | Tényleges eredmény                           | Megjegyzés                         |
| ------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------ | -------------------------------------------- | ---------------------------------- |
| __NK_t009__         | __"Kezdj bele" gomb__                        | A gomb átirányít arra az oldalra, ahol lehetőségünk lesz elkezdeni a 'munkát'. | A gomb nem visz sehova.                      | Javítani szükséges.                |
| __NK_t010__         | __"Főoldal" gomb__                              | A gomb elvisz a főoldalra.                                                     | Ugyanaz, mint az Elvárt eredmény szekcióban. | Nem találtam hibára utaló jeleket. |
| __NK_t011__         | __"Dokumentáció" gomb__                        | A gomb elvisz a "documentation" oldalra.                                       | Ugyanaz, mint az Elvárt eredmény szekcióban. | Nem találtam hibára utaló jeleket. |
| __NK_t012__         | __"Trello kártyák" gomb__                       | A gomb elvisz a "trello_cards" oldalra.                                        | Ugyanaz, mint az Elvárt eredmény szekcióban. | Nem találtam hibára utaló jeleket. |
| __NK_t013__         | __"Kód gomb__                                   | A gomb elvisz a code oldalra.                                                  | Ugyanaz, mint az Elvárt eredmény szekcióban. | Nem találtam hibára utaló jeleket. |
| __NK_t014__         | __"Profilom" gomb__                          | A gomb elvisz a trello_cards oldalra.                                          | Ugyanaz, mint az Elvárt eredmény szekcióban. | Nem találtam hibára utaló jeleket. |
| __NK_t015__         | __"Felhasználók" gomb__                        | A gomb elvisz a "users" oldalra.                                               | Ugyanaz, mint az Elvárt eredmény szekcióban. | Nem találtam hibára utaló jeleket. |
| __NK_t016__         | __"Visszatérés a főoldalra!" gomb__ | A gomb visszavisszavisz a főoldalra.                                           | Ugyanaz, mint az Elvárt eredmény szekcióban. | Nem találtam hibára utaló jeleket. |


### Profilok megtekintésének tesztelése:
**Tesztelő:** Nagy Kristóf

**Tesztelés dátuma:** 2023.12.13

| Teszteset azonosító | Teszteset                                | Elvárt eredmény                                                                                                                                                                                   | Tényleges eredmény                              | Megjegyzés                         |
| ------------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- | ---------------------------------- |
| __NK_t017__         | A __felhasználók megtekintése__ | A megfelelő gombra kattintva,megfelelő jogosultsággal rendelkezve kilistáza a felhasználókat | Ugyanaz, mint az Elvárt eredmény szekcióban.    | Nem találtam hibára utaló jeleket. |          |

