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
We consider different instances of LowMC, where n denotes the block size (and the key size) and s denotes the number of S-boxes in each round. Specifically, we make a distinction between *partial S-box layers* and *full S-box layers*:
- n = 128, s = 1
- n = 128, s = 10
- n = 129, s = 43 (full S-box layer)
- n = 192, s = 1
- n = 192, s = 10
- n = 192, s = 64 (full S-box layer)
- n = 256, s = 1
- n = 256, s = 10
- n = 255, s = 85 (full S-box layer)

### The Cryptanalysis Challenge
The goal of all attacks here is to recover the secret key. We have following challenges and prices in mind for the versions with full S-box layers:
- Submitters of the *fastest attack* on 2 rounds win EUR 2k.
- Submitters of the *fastest attack* on 3 rounds win EUR 3k.
- Submitters of the *fastest attack* on 4 rounds win EUR 4k.

For the versions with partial S-box layers, let again denote by n the block size (and key size) and by s the number of S-boxes. Using this notation, we have following prices in mind for the possible instances from above:
- Submitters of the *fastest attack* on floor(n/s)*0.8 rounds win EUR 2k.
- Submitters of the *fastest attack* on floor(n/s)*1.0 rounds win EUR 3k.
- Submitters of the *fastest attack* on floor(n/s)*1.2 rounds win EUR 4k.

In total, EUR 22k may be earned in the first round. By the *fastest attack* we mean the biggest gain in efficiency over exhaustive search. Note that we always use a data complexity of 1 for these attacks, which means that no more than a single (plaintext, ciphertext) pair is allowed. The claimed security levels are always n bits.

In addition, we also offer a bonus prize for finding an interesting property of LowMC or for showing a new technique (we will consider weak-key attacks, but not related-key attacks). The winner of this side challenge gets EUR 4k.

<!--
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
-->

### Schedule and Rules
Schedule:
- The first quick round is until August 10 2020 (one week before Crypto 2020), and winners will be announced after that.
- Tentative: The second round is planned to run until FSE 2020 (November 2020)
- Potentially, a third round will be held until June 1 2021.
- Overall duration is around 2 years (money not spent remains in the pot and is part of the following round)

Rules:
- Results with the fastest attacks are better (date of submission does not count)
- Verifiability is important
- Submissions will be published
- Brute force-like with minor gains will not be considered
- If two attacks are equally efficient, the one submitted earlier wins

### Reference Implementations
You can find reference implementations of above-mentioned instances and all needed values (e.g., matrices, constants) in [this folder](https://github.com/lowmcchallenge/lowmcchallenge.github.io/tree/master/reference).

### Contact
You've solved a challenge or have any other questions? Let us know by writing a mail to [lowmc-challenge@iaik.tugraz.at](mailto:lowmc-challenge@iaik.tugraz.at)