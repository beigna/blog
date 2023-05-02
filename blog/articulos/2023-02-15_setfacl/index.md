# Usar Docker sin sudo ni root
15 de Febrero de 2023

## Introducción
La clásica, querés hacer algo en Docker y lo primero que hacés es agregar tu usuario al grupo docker y dejar nuestro usuario expuesto o usar sudo a lo bobo.

## LA Solución!
El viejo y querido setfacl, al que nunca le encontré utilidad... hasta ahora:

```
sudo setfacl -m user:$USER:rw /var/run/docker.sock
```

Con esta mágia línea le cambiamos el owner dicho archivo y Docker nos va a dar pelota de manera transparente.
PD: Esto habrá que ejecutarlo cada vez que reiniciemos Docker o la PC ¿Sale Makefile? No lo sé

Saludos!