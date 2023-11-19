from flask import Flask, render_template, request

app = Flask(__name__)

# Lista para almacenar la información de los números
notas = []
nombres = []


# Ruta principal que muestra ambas páginas
@app.route('/')
def mostrar_pagina_principal():
    return render_template('pagina_principal.html', resultado=None, Nombre_mas_largo=None, Largo_nombre_mas_largo=None)

# Ruta para procesar el promedio
@app.route('/procesar_promedio', methods=['POST'])
def procesar_promedio():
    try:
        nota1 = int(request.form.get('nota1'))
        nota2 = int(request.form.get('nota2'))
        nota3 = int(request.form.get('nota3'))
        asistencia = int(request.form.get('asistencia'))

        # Agregar los números a la lista
        notas.extend([nota1, nota2, nota3])

        porcentaje_asistencia = 0 

        # Calcular el promedio solo si hay notas en la lista
        if notas:
            suma_notas = sum(notas)
            cantidad_elementos = len(notas)
            promedio = suma_notas / cantidad_elementos

            if 75 <= asistencia <= 100:
                porcentaje_asistencia += 1
            elif 0 <= asistencia <= 74:
                porcentaje_asistencia += 0
            elif asistencia < 0:
                porcentaje_asistencia += 0
            else:
                print("Valor incorrecto")

            # Lógica para determinar si está aprobado o no
            if promedio >= 40 and porcentaje_asistencia:
                resultado = 'Aprobado'
            else:
                resultado = 'Reprobado'

            return render_template("pagina_promedio.html", resultado=resultado)

    except ValueError:
        return "Error: Ingresa números enteros."



        return render_template("pagina_promedio.html", resultado=resultado)
    except ValueError:
        return "Error: Ingresa números enteros."
    
    
    
    
    
    
    

# Ruta para procesar nombres
@app.route('/procesar_nombres', methods=['POST'])
def procesar_nombres():
    try:
        nombre1 = request.form.get("nombre1")
        nombre2 = request.form.get("nombre2")
        nombre3 = request.form.get("nombre3")

        # Agregar los nombres a la lista
        nombres.extend([nombre1, nombre2, nombre3])

        # Lógica para evaluar nombres
        nombre_mas_largo = max(nombres, key=len)

        largo_nombre_mas_largo = len(nombre_mas_largo)

        return render_template("pagina_nombres.html", Nombre_mas_largo=nombre_mas_largo, Largo_nombre_mas_largo=largo_nombre_mas_largo)

    except ValueError:
        return "Error: Ingresa un nombre."

# Rutas adicionales para mostrar los formularios de promedios y nombres
@app.route('/mostrar_pagina_promedio')
def mostrar_pagina_promedio():
    return render_template('pagina_promedio.html')

@app.route('/mostrar_pagina_nombres')
def mostrar_pagina_nombres():
    return render_template('pagina_nombres.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
