```python
Filoversikt:
-----------------------------------------------------------------------------------------------------------
HitTheTarget.py           | Pygame program for simulering
Kalman.py                 | Alpha-Beta-Gamma filter
myHitTheTarget.py         | Nedstrippet program uten grafikk, for simulering
output.txt                | Resultat av test for beste a/b/g verdi
-----------------------------------------------------------------------------------------------------------
```


# Introduksjon

I oblig 1 var oppgaven å lage et filter for å beregne posisjonen til et objekt hvor posisjonen obfskuseres av støy. Filteret skulle være av typen kalmanfilter eller alpha-beta-gamma filter. 

Et Kalman-filter med bruk av matriser i utregninger er en kompleks oppgave som jeg kjapt innså at jeg ville ha problemer med å forklare, og forstå, så jeg har valgt alpha-beta-gamma varianten til denne oppgaven. Jeg har oppnådd i overkant av  90% prosent nøyaktighet med dette filteret etter mye prøving og feiling. Det viste seg at den største utfordringen var å finne de riktige verdiene for alpha/beta/gamma, så her endte jeg med å skrive en egen test for dette. Mer om det tilslutt. Det er også verdt å nevne at med en en liten forandring i koden til HitTheTarget.py så er det mulig å oppnå nesten 100% hitrate, det kan du også lese lenger ned.


![HitTheTarget.png](https://github.com/trombasso/Obligs-UiT-21-22/blob/main/2022H/HitTheTarget/HitTheTarget.png?raw=true)
`Bildet viser programmet som skulle brukes i denne oppgaven. Det viser seg at pygame fungerer dårlig på Mac, så her har jeg vært nødt til å bruke en forandret utgave for testing slik at jeg fikk kjørt tilstrekkelig antall iterasjoner for å kunne måle med god nok nøyaktighet.`


# Teorien og utvikling

Nettsida <http://www.kalmanfilter.net> har vært til stor hjelp i denne oppgaven, og formlene over er hentet derfra. Jeg har ikke funnet andre kilder som gir en bedre forklaring på bakgrunn eller funksjon, og de mange eksemplene gjør det enkelt å se hvordan man selv kan implementere filteret i andre sammenhenger. Det ville vært langt vanskeligere uten denne ressursen.

For å komme i gang så brukte jeg øvingsoppgave-Kalman for å først bygge et alpha-filter og deretter et alpha-beta filter. Alpha filteret ser ut slik som dette:

```python
def kalman_alpha(values: list) -> list:
	estimates = []
	prev_value = values[0]
	a = 1
	for n in range(0, len(values) - 1):
		a = 1 / (n + 1)
		estimate = prev_value + a * (values[n] - prev_value)
		prev_value = estimate
		estimates.append(estimate)
	return estimates
```
`Øvinsoppgave-kalman`

Dette var en enkel og ukomplisert måte å starte på hvor man bruker en omskriving av formelen for gjennomsnitt, som vist her: $$x_{n,n}={1\over n}(z_1+z_2+...+z_{n-1}+z_n)={1\over n}\Sigma^n_{i-1}(z_i)$$
Her kan vi se at sluttformelen starter med $1\over n$ , en verdi som blir mindre i takt med antallet målinger. I et kalman-filter har denne verdien fått navnet kalman-gain og er å finne igjen i både beta og gamma delen av filteret som vi skal se på under. Omskrevet til en formel som vi kan bruke i en iterativ sammenheng vil overstående se slik ut:
$$x_{1,1}=x_{1,0}+\alpha(measurement−x_{1,0})$$
Her kan vi se at $1\over n$ er byttet ut med $\alpha$ som vil sørge for å justere "viktigheten" av målingen som legges til grunn for neste iterasjon. Jo nærmere vi kommer en reel verdi, jo mindre vil justeringen bli.

I del 2 av øvingsoppgave-kalman ble det klart for meg at det lønnte seg å legge opp til en klasse for selve filteret, da det forenklet jobben med å behandle verdier. Her jobber jeg riktignok med dictionaries og ikke enkeltverdier som i hovedoppgaven, men man kan se utviklingen fra forrige kodesnutt som kun beror på en *State Update Equation*, hvor vi her også bruker *State Extrapolation Equation*. Begge to er et sett med ligninger for posisjon, fart og akselerasjon som vi skal se litt nærmere på under.

```python
class Kalman_alphaBeta:
	def __init__(self, values: Dict[float, float]):
	self.values = values
	self.estimated_values: Dict[float, float] = deepcopy(values)

def make_prediction(self) -> None:
	STEP = 0.5
	step = 0.5
	alpha = 0.2
	beta = 0.1
	t = len(self.values) / 2
	  
	# setting init values
	x_prev = self.values[0]
	v_prev = sqrt(((self.values[0 + STEP] - self.values[0])) ** 2) / t
	  
	while step != max(self.values):
		# Set next measurement
		z = self.values[step]
		# State Update Equation, calculate current estimate
		x_curr = x_prev + alpha * (z - x_prev)
		v_curr = v_prev + beta * ((z - x_prev) / t)  
		# State Extrapolation Equation, calculate next estimate
		x_next = x_curr + t * v_curr
		v_next = v_curr
		# Store next updated value
		self.estimated_values[step] = x_next
		  
		x_prev = x_next
		v_prev = v_next
		step += STEP
```
`Øvingsoppgave-kalman`

Så da er vi kommet til sakens kjerne, vi skal hovedsaklig se på en alpha-beta-gamma filter som er det jeg endte med å bruke i denne oppgaven. Et slikt filter består av alle elementene fra filterene over som bruker kun alpha og beta, og legger til en ligning med gammaverdi for akselerasjon. Settet  med ligninger som er brukt i min oppgave er som følger:

#### State Update Equations (oppdatering)

$$x_{1}=x_{0}+\alpha(measurement−x_{0})$$

$$velocity_{1}=velocity_{0}+\beta({measurement−x_{0}\over \triangle t})$$

$$acceleration_{1}=acceleration_{0}+ \gamma ({measurement-x_{0}\over0,5\triangle t^2})$$

#### State Extrapolation Equations (finne neste beregning)

$$x_{0}=x_{1,1}+velocity_{1}\triangle t^2+acceleration_{1}{\triangle t^2 \over 2}$$

$$velocity_{0}=velocity_{1}+acceleration_{1}\triangle t^2$$

$$acceleration_{0}=acceleration_{1}$$

***State Update Equation*** (SUE) vil i første iterasjon beregne nåværende beste aproksimasjon for posisjon, fart og akselerasjon basert på initial-betingelser satt av programmerer. Dette kan enten være en kalkulert eller ukalkulert gjetning, eller en kalkulasjon basert på f.eks to første målinger (dersom man har disse, slik som i øvingsoppgave-kalman). I neste iterasjon vil startbetingelsene i SUE være beregnet av de neste tre ligningene, ***State Extrapolate Equations*** (SEE). Disse formlene vil gi en prediksjon på neste startverdi ($x_0$) som SUE bruker i de neste beregningene med neste måling.

Her kan vi også legge merke til, for alle parametere (posisjon, fart og akselerasjon) så vil den nye verdien som legges til/trekkes fra (kommer ann på om verdiene blir positive eller negative) predikeres med enten alpha, beta eller gamma. I motsetning til filterene fra øvingsoppgave-kalman, så settes verdiene nå konstante, slik at hver ny måling vil vektes like mye som den forrige. Nøyaktig hvorfor er jeg usikker på, og det har vært vanskelig å finne noe svar på dette. Ifølge de retningslinjene jeg har funnet så skal alpha settes en plass mellom 0 - 1, beta en hundredel av alpha, og gamma en hundredel av beta. Her var det mye prøving og feiling med verdier, godt hjulpet av Notebooken *test_filter_visualize_results*.  Her endte jeg med å skrive en funksjon som hjalp meg å fintune verdiene, denne testen endte opp med å ta i overkant av 20 timer å kjøre. Jeg legger ved deler av testresultatet lenger ned.

# Koden


```python
class Kalman:
def __init__(
		 self, dt: int = 1,
		 x_0: float = 0, 
		 v_0: float = 0.007, 
		 a_0: float = 0.01, 
		 alpha: float = 2e-2, 
		 beta: float = 8.15e-5, 
		 gamma: float = 2.8e-7
		 ):

self.x_prev = x_0 # Initverdi for posisjon
self.v_prev = v_0 # Initverdi for hastighet
self.a_prev = a_0 # Initverdi for akselerasjon
self.alpha = alpha # Filterparameter for posisjon
self.beta = beta # Filterparameter for hastighet
self.gamma = gamma # Filterparameter for akselerasjon
self.dt = dt # Tidssteg

  
def estimate_current_position_and_velocity(self, zi):
# State Update Equation, calculate current estimate
self.x_curr = self.x_prev + self.alpha * (zi - self.x_prev)
self.v_curr = self.v_prev + self.beta * ((zi - self.x_prev) / self.dt)
self.a_curr = self.a_prev + self.gamma * ((zi - self.x_prev) / (0.5 * self.dt**2))

# State Extrapolation Equation, calculate next estimate
self.x_prev = self.x_curr + self.v_curr * self.dt + self.a_curr * ((self.dt**2) / 2)
self.v_prev = self.v_curr + self.a_curr * self.dt
self.a_prev = self.a_curr

return self.x_curr, self.v_curr

```
Dette er mitt $\alpha - \beta - \gamma$ filter. Initialverdiene er satt til det som kom ut av prøving og feiling, samt fintuning med overnevnte test.


# Problemer med pygame

For å kunne kjøre koden og få et tilstrekkelig godt resultat var det nødvendig med svært mange iterasjoner. Her støtte jeg på et problem. Som du kan se i denne videoen (https://youtu.be/sm0rf7k7VT8) så går simulasjonen svært sakte. Det viste seg å være et problem med mac og pygame generelt, og jeg fant ingen fiks for dette problemet. Løsningen for meg var å fjerne den grafiske delen fra filen *HitTheTarget.py* og kjøre testing kun gjennom terminal. Denne filen er vedlagt og heter *myHitTheTarget.py*.

***!! Det er ingen problem å kjøre filen Kalman.py ned originalfilene som ble levert med oppgaven !!***


# Testing og resultater

Alle tester er kjørt med myHitTheTarget.py slik at jeg fikk et skikkelig sammenligningsgrunnlag. De samme verdiene skal være mulig å oppnå ved bruk av originalkoden til oppgaven (HitTheTarget.py).

De første resultatene før jeg fikk finjusert innstillingene var temmelig dårlige, her er tre udrag fra en rekke tester som bestod av prøving og feiling.:

```zsh
Searching for class Kalman in file Kalman.py...
Found it!

1 | Running iterations..............................................................................
Hit rate after 1000 iterations:
Without filter: 11.1 %
With filter:    9.1 %
Initial values: Position 0 Velocity 0 Acceleration 0
Kalman Gaines: Alpha 0.1 Beta 0.0001 Gamma 1e-07
Time for trial: 0:00:04 
----------------------------------------------------------------------------------------------------
2 | Running iterations..............................................................................
Hit rate after 1000 iterations:
Without filter: 8.3 %
With filter:    55.7 %
Initial values: Position 0 Velocity 0 Acceleration 0
Kalman Gaines: Alpha 0.02 Beta 0.0005 Gamma 5e-07
Time for trial: 0:00:04 
----------------------------------------------------------------------------------------------------
3 | Running iterations..............................................................................
Hit rate after 1000 iterations:
Without filter: 6.0 %
With filter:    87.3 %
Initial values: Position 0 Velocity 0 Acceleration 0
Kalman Gaines: Alpha 0.02 Beta 7e-05 Gamma 2e-07
Time for trial: 0:00:04 
----------------------------------------------------------------------------------------------------
```


Etter, som tidligere nevnt, mye prøving og feiling, kom jeg fram til følgende resultater. Her har jeg i sammarbeid med Konrad og Markus i klassen også tweaket initialbetingelsene for hastighet og akselerasjon. Presisjonen som utvises her er vi ganske fornøyd med.

```zsh
Searching for class Kalman in file Kalman.py...
Found it!

1 | Running iterations..........................................................................
Hit rate after 40000 iterations:
Without filter: 6.3 %
With filter:    94.3 %
Initial values: Position 0 Velocity 0.007 Acceleration 0.01
Kalman Gaines: Alpha 0.02 Beta 8.15e-05 Gamma 2.8e-07
Time for trial: 0:02:51 
----------------------------------------------------------------------------------------------------
```
`Utskrift fra en testkjøring med 40.000 iterasjoner fra myHitTheTarget.py`


Testen med HitTheTarget.py og pygame ser slik ut. Her ser vi noenlunde samme resultater men testen tar lang tid. Disse 100 iterasjonene tok like lang tid som de 40000 i testen over...
```zsh
Hit rate after 100 iterations:
Without filter: 10.0 %
With filter:    90.0 %
Hit rate after 101 iterations:
Without filter: 9.9 %
With filter:    91.1 %
Hit rate after 102 iterations:
Without filter: 9.8 %
With filter:    92.3 %
Hit rate after 103 iterations:
Without filter: 9.7 %
With filter:    90.4 %
```
`Utskrift fra en testkjøring med HitTheTarget.py. Denne kjøringen tok ca like lang tid som den over.`


# Tilslutt, kanskje en liten feil i HitTheTarget.py ??? 

Tilslutt har jeg lyst til å ta med noen som jeg mener er en feil i koden HitTheTarget.py. I "Main game loop" finner du denne koden:
```python
# Check if missile(s) hit
coll = missile.rect.colliderect(target.rect)
if coll:
	reg_score += 1
  
if kalman_implemented:
	k_coll = k_miss.rect.colliderect(target.rect) # kommenter inn denne linjen naar Kalman er implementert
	if k_coll:
		kalman_score += 1

# End trial if missile(s) hit, or missile is sufficiently high up
oob = missile.rect.y < 20
	if oob or coll or (kalman_implemented and k_coll):
	trial = False
```

Dersom den coll (originale prosjektilet) treffer målet én pixel før vår eget kalmanstyrte prosjektil treffer så vil gameloopen avbrytes og kun coll vil få uttelling for treffet. Det er uheldig, for det vil gi et feil bilde av hvor nøyaktig det implementerte kalmanfilteret vil kunne treffe. 

Dersom jeg gjør folgende forandring på linje 227:

```python 
oob = missile.rect.y < 20
	if oob or (kalman_implemented and k_coll):
	trial = False
```

Så vil resultat forbedres kraftig:

```zsh
1 | Running iterations..............................................................................
Hit rate after 1000 iterations:
Without filter: 0.0 %
With filter:    99.8 %
Initial values: Position 0 Velocity 0.007 Acceleration 0.01
Kalman Gaines: Alpha 0.02 Beta 8.15e-5 Gamma 2.8e-07
Time for trial: 0:00:04 
----------------------------------------------------------------------------------------------------
```

Dette vil i min mening være en mer korrekt måling på treffsikkerheten til filteret.



# Finjustering av $\alpha -\beta -\gamma$, egentest.

Som nevnt tidligere så skrev jeg en funksjon for å finjustere kalman-gain. Under ser du et lite udrag av en test som tok i overkant av 20 timer. Totalt testet jeg 410 forskjellige kombinasjoner av $\alpha -\beta -\gamma$ verdier. Høyeste verdi jeg klarte å oppnå var 89.8%. Det ble oppnådd ca 1/3 dels vei inn i testen. Hele output.txt ligger vedlagt. Funksjonen for å kjøre testen ligger i myHitTheTarget.py og heter ***test_different_kalman_gains()***. Denne testen gav meg sikkerheten i at a/b/g-verdiene var til å stole på.

```zsh
% 88.9 | a 2.00e-02 b 8.05e-05 g 3.20e-07 
% 88.7 | a 2.00e-02 b 8.05e-05 g 3.30e-07 
% 88.2 | a 2.00e-02 b 8.05e-05 g 3.40e-07 
% 88.9 | a 2.00e-02 b 8.10e-05 g 2.50e-07 
% 89.7 | a 2.00e-02 b 8.10e-05 g 2.60e-07 
% 89.5 | a 2.00e-02 b 8.10e-05 g 2.70e-07 
% 89.3 | a 2.00e-02 b 8.10e-05 g 2.80e-07 
% 89.6 | a 2.00e-02 b 8.10e-05 g 2.90e-07 
% 89.1 | a 2.00e-02 b 8.10e-05 g 3.00e-07 
% 88.9 | a 2.00e-02 b 8.10e-05 g 3.10e-07 
% 88.5 | a 2.00e-02 b 8.10e-05 g 3.20e-07 
% 88.2 | a 2.00e-02 b 8.10e-05 g 3.30e-07 
% 87.7 | a 2.00e-02 b 8.10e-05 g 3.40e-07 
% 89.7 | a 2.00e-02 b 8.15e-05 g 2.50e-07 
% 89.6 | a 2.00e-02 b 8.15e-05 g 2.60e-07 
% 89.8 | a 2.00e-02 b 8.15e-05 g 2.70e-07 
% 89.8 | a 2.00e-02 b 8.15e-05 g 2.80e-07 
% 89.2 | a 2.00e-02 b 8.15e-05 g 2.90e-07 
% 89.1 | a 2.00e-02 b 8.15e-05 g 3.00e-07 
% 89.0 | a 2.00e-02 b 8.15e-05 g 3.10e-07 
% 88.9 | a 2.00e-02 b 8.15e-05 g 3.20e-07 
% 88.5 | a 2.00e-02 b 8.15e-05 g 3.30e-07 
% 87.6 | a 2.00e-02 b 8.15e-05 g 3.40e-07 
% 89.2 | a 2.00e-02 b 8.20e-05 g 2.50e-07 
% 89.4 | a 2.00e-02 b 8.20e-05 g 2.60e-07 
% 89.7 | a 2.00e-02 b 8.20e-05 g 2.70e-07 
% 89.3 | a 2.00e-02 b 8.20e-05 g 2.80e-07 
% 89.5 | a 2.00e-02 b 8.20e-05 g 2.90e-07 
% 89.2 | a 2.00e-02 b 8.20e-05 g 3.00e-07 
% 88.9 | a 2.00e-02 b 8.20e-05 g 3.10e-07 
% 88.7 | a 2.00e-02 b 8.20e-05 g 3.20e-07 
% 87.9 | a 2.00e-02 b 8.20e-05 g 3.30e-07 
% 87.7 | a 2.00e-02 b 8.20e-05 g 3.40e-07 
% 89.5 | a 2.00e-02 b 8.25e-05 g 2.50e-07 
% 89.5 | a 2.00e-02 b 8.25e-05 g 2.60e-07 
% 89.4 | a 2.00e-02 b 8.25e-05 g 2.70e-07 
```

<hr>
Skrevet av *Anders Lea Karlskås* for *UiT DTE-2602 Maskinlæring og AI* 2022. 