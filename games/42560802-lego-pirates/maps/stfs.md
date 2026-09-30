# Mapa STFS — save de referência

## Container

- Tipo: `CON`
- Header size: `0x971A`
- Data section alinhada: `0xA000`
- Volume descriptor: `0x379`
- Flags do volume: `0x02`
- Formato gravável: sim
- Root active index: sim
- Hash-table blocks por nível: 2

## File table

- File table block count: 1
- File table block number: 2
- File table physical offset: `0xE000`

Entrada encontrada:

| Arquivo | Flags | Blocos | Primeiro bloco | Tamanho |
|---|---:|---:|---:|---:|
| `GAME1` | `0x05` | 14 | 13 | 56.656 bytes |

## Cadeia física de GAME1

Blocos lógicos:

`13 → 8 → 11 → 18 → 10 → 12 → 15 → 16 → 3 → 4 → 14 → 17 → 6 → 7`

Offsets físicos:

| Bloco | Offset |
|---:|---:|
| 13 | `0x19000` |
| 8 | `0x14000` |
| 11 | `0x17000` |
| 18 | `0x1E000` |
| 10 | `0x16000` |
| 12 | `0x18000` |
| 15 | `0x1B000` |
| 16 | `0x1C000` |
| 3 | `0x0F000` |
| 4 | `0x10000` |
| 14 | `0x1A000` |
| 17 | `0x1D000` |
| 6 | `0x12000` |
| 7 | `0x13000` |

## Integridade interna de GAME1

- checksum armazenado: offset `0x0C` a `0x0F`, big-endian;
- range calculado: `GAME1[0x10:EOF]`;
- algoritmo: FNV-1 32-bit;
- valor inicial: `0xFFFFFFFF`;
- prime: `0x01000193`;
- operação final: XOR `0xFFFFFFFF`.

No save de referência o checksum armazenado é `0x67C89863`, e o cálculo reproduz exatamente esse valor.
