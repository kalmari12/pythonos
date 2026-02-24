szoveg = str("Ebben a korban a kézművesek száma és szerepe gyorsan nőtt a gazdaságban. Messze előrehaladt a specializáció a körükben, sokféle szakma képviselői kínálták szolgáltatásaikat, kőművesek, kőfaragók, asztalosok, fazekasok, papírgyártók, fémöntők, szövők, tímárok, borbélyok, cipészek, kosárfonók, kovácsok, lakk-készítők és sokan mások. Egy részük a vállukon átvetett rúd két végén elhelyezett vödrökben hordta, vagy kis kocsikon tolta egész műhelyét. Mások saját kis szerény műhelyeikben dolgoztak, legtöbbször egész családjukkal együtt.[17] A kézművesek gyakran céhekbe tömörültek, segítették egymást, megalkották szakmájuk alapszabályait, igyekeztek megoldani belső konfliktusaikat. A céhmesterek részt vettek a vásárokon, az ünnepi szertartásokon, adományokat nyújtottak és gyűjtöttek. A különböző szakmáknak, céheknek megvolt a maguk „védőszentje”. Például Lu Pan, az i. e. 5. századra datált mitikus hős volt a faművesek, a fával foglalkozó kézművesek „istene”. Őt tisztelték a fűrész, a véső, a vakolókanál, a szögmérő, a fejsze, a mérőzsinór feltalálójának. Kiadtak egy ács-szakkönyvet is az ő neve alatt, amiben leírták, hogyan kell házat, palotát, templomot, hidat építeni, ajtót, ablakot, bútort készíteni. A többi szakmának is megvoltak a maguk patrónusai, akiknek áldozati ajándékot vittek a templomaikba – ez jó alkalmat nyújtott a szakmai összejövetelekre és mulatságokra is.[17] A túlzott terhek ellen nem csak a parasztok, hanem a kézművesek is fellázadtak időnként: ilyenkor megölték az adószedőket, felgyújtották a hivatalokat. A lázadásokat általában természetesen leverte a császári hatalom, de utána gyakran levonták a tanulságokat és enyhítettek a terheken.[17] A kézművesek egy része csak az államnak dolgozott és a Tiltott Városban, a hercegi palotákon, vagy például az állami hajóépítő telepeken dolgozott. Mások idejük nagy részében szabadon vállalhattak munkát, de egyfajta kézműipari robotként rendszeres időközönként állami célokra is kellett dolgozniuk.[18] A kézművesség egyes ágai a 16. században ipari jelleget öltöttek és gyors fejlődésnek indultak. A legjelentősebb a textilipar volt, Szucsou, Hangcsou, Nanking és a mai Sanghaj környékén elterülő egykori Szungcsiang városokkal, mint fő központokkal. Egyes centrumokban már százezres nagyságrendben foglalkoztattak munkásokat. Egyre több textilféleséget készítettek (selymet, lenvásznat, gyapjúszövetet, pamutot, csalánszövetet), különböző kikészítési módokat alkalmaztak (így alakult ki a muszlin, a szatén, a fátyolszövet, a bársony), és a munkások is specializálódtak különféle szakmákra, különváltak a kártolók, a fonók, a kelmefestők, a hímzőmunkások és mások. Bedolgozókat is nagy számban foglalkoztattak.[19] A porcelángyártás is nagyrészt állami tulajdonban volt; a Ming-dinasztia alapításakor húsz állami manufaktúra volt, az 1420-as évekre számuk 58-ra emelkedett. A magántulajdonban lévő porcelángyártó üzemek általában gazdag családoknak dolgoztak, de kaptak állami megrendeléseket is. A száz-százötvenezer darabos császári megrendelések sem számítottak ritkaságnak. A termékek jelentős része exportra került. A 15. században az egyszínű, vagy a kék-fehér porcelánok voltak a legdivatosabbak. A tömeggyártás idővel rontott a minőségükön. Nagyon sokféle porcelánt gyártottak, a hatalmas méretű vázáktól a finom apró „tojáshéj-porcelán” csészékig. A munkamegosztás szinte a futószalaghoz hasonlítható volt: amíg egy darab a kemencébe jutott, addig mintegy hetven kézen, az előkészítők, formázók, festők tucatjain ment át.[20] Nagyon jelentős iparág volt még a teljesen állami kézen lévő fegyvergyártás. A 17. század végére már a papírgyártás is jelentős iparág volt: csak Csianghszi tartományban körülbelül harminc nagy papírgyártó manufaktúra működött, ötvenezer főnyi munkáslétszámmal.[20] A munkások a parasztság soraiból származtak, vagy elszegényedett kézművesek voltak. Egy részük állandóan egy műhelyben dolgozott, mások időszaki munkát vállaltak, természetesen általában szóbeli megállapodás alapján. A fizetség időbér vagy darabbér egyaránt lehetett. A munkát keresők Szucsouban például szakmák szerint gyülekeztek hajnalban a város különböző pontjain, a toborzók érkezésére várva.[20]")

szoveg = szoveg.lower()

jelek = [".",',',"[","]","(",")",":","-"]

for jel in jelek:
    szoveg = szoveg.replace(jel, "")

szoveglista = szoveg.split()

# szokereses
talaltlista = []

adjameg = str(input("Adja meg a keresendo szot: "))

for szo in szoveg:
    if szo == adjameg:
        talaltlista.append(szo)

print(talaltlista)

with open("python/string/ming-dinasztia/export.txt", "w", encoding="utf-8")as adat:
    print(*talaltlista,sep=" // ", file=adat)

with open("python/string/ming-dinasztia/export.txt", "r", encoding="utf-8")as impadat:
    t = impadat.read()

    print(f"A megatalalt szavak:\n {t}")

szamok = []

for szo in szoveg:
    if szo.isdigit() and len(szo) < 4 and  szo not in szamok: