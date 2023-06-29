<?php
// PHP é case sensitive, logo diferencia letras maiusculas de minusculas.
define("CONSTANTE", "Olá Mundo.");
echo CONSTANTE; // imprime "Olá Mundo."
echo Constante; // Lança um erro Error: Undefined constant "Constante"
echo "Olá a todos." 

?>