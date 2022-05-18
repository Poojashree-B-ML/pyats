import logging

from pyats import aetest

logger = logging.getLogger(__name__)
class CommonSetup(aetest.CommonSetup):

    @aetest.subsection
    def check_topology(self,
                       testbed):

        assert testbed

        testbed.connect()


class GetTestcase(aetest.Testcase):

    @aetest.setup
    def setup(self):
        pass

    @aetest.test
    def test(self):
        pass

    @aetest.cleanup
    def cleanup(self):
        pass

class CommonCleanup(aetest.CommonCleanup):
    '''CommonCleanup Section
    < common cleanup docstring >
    '''

if __name__ == '__main__':
    import argparse
    from pyats.topology import loader

    parser = argparse.ArgumentParser()
    parser.add_argument('--testbed', dest = 'testbed',
                        type = loader.load)

    args, unknown = parser.parse_known_args()

    aetest.main(**vars(args))
