import generate_matrices
import math
n = 128
s = 10
num_rounds = 14
gen = generate_matrices.grain_ssg()

linear_layer_matrices = []
for _ in range(0, num_rounds):
    linear_layer_matrices.append(generate_matrices.instantiate_matrix(n, n, gen))

round_constants = []
for _ in range(0, num_rounds):
    round_constants.append([next(gen) for _ in range(n)])

round_key_matrices = []
for _ in range(0, num_rounds):
    round_key_matrices.append(generate_matrices.instantiate_matrix(n, n, gen))

def addition(state, operand):
    for i in range(0, n):
        state[i] = state[i] ^ operand[i]
    return state

def matrix_mul(state, matrix):
    new_state = [0] * n
    for i in range(0, n):
        for j in range(0, n):
            new_state[i] = new_state[i] ^ (matrix[i][j] & state[j])
    return new_state

def s_boxes(state, s):
    old_state = state
    for i in range(0, s):
        start = 3*i
        state[start] = old_state[start] ^ (old_state[start + 1] & old_state[start + 2])
        state[start + 1] = old_state[start] ^ old_state[start + 1] ^ (old_state[start] & old_state[start + 2])
        state[start + 2] = old_state[start] ^ old_state[start + 1] ^ old_state[start + 2] ^ (old_state[start] & old_state[start + 1])
    return state

plaintext = [1] * int(math.ceil(n / 2.0)) + [0] * int(math.floor(n / 2.0))
key = [0] * int(math.ceil(n / 2.0)) + [1] * int(math.floor(n / 2.0))
original_key = key

state = plaintext
# Initial key addition
state = addition(state, key)

for r in range(0, num_rounds):
    # S-boxes
    state = s_boxes(state, s)

    # Linear layer
    state = matrix_mul(state, linear_layer_matrices[r])

    # Constants
    state = addition(state, round_constants[r])

    # New round key, add to state
    key = matrix_mul(key, round_key_matrices[r])
    state = addition(state, key)

ciphertext = state

print "P:", plaintext
print "K:", original_key
print "C:", ciphertext