
from __future__ import print_function
from __future__ import division

import myhdl
from myhdl import (Signal, intbv, always_comb, instance, delay,
                   StopSimulation,)
from rhea.system import Clock, Reset
from rhea.utils.test import run_testbench, tb_args, tb_default_args

from parallella_serdes import parallella_serdes


def test_parallella_serdes(args=None):
    args = tb_default_args(args)

    clock = Clock(0, frequency=50e6)
    reset = Reset(0, active=1, async=True)
    txp = Signal(intbv(0)[6:])
    txn = Signal(intbv(0)[6:])
    rxp = Signal(intbv(0)[6:])
    rxn = Signal(intbv(0)[6:])

    def _bench_serdes():
        tbdut = parallella_serdes(clock, reset, txp, txn, rxp, rxn)
        tbclk = clock.gen()

        @always_comb
        def tblpk():
            rxp.next = txp
            rxn.next = txn

        @instance
        def tbstim():
            yield reset.pulse(32)
            yield clock.posedge

            for ii in range(1000):
                yield clock.posedge

            yield delay(1000)
            raise StopSimulation

        return tbdut, tbclk, tblpk, tbstim

    run_testbench(_bench_serdes, timescale='1ps', args=args)

    myhdl.toVerilog.directory = "output"
    myhdl.toVerilog(parallella_serdes, 
                    clock, reset, txp, txn, rxp, rxn)


if __name__ == '__main__':
    test_parallella_serdes()