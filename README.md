# PMCN Xbox 360 Save Lab

Laboratório de engenharia reversa e modificação de saves do Xbox 360.

## Objetivo

Documentar formatos de save, checksums, estruturas internas e modificações reproduzíveis, sempre preservando uma referência original e registrando o que foi alterado.

## Status

Primeiro jogo em estudo:

- **LEGO Pirates of the Caribbean: The Video Game**
- Title ID: `42560802`
- Media ID: `462C5F7C`
- Base Version: `00000008`
- TU: nenhuma aplicada no save de referência

## Regras do projeto

- Nunca sobrescrever a referência original.
- Toda alteração deve ter hash e changelog.
- Separar desbloqueios de conteúdo de progresso de campanha.
- Só marcar uma versão como **VALIDADA** após teste real no Xbox 360.
- Não publicar identificadores pessoais em documentação textual.

> Observação: pacotes CON de save podem conter identificadores do perfil/dispositivo/console. Como este repositório é público, arquivos binários brutos devem ser publicados conscientemente.
