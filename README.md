# BlinkSMP Resource Packs

Public downloads for the BlinkSMP Minecraft resource pack. No plugin source code or server credentials are stored here.

## Zombies 0.3.2

Custom textures for all seven zombie masks, the crate keys and Frostbite sword. Compatible with BlinkZombie 0.3.0 on Minecraft 1.21.11.

Direct download: https://raw.githubusercontent.com/jryoung201-code/BlinkSMP-texure/main/BlinkSMP-ResourcePack-Zombies-0.3.2.zip

Server configuration:
```properties
require-resource-pack=true
resource-pack=https://raw.githubusercontent.com/jryoung201-code/BlinkSMP-texure/main/BlinkSMP-ResourcePack-Zombies-0.3.2.zip
resource-pack-sha1=91888771f4fa3689a3f6d07378ef8f558fa1900c
```

Stop the server before editing server.properties, save, then start it again. Keep the ZIP unchanged.

0.3.2 fixes missing mask textures by placing the artwork in the item texture directory and explicitly registering it in the item and block atlases. The original artwork and existing key/sword assets are preserved. No plugin update is required.
