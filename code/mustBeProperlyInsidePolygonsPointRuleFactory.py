# encoding: utf-8

import gvsig
import sys

from gvsig import uselib
uselib.use_plugin("org.gvsig.topology.app.mainplugin")

from org.gvsig.fmap.geom import Geometry
from org.gvsig.tools.util import ListBuilder
from org.gvsig.topology.lib.api import TopologyLocator
from org.gvsig.topology.lib.spi import AbstractTopologyRuleFactory

from mustBeProperlyInsidePolygonsPointRule import MustBeProperlyInsidePolygonsPointRule

class MustBeProperlyInsidePolygonsPointRuleFactory(AbstractTopologyRuleFactory):
      
    def __init__(self):
        AbstractTopologyRuleFactory.__init__(
            self,
            "MustBeProperlyInsidePolygonsPoint",
            "Must Be Properly Inside Polygons Point Rule JOC",
            "The rule evaluates the point situation in or out polygons. This point's rule return True when the points falls within the polygon's area, not on the boundary or out of it.\n NOTE 1: If the Tolerance equals zero, the rule does as above. If the tolerance is greater than zero, the point are transformed into polygon. If one point of this new polygon are inside of dataset 2 polygon, the rule return True.\n NOTE 2: The behavior of the rule in multigeometries is simple. For multipoints, if all of their geometries are within the polygon or multipoligon, the rule returns True. For Multipolygon, if one of these geometries has at least one point or multipoint inside, the rule returns True.",
            ListBuilder().add(Geometry.TYPES.POINT).add(Geometry.TYPES.MULTIPOINT).asList(),
            ListBuilder().add(Geometry.TYPES.POLYGON).add(Geometry.TYPES.MULTIPOLYGON).asList()
        )
    
    def createRule(self, plan, dataSet1, dataSet2, tolerance):
        rule = MustBeProperlyInsidePolygonsPointRule(plan, self, tolerance, dataSet1, dataSet2)
        return rule

def selfRegister():
    try:
        manager = TopologyLocator.getTopologyManager()
        manager.addRuleFactories(MustBeProperlyInsidePolygonsPointRuleFactory())
    except:
        ex = sys.exc_info()[1]
        gvsig.logger("Can't register rule. Class Name: " + ex.__class__.__name__ + ". Exception: " + str(ex), gvsig.LOGGER_ERROR)

def main(*args):
    pass