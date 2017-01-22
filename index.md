

<H1>EgaraGO</H1>

Benvinguts a la pàgina web del nostre projecte !
Aquí trobareu informació sobre el seu desenvolupament.

***

***  

<table> 
        <thead>
        <tr>
              <th BGCOLOR="#01DFA5">Progress Report (Slides)</th>
              <th BGCOLOR="#01DFA5">Demo ( Notebook )</th>
           </tr>
           </thead>
           <tbody >
           <tr>
              <td><a href="https://docs.google.com/presentation/d/1UeMRaRQHtqzRAGYTKyew4l1ZVFne8FykBzHa77rgHTE/edit#slide=id.p" > Sessio 3</a> </td>
              <td> <a href= "https://github.com/gdsa-upc/EgaraGO/blob/master/Sessio3/PrimerScript.ipynb2"> Feature extractor</a> </td>
          </tr>
          <tr>
              <td><a href="https://docs.google.com/presentation/d/1FElw3wB09kewor5mdKbvPPm-bbtXHXuGJ7aZfIRPLeA/edit#slide=id.g19dadb106c_0_59" > Sessio 4</a></td>
              <td> <a href="https://github.com/gdsa-upc/EgaraGO/tree/master/Sessio4" >Random system </a></td>
          </tr>
          <tr>
              <td><a href="https://docs.google.com/presentation/d/1fBsOT1efNTmQegLOExFy2-xjiymivh_vvsCnBiclJPw/edit#slide=id.g1a029ee159_2_22" > Sessió 5 </a></td>
              <td> <a href="https://github.com/gdsa-upc/EgaraGO/blob/master/Sessio5/sesion5.ipynb">First search engine</a></td>
          </tr>
          <tr>
              <td><a href="https://docs.google.com/presentation/d/1kPW7dIn1MHWKluWvtV3_aR2NJTlmm2-AdDa4cySGnJ0/edit#slide=id.p" > Sessio 6</a> </td>
              <td> <a href= "https://github.com/gdsa-upc/EgaraGO/blob/master/Sessio6/Ranking.ipynb"> Ranking</a> </td>
          </tr>
           <tr>
              <td><a href=" " > Presentació Final</a> </td>
              </tr>
          </tbody>
        </table>
   
### **EQUIP** 
Som tres estudiants del grau d'Enginyeria de Sistemes Audiovisuals a la Universitat Politècnica de Catalunya :

* PABLO LÓPEZ 
* SERGI NAVARRO 
* ADRIÀ MÁRQUEZ


### **Què És EgaraGo?**

<strong>*EgaraGo*</strong> és un projecte basat en un sistema de reconeixement d'imatge que es troba actualment en fase de desenvolupament.
Per ara tenim implementat un ranking segons la semblança de la imatge de consulta amb les de la bases de dades. 

Resultats de la primera prova del ranking :
![foto](https://github.com/gdsa-upc/EgaraGO/blob/gh-pages/images/Pantallazo-2016-12-09%2011-37-16.png?raw=true)

En aquest cas busquem imatges del Castell Cartoixa de Terrassa. La primera imatge, amb un requadre blau, és la imatge que passem al sistema per tal que aquest ens retorni aquelles imatges on detecta el castell. Podem veure que les 4 primeres imatges les retorna com bones de forma correcta. 


### **El Mean Average Precision del nostre programa *(a Desembre de 2016)* era de 0.245.** 
Segons la imatge, el resultat és diferent. Podem clasificar-los en la següent gràfica per poder obtenir una millor visualització segons el tipus d'imatge. 

![foto](https://github.com/gdsa-upc/EgaraGO/blob/gh-pages/images/Pantallazo-2016-12-21%2023-13-18.png?raw=true)


### **Kaggle** 
Pel que fa la competició a nivell de classe, es porta a terme a travès del Kaggle . 
Aquest és el resultat de la primera prova amb <strong>11000 clusters i rootsift</strong> :

![foto](https://github.com/gdsa-upc/EgaraGO/blob/gh-pages/images/Pantallazo-2017-01-21%2022-37-03.png?raw=true)



I aquest el segon, amb <strong>11500 clusters</strong>:

![foto](https://github.com/gdsa-upc/EgaraGO/blob/gh-pages/images/Pantallazo-2017-01-21%2022-57-19.png?raw=true)


Com no ha millorat el resultat anterior el Kaggle guarda el MAP de la primera prova i descarta aquest. 


El tercer intent ha estat realitzat amb <strong>12000 clusters</strong> , cosa que ha millorat substancialment el resultat: 
![foto](https://github.com/gdsa-upc/EgaraGO/blob/gh-pages/images/Pantallazo-2017-01-22%2019-27-12.png?raw=true)


Com podem veure, arribem gairebé a un <strong>MAP de 0.28 *(0.278)*</strong> , un resultat bastant positiu. 

