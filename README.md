# OOPZ4
Proyecto Integrador 2022 - Proyecto Gama

# Integrantes 
Olivera, Daiana
Ortiz, Oscar
Paz, F. Gabriel
Zorrilla, Juan Pedro

La siguiente aplicación fue realizada para extraer **diariamente** datos económicos de
distintas fuentes utilizando la practica conocida como **web scraping**
,con el fin de ser utilizados posteriormente para hacer reportes.

#  Sitios utilizados como fuentes de datos:
* [Banco Nacion](https://www.bna.com.ar/Personas) y [Rofex](https://www.matbarofex.com.ar/) : Se hace web scraping para obtener datos del Banco Nación y Rofex, obteniendo la cotización del dólar mayorista para el primer caso y la cotización del mes actual y 4 meses posteriores al corriente para el segundo, luego se agregan los valores a la base de datos.
* [Bloomberg](https://www.bloomberg.com) : El script que realiza el scraping obtiene los datos de Bloomberg, obteniendo la cotización de:
  * WTI NYMEX M+1 USS/bbl y change
  * BRENT NYMEX M+2 USD/bbl y change 
  * RBOB87 M+1 cpg y change
  * Heating Oil M+1 cpg y change
* [CME Group](https://www.cmegroup.com/) :  El siguiente script hará web scraping para obtener datos de CME, obteniendo la cotización de:
  * Dated Brent USD/bbl  
  * ICE Brent USD/bbl 
  * WTI USD/bbl
  * RBOB87 USD/gal
  * Heating Oil USD/gal 
  * Jet54 USGC USD/Gal
  * FO NY USD/bbl
  * Propane OPIS USD/Gal
  * Butane OPIS USD/Gal
  * Naphtha CIF NWE USD/Tn
para cada uno traerá los datos ‘Last’ en caso que exista, de no ser así, tomará el dato ‘Prior Settle’ desde M hasta M+5, es decir, el mes corriente y los 5 meses posteriores al mismo. Los mismos serán almacenados en la base de datos de MySQL.

# Configuraciones iniciales: 
### Configurar el entorno virtual de Python 3
Windows / Linux:
```bash
1) $ python -m venv venv
2) $ cd venv\Scripts & .\activate
3) $ cd .. & cd .. & pip install -r requirements.txt
```
### Correr el Script
```bash
4) $ python main.py
```
### Iniciar sesión con una cuenta asociada para la escritura del spreadsheat de Google
La primera vez que se ejecuta la aplicación se generará un token de uso local asociado a la cuenta con la que se enviará la información al spreadsheet indicado para la visualización de datos. Previamente se debe solicitar asociar la cuenta personal de Google a la API o, en su defecto, solicitar la cuenta de servicio.

# Arquitectura de la API:
