## Welcome to the LowMC cryptanalysis challenge!

This website contains information about the LowMC cryptanalysis challenge. *Note that this is not a formal announcement yet, but a preview.*

<!--
### Sponsors
<p align="center">
  <img height="80" src="https://raw.githubusercontent.com/lowmcchallenge/lowmcchallenge.github.io/master/media/logo_microsoft.png" />
  <img height="80" src="https://raw.githubusercontent.com/lowmcchallenge/lowmcchallenge.github.io/master/media/logo_iov42.png" />
</p>

### Developers
<p align="center">
  <img height="80" src="https://raw.githubusercontent.com/lowmcchallenge/lowmcchallenge.github.io/master/media/logo_tugraz.png" />
</p>
-->

### LowMC
LowMC ([ePrint](https://eprint.iacr.org/2016/687), [Springer](https://link.springer.com/chapter/10.1007/978-3-662-46800-5_17)) is a very parameterizable block cipher design, where the block size, the key size, and various other internals can be chosen freely by the user. The design is a partial substitution-permutation network, meaning that the nonlinear layers in each round do not cover the full state. This construction approach has shown to be beneficial for use cases like MPC, where the number of nonlinear gates has to be kept low.

Another use case where this design is efficient is a novel post-quantum signature scheme named Picnic ([ePrint](https://eprint.iacr.org/2017/279), [ACM](https://dl.acm.org/citation.cfm?doid=3133956.3133997)), which is currently a round-2 candidate in the NIST PQ competition. In Picnic, the number of multiplications of the underlying primitive has a direct impact on the resulting signature size.

From a cryptanalytic point of view, this scenario is interesting because a potential attacker is only ever able to have access to a single (plaintext, ciphertext) pair. The purpose of this cryptanalysis challenge is therefore to gain a deeper knowledge about the security of LowMC in this setting.

### Instances
We consider following instances of LowMC (n = block size = key size, s = number of S-boxes in each round):
- n = 128, s = 1
- n = 128, s = 10
- n = 129, s = 43 (full nonlinear layer)
- n = 192, s = 1
- n = 192, s = 10
- n = 192, s = 64 (full nonlinear layer)
- n = 256, s = 1
- n = 256, s = 10
- n = 255, s = 85 (full nonlinear layer)

### The Cryptanalysis Challenge
The goal of the attacks is to recover the key. The challenge is to use one of our proposed instances and to find an attack covering more rounds than what is suggested by the following table.

| n   | s  | r   |
|-----|----|-----|
| 128 | 1  | 140 |
| 128 | 10 | 14  |
| 129 | 43 | 4   |
| 192 | 1  | 210 |
| 192 | 10 | 21  |
| 192 | 64 | 4   |
| 256 | 1  | 280 |
| 256 | 10 | 28  |
| 255 | 85 | 4   |

### Tentative Schedule, Rules, and Prizes
Schedule:
- First deadline is March 15 (i.e., the week before FSE 2020)
- Overall duration is around 2 years; money that is not spent remains in the pot and is part of the following round
- The goal is that the total money (100k€) is largely spent at the end

General rules:
- Earlier results are better
- Verifiability is important
- Submissions will be published

You can win following prizes for each of the nine challenges:
- 2k€ for an attack covering more rounds (partial SPN)
- 2k€ for the fastest attack covering the highest number of rounds vulnerable to current attacks (partial SPN)
- 5k€ for the first attack covering 4 or more rounds (full SPN)
- 2k€ for the fastest attack on 3 rounds (full SPN)

### Reference Implementations
You can find reference implementations of above-mentioned instances and all needed values (e.g., matrices, constants) in [this folder](https://github.com/lowmcchallenge/lowmcchallenge.github.io/tree/master/reference).
