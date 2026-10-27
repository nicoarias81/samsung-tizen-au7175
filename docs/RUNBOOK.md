# Runbook probado

## Estado aplicado

En `UE55AU7175UXXC`, build `T-KSU2EDEUC-REL-202607211851`:

1. Snapshot íntegro de `.pkgmgr_parser.db`, `.app-context.db` y `.webappservice.db`.
2. Diez componentes observados de publicidad/ACR/promoción y `com.samsung.tv.tvplus` quedaron con:
   - `app_disable=true`
   - `app_onboot=false`
   - `app_autorestart=false`
3. `db/menu/autorun_tv_plus` cambió de Boolean `True` a `False` mediante `vconftool set -t bool -f`.
4. Verificación posterior: 11/11 filas y `PRAGMA quick_check=ok`.
5. Restauraciones guardadas localmente y bajo `/opt/usr/share/quiet-tizen-backups/au7175-preclean-20261025T200506Z/`.

No se modificaron Home, navegador, voz, SmartThings, unidades systemd, markers ni binarios del sistema.

## Activación

No reiniciar desde automatización. Hacer un reinicio normal desde la TV y dejarla 5–10 minutos estable en la misma entrada antes de medir.

## Métricas posteriores

```bash
python tools/metrics_snapshot.py \
  --host TV_IP \
  --sdb 'C:/Users/nicoa/AppData/Local/TizenStudio/tools/sdb.exe' \
  --vendor-root 'RUTA/A/CHECKOUT/AUDITADO' \
  --output private/metrics-after.json
```

El host no se guarda salvo que se añada `--include-host`. Comparar memoria disponible, swap, carga y RSS de procesos objetivo. Una sola muestra no demuestra causalidad; mantener misma entrada y período de reposo.

## Restauración

Revalidar modelo y build antes de restaurar. Los archivos `restore.sh` y `restore-tvplus-autorun.sh` están auditados, pero Tizen puede bloquear ejecución directa de scripts sin firma. En ese caso usar contenido LF revisado mediante `/bin/sh < script` dentro de una sesión root autenticada.
