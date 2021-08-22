# Backtesting-stocks

Modelo de backtesting de acciones locales y extranjeras en Django.

Instalar el archivo "requeriments.tx" con el comando pip install -r requirements.txt para tener todas las librerias necesarias. ( recomiendo crear un entorno virtual)
Correr el programa ejecutando el comando "python manage.py runserver" ,el cual nos va a proporcionar una direccion http para poder ingresar a la web(host). 

Pagina de inicio:

El modelo cuenta con 3 apartados: 
* Evaluar estrategia : para correr una de las 3 estrategias (agregaré otras proximamente) y evaluar los resultados para la accion seleccionada.
* Encontrar mejor configuracion: consiste en un bucle sobre la estrategia elegida que nos dara como resultado los mejores seteos para la acccion seleccionada.
* Screener : barre todos los stocks de mercado y arroja las accciones que dan compra segun la estrategia elegida.


![inicio](https://user-images.githubusercontent.com/85622107/130371396-608489f1-067b-419c-beb6-db64622579a2.png)


Pagina para evaluar estrategia:
![Evalua estrategia](https://user-images.githubusercontent.com/85622107/130371345-99c7f00a-6961-47e4-bf71-6f545f74fe5f.png)

El resultado de esta pagina nos dará:
Grafico comparativo de la estrategia vs mantenerla en cartera
![Estrategia Corrida](https://user-images.githubusercontent.com/85622107/130371351-e37b9149-63e8-4f83-84d8-973baf7f13cd.png)
Tabla con todos los movimientos de la estrategia:
![Estrategia Corrida 2](https://user-images.githubusercontent.com/85622107/130371352-9b06d659-c753-46d8-889f-ca71226dbeb3.png)

Pagina para encontrar mejor configuracion:
![Mejores combinaciones](https://user-images.githubusercontent.com/85622107/130371376-0ff90893-df7d-493d-89d3-5ad034863cb3.png)

El resultado nos dara una tabla con las mejores 10 combinaciones ( en caso de que sean mas de 10) y el grafico comparativo entre ellas.
Podremos usar los botones de revisar para entrar en cada estrategia y ver sus movimientos.
![Mejores combinaciones 2](https://user-images.githubusercontent.com/85622107/130371378-1469d3b5-dc2b-44c2-b645-eb6de9fb1028.png)


Pagina Screener:
![screener](https://user-images.githubusercontent.com/85622107/130371445-a3a661f3-f581-4e83-8a7a-233fb3d4cdfe.png)

El resultado del screener nos arroja las acciones a comprar segun la estrategia elegida.
![Resultados Screener](https://user-images.githubusercontent.com/85622107/130371456-e3aa1871-b437-49f2-804d-05a85994fd47.png)
