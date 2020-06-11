# Must be properly inside polygons Topology Rule
![TopologyRuleMustBeProperlyInsidePolygonsPoint](https://github.com/jolicar/TopologyRuleMustBeProperlyInsidePolygonsPoint/blob/master/img/TP00R01_img1.png)
* **Rule type:** *Point rule*
* **Primary dataset:** Point dataset (2D, 2DM, 3D and 3DM) (*Multygeometry allowed*)
* **Secundary dataset:** Polygon dataset (2D, 2DM, 3D and 3DM) (*Multygeometry allowed*)
* **Brief description:** The rule evaluates the point situation in or out polygons. This point's rule return *True* when the points falls within the polygon's area, not on the boundary or out of it. The red points does the rule false and the green points give a positive result on the rule. In 2DM, 3D and 3DM formats, the Z coordinate or M coordinate are ignored.

***NOTE 1:** When the Tolerance equals zero, the rule does the above. If the tolerance is greater than zero, the point are transformed into "polygon". If one point of this new polygon are inside of dataset 2 polygon, the rule return True.*

***NOTE 2:** The behavior of the rule in multigeometries is simple. For multipoints, if all of their geometries are within the polygon or multipoligon, the rule returns True. For Multipolygon, if one of these geometries has at least one point or multipoint inside, the rule returns True.*

* **Potential fixes actions:** 
	- **Delete** The delete action removes points features for cases when *Must be properly inside polygons* Topology Rule it is false.

***NOTE 3:** The behavior of the delete action in multigeometries is simple. If one of multipoint geometry is outside a polygon o or multipolygon, the action removes the multipoint completely.*

#### [*Back to GSoC2020 Project Wiki*](https://github.com/jolicar/GSoC2020/wiki/GSoC2020-New-rules-for-the-Topology-Framework-in-gvSIG-Desktop)