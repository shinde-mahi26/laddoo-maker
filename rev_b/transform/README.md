# Transformation studio

Interactive Three.js choreography and a 36-second 1280x720, 30 fps WebM film. All 55 image catalogue types have a 3D representative: the existing 46 source CAD instances plus 42 illustrative hardware instances. Fastener quantities and placements are visual proposals, not an engineering BOM. Purchased-component detailing is procedural illustration; it is not an image-to-CAD reconstruction.

The sequence starts with the whole machine, releases fittings and the guard, spreads the component groups, pauses in an exploded pose, then returns to the original assembly coordinates. Paths, rotations and timing are cinematic rather than collision-checked service instructions. CAD source files remain unchanged. Motor and electronic interiors are not separately modelled.

Controls: play/pause, timeline scrub, whole-machine and exploded states, drag orbit, scroll zoom, hardware toggle, clickable parts, and searchable image library. Respect reduced-motion preferences by starting paused and disabling camera drift. Video is silent.

Run `node scripts/record_transformation.cjs --preview` to inspect five deterministic keyframes. Run without the flag to render the video using the installed Chromium and FFmpeg. Local server must serve rev_b at port 8767. Run `node scripts/verify_transformation.cjs` for interface checks. Run `python scripts/package_explorer.py` to stage the site for GitHub Pages.
