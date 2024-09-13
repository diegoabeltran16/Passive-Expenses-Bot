# Cronograma

## Plan de desarrollo
Estructuraremos el desarrollo en ciclos de bloques de programación por prerrequisitos, avanzando de lo más simple a lo más complejo. Cada ciclo se desarrollará en una rama Git independiente, asegurando que cada fase de prueba de forma independiente antes de fusionarse en la rama principal. Este enfoque facilitará la integración continua, las mejoras incrementales y un bot robusto, escalable y fácil de usar.

### Ciclo 1: Configuración básica y características iniciales (20 Dias)
- Nombre de la rama: cycle-1-basic-setup
- Objetivos:
  - Configurar la estructura básica del proyecto.
  - Implementar el manejo básico de comandos.
  - Establecer la base de datos SQLite y las operaciones CRUD.
  - Integrar soporte multilingüe básico.

- Tareas:
  - Configuración del proyecto:
    - Crear la estructura de directorios del proyecto.
    - Inicializar repositorio Git.
    - Configurar requirements.txt con las librerías necesarias (discord.py, sqlite3).
  - Manejo básico de comandos:
    - Crear un bot de Discord.
    - Implementar comando básico para probar la conectividad (por ejemplo, !ping).
  - Configuración de la base de datos:
    - Diseñar el esquema de la base de datos para almacenar los gastos y las preferencias de los usuarios.
    - Implementar operaciones CRUD.
  - Configuración multilingüe:
    - Integrar soporte inicial para inglés y español en comandos básicos.

### Ciclo 2: Manipulación mejorada de comandos e interacción con el usuario (20 Dias)
- Nombre de la rama: cycle-2-enhanced-commands
- Objetivos:
  - Ampliar el manejo de comandos para incluir comandos de alias y procesamiento de lenguaje natural (NLP).
  - Desarrollar el módulo de incorporación para nuevos usuarios.
  - Implementar el flujo de interacción con el usuario con soporte multilingüe.

- Tareas:
  - Ampliación del gestor de comandos:
    - Implementar la resolución de alias para comandos.
    - Integrar el módulo NLP para procesar entradas de lenguaje natural tanto en inglés como en español.
  - Módulo de incorporación:
    - Desarrollar un proceso de incorporación interactivo que guíe a los nuevos usuarios a través de la configuración.
    - Asegúrese de que el proceso de incorporación sea compatible con varios idiomas.
  - Flujo de interacción con el usuario:
    - Diseñar e implementar un flujo de interacción intuitivo para registrar gastos, establecer presupuestos y comprobar resúmenes.

### Ciclo 3: Informes y gestión de datos (20 Dias)
- Nombre de la rama: cycle-3-reporting-data
- Objetivos:
  - Implementar el módulo de informes para generar resúmenes de gastos.
  - Desarrollar funciones de gestión de datos, incluidas la copia de seguridad y la exportación.
  - Ampliar las pruebas para incluir soporte multilingüe y funciones interactivas.

- Tareas:
  - Módulo de informes:
    - Desarrollar la funcionalidad para generar resúmenes mensuales por categoría.
    - Garantizar que los informes se generen en el idioma preferido del usuario.
  - Gestión de datos:
    - Implementar rutinas de copia de seguridad de datos.
    - Desarrollar la función de exportación de datos a CSV.
  - Ampliación de las pruebas:
    - Ampliar el conjunto de pruebas para cubrir las nuevas funciones, garantizando la fiabilidad tanto en inglés como en español.

### Ciclo 4: Funciones avanzadas e integración final (20 Dias)
- Nombre de la rama: cycle-4-advanced-integration
- Objetivos:
  - Implementar funciones avanzadas, incluida la gestión de presupuestos y la limpieza automatizada de datos.
  - Finalizar la integración de todos los componentes y preparar el despliegue.
  - Realizar pruebas exhaustivas de todas las funciones.

- Tareas:
  - Gestor presupuestario:
    - Desarrollar el sistema de seguimiento de presupuestos, incluidas las alertas por presupuestos cercanos o superados.
    - Garantizar que las notificaciones presupuestarias estén disponibles tanto en inglés como en español.
  - Validación de datos:
    - Implantar controles automatizados de limpieza y validación de datos.
    - Proporcionar al usuario indicaciones para revisar y corregir las entradas marcadas.
  - Integración final:
    - Integrar todos los componentes y asegurarse de que funcionan a la perfección.
    - Realizar pruebas de extremo a extremo para validar la funcionalidad del bot.
    - Preparar el bot para su despliegue, asegurándose de que toda la documentación está actualizada y disponible en ambos idiomas.