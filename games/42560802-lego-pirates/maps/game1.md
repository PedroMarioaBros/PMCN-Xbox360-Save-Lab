# GAME1 — mapa de engenharia reversa

Status: **em construção, com campos confirmados**.

## Campos confirmados

| Offset | Tamanho | Formato | Função | Save de referência |
|---|---:|---|---|---|
| `0x04` | 4 bytes | float32 big-endian | Porcentagem de conclusão | `41 F1 72 DD` = **30,1810856%** |
| `0x0C` | 4 bytes | uint32 big-endian | Checksum interno LEGO | `0x67C89863` |
| `0x80B0` | 8 bytes | uint64 big-endian | Total de studs | **414.170** |

### Studs

A assinatura estrutural usada pelos saves LEGO coloca o total em `0x80B0` neste GAME1.

Valor original:
`00 00 00 00 00 06 51 DA` = **414.170**

Valor preparado para a v0.01:
`00 00 00 E8 D4 A5 0F FF` = **999.999.999.999**

Após essa única alteração, o checksum interno passa para:
`0x10943937`.

A porcentagem em `0x04` permanece byte a byte idêntica.

## Checksum

- campo: `0x0C–0x0F`;
- range: `GAME1[0x10:EOF]`;
- algoritmo: FNV-1 32-bit;
- inicial: `0xFFFFFFFF`;
- prime: `0x01000193`;
- XOR final: `0xFFFFFFFF`.

## Personagens personalizados

Os dez slots personalizados são registros espaçados em `0x46C` bytes e serão preservados:

- Custom A: `0x8520`
- Custom B: `0x898C`
- Custom C: `0x8DF8`
- Custom D: `0x9264`
- Custom E: `0x96D0`
- Custom F: `0x9B3C`
- Custom G: `0x9FA8`
- Custom H: `0xA414`
- Custom I: `0xA880`
- Custom J: `0xACEC`

**Correção importante:** a região em torno de `0xAE7E`, inicialmente candidata a flags, cai dentro do registro de Custom J e foi descartada. Ela não será usada como tabela de desbloqueio.

## Alvos ainda em mapeamento

1. estado serializado de desbloqueio/aquisição de todos os personagens;
2. estado de aquisição dos 20 Extras / Red Hats;
3. flags especiais, inclusive o personagem secreto por código;
4. separação rigorosa entre desbloqueio e progresso de campanha.

Nenhum candidato será escrito no save final até ser ligado ao estado correto por evidência independente ou comparação diferencial.
