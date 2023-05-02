# Instalando paquetes desde AUR
16 de Febrero de 2023

## Packetes de AUR al segundo
Bueno, siempre me olvido de cómo hacer instalar paquetes de AUR en mi ArchLinux así que escribiré este ayudamemorias

```
makepkg -rsci ./
```

Así de simple y sin preámbulos obsoletos de esos que están de moda (?).

* s: Instala las dependencias automáticamente
* r: Desinstala las dependencias que se usaron para compilar el paquete
* c: Borra todos los temporales de compilación
* i: Instala el paquete en el sistema

Y así terminamos el post de hoy. Saludos!