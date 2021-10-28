import falcon
import sys
import config
sys.dont_write_bytecode = True

app = falcon.App()

# FRS
from frs.propagation import FRSPropagation
app.add_route("/frs/_propagate", FRSPropagation())

from frs.termination import FRSTermination
app.add_route("/frs/_terminate", FRSTermination())

from frs.lock import Lock
app.add_route("/_lock", Lock())

from frs.unlock import Unlock
app.add_route("/_unlock", Unlock())

# 2PL
from two_pl.propagation import TPLPropagation
app.add_route("/2pl/_propagate", TPLPropagation())

from two_pl.termination import TPLTermination
app.add_route("/2pl/_terminate", TPLTermination())

# common
from common.ycsb import YCSB
app.add_route("/ycsb", YCSB())

from common.test import Test
app.add_route("/_test", Test())

from common.zipf import Zipf
app.add_route("/zipf", Zipf())

from common.ycsb_load import YCSBLoad
app.add_route("/load", YCSBLoad())

from frs.tpcc_load_local import TPCCLoad_Local
app.add_route("/localload_TPCC", TPCCLoad_Local())

from frs.tpcc_load_customer import TPCCLoad_Customer
app.add_route("/customerload_TPCC", TPCCLoad_Customer())

if __name__ == "__main__":
    from wsgiref.simple_server import *
    from socketserver import *
    class ThreadingWsgiServer(ThreadingMixIn, WSGIServer):
        pass

    httpd = make_server('0.0.0.0', 8000, app, ThreadingWsgiServer)
    print("serving on port 8000")
    httpd.serve_forever()
