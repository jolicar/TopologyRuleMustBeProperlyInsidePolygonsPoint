# encoding: utf-8

import gvsig
import sys

from org.gvsig.topology.lib.spi import AbstractTopologyRuleAction

class DeletePointAction(AbstractTopologyRuleAction):
    
    def __init__(self):
        AbstractTopologyRuleAction.__init__(
            self,
      "mustBeProperlyInsidePolygonsPoint",
            "DeletePointAction",
            "Delete Point Action",
            "The delete action removes points features for cases when Must be properly inside polygons Topology Rule it is false. This point's rule return True when the points falls within the polygon's area, not on the boundary or out of it."
        )
    
    def execute(self, rule, line, parameters):
        try:
            dataSet = rule.getDataSet1()
            dataSet.delete(line.getFeature1())
        except:
            ex = sys.exc_info()[1]
            gvsig.logger("Can't execute action. Class Name: " + ex.__class__.__name__ + ". Exception: " + str(ex), gvsig.LOGGER_ERROR)

def main(*args):
    pass