def test_coastlines():
    import nzgeom.coastlines
    import geopandas

    c = nzgeom.coastlines.get_NZ_coastlines()
    assert isinstance(c, geopandas.GeoDataFrame)
    assert len(c) == 9139  # there should be 9139 polygons in the dataframe


def test_regions():
    import nzgeom.regions
    import geopandas
    import shapely

    r = nzgeom.regions.NZRegions()
    r.list_regions()

    all_regions = [
        "Northland Region",
        "Auckland Region",
        "Waikato Region",
        "Bay of Plenty Region",
        "Gisborne Region",
        "Hawke's Bay Region",
        "Taranaki Region",
        "Manawatu-Wanganui Region",
        "Wellington Region",
        "West Coast Region",
        "Canterbury Region",
        "Otago Region",
        "Southland Region",
        "Tasman Region",
        "Nelson Region",
        "Marlborough Region",
        "Area Outside Region",
    ]
    for this_region in all_regions:
        gdf = r.get_region_geodataframe(this_region)
        assert isinstance(gdf, geopandas.GeoDataFrame)

    for this_region in all_regions:
        p = r.get_region_polygon(this_region)
        print(this_region, p)
        assert isinstance(p, shapely.geometry.Polygon) or isinstance(
            p, shapely.geometry.MultiPolygon
        )
