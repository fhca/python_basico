encabezados = "Universidad Autónoma de la Ciudad de México"
destinatario = "Comité de Becas"
fecha = "1 de mayo de 2020"
remitente = "Evaristo Galois"
adscripcion = "Estudiante de la Maestría en Ciencias de la Complejidad"

contenido = """
Por este medio le solicito su atención  para el  problema surgido por la contin-
gencia en que estamos actualmente.

El Comité de Becas nos está solicitando entregar los comprobantes de estudio du-
rante este período pero  las oficinas de la UACM  se encuentran cerradas, por lo
que ponemos  a  su consideración el que  se nos acepte un justificante elaborado
por nosotros, y copia electrónica de  el  aval  de los  profesores con que hemos
tomado curso en este período, con el  compromiso de que regresando de la contin-
gencia  entreguemos  un justificante  oficial,  tan pronto  las  oficinas  estén
abiertas.    

Sin otro particular, reciban un cordial saludo."""


carta = f"""
{encabezados:^80}

{"Ciudad de México a "+fecha:>80}
Honorable {destinatario}

{contenido:>80}

Atte.
{remitente:^80}
{adscripcion:^80}
"""

print(carta)


# la justificación de ambos bordes, al parecer se sale de lo que las f-strings pueden hacer
# nos queda pendiente buscar si una biblioteca de Python puede hacer tales justificaciones
# o por lo menos, buscar una biblioteca que pueda pasar el texto a "formateadores" como el LaTeX.
