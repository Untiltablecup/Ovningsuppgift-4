def lönen(hur_många_kronor): #Definerar functionen lönen och tar in en parameter som heter hur_många_kronor
    ett_öre = 1  #Ger variablen ett_öre värdet 1
    öre_till_krona = ett_öre/100  #Görom ett_öre till kronor
    dagar = 1  #Ger variablen dagar värdet 1
    while öre_till_krona < hur_många_kronor:  #Gör så att så länge som lönen inte har nått 10miljoner kr så lopar den
        öre_till_krona = öre_till_krona * 2  #Räknar ut den nya lönen för varje dag
        dagar += 1  #Räknar varje dag till lönen blir 10miljoner kr
    return"Det tar " +str(dagar)+ " dagar för att lönen ska bli 10miljoner kr!"  #Den returnerar en sträng som talar om hur många dagar det tar för lönen att bli 10miljoner kr
print(lönen(10000000))  #Den anropar funtionen lönen och skriver ut resultatet