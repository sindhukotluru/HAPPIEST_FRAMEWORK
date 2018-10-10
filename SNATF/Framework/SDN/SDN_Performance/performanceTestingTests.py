from __future__ import absolute_import
import unittest
from SdnBenchmarking import SdnBenchmarking


class SdnBenchmarkTest(unittest.TestCase):


    def testThroughput(self):
        odlcontroller = '10.22.18.51'
        onoscontroller = '10.22.20.73'
        sdnob = SdnBenchmarking()

        #Test ODL
        print "-------------THROUGHPUT-----------------------"
        print "TestCaseID           : TC5"
        print "Time (ms)            : 1000"
        print "Loop                 : 5"
        print "Switches             : 5"
        print "Hosts                : 100"
        print "----------------------------------------------"




        print "Start Cbench Throughput test with ODL : {}".format(odlcontroller)


        odlThroughput = sdnob.cbench_throughput(controller = odlcontroller,
                  port = '6633',
                  loops = 5,
                  msPerTest = 1000,
                  macPerSwitch = 100,
                  startupDelay = 100,
                  warmup = 1,
                  switch = 5)

        #Test ONOS
        print "Start Cbench Throughput test with ONOS : {}\n".format(onoscontroller)

        onosThroughput = sdnob.cbench_throughput(controller=onoscontroller,
                                                port='6633',
                                                loops=5,
                                                msPerTest=1000,
                                                macPerSwitch=100,
                                                startupDelay=100,
                                                warmup=1,
                                                switch=5)




        #compare output
        print "----------------------------------------------"
        print "-----------------TEST RESULTS-----------------"
        print "Performance Throughput Test ODL and ONOS : \nODL Throughput : {} responses/sec \nONOS Throughput : {} responses/sec  \n".format(odlThroughput, onosThroughput)

        self.assertIsNotNone(odlThroughput,msg="ODL returned None value")
        self.assertIsNotNone(onosThroughput, msg="ONOS returned None value")
        if odlThroughput != None:
            if onosThroughput !=None:
                if odlThroughput > onosThroughput:
                    print "Conclusion : ODL performs better than ONOS"
                    #print "Performance Throughput Test ODL and ONOS : \nODL Throughput : {} responses/sec \nONOS Throughput : {} responses/sec  \nConclusion : ODL performs better than ONOS".format(odlThroughput, onosThroughput)
                else:
                    print "Conclusion : ONOS performs better than ODL"
                    #print "Performance Throughput Test over ODL and ONOS : \nODL Throughput : {} responses/sec \nONOS Throughput : {} responses/sec \nConclusion : ONOS performs better than ODL".format(odlThroughput, onosThroughput)

        print "----------------------------------------------"



    def testLatency(self):
        odlcontroller = '10.22.18.51'
        onoscontroller = '10.22.20.73'
        sdnob = SdnBenchmarking()
        #Test ODL
        print "-------------LATENCY--------------------------"
        print "TestCaseID           : TC5"
        print "Time (ms)            : 1000"
        print "Loop                 : 5"
        print "Switches             : 5"
        print "Hosts                : 100"
        print "----------------------------------------------"

        print "Start Cbench Latency test with ODL : {} ".format(odlcontroller)

        odlLatency = sdnob.cbench_latency(controller = odlcontroller,
                  port = '6633',
                  loops = 5,
                  msPerTest = 1000,
                  macPerSwitch = 100,
                  startupDelay = 100,
                  warmup = 1,
                  switch = 5)


        #Test ONOS

        print "Start Cbench Latency test with ONOS : {} ".format(onoscontroller)

        onosLatency = sdnob.cbench_latency(controller=onoscontroller,
                                                port='6633',
                                                loops=5,
                                                msPerTest=1000,
                                                macPerSwitch=100,
                                                startupDelay=100,
                                                warmup=1,
                                                switch=5)




        #compare output
        print "----------------------------------------------"
        print "-----------------TEST RESULTS-----------------"
        self.assertIsNotNone(odlLatency, msg="ODL returned None value")
        self.assertIsNotNone(onosLatency, msg="ONOS returned None value")
        if odlLatency !=None:
            if onosLatency !=None:
                if odlLatency < onosLatency:
                    print "Performance Latency Test over ODL and ONOS : \nODL Latency : {} ms \nONOS Latency : {} ms \nConclusion : ODL performs better than ONOS".format(odlLatency, onosLatency)
                else:
                    print "Performance Latency Test over ODL and ONOS : \nODL Latency : {} ms; \nONOS Latency : {} ms \nConclusion : ONOS performs better than ODL".format(odlLatency, onosLatency)
        print "----------------------------------------------"

if __name__ == '__main__':
    unittest.main()
