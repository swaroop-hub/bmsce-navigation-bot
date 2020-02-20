var x=null;
var x0=null;
var v=null;
var t=null;

function FuncionParaX() {
  if (x0===null || v===null || t===null) {
    window.x = document.getElementById("main").value;
    document.getElementById("px").innerHTML = x;
  }else{
    window.fin = parseFloat(x0)+parseFloat(v)*parseFloat(t);
    document.getElementById("px").innerHTML = fin;
    document.getElementById("main").innerHTML = fin;
  }
}

function FuncionParaX0(){
  if (x===null || v===null || t===null) {
    window.x0 = document.getElementById("main").value;
    document.getElementById("px0").innerHTML = x0;
  }else{
    window.fin = parseFloat(x)-parseFloat(v)*parseFloat(t);
    document.getElementById("px0").innerHTML = fin;
    document.getElementById("main").innerHTML = fin;
  }
}

function FuncionParaV(){
  if (x===null || x0===null || t===null) {
    window.v = document.getElementById("main").value;
    document.getElementById("pv").innerHTML = v;
  }else{
    window.fin = (parseFloat(x)-parseFloat(x0))/parseFloat(t);
    document.getElementById("pv").innerHTML = fin;
    document.getElementById("main").innerHTML = fin;
  }
}

function FuncionParaT(){
  if (x===null || v===null || x0===null) {
    window.t = document.getElementById("main").value;
    document.getElementById("pt").innerHTML = t;
  }else{
    window.fin = (parseFloat(x)-parseFloat(x0))/parseFloat(v);
    document.getElementById("pt").innerHTML = fin;
    document.getElementById("main").innerHTML = fin;
  }
}

function Borrar(){
  var x=null;
  var x0=null;
  var v=null;
  var t=null;
  document.getElementById("px").innerHTML = x;
  document.getElementById("px0").innerHTML = x0;
  document.getElementById("pv").innerHTML = v;
  document.getElementById("pt").innerHTML = t;
  
}