# 15.01.2025 - Prima settimana
## Loris Bazzuri
Oggi abbiamo capito come runnare app.py con streamlit, ovvero bisogna fare quest'operazione: python -m streamlit run app.py.
Andando piu nel preciso nel nostro progetto noi abbiamo deciso di creare il gioco di carta Briscola, pertanto abbiamo dovuto scaricare nuove immagini per le carte napoletane da wikipedia (faccia e retro), poi abbiamo dovuto modificare l'oggetto carte( class card) e adattarlo con i rank e i suit (ovvero i nomi dei semi e i valori) delle carte napoletane e in più abbiamo aggiunto la possibilita che ci siano delle carte girate (ovvero che si vede il retro).
Inoltre stiamo cercando di creare la definizione per inizializzare il gioco, quindi riuscire a dare 3 carte per giocatore e poi aggiungere la carta briscola sotto il mazzo, una volta che riusciremo a fare in modo che dopo aver dato le carte esse vengono eliminate dal mazzo creeremo un' altra funzione che serve per continuare il gioco (ovvero pescare la carta dal mazzo e giocarne una), anche se per ora non funziona.
# 22.01.2025 - Seconda settimana
## Filippo De Vito
Oggi abbiamo creato le funzioni per cominciare a giocare, starting_hand() che da 3 carte ad un giocatore (danone una a testa) e backseventh() che mette la settimana in fondo al mazzo. Abbiamo anche cominciato a creare il file dove poter realmente giocare a briscola, anche se non ancora neanche lontanamente funzionale (game.py). Abbiamo invece deciso di usare app.py per motivi di debugging (ad esempio testare le funzioni avendo il mazzo completamente visibile e in ordine).
# 29.01.2025 - Terza settimana 
## Loris Bazzuri
Oggi abbiamo deciso di far diventare il game un oggetto (diventando una class Game), riportando dunque l' app.py come file principale. Per evitare problemi futuri abbiamo inoltre creato un file di debug (debug.py) per il nostro file principale. In seguito oggi abbiamo anche creato un oggetto table (class Table) in cui ho iniziato a creare le regolette del gioco quando si buttano delle carte (quando ci sono delle carte attive): regole come chi vince la mano in base alla carta giocata, e poi che il vincitore della mano prenda le carte. E stiamo poi lavorando a una funzione che giri le carte.
## Filippo De Vito
In seguito migliorata la grafica quando si gioca senza guardare ancora però la logica dietro al gioco (Commit: Update Grafico).
# 05.02.2025 - Quarta settimana
## Filippo De Vito
Oggi abbiamo lavorato alla logica dietro alla vittoria tra due carte diverse (nel table). Anche se non è ancora stata nè testata, nè collegata alla classe game e dunque alla visualizzazione grafica di questa.
Abbiamo creato una funzione per calcolare il punteggio finale di un player (points_sum) grazie ad una variabile delle carte (points) utilizzata anche per determinare la "forza" della carta (ossia, su chi vince, e su chi perde).