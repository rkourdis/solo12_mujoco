### URDF

- Added XYZ parameters (meshes and optimization) to `robot_properties_solo`

- Converted with MuJoCo (`compile.exe`)

- Added comments

### Visuals

- Coloured elements in Solidworks

- Exported as `.ply` to preserve colours
  
  - `does solidworks not do obj?`

- Created reference points at the locations used for the simplified meshes in Solidworks and used Measure to figure out coordinates

- Rotated / Translated in Meshlab to match axes and exported as `.obj`
  
  - `something about 3mf saved to obj not working in obj2mjcf, why did I export to 3mf? for the axes?`

- Ran `obj2mjcf` on visuals to separate materials:
  
  ```
  obj2mjcf --obj-dir ./ --save-mjcf --compile-model --verbose
  ```

- Fixed Alpha and merged with the collision .xml's

- Removed unnecessary components:
  
  - `TODO`

- Removed unnecessary materials and extracted them in a common asset file:
  
  - `TODO`

- Simplified by using a single mesh file but rotated

### Collisions

- Converted from `.stl` to `.obj`

- Ran `obj2mjcf`the simplified meshes to convex decompose:
  
  ```bash
   obj2mjcf --obj-dir .\obj\ --save-mjcf --compile-model --verbose --vhacd-args.enable --vhacd-args.max-output-convex-hulls 16 --vhacd-args.max-hull-vert-count 128 --vhacd-args.split-hull --vhacd-args.voxel-resolution 1000000 --vhacd-args.volume-error-percent 0.1 --overwrite
  ```
  
  - Multiple iterations to avoid crashes during compilation due to weird decompositions



### Failed Attempts

1. Using AO to simplify meshes easily:
   
   - Didn't preserve colours, see stackoverflow

2- 
















