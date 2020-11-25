
function validarNombre() {
    var nom = document.getElementById("txtNombre").value;
    if (nom.length >= 3 && nom.length <= 80) {
        return true;
    } else {
        alert("Largo del nombre debe estar entre 3 y 80");
        return false;
    }
}
function validarApellido() {
    var ape = document.getElementById("txtapellido").value;
    if (ape.length >= 3 && ape.length <= 80) {
        return true;
    } else {
        alert("Largo del apellido debe estar entre 8 y 80");
        return false;
    }
}


function validarNombreUsuario() {
    var nombusuario = document.getElementById("txtNombreusuario").value;
    if (nombusuario.length >= 8) {
        return true;
    } else {
        alert("El nombre de usuario debe tener 8 caracteres como mínimo");
        return false;
    }
}
function validarContraseña() {
    var contra = document.getElementById("txtPass").value;
    if (contra.length >= 8) {
        return true;
    } else {
        alert("La contraseña debe tener como mínimo 8 caracteres");
        return false;
    }
}

function validarcliente(){
    
    resp =validarNombre();
    if (resp == false) {
        return false;
    }
    resp =  validarApellido();
    if (resp == false) {
        return false;
    }
    
    resp = validarNombreUsuario();
    if (resp == false) {
        return false;
    }
    resp = validarContraseña();
    if (resp == false) {
        return false;
    }
}