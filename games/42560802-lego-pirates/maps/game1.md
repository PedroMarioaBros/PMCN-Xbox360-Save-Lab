# GAME1 — mapa de engenharia reversa

Status: **em construção**.

## Cabeçalho conhecido

- `0x0C–0x0F`: checksum FNV-1 32-bit do intervalo `0x10..EOF`.

## Estruturas observadas

O arquivo contém estruturas repetidas relacionadas a estado do jogo e registros de personagens personalizados.

Strings confirmadas no save de referência:

- `Custom A` em torno de `0x8520`;
- `Custom J` em torno de `0xACEC`.

Os dez slots `Custom A` a `Custom J` serão preservados durante a primeira modificação.

## Alvos de mapeamento

1. estado de desbloqueio/aquisição de todos os personagens;
2. quantidade de studs;
3. estado de aquisição dos 20 Extras / Red Hats;
4. flags especiais, incluindo personagens liberáveis por código;
5. separação entre desbloqueio e progresso de campanha.

Nenhum offset será promovido a **confirmado** apenas por semelhança: cada campo será validado por comparação, checksum e teste no console.
