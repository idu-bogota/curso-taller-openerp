[[
title: Lección 11: Wizards
author: STRT Grupo I+D+I
]]

Lección 11: Wizards
===================

[TOC]

Wizards
-------

Los Wizards son secuencias de interacción entre el cliente y el servidor. Para definir un wizard, se debe crear una clase que hereda de wizard.interface e instanciarla, cada wizard debe tener un nombre único.


¿Cómo adicionar un nuevo Wizard?
--------------------------------

1. Crear subdirectorio wizard en el módulo, adicionar el archivo __init__.py y el archivo .py para crear el wizard.
1. Adicionar el subdirectorio wizard a la lista de declaraciones de importación en el archivo __init__.py del módulo,
1. Adicionar el nombre del archivo .py en el archivo __init__.py del subdirectorio wizard.
1. Adicionar el archivo .xml para la vista del archivo .py
1. La acción que ejecuta el objeto debe ser: *<field name="target">new</field>*


**Estructura de definición**


Ejemplo:



**Ejemplo de aplicación**:

* **Crear archivo .py**

* **Crear archivo .xml**


Ejercicios propuestos
---------------------

1. 
