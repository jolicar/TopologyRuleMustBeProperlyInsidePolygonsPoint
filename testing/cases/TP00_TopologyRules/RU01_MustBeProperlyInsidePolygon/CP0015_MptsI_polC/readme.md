## TP00RU01CP0015 Test that incorrect 2D multipoints don't are inside 2D polygon. 

[First, check the open issues of this test](https://redmine.gvsig.net/redmine/projects/gvsig-desktop/issues?utf8=%E2%9C%93&set_filter=1&f%5B%5D=status_id&op%5Bstatus_id%5D=o&f%5B%5D=subject&op%5Bsubject%5D=%7E&v%5Bsubject%5D%5B%5D=TP00RU01CP0015&f%5B%5D=&c%5B%5D=tracker&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=subject&c%5B%5D=assigned_to&c%5B%5D=updated_on&group_by=)

### Description

This test case checks the topology rule when we use incorrect 2D multipoint dataset and 2D polygon dataset. One geometry of one multipoint are not inside of the polygons. The final result generates a error.

### Requirements

1. Have *gvSIG desktop 2.5.1* and *Topology framework plugin* installed.
2. Have acces to [**TP00RU01CP0015_pol2D_C.csv**](https://github.com/jolicar/TopologyRuleMustBeProperlyInsidePolygonsPoint/blob/master/testing/cases/TP00_TopologyRules/RU01_MustBeProperlyInsidePolygon/CP0015_MptsI_polC/TP00RU01CP0015_pol2D_C.csv) and [**TP00RU01CP0015_Mpts2D_I.csv**](https://github.com/jolicar/TopologyRuleMustBeProperlyInsidePolygonsPoint/blob/master/testing/cases/TP00_TopologyRules/RU01_MustBeProperlyInsidePolygon/CP0015_MptsI_polC/TP00RU01CP0015_Mpts2D_I.csv) files.

### Steps...

1. Load the layer **TP00RU01CP0015_pol2D_C.csv** in the view.
2. Load the layer **TP00RU01CP0015_Mpts2D_I.csv** in the view.
3. Create a new empty topology plan.
4. Fill the basic topology plan data.
5. Add the **TP00RU01CP0015_pol2D_C.csv** file like a dataset.
6. Add the **TP00RU01CP0015_Mpts2D_I.csv** file like a dataset.
7. Add a new rules parameters on Rules tab.
8. On those rule parameters identify the *primary dataset*, the *second dataset*, the *Must Be Properly Inside topology rule* and the *tolerancy*. This tolerancy can be zero or greater.
9. Click on the "Ok" button.
10. Click on the "Ok" button to finish the topology plan creation.
11. Execute the topology plan.

### Expected result

The expected results are the *Inspector de errores del Plan de topologia* window have one record. The point with ID equals to 1 does false the rule, one of his geometries is out of polygons.


### Bug report


In case the obtained results are not correct, you can report an issue on *redmine* of *gvSIG deskop*. You can locate at
https://redmine.gvsig.net/redmine/projects/gvsig-desktop/issues .

[Open a a new issue of this test](https://redmine.gvsig.net/redmine/projects/gvsig-desktop/issues/new?issue[subject]=TP00RU01CP0015+Test+that+incorrect+2D+multipoints+dont+are+inside+2D+polygon)