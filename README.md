# Samsung Tizen AU7175 — inventario y debloat seguro

Repositorio reproducible de la intervención realizada sobre una Samsung **UE55AU7175UXXC** con Tizen 6.0 y build `T-KSU2EDEUC-REL-202607211851`.

> No es un debloater universal. Los planes incluidos están ligados literalmente a este modelo, firmware, esquema SQLite e inventario observado.

## Resultado comprobado

- 10 componentes de publicidad, ACR y promoción deshabilitados en el registro de paquetes.
- Samsung TV Plus deshabilitado.
- Autorun de TV Plus: Boolean `True → False`.
- 11/11 filas verificadas después de escribir.
- Bases SQLite verificadas con `PRAGMA quick_check`.
- Restauración inversa conservada localmente y en la TV.
- Sin cambios en Home, navegador, voz, SmartThings, servicios, markers ni binarios del sistema.

Los cambios de `onboot` y `autorestart` terminan de activarse tras un reinicio normal de la TV. El proyecto no reinicia dispositivos automáticamente.

## Estructura

```text
profiles/          Perfil específico del modelo y firmware
plans/             SQL y shell de aplicación/restauración revisados
evidence/          Evidencia estructurada de cambios no sensible
payload-manifests/ Hashes de payloads conocidos; no contiene binarios
tools/             Validación de artefactos y captura de métricas
tests/             Tests offline
docs/              Seguridad, runbook y procedencia
private/           Marcador para datos locales excluidos de Git
```

## Validación offline

```bash
python tools/verify_artifacts.py
python -m unittest discover -s tests -v
```

## Medición posterior al reinicio

Consultar [`docs/RUNBOOK.md`](docs/RUNBOOK.md). `tools/metrics_snapshot.py` sólo ejecuta consultas de lectura mediante SDB y omite la IP del archivo de salida de forma predeterminada.

## Datos privados y payloads

Los snapshots SQLite, inventarios completos, direcciones IP, logs y DLL root funcionales están deliberadamente excluidos. El manifiesto de hashes permite comprobar los payloads locales sin redistribuir código de terceros ni material sensible del televisor.

## Advertencias

- Leer [`docs/SAFETY.md`](docs/SAFETY.md) antes de usar cualquier plan.
- No reutilizar el perfil quiet-tizen U8000F.
- La ruta root es compatible de forma condicional; upstream no certifica este modelo.
- La adquisición de root crea staging temporal y una interrupción puede dejar residuos.

## Licencia

El código original de este repositorio se distribuye bajo MIT. Los proyectos y payloads de terceros mantienen sus propias licencias; ver [`docs/THIRD_PARTY.md`](docs/THIRD_PARTY.md).
