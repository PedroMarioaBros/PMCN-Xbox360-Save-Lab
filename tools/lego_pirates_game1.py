#!/usr/bin/env python3
"""Utilitários iniciais para GAME1 de LEGO Pirates (Xbox 360).

Não re-assina o pacote STFS. O objetivo desta etapa é validar/recalcular
o checksum interno de GAME1 e documentar alterações reproduzíveis.
"""

from __future__ import annotations

import argparse
from pathlib import Path

FNV_PRIME = 0x01000193
MASK32 = 0xFFFFFFFF


def lego_fnv1(data: bytes) -> int:
    h = MASK32
    for b in data:
        h = ((h * FNV_PRIME) & MASK32) ^ b
    return h ^ MASK32


def stored_checksum(game1: bytes) -> int:
    if len(game1) < 0x10:
        raise ValueError("GAME1 pequeno demais")
    return int.from_bytes(game1[0x0C:0x10], "big")


def update_checksum(game1: bytearray) -> int:
    if len(game1) < 0x10:
        raise ValueError("GAME1 pequeno demais")
    checksum = lego_fnv1(game1[0x10:])
    game1[0x0C:0x10] = checksum.to_bytes(4, "big")
    return checksum


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("game1", type=Path)
    ap.add_argument("--fix", action="store_true")
    ap.add_argument("-o", "--output", type=Path)
    args = ap.parse_args()

    raw = bytearray(args.game1.read_bytes())
    old = stored_checksum(raw)
    calc = lego_fnv1(raw[0x10:])
    print(f"stored=0x{old:08X}")
    print(f"calc  =0x{calc:08X}")
    print("OK" if old == calc else "MISMATCH")

    if args.fix:
        new = update_checksum(raw)
        out = args.output or args.game1.with_suffix(args.game1.suffix + ".fixed")
        out.write_bytes(raw)
        print(f"updated=0x{new:08X}")
        print(out)


if __name__ == "__main__":
    main()
