function validarNomInsumo(){
    var nominsumo = document.getElementById("txtNombreInsumo").value;
    if (nominsumo.length >= 3 && nominsumo.length <= 120) {
        return true;
    } else {
        alert("Largo del nombre del insumo debe estar entre 3 y 120");
        return false;
    }
}

function validarPreInsumo(){
    var precioinsumo = document.getElementById("txtPrecio").value;
    if (precioinsumo>=1) {
        return true;
    } else {
        alert("El precio mínimo del insumo es de 1 peso");
        return false;
    }
}

function validarDes(){
    var des = document.getElementById("txtDescripcion").value;
    if(des.length>0){
    if (des.length >= 3 && des.length <=200) {
        return true;
    } else {
        alert("El Largo de la descripción debe estar entre 3 y 200");
        return false;
    }
    }
    else{
        return true;
    }
}

function validarStock(){
    var stock = document.getElementById("txtstock").value;
    if (precioinsumo>=0) {
        return true;
    } else {
        alert("Debe completar este campo");
        return false;
    }
}

function validarInsumo() {
    var resp;
    resp = validarNomInsumo();
    if (resp == false) {
        
        return false;
    }
    resp = validarPreInsumo();
    if (resp == false) {
        return false;
    }
    resp = validarDes();
    if (resp == false) {

        return false;
    }
    resp = validarStock();
    if (resp == false) {
        return false;
    }

}