# encoding: utf-8

import gvsig
import sys

from gvsig import geom
from gvsig import uselib #para cargar plugins, scripting no tiene cargados todos los plugins
uselib.use_plugin("org.gvsig.topology.app.mainplugin")

from org.gvsig.expressionevaluator import GeometryExpressionEvaluatorLocator, ExpressionEvaluatorLocator
from org.gvsig.topology.lib.api import TopologyLocator
from org.gvsig.topology.lib.spi import AbstractTopologyRule
from org.gvsig.fmap.geom import GeometryLocator

from deletePointAction import DeletePointAction

class MustBeProperlyInsidePolygonsPointRule(AbstractTopologyRule):


  def __init__(self, plan, factory, tolerance, dataSet1, dataSet2):
      AbstractTopologyRule.__init__(self, plan, factory, tolerance, dataSet1, dataSet2)
      self.addAction(DeletePointAction())

      self.expression = ExpressionEvaluatorLocator.getManager().createExpression()
      self.expressionBuilder = GeometryExpressionEvaluatorLocator.getManager().createExpressionBuilder()
      self.geomName=None


  def contains(self, point1, dataSet2):
    if dataSet2.getSpatialIndex() != None:
      for featureReference in dataSet2.query(point1): # change query for getFeaturesThatEnvelopeIntersectsWith
        feature2 = featureReference.getFeature()
        polygon2 = feature2.getDefaultGeometry()
        if polygon2.contains(point1):
          return  True
      return False

    if self.geomName==None:
      store2 = dataSet2.getFeatureStore()
      self.geomName = store2.getDefaultFeatureType().getDefaultGeometryAttributeName()

    self.expression.setPhrase(
      self.expressionBuilder.ifnull(
        self.expressionBuilder.column(self.geomName),
        self.expressionBuilder.constant(False),
        self.expressionBuilder.ST_Contains(
          self.expressionBuilder.column(self.geomName),
          self.expressionBuilder.geometry(point1) 
        )
      ).toString()
    )
    if dataSet2.findFirst(self.expression) != None:
      return True
    return False


  def intersectsWithBuffer(self, point1, dataSet2):
    buffer1 = point1.buffer(self.getTolerance())

    if dataSet2.getSpatialIndex() != None:
      for featureReference in dataSet2.query(buffer1): # change query for getFeaturesThatEnvelopeIntersectsWith
        feature2 = featureReference.getFeature()
        polygon2 = feature2.getDefaultGeometry()
        if polygon2.intersects(buffer1):
          return  True
      return False

    if self.geomName==None:
      store2 = dataSet2.getFeatureStore()
      self.geomName = store2.getDefaultFeatureType().getDefaultGeometryAttributeName()

    self.expression.setPhrase(
      self.expressionBuilder.ifnull(
        self.expressionBuilder.column(self.geomName),
        self.expressionBuilder.constant(False),
        self.expressionBuilder.ST_Intersects(
          self.expressionBuilder.column(self.geomName),
          self.expressionBuilder.geometry(buffer1) 
        )
      ).toString()
    )

    if dataSet2.findFirst(self.expression) != None:
      return True
    return False


  def check(self, taskStatus, report, feature1):
    try:
      point1 = feature1.getDefaultGeometry()
      tolerance = self.getTolerance()
      dataSet2 = self.getDataSet2()
      geometryType1 = point1.getGeometryType()
      
      geomManager = GeometryLocator.getGeometryManager()
      subtype = geom.D2

      mustConvert2D=(not geometryType1.getSubType() == geom.D2)

      if tolerance==0:
        operation=self.contains
      else:
        operation=self.intersectsWithBuffer
        
      if geomManager.isSubtype(geom.POINT,geometryType1.getType()):
        if mustConvert2D:
          proj=point1.getProjection()
          point1 = geomManager.createPoint(point1.getX(),point1.getY(), subtype)
          point1.setProjection(proj)
        if not operation(point1, dataSet2):
          report.addLine(self,
            self.getDataSet1(),
            self.getDataSet2(),
            point1,
            point1,
            feature1.getReference(),
            None,
            -1,
            -1,
            False,
            "The point is not contained by the polygon.",
            ""
          )

      elif geomManager.isSubtype(geom.MULTIPOINT,geometryType1.getType()):
        if mustConvert2D:
          multipoint=geomManager.createMultiPoint(subtype)
          proj=point1.getProjection()
          multipoint.setProjection(proj)
          nPrimitives = point1.getPrimitivesNumber()
          for i in range(0, nPrimitives-1):
            point=point1.getPointAt(i)
            point = geomManager.createPoint(point.getX(),point.getY(), subtype)
            multipoint.addPoint(point)
        else:
          multipoint=point1
        if not operation(multipoint, theDataSet2):
          report.addLine(self,
            self.getDataSet1(),
            self.getDataSet2(),
            point1,
            point,
            feature1.getReference(), 
            None,
            i,
            -1,
            False,
            "The multipoint is not contained by the polygon.",
            ""
        )

      else:
        report.addLine(self,
          self.getDataSet1(),
          self.getDataSet2(),
          point1,
          point1,
          feature1.getReference(),
          None,
          -1,
          -1,
          False,
          "Unsupported geometry type.",
          ""
      )

    except:
      ex = sys.exc_info()[1]
      gvsig.logger("Can't execute rule. Class Name: " + ex.__class__.__name__ + ". Exception: " + str(ex), gvsig.LOGGER_ERROR)


def main(*args):
    pass