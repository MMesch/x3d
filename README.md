# How to produce a working x3d file from obspy:

## Moment tensor:

1. save a mayavi scene as x3d
2. copy the x3d content into the HTML TEMPLATE that is attached at the bottom
   of this text file
3. add true closure nodes, as in the HTML TEMPLATE. E.g. 
   `<DirectionalLight ... on="true"/>`
  becomes:
   `<DirectionalLight ... on="true"></DirectionalLight>`
  This seems to be a major issue with many browsers.
4. another point is to check that the order of the x3d elements is the same as below


## HTML TEMPLATE
```
<html> 
<head> 
    <title>Obspy Moment Tensor</title>		
    <script type='text/javascript' src='http://www.x3dom.org/download/x3dom.js'> </script> 
    <link rel='stylesheet' type='text/css' href='http://www.x3dom.org/download/x3dom.css'></link> 
    <style>
        x3d
        {
            width:80%;
            height:80%;
            display:block;
            position:absolute;
            top:10%;
            left:10%;
            border:1px green;
        }
        body
        {
            background-color: black;
        }
        h1
        {
            text-align:center;
            color:#F7F2E0;
        }
    </style>
</head>
<body> 
    <h1>Obspy Moment Tensor</h1> 
    <X3D showStat="false", version="3.0", width="800px", height="600px">
      <Scene>
      <navigationInfo avatarSize='0.25 1.75 0.75' headlight='false' type='"EXAMINE" "ANY"'></navigationInfo>
      <background skyColor='0.0 0. 0.'></background>
      <viewpoint DEF='Camera' fieldOfView="0.523599" position="4.33517 4.33703 4.33399" description="Default View" orientation="0.187053 0.451587 0.872399 -3.83511" centerOfRotation="1.89543e-05 0.00188345 -0.00116277"></viewpoint>
        <Shape>
          <Appearance>
            <Material ambientIntensity="0" emissiveColor="1 1 1" diffuseColor="1 1 1" specularColor="0 0 0" shininess="0.0078125" transparency="0"/>
          </Appearance>
          <IndexedLineSet colorPerVertex="true" coordIndex="
            0 1 -1 
            2 3 4 -1"/>
            <Coordinate DEF="VTKcoordinates0000" point="
              0 0 1,
              0 8.92286e-18 1.10304,
              8.92286e-19 0.0103041 1.07213,
              0 8.92286e-18 1.10304,
              -8.92286e-19 -0.0103041 1.07213"></Coordinate>
            <Color DEF="VTKcolors0000" color="
              0.917647 1 0,
              0.917647 1 0,
              0.917647 1 0,
              0.917647 1 0,
              0.917647 1 0"></Color>
          </IndexedLineSet>
        </Shape>
      </Transform>
      <DirectionalLight direction="-0.5 -0.707107 -0.5" color="1 1 1" intensity="1" on="true"></DirectionalLight>
      <DirectionalLight direction="0.75 0.5 -0.433013" color="1 1 1" intensity="0.6" on="true"></DirectionalLight>
      <DirectionalLight direction="-0.75 0.5 -0.433013" color="1 1 1" intensity="0.5" on="true"></DirectionalLight>
      <DirectionalLight direction="0 0 -1" color="1 1 1" intensity="1" on="false"></DirectionalLight>
      </scene>
    </X3D>
</body> 
</html>
```
