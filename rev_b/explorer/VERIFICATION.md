# Viewer verification — 8 September 2026

Tested the running local app in the Codex in-app Chromium browser at desktop 1280 × 720 and mobile 390 × 844. Inspected actual rendered assembly, isolated dimensions, parts atlas, mobile panels and process mode. No application console errors were recorded. The existing bundled Three.js emits its legacy-script deprecation warning.

## Browser integration: 18 / 18 passed

- WebGL initialization and 46 distinct stable IDs.
- Explosion moves source parts; assemble restores exact positions and identity orientations for every instance.
- Scoped explosion leaves other subassemblies at their original transforms.
- Tree and inspector select the correct physical instance.
- Dimension labels match the source and remain unchanged while exploding.
- Isolate preserves the chosen part; independent 90-degree rotation works.
- Hide, restore and related-assembly visibility work.
- All separated CAD bounding boxes are non-overlapping.
- Grid and BOM selections synchronize with the inspector.
- Empty search explains the empty state; reset restores all 46 instances and exact transforms.

The repeatable in-app checks are available at `?verify`. They exercise actual renderer objects and UI handlers, not a physics simulation. The complete original pose was compared after transition settling, not merely the requested slider value.

## Direct browser interaction

- Search `RB-20` selects the tipping weigh cup and its `96 × 96 × 60 mm` source record.
- Isolate and dimension controls show the actual cup, extension lines, arrowheads and unit labels.
- Direct mobile model click on the hopper selected `RB-10 / Open hopper cassette`.
- Mobile components panel, inspector open/close and reset work. Document width and viewport width both measured 390 px: no horizontal page overflow.
- Selecting the levelling-foot CAD tile selects `RB-020`.
- BOM search `weigh` returns the cup, cell, cradle and actuator; the modal scrolls horizontally on mobile.
- Direct CSV file download returned a browser download event. The earlier blob-based export did not produce a reliable event in the host, so it was replaced with the generated local CSV asset.
- Process next-step control displays the documented weigh-and-tip step and its illustrative-motion notice.

## Independent downloadable-asset verification

`asset-verification.json` records checks for every one of the 46 parts:

- Original STEP SHA-256 matches the catalog; source CAD files are unchanged.
- STEP declares millimetre units.
- Independently imported STEP bounding boxes match the record within 0.02 mm rounding tolerance.
- Binary STL triangle count and byte length match the original tessellation.
- STL bounds match source tessellation coordinates within 0.001 mm float precision.

No new CAD rebuild was necessary. These checks establish source fidelity and viewer behavior, not fabrication readiness, complete interference clearance, guarding compliance, food performance or production capacity. Fullscreen is browser-host dependent and was not included in the passing checks.
