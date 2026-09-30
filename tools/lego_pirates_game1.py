#!/usr/bin/env python3
"""LEGO Pirates GAME1 utility — Xbox 360 save research.

Patch v0.1:
- enables the 40 roster flags absent in the reference save;
- sets the 20-bit Extras/Red Hats ownership mask;
- recalculates the internal FNV-1 checksum.

This script operates on extracted GAME1 only. STFS package hashes are a
separate layer.
"""

from __future__ import annotations

import argparse
from pathlib import Path

FNV_PRIME = 0x01000193
MASK32 = 0xFFFFFFFF

CHARACTER_UNLOCK_OFFSETS = (
    0xAE80,0xAE81,0xAE8C,0xAE8F,0xAE97,0xAE99,0xAEA0,0xAEA1,0xAEA2,0xAEA4,
    0xAEA6,0xAEA9,0xAEAE,0xAEAF,0xAEB2,0xAEB4,0xAEB5,0xAEBC,0xAEC0,0xAEC7,
    0xAECC,0xAECD,0xAECE,0xAECF,0xAED0,0xAED4,0xAEDC,0xAEDD,0xAEE0,0xAEE1,
    0xAEE9,0xAEEB,0xAEF6,0xAEF7,0xAEFD,0xAEFF,0xAF0B,0xAF0C,0xAF13,0xAF20,
)

EXTRAS_MASK_OFFSET = 0xB158
EXTRAS_MASK = bytes.fromhex("FFFF0F")


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
    checksum = lego_fnv1(game1[0x10:])
    game1[0x0C:0x10] = checksum.to_bytes(4, "big")
    return checksum


def patch_unlocks(game1: bytearray) -> None:
    if len(game1) != 56656:
        raise ValueError(f"GAME1 inesperado: {len(game1)} bytes; esperado 56656 para esta versão Xbox 360")
    for offset in CHARACTER_UNLOCK_OFFSETS:
        game1[offset] = 1
    game1[EXTRAS_MASK_OFFSET:EXTRAS_MASK_OFFSET + 3] = EXTRAS_MASK
    update_checksum(game1)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("game1", type=Path)
    ap.add_argument("--fix-checksum", action="store_true")
    ap.add_argument("--unlock-v01", action="store_true")
    ap.add_argument("-o", "--output", type=Path)
    args = ap.parse_args()

    raw = bytearray(args.game1.read_bytes())
    old = stored_checksum(raw)
    calc = lego_fnv1(raw[0x10:])
    print(f"stored=0x{old:08X}")
    print(f"calc  =0x{calc:08X}")
    print("OK" if old == calc else "MISMATCH")

    if args.unlock_v01:
        patch_unlocks(raw)
    elif args.fix_checksum:
        update_checksum(raw)

    if args.unlock_v01 or args.fix_checksum:
        out = args.output or args.game1.with_suffix(args.game1.suffix + ".mod")
        out.write_bytes(raw)
        print(f"new=0x{stored_checksum(raw):08X}")
        print(out)


if __name__ == "__main__":
    main()
