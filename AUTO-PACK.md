# Automatic pack updates

BlinkZombie 0.3.1 reads latest.properties every five minutes, verifies the ZIP and SHA1 off-thread, and sends changed packs to online players and joining players. Future pack updates only require uploading a new versioned ZIP and changing latest.properties here.

One-time server.properties setup:
```properties
resource-pack=
resource-pack-sha1=
require-resource-pack=false
```

The plugin supplies the pack. Keep the server in Adventure mode if desired. The pack is optional by default until rendering is confirmed. No player data reset is needed.

0.3.3 uses a 512x512 RGBA texture sheet and item-only atlas registration. Download and reference validation cannot substitute for checking the exact client error in latest.log if it still fails.
