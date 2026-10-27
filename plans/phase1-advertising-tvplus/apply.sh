#!/bin/sh
# Generated from the operator's snapshot. Run through tools/tv.py exec --script.
set -eu
test "$(id -u)" = 0
test "$(sqlite3 -readonly /opt/dbspace/.pkgmgr_parser.db 'PRAGMA quick_check;')" = ok
sqlite3 -bail /opt/dbspace/.pkgmgr_parser.db <<'QUIET_SQL'
BEGIN IMMEDIATE;
CREATE TEMP TABLE quiet_guard(ok INTEGER CHECK(ok=1));
INSERT INTO quiet_guard SELECT count(*)=1 FROM package_app_info WHERE app_id='com.samsung.tizen.samsung-analytics' AND app_disable IS 'false' AND app_onboot IS 'false' AND app_autorestart IS 'false';
INSERT INTO quiet_guard SELECT count(*)=1 FROM package_app_info WHERE app_id='com.samsung.tv.acr' AND app_disable IS 'false' AND app_onboot IS 'false' AND app_autorestart IS 'true';
INSERT INTO quiet_guard SELECT count(*)=1 FROM package_app_info WHERE app_id='com.samsung.tv.canalysis-service' AND app_disable IS 'false' AND app_onboot IS 'false' AND app_autorestart IS 'true';
INSERT INTO quiet_guard SELECT count(*)=1 FROM package_app_info WHERE app_id='com.samsung.tv.contents-recognition-dbmgr' AND app_disable IS 'false' AND app_onboot IS 'false' AND app_autorestart IS 'false';
INSERT INTO quiet_guard SELECT count(*)=1 FROM package_app_info WHERE app_id='com.samsung.tv.adagent-service' AND app_disable IS 'false' AND app_onboot IS 'false' AND app_autorestart IS 'false';
INSERT INTO quiet_guard SELECT count(*)=1 FROM package_app_info WHERE app_id='com.samsung.tv.pisa-service' AND app_disable IS 'false' AND app_onboot IS 'false' AND app_autorestart IS 'false';
INSERT INTO quiet_guard SELECT count(*)=1 FROM package_app_info WHERE app_id='org.tizen.pisa-control-service' AND app_disable IS 'false' AND app_onboot IS 'false' AND app_autorestart IS 'false';
INSERT INTO quiet_guard SELECT count(*)=1 FROM package_app_info WHERE app_id='com.samsung.tv.targeted-ad-service' AND app_disable IS 'false' AND app_onboot IS 'true' AND app_autorestart IS 'true';
INSERT INTO quiet_guard SELECT count(*)=1 FROM package_app_info WHERE app_id='yL49PNFmjW.PromotionApp' AND app_disable IS 'false' AND app_onboot IS 'false' AND app_autorestart IS 'false';
INSERT INTO quiet_guard SELECT count(*)=1 FROM package_app_info WHERE app_id='yL49PNFmjW.service' AND app_disable IS 'false' AND app_onboot IS 'false' AND app_autorestart IS 'false';
INSERT INTO quiet_guard SELECT count(*)=1 FROM package_app_info WHERE app_id='com.samsung.tv.tvplus' AND app_disable IS 'false' AND app_onboot IS 'false' AND app_autorestart IS 'false';
UPDATE package_app_info SET app_disable='true',app_onboot='false',app_autorestart='false' WHERE app_id='com.samsung.tizen.samsung-analytics';
UPDATE package_app_info SET app_disable='true',app_onboot='false',app_autorestart='false' WHERE app_id='com.samsung.tv.acr';
UPDATE package_app_info SET app_disable='true',app_onboot='false',app_autorestart='false' WHERE app_id='com.samsung.tv.canalysis-service';
UPDATE package_app_info SET app_disable='true',app_onboot='false',app_autorestart='false' WHERE app_id='com.samsung.tv.contents-recognition-dbmgr';
UPDATE package_app_info SET app_disable='true',app_onboot='false',app_autorestart='false' WHERE app_id='com.samsung.tv.adagent-service';
UPDATE package_app_info SET app_disable='true',app_onboot='false',app_autorestart='false' WHERE app_id='com.samsung.tv.pisa-service';
UPDATE package_app_info SET app_disable='true',app_onboot='false',app_autorestart='false' WHERE app_id='org.tizen.pisa-control-service';
UPDATE package_app_info SET app_disable='true',app_onboot='false',app_autorestart='false' WHERE app_id='com.samsung.tv.targeted-ad-service';
UPDATE package_app_info SET app_disable='true',app_onboot='false',app_autorestart='false' WHERE app_id='yL49PNFmjW.PromotionApp';
UPDATE package_app_info SET app_disable='true',app_onboot='false',app_autorestart='false' WHERE app_id='yL49PNFmjW.service';
UPDATE package_app_info SET app_disable='true',app_onboot='false',app_autorestart='false' WHERE app_id='com.samsung.tv.tvplus';
DROP TABLE quiet_guard;
COMMIT;
QUIET_SQL
test "$(sqlite3 -readonly /opt/dbspace/.pkgmgr_parser.db 'PRAGMA quick_check;')" = ok
echo 'Registry transaction complete. This does not terminate already-running processes.'
