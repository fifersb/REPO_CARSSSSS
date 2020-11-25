function validadFormu(){

    var validad_el_rute=  validaRut();

    if (validad_el_rute) {
        
    }



}

function validaRut(){
   var rut=document.getElementById("txtRut").value;
 //  alert("El rut:"+rut);
   if (rut.length!=10) {
       alert("rut incompleto");
       return false;
   }
    //proceso de validacion de rut
var  suma=0;
var num=3;
for (let index = 0; index < 8; index++) {
   var car= rut.slice(index, index + 1);
   alert(car);
   suma = suma+(car*num);
   num = num - 1;
   if(num == 1){
       num = 7;
   }
}

var resto =  suma % 11;
var dv = 11 - resto;

if (dv<10) {
 
    
} else {
    if (dv==10) {
        dv='K';
    }else {
        dv='0';
    }
}
//alert("dv:"+ dv);
var dv_usuario=rut.slice(-1).toUpperCase();
// alert("Digito del usu:"+dv_usuario);
if (dv!=dv_usuario) {
    alert("Digito Verificador incorrecto");
    return false;
}else{
    alert("rut valido");
    return true;
}


}