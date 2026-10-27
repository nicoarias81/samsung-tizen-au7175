# Seguridad

Este repositorio documenta una intervención comprobada en un único modelo y firmware. No es un debloater universal.

## Guards obligatorios

- Modelo SDB literal: `UE55AU7175UXXC`.
- Build exacto: `T-KSU2EDEUC-REL-202607211851`.
- Tizen 6.0, ARMv7, Linux 4.1.10 y .NET Core 3.1.3.
- Usar solamente `archive-root` con payloads `netcoreapp3.1` compilados mediante SDK 3.1.426.
- Verificar UID/EUID/GID/EGID 0, callback autenticado, staging limpio y hashes invariantes de `/etc/passwd` y la clave pública SDB.
- Antes de escribir: snapshots SQLite con `PRAGMA quick_check`, hashes SHA-256 y restauración inversa local y en la TV.
- Scripts shell con LF; Tizen rechaza CRLF. Ante UEP, ejecutar contenido auditado mediante `/bin/sh < script`.
- No reiniciar automáticamente.

## Prohibido reutilizar

No usar el perfil U8000F, Home replacement, service markers, assemblies privados, payloads net6 ni IDs HDMI de otro modelo.

## Alcance de la garantía

`system_files_unchanged` sólo comprueba `/etc/passwd` y la clave SDB. No equivale a un hash completo del sistema. La adquisición de root crea staging temporal y puede dejar residuos si se corta la energía o la red.
