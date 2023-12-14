### Kijelentkezés Tesztelése:

**Tesztelő:** Jaczina Norbert

**Tesztelés dátuma:** 2023.12.11

| Demonstráló azonosító | Szimulációs példa | Referenciaeredmény | Valós eredmény | Visszajelzések |
| ------------------- | --------- | --------------- | ------------------ | ---------- |
| __JN_t001__ | Kijelentkezési gombra való kattintással: | Az oldal sikeresen kijelentkezteti a felhasználót, közben egy üzenet jelenik meg, amely értesíti a felhasználót a sikeres kijelentkezésről. Ezt követően a rendszer átnavigálja a felhasználót a bejelentkezési oldalra. | Az elvárásoknak megfelelően zajlott le. | Nem észleltem olyan jeleket, amelyek hibára utalnának.
| __JN_t002__ | Kijelentkezés után újra bejelentkezés: | A felhasználó újra be tud lépni, és újra eléri az oldal funkcióit. | Az elvárásoknak megfelelően zajlott le. | Nem észleltem olyan jeleket, amelyek hibára utalnának.
| __JN_t003__ | Kijelentkezés után: | Bármilyen URL-t beírva, a felhasználó kijelentkezés után csak a bejelentkezési oldalt fogja látni, mivel sikeresen kijelentkezett. | Az elvárásoknak megfelelően zajlott le. | Nem észleltem olyan jeleket, amelyek hibára utalnának. |

### Bejelentkezés Tesztek:

**Tesztelés dátuma:** 2023.12.11

| Demonstráló azonosító | Szimulációs példa | Referenciaeredmény | Valós eredmény | Visszajelzések |
| ------------------- | --------- | --------------- | ------------------ | ---------- |
| __JN_t004__ | Sikeres Bejelentkezés: | Sikeresen kitöltöm a felhasználónév és jelszó mezőket, majd megfelelően működik a bejelentkezés gombra kattintva. | A rendszer beenged a felhasználói fiókomba, és az elvárt kezdőoldalra navigál. | A bejelentkezés sikeres volt, és a kezdőoldalra irányított.
| __JN_t005__ | Sikertelen Bejelentkezés - Hibás Jelszó: | Hibás jelszót adok meg, de helyes felhasználónévvel, majd megfelelően kattintok a bejelentkezés gombra. | Az oldal megjeleníti a megfelelő hibaüzenetet és nem enged be a rendszerbe. | A rendszer helyesen kezelte a hibás jelszót, és megfelelő hibaüzenetet adott vissza.

### Kijelentkezés Tesztek:

**Tesztelés dátuma:** 2023.12.11

| Demonstráló azonosító | Szimulációs példa | Referenciaeredmény | Valós eredmény | Visszajelzések |
| ------------------- | --------- | --------------- | ------------------ | ---------- |
| __JN_t006__ | Sikeres Kijelentkezés: | Sikeresen kijelentkezem a felhasználói fiókomból. | Az oldal sikeresen kijelentkezteti a felhasználót és átnavigál a bejelentkezési oldalra. | A kijelentkezés sikeres volt, és a bejelentkezési oldalra irányított.

### Tartalom Böngészés Tesztek:

**Tesztelés dátuma:** 2023.12.11

| Demonstráló azonosító | Szimulációs példa | Referenciaeredmény | Valós eredmény | Visszajelzések |
| ------------------- | --------- | --------------- | ------------------ | ---------- |
| __JN_t007__ | Kategória Kiválasztása és Tartalom Böngészése: | Kiválasztok egy kategóriát, majd böngészek a tartalmak között. | Az oldal megjeleníti a kiválasztott kategória tartalmait, és lehetővé teszi a böngészést. | A tartalomböngészés sikeres volt a választott kategóriában.
| __JN_t008__ | Keresés Funkció Használata: | Használom a keresés funkciót egy specifikus tartalomra. | Az oldal megjeleníti a keresési eredményeket, és lehetővé teszi a specifikus tartalomra való kattintást. | A keresési eredmények megfelelnek az elvárásoknak, és a kiválasztott tartalom megnyílik.