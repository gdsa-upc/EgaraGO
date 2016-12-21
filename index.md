<font face="Comic Sans MS"> EgaraGO</font>
## Projecte GDSA

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
          </tbody>
        </table>
   
### **EQUIP** 
Som tres estudiants del grau d'Enginyeria de Sistemes Audiovisuals a la Universitat Politècnica de Catalunya :

* PABLO LÓPEZ 
* SERGI NAVARRO 
* ADRIÀ MÁRQUEZ


### **Què És EgaraGo?**

EgaraGo és un projecte basat en un sistema de reconeixement d'imatge que es troba actualment en fase de desenvolupament.
Per ara tenim implementat un ranking segons la semblança de la imatge de consulta amb les de la bases de dades. 

Resultats de la primera prova del ranking :
![foto](https://github.com/gdsa-upc/EgaraGO/blob/gh-pages/images/Pantallazo-2016-12-09%2011-37-16.png?raw=true)

En aquest cas busquem imatges del Castell Cartoixa de Terrassa. La primera imatge, amb un requadre blau, és la imatge que passem al sistema per tal que aquest ens retorni aquelles imatges on detecta el castell. Podem veure que les 4 primeres imatges les retorna com bones de forma correcta. 


### El Mean Average Precision del nostre programa, actualment , és de 0.245. 
Segons la imatge, el resultat és diferent. Podem clasificar-los en la següent gràfica per poder obtenir una millor visualització segons el tipus d'imatge. 

![foto](https://github.com/gdsa-upc/EgaraGO/blob/gh-pages/images/Pantallazo-2016-12-21%2023-13-18.png?raw=true)
