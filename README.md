# heladeria_odoo


## English

This module is intended for the world of cuisine, namely, for ice cream shops. Its aim is to allow the user to manage all their own recipes, establishing -among other things- the creator of the recipe, modify those recipes that were previously created, their state of developement and, of course, the recipe itself with its steps.

## Galego
Este módulo está dirixido á hostalería, máis concretamente, a unha xeladería. O obxectivo do mesmo é permitir levar o control dunha serie de receitas de xeados, establecendo entre outras cousas o seu creador, o seu estado de desenvolvemento, e por suposto, a propia receita.
A interface é sinxela e está orientada a permitir dar de alta novas receitas, modificar as xa feitas e ter unha visión xeral de todas as receitas que se seguen na xeladería.

## Interface e funcionamento.

O módulo consta dun menú que (a través dos submenús, se é necesario) nos permite acceder ás dúas entidades/modelos básicos: Produtos e Reposteiros. 

### Manexando produtos
En Produtos podemos dar de alta recetas de novos xeados e sorbetes. Pódese dar de alta un xeado ou un sorbete accedendo ás vistas a través do submenú correspondente.
Os formularios de alta permiten indicar uns determinados campos, establecendo certos controis sobre os mesmos -por exemplo, non se poden dar de alta certas recetas que violen certas normas establecidas sobre a elaboración de xeados. 

O obxectivo principal e levar unha "contabilidade" ou control da elaboración de recetas, por elo, cóllese a data de alta da receita, ou seu estado de desenvolvemento (experimental, lista para producir...) e o autor da mesma. 
Estes campos logo utilízanse nas diferetens vistas. 
Ademáis das vistas tipo tree e tipo form (a visualización básica), temos acceso áavistas tipo Calendar. Estas vistas dannos unha visual de cal é o ritmo de desarrollo de receitas. Por outra banda, os sorbetes conteñen moitas veces ingredientes que poden resultar alérxicos. Nunha vista tipo kanban podemos ver cales conteñen alérxenos coñecidos e cales non. 

### Manexando reposteiros.
 Os resposteiros son ao autores das receitas. A información recollida sobre os mesmos é menor, en tanto que neste módulo so nos interesa saber quenes son para poder levar unha contabilidade/historial das receitas. 
Conta coas vistas de tipo tree e tipo form que permiten tanto ver dun vistazo todos os respoteiros da empresa, como un formulario onde se poden engadir novos reposteiros. Dende este formulario pódense engadir novos liñas de de produto asociadas a cada reposteiro, e saber cales destes produtos realizou cada un.
