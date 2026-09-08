# Individual component image catalogue

55 separate AI-generated concept illustrations: 39 current CAD component types and 16 proposed hardware types. Repeated physical instances share their type image. Generated using the built-in imagegen tool; generation prompts are recorded in prompts.json (first batch entries are reconstructed summaries).

`references/` contains direct VTK renders of the source CAD tessellation used to guide the illustrations. These are references, not AI images. `manifest.json` carries source metadata and clearly separates CAD-guided illustrations, proposed detailing of CAD envelopes, and proposed hardware absent from the CAD.

The original STEP files, dimensions, geometry, and engineering status are unchanged. Illustrations may vary in edges, proportions and finish. Simplified shapes remain simplified: the base is a flat sheet, levelling foot lacks its stud, belt cassette shows only modeled belt runs, upper forming cavity is hidden in the chosen view. Proposed motors, electrical components and fittings do not identify selected products or establish fit. Internal motor/electronic components and exact fastener counts are not defined by this catalogue.

Run `python rev_b/build_image_catalog.py` to rebuild metadata, then `python scripts/package_explorer.py` to stage the gallery with the existing GitHub Pages site.
