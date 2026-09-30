# PS3 100% reference — status

A reference save from Apollo Save Database is being used only to map flags against the Xbox 360 GAME1.

## Confirmed encryption key database entry

For **LEGO Pirates of the Caribbean**:

- PS3 IDs: `BLUS30744 / NPUB30560 / BLES01239 / BLES01241 / NPEB00654`
- `secure_file_id`: `12010B10080605120E0519080F150708`

The downloaded `GAME1` is wrapped by the PS3 savedata encryption layer and therefore must be decrypted before any byte-level comparison with the Xbox 360 plaintext GAME1.

## Reference package

Apollo description: **100% Complete / 23 billion studs**.

Contained files:

- `GAME1`: 56,672 bytes encrypted (16-byte aligned wrapper)
- `PARAM.PFD`
- `PARAM.SFO`
- `ICON0.PNG`

Next step: decrypt GAME1 with its PARAM.PFD entry and the secure file ID above, then align against Xbox GAME1.
