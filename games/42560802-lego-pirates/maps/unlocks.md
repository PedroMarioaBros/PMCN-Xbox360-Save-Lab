# Unlock map — LEGO Pirates (Xbox 360)

Reference save: Title ID `42560802`, Base Version `00000008`.

## Character roster — confirmed differential candidate

Xbox GAME1 range: approximately `0xAE80..0xAF20`.

Comparison used:

- Pietro's Xbox 360 save;
- decrypted PS3 100% save from the same TT Games save family;
- structures aligned by the custom-character records.

The current Xbox save has 37 active roster flags in this region. The 100% reference has 77. There are exactly **40 missing flags**, and all 40 are clean `0x00 -> 0x01` differences. There are no `1 -> 0` differences in this roster differential.

Offsets changed by v0.1:

```
AE80 AE81 AE8C AE8F AE97 AE99 AEA0 AEA1 AEA2 AEA4
AEA6 AEA9 AEAE AEAF AEB2 AEB4 AEB5 AEBC AEC0 AEC7
AECC AECD AECE AECF AED0 AED4 AEDC AEDD AEE0 AEE1
AEE9 AEEB AEF6 AEF7 AEFD AEFF AF0B AF0C AF13 AF20
```

Each byte is set to `01`.

## Extras / Red Hats — 20-bit ownership mask

Xbox GAME1:

- offset: `0xB158..0xB15A`
- original: `01 00 00`
- 100% reference: `FF FF 0F`

`FF FF 0F` means the low **20 bits** are set, exactly matching the game's 20 Extras / Red Hats. v0.1 changes only this ownership/unlock mask; it does not force Extras to remain enabled.

## Deliberately untouched

The following were not copied from the 100% reference:

- campaign-completion masks;
- level completion;
- True Pirate;
- minikits;
- compass items;
- Gold Bricks;
- percentage;
- variable-length tail records after the Extras area;
- Custom A–J contents.

This is intentional so v0.1 can maximize usable content without forcing 100% progression.

## v0.1 integrity

GAME1 changes:

- 40 roster bytes;
- Extras mask at `B158..B15A`;
- GAME1 checksum at `0C..0F`.

New GAME1 checksum: `FCA0F5B3`.

STFS package rehash updates:

- affected GAME1 logical blocks: `13, 14, 17`;
- active level-0 block hashes;
- top hash table SHA-1;
- header/content SHA-1.

No campaign-state block was imported from the 100% save.
