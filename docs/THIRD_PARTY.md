# Terceros y procedencia

Este repositorio no redistribuye payloads binarios ni código de exploits.

La intervención se apoyó, tras auditoría estática, en:

- `jss8649/quiet-tizen`, commit `cf518d7a9278dca7990e27756218258e44044a29`.
- `jss8649/samsung-tv-root`, commit `4ad2c4d3b0d0e0da4b5b7ebe4a787e94596f416b`.
- Tizen Studio CLI 6.1 y su cliente SDB.
- .NET SDK 3.1.426 para generar los assemblies `netcoreapp3.1`.

`payload-manifests/common31-sdk3.1.426.json` conserva únicamente hashes de los binarios usados. Obtener las fuentes y revisar sus licencias desde los repositorios upstream.

Hallazgo reproducible: `payloads/common31/global.json` upstream fija SDK 6.0.428. Los payloads probados en esta TV se compilaron explícitamente con SDK 3.1.426.
