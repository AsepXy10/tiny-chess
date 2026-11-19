# tiny-chess

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/AsepXy10/tiny-chess/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/AsepXy10/tiny-chess/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A chess engine in 4,085 bytes of pure Python 3.13 stdlib, written from scratch for the make.fun "Build the strongest chess engine in 4 KB of Python" bounty. It is a 0x88 negamax search with alpha-beta pruning and unified quiescence, iterative deepening to a fixed 90,000-node budget, material and pawn-advancement evaluation, per-ply killer moves, and MVV-LVA move ordering. Fully deterministic: a fixed node count, never a clock, no randomness. Practice Elo around 1,190 on the kit's sealed scorer, above the 1,154 bar for the final.

The size rule: `main.py` is the whole engine, at most 4,096 bytes as committed. It reads, imports, or execs no other file in the repository. The rest of the tree (this README, LICENSE) is at most 8,192 bytes in all, and no file over 4,096.

## Run it

```sh
makefun grade-local --kit . --bot AsepXy10/tiny-chess --driver docker
```

It plays one practice trial against the house engines and prints the Elo the scorer gives it.

---

<sub>Entered on [make.fun](https://make.fun/?ref=effk6c6f&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
