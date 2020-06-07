# Must be properly inside polygons Topology Rule
![TopologyRuleMustBeProperlyInsidePolygonsPoint](https://github.com/jolicar/TopologyRuleMustBeProperlyInsidePolygonsPoint/blob/master/img/TP00R01_img1.png)
* **Rule type:** *Point rule*
* **Primary dataset:** Point dataset (2D, 2DM, 3D and 3DM) (*Multygeometry allowed*)
* **Secundary dataset:** Polygon dataset (2D, 2DM, 3D and 3DM) (*Multygeometry allowed*)
* **Brief description:** The rule evaluates the point situation in or out polygons. This point's rule return *True* when the points falls within the polygon's area, not on the boundary or out of it. The red points does the rule false and the green points give a positive result on the rule. In 2DM, 3D and 3DM formats, the Z coordinate or M coordinate are ignored.
* **Potential fixes actions:** 
	- **Delete** The delete action removes points features for cases when *Must be properly inside polygons* Topology Rule it is false.

#### [*Back to GSoC2020 Project Wiki*](https://github.com/jolicar/GSoC2020/wiki/GSoC2020-New-rules-for-the-Topology-Framework-in-gvSIG-Desktop)