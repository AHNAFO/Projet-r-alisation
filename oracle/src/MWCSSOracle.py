import z3
import struct

from Predictor import Predictor

#attend un tabeau de 5 éléments 
class MWCSSOracle(Predictor):

    def __init__(self):
        super().__init__("MWCSS", "tab")

    def predictNextNumber(self):
        sequence = self.getNumberSequence()[-5:]

        sequence = sequence[::-1]

        solver = z3.Solver()

        se_state0, se_state1 = z3.BitVecs("se_state0 se_state1", 64)

        for i in range(len(sequence)):

            se_s1 = se_state0
            se_s0 = se_state1
            se_state0 = se_s0
            se_s1 ^= se_s1 << 23
            se_s1 ^= z3.LShR(se_s1, 17)  # Logical shift instead of Arthmetric shift
            se_s1 ^= se_s0
            se_s1 ^= z3.LShR(se_s0, 26)
            se_state1 = se_s1

            float_64 = struct.pack("d", sequence[i] + 1)
            u_long_long_64 = struct.unpack("<Q", float_64)[0]

            # Get the lower 52 bits (mantissa)
            mantissa = u_long_long_64 & ((1 << 52) - 1)

            # Compare Mantissas
            solver.add(int(mantissa) == z3.LShR(se_state0, 12))


        if solver.check() == z3.sat:
            model = solver.model()

            states = {}
            for state in model.decls():
                states[state.__str__()] = model[state]

            state0 = states["se_state0"].as_long()

            u_long_long_64 = (state0 >> 12) | 0x3FF0000000000000
            float_64 = struct.pack("<Q", u_long_long_64)
            next_sequence = struct.unpack("d", float_64)[0]
            next_sequence -= 1

            self.setNextNumberPredicted(next_sequence)