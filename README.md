# 🎲 Juego de Azar en Python

Este es un sencillo juego de azar desarrollado en Python, en el que el jugador debe adivinar 3 números seleccionados al azar por el sistema. Perfecto como ejercicio educativo o para mejorar habilidades básicas de programación.

---

## 📝 Instrucciones

1. El jugador selecciona 3 números distintos del 1 al 21.
2. El sistema también selecciona 3 números aleatorios dentro del mismo rango.
3. Si el jugador acierta los 3 números del sistema, ¡gana la partida!

---

## 🚀 Cómo ejecutar

1. Clona este repositorio o copia el archivo en tu entorno local.
2. Ejecuta el archivo en una terminal con Python 3:
   ```bash
   python juego_azar.py


- Sigue las instrucciones en pantalla para jugar.

🧠 Lógica del juego
- Se utiliza random.sample() para seleccionar números aleatorios sin repetición.
- Se compara la selección del jugador con la del sistema utilizando conjuntos (set) para detectar coincidencias.
- Se maneja entrada inválida y se previene la repetición de números por parte del jugador.

📦 Requisitos
- Python 3.7+
- No requiere librerías externas

💡 Ideas de mejora
- Contador de intentos o historial de partidas
- Sistema de puntuación o clasificación
- Interfaz gráfica con tkinter o pygame
- Asociación lógica entre números y desafíos educativos

📁 Autor
Desarrollado por Luis Enrique Díaz Huenulef
Especialista en soporte técnico y programación educativa.

📜 Licencia
Este proyecto puede adaptarse y reutilizarse libremente con fines educativos y personales. Créditos al autor son bienvenidos.
