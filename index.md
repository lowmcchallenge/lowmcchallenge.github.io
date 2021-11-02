This website contains information about the LowMC cryptanalysis challenge.

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

**Sponsoring: Currently USD 50k from Microsoft and EUR 50k from iov42**

The goal of all attacks here is to recover the secret key. We have following challenges and prices in mind for the versions with full S-box layers:
- Submitters of the *fastest attack* on 2 rounds win EUR 2k.
- Submitters of the *fastest attack* on 3 rounds win EUR 3k.
- Submitters of the *fastest attack* on 4 rounds win EUR 4k.

For the versions with partial S-box layers, let again denote by n the block size (and key size) and by s the number of S-boxes. Using this notation, we have following prices in mind for the possible instances from above:
- Submitters of the *fastest attack* on floor(n/s)*0.8 rounds win EUR 2k.
- Submitters of the *fastest attack* on floor(n/s)*1.0 rounds win EUR 3k.
- Submitters of the *fastest attack* on floor(n/s)*1.2 rounds win EUR 4k.

By the *fastest attack* we mean the biggest gain in efficiency over exhaustive search. Note that we always use a data complexity of 1 for these attacks, which means that no more than a single (plaintext, ciphertext) pair is allowed. The claimed security level is always n bits.

Additionally, we also offer a bonus prize for finding an interesting property of LowMC or for showing a new technique (we will consider weak-key attacks, but not related-key attacks). The winner of this side challenge gets EUR 4k.

In total, EUR 22k may be earned in this current round.

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
Tentative schedule:
- ~~The first quick round is until August 10 2020 (one week before Crypto 2020), and winners will be announced after that~~
- ~~The second round is until December 1 (one week before Asiacrypt 2020)~~
- ~~A third round is now running until April 27 2021~~
- Overall duration is around 2 years (money not spent remains in the pot and is part of the following rounds)

Rules:
- Results with the fastest attacks are better (date of submission does not count)
- If two attacks are equally efficient or very similar, the one submitted earlier wins
- Verifiability is important
- Submissions will be published
- Brute force-like approaches with minor gains will not be considered

### Further Material
The current status with some of our baseline approaches and new attacks found during this competition can be downloaded [here](https://raw.githubusercontent.com/lowmcchallenge/lowmcchallenge-material/master/docs/survey.pdf).

You can find reference implementations of LowMC and scripts to generate all needed values (e.g., matrices, constants) in the [original LowMC repository](https://github.com/LowMC/lowmc). Our implementation of the decoding attack on LowMC is available [here](https://github.com/lowmcchallenge/lowmcchallenge-material/tree/master/code/decoding-attack).

### Results after Third Round
We thank all the submitters in the first three rounds of this challenge for new insights regarding low-data attacks against LowMC! Specifically, the attacks found during the first three rounds of the challenge where the following:
- An attack that combines lineariziation with guess-and-determine and meet-in-the-middle technique. The attack was found by Subhadeep Banik (EPFL), Khashayar Barooti (EPFL), Serge Vaudenay (EPFL), and Hailun Yan (EPFL), and is further described [here](https://raw.githubusercontent.com/lowmcchallenge/lowmcchallenge-material/master/docs/lowmc_analysis_1.pdf).
Published at Asiacrypt 2021 and subsequently referred to as "Linearization + G&D + MITM"
- A new polynomial method for solving multivariate equation systems over GF(2) found by Itai Dinur (Ben-Gurion University) which is described [here](https://raw.githubusercontent.com/lowmcchallenge/lowmcchallenge-material/master/docs/lowmc_analysis_1.pdf).
Published at Eurocrypt 2021 and subsequently referred to as "Polynomial Method".

The tables below show a comparison of these attacks in terms of time complexities in bit operations (T) and memory complexities in bits (M), if available. In the following, n denotes the state size, r the number of rounds and s the number of S-Boxes in rounds with partial S-Box layer. The data complexity is 1 in all cases.

**Full S-Box Layer**

<!--
| (129,2) | Linearization + G&D | 101.2 | 16.5 | [1] |
| (192,2) | Linearization + G&D | 142.9 | 17.7 | [1] |
| (255,2) | Linearization + G&D | 184.8 | 18.3 | [1] |
| (129,3) | Linearization + G&D | 143.9 | 17.7 | [1] |
| (192,3) | Linearization + G&D | 206.3 | 18.8 | [1] |
| (255,3) | Linearization + G&D | 268.7 | 19.6 | [1] |
-->

| (n,r) | Method | log_2(T) | log_2(M) | Winner |
|---|---|---|---|---|
| (129,2) | Linearization + G&D + MITM | 101.4 | na | <span> &#9733;</span> | [2] |
| (192,2) | Linearization + G&D + MITM | 142.6 | na |<span> &#9733;</span> | [2] |
| (255,2) | Linearization + G&D + MITM | 184.2 | na | <span> &#9733;</span> | [2] |
| (129,3) | Linearization + G&D + MITM | 144.4 | na | | [2] |
| (192,3) | Linearization + G&D + MITM | 206.6 | na | | [2] |
| (255,3) | Linearization + G&D + MITM | 269.2 | na | | [2] |
| (129,2) | Polynomial Method | 118 | >65 | | [3] |
| (192,2) | Polynomial Method | 170 | >95 | | [3] |
| (255,2) | Polynomial Method | 222 | >120 | | [3] |
| (129,3) | Polynomial Method | 125 | >65 | <span> &#9733;</span> | [3] |
| (192,3) | Polynomial Method | 180 | >95 | <span> &#9733;</span> | [3] |
| (255,3) | Polynomial Method | 235 | >120 | <span> &#9733;</span> | [3] |
| (129,4) | Polynomial Method | 130 | >65 | <span> &#9733;</span> | [3] |
| (192,4) | Polynomial Method | 188 | >95 | <span> &#9733;</span> | [3] |
| (255,4) | Polynomial Method | 245 | >120 | <span> &#9733;</span> | [3] |


**Partial S-Box Layer with 0.8*n/s Rounds**

<!--
| (128,1,102) | Linearization + G&D | 118   | 17.1 | [1] |
| (192,1,153) | Linearization + G&D | 168.6 | 17.7 | [1] |
| (256,1,204) | Linearization + G&D | 219.3 | 18.8 | [1] |
| (128,10,9)  | Linearization + G&D | 115   | 16.5 | [1] |
| (192,10,15) | Linearization + G&D | 164.6 | 18.3 | [1] |
| (256,10,20) | Linearization + G&D | 214.3 | 18.8 | [1] |
-->

| (n,s,r) | Method | log_2(T) | log_2(M) | Winner |
|---|---|---|---|---|
| (128,1,102) | Linearization + G&D + MITM | 121.7 | na | <span> &#9733;</span> | [2] |
| (192,1,153) | Linearization + G&D + MITM | 174.4 | na | <span> &#9733;</span> | [2] |
| (256,1,204) | Linearization + G&D + MITM | 226.7 | na | <span> &#9733;</span> | [2] |
| (128,10,9)  | Linearization + G&D + MITM | 117.2 | na | <span> &#9733;</span> | [2] |
| (192,10,15) | Linearization + G&D + MITM | 178.1 | na | <span> &#9733;</span> | [2] |
| (256,10,20) | Linearization + G&D + MITM | 219.4 | na | <span> &#9733;</span> | [2] |

**Partial S-Box Layer with n/s Rounds**

<!--
| (128,1,128) | Linearization + G&D | 121.9 | 17.7 | [1] |
| (192,1,192) | Linearization + G&D | 183.5 | 18.8 | [1] |
| (256,1,256) | Linearization + G&D | 245.5 | 19.6 | [1] |
| (128,10,12) | Linearization + G&D | 117.3 | 17.7 | [1] |
| (192,10,19) | Linearization + G&D | 184.9 | 18.8 | [1] |
| (256,10,25) | Linearization + G&D | 242.9 | 19.6 | [1] |
-->

| (n,s,r) | Method | log_2(T) | log_2(M) | Winner |
|---|---|---|---|--|
| (128,1,128) | Linearization + G&D + MITM | 147   | na | <span> &#9733;</span> | [2] |
| (192,1,192) | Linearization + G&D + MITM | 212.8 | na | <span> &#9733;</span> | [2] |
| (256,1,256) | Linearization + G&D + MITM | 278   | na | <span> &#9733;</span> | [2] |
| (128,10,12) | Linearization + G&D + MITM | 136.6 | na | <span> &#9733;</span> | [2] |
| (192,10,19) | Linearization + G&D + MITM | 208.4 | na | <span> &#9733;</span> | [2] |
| (256,10,25) | Linearization + G&D + MITM | 268.6 | na | <span> &#9733;</span> | [2] |


<!-- **Sources**
[1] https://eprint.iacr.org/2021/255
[2] Private Communication
[3] https://eprint.iacr.org/2021/578
-->


### News and Updates
**19 October 2021**

Updated the results after the third round including the current attack approaches.

**5 January 2021**

Congratulations to the second winners, who are Subhadeep Banik (EPFL), Khashayar Barooti (EPFL), and Serge Vaudenay (EPFL)! [In their paper](https://raw.githubusercontent.com/lowmcchallenge/lowmcchallenge-material/master/docs/lowmc_analysis_2.pdf), they describe new and faster attacks on 2 rounds (full S-box layers) and floor(n/s)*0.8 rounds (partial S-box layers).

**18 August 2020**

The second round is announced. More details about this can be found in our [Crypto 2020 rump session slides](https://raw.githubusercontent.com/lowmcchallenge/lowmcchallenge-material/master/docs/LowMC_crypto_rump2020_v02.pdf).

**17 August 2020**

Congratulations to the first winners, who are Subhadeep Banik (EPFL), Khashayar Barooti (EPFL), F. Betül Durak (Bosch Research), and Serge Vaudenay (EPFL)! [In their paper](https://raw.githubusercontent.com/lowmcchallenge/lowmcchallenge-material/master/docs/lowmc_analysis_1.pdf), they describe a 2-round attack and an attack on floor(n/s)*0.8 rounds, both with lowest complexities. The price they claim is EUR 4k.

**2 June 2020**

[iov42](https://iov42.com/) has joined our sponsors with EUR 50k!

**15 May 2020**

Corrected some mistakes in the reference implementations regarding the plaintext output and a missing matrix multiplication. Thanks to Vukasin Karadzic (TU Darmstadt) for pointing this out.

**13 May 2020**

Challenge started!

### Contact
You've solved a challenge or have any other questions? Let us know by writing an email to [lowmc-challenge@iaik.tugraz.at](mailto:lowmc-challenge@iaik.tugraz.at)!