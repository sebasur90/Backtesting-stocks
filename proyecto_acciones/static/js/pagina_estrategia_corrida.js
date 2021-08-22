
const accion_evaluada_sin_parsear = JSON.parse(document.getElementById('accion_evaluada').textContent);
const momento_compra_sin_parsear = JSON.parse(document.getElementById('momento_compra').textContent);
const momento_venta_sin_parsear = JSON.parse(document.getElementById('momento_venta').textContent);
const nombre_completo_accion = document.getElementById('nombre_completo_accion').textContent;
const accion = (JSON.parse(accion_evaluada_sin_parsear))
const momento_compra = (JSON.parse(momento_compra_sin_parsear))
const momento_venta = (JSON.parse(momento_venta_sin_parsear))


console.log(accion)

var datos_close = []
var ohlc = []
var volume = []
var buy_hold = []
var capital_estrategia = []

for (let indice = 0; indice < accion.length; indice++) {
  var lista_ohlc = []
  var lista_vol = []
  var lista_buy_hld = []
  var lista_capital_estrategia = []
  var lista_datos_close = []
  lista_datos_close.push(accion[indice].Date)
  lista_ohlc.push(accion[indice].Date)
  lista_vol.push(accion[indice].Date)
  lista_buy_hld.push(accion[indice].Date)
  lista_capital_estrategia.push(accion[indice].Date)
  lista_ohlc.push(accion[indice].Open)
  lista_ohlc.push(accion[indice].High)
  lista_ohlc.push(accion[indice].Low)
  lista_ohlc.push(accion[indice].Close)
  lista_datos_close.push(accion[indice].Close)
  lista_vol.push(accion[indice].Volume)
  lista_buy_hld.push(accion[indice].Buy_and_Hold)
  lista_capital_estrategia.push(accion[indice].capital_estrategia)
  ohlc.push(lista_ohlc)
  volume.push(lista_vol)
  buy_hold.push(lista_buy_hld)
  capital_estrategia.push(lista_capital_estrategia)
  datos_close.push(lista_datos_close)
}
var buy_hold_y_estrategia = [buy_hold, capital_estrategia]
buy_hold_y_estrategia.push(buy_hold)
buy_hold_y_estrategia.push(capital_estrategia)




var fecha_momentos_venta = []
var momentos_venta = []
for (let indice = 0; indice < momento_venta.length; indice++) {
  var lista = []
  fecha_momentos_venta.push({ 'x': momento_venta[indice].Date, 'title': 'V', text: 'Shape: "Venta"' })
  lista.push(accion[indice].Date)
  lista.push(accion[indice].Close)
  momentos_venta.push(lista)
}

var fecha_momentos_compra = []
var momentos_compra = []
for (let indice = 0; indice < momento_compra.length; indice++) {
  var lista = []
  fecha_momentos_compra.push({ 'x': momento_compra[indice].Date, 'title': 'C', text: 'Shape: "Compra"' })
  lista.push(accion[indice].Date)
  lista.push(accion[indice].Close)
  momentos_compra.push(lista)
}



var seriesOptions = [],
  seriesCounter = 0,
  names = ['Buy_hold', 'Estrategia'];

/**
 * Create the chart when all data is loaded
 * @returns {undefined}
 */
function createChart() {

  Highcharts.stockChart('container', {


    title: {
      text: "Estrategia VS Buy and Hold"
    },

    yAxis: {
      labels: {
        formatter: function () {
          return (this.value > 0 ? ' + ' : '') + this.value + '%';
        }
      },
      plotLines: [{
        value: 0,
        width: 2,
        color: 'silver'
      }]
    },

    plotOptions: {
      series: {
        compare: 'percent',
        showInNavigator: true
      }
    },

    tooltip: {
      pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> ({point.change}%)<br/>',
      valueDecimals: 2,
      split: true
    },

    series: seriesOptions
  });
}

function success(buy_hold_y_estrategia) {

  seriesOptions[0] = {
    name: names[0],
    data: buy_hold
  };
  seriesOptions[1] = {
    name: names[1],
    data: capital_estrategia
  };

  createChart()
}
success()






Highcharts.stockChart('container3', {
  title: {
    text: "Puntos de compras y ventas"
  },

  yAxis: [{
    labels: {
      align: 'left'
    },
    height: '80%',
    resize: {
      enabled: true
    }
  }, {
    labels: {
      align: 'left'
    },
    top: '80%',
    height: '20%',
    offset: 0
  }],
  tooltip: {
    shape: 'square',
    headerShape: 'callout',
    borderWidth: 0,
    shadow: false,
    positioner: function (width, height, point) {
      var chart = this.chart,
        position;

      if (point.isHeader) {
        position = {
          x: Math.max(
            // Left side limit
            chart.plotLeft,
            Math.min(
              point.plotX + chart.plotLeft - width / 2,
              // Right side limit
              chart.chartWidth - width - chart.marginRight
            )
          ),
          y: point.plotY
        };
      } else {
        position = {
          x: point.series.chart.plotLeft,
          y: point.series.yAxis.top - chart.plotTop
        };
      }

      return position;
    }
  },
  series: [{
    type: 'candlestick',
    id: 'ohlc',
    name: 'Precio',
    data: ohlc
  }, {
    type: 'column',
    id: 'volume',
    name: 'Volume',
    data: volume,
    yAxis: 1
  },
  {
    type: 'flags',
    data: fecha_momentos_venta,
    onSeries: ohlc
  },
  {
    type: 'flags',
    data: fecha_momentos_compra,
    onSeries: ohlc
  }],
  responsive: {
    rules: [{
      condition: {
        maxWidth: 800
      },
      chartOptions: {
        rangeSelector: {
          inputEnabled: false
        }
      }
    }]
  }
});


var titulos_tabla = ['Date', 'Open', 'Low', 'High', 'Close', 'Volume', 'Trade', 'Posicion', 'Buy_and_Hold', 'capital_estrategia']




function tableCreate() {
  var body = document.getElementById('div_tabla'),
    tbl = document.createElement('table');
  tbl.style.width = '100px';
  tbl.style.border = '1px solid black';

  var thead = document.createElement('thead');
  tbl.appendChild(thead);
  for (var i = 0; i < titulos_tabla.length; i++) {
    thead.appendChild(document.createElement("th")).
      appendChild(document.createTextNode(titulos_tabla[i]));

  }
  for (let indice in accion) {

    var tr = tbl.insertRow();

    var td = tr.insertCell();
    var date = new Date(accion[indice].Date);
    var now_utc = date.toISOString()
    td.appendChild(document.createTextNode(now_utc));
    td.style.border = '1px solid black';
    var td = tr.insertCell();
    td.appendChild(document.createTextNode((accion[indice].Open).toFixed(2)));
    td.style.border = '1px solid black';
    var td = tr.insertCell();
    td.appendChild(document.createTextNode((accion[indice].Low).toFixed(2)));
    td.style.border = '1px solid black';
    var td = tr.insertCell();
    td.appendChild(document.createTextNode((accion[indice].High).toFixed(2)));
    td.style.border = '1px solid black';
    var td = tr.insertCell();
    td.appendChild(document.createTextNode((accion[indice].Close).toFixed(2)));
    td.style.border = '1px solid black';
    var td = tr.insertCell();
    td.appendChild(document.createTextNode(accion[indice].Volume));
    td.style.border = '1px solid black';
    var td = tr.insertCell();
    td.appendChild(document.createTextNode(accion[indice].Trade));
    td.style.border = '1px solid black';
    var td = tr.insertCell();
    td.appendChild(document.createTextNode(accion[indice].Posicion));
    td.style.border = '1px solid black';
    var td = tr.insertCell();
    td.appendChild(document.createTextNode((accion[indice].Buy_and_Hold)));
    td.style.border = '1px solid black';
    var td = tr.insertCell();
    td.appendChild(document.createTextNode((accion[indice].capital_estrategia).toFixed(2)));
    td.style.border = '1px solid black';



  }
  body.appendChild(tbl);
}
tableCreate();
