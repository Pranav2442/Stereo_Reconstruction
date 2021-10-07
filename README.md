




# Stereo_Reconstruction

The general idea of the stereo reconstruction algorithm which reconstructs depth information from two camera views. 

## Stereo Pair

A stereo-pair image contains two views of a scene side by side. One of the views is intended for the left eye and the other for the right eye. 

##Types of Projections:-

1) Eucledian or Isometric transformation:-<br/>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; Whenever Image is transformed or rotated around any point is called as Eucledian transfrom.Eucledian transform is a subset of affine transform.

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;a) Distance is Preserved.<br/>

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;b) Angles are preserved.<br/>

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;c) Shapes are preserved.<br/>

<br/>
<br/>

2) Affine Transformation:-<br/>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;A transformation that can be expressed in the form of a matrix multiplication (linear transformation) followed by a vector addition (translation).There are 6 degrees of freedom.2 Degrres for translation,1 for rotation, 1 for scaling,1 for scaling direction and 1 for scaling ratio.Using 2*3 matrix It can be rotated,sheared,translated and scale the image.<br/>

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; a) Square won't be square <br/>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; b) Parallel lines are preserved but many be sheared.<br/>

3) Projective Transform :- <br/>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; A projective transformation is a transformation used in projective geometry: it is the composition of a pair of perspective projections. It describes what happens to the perceived positions of observed objects when the point of view of the observer changes. 

## Difference Between Projective and Affine Transformations :- <br/>
<br/><br/>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; a) In the projective transformation parallelism,length and angles are not preserved but it can preserve &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;collinearity and incidence.<br/>

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;b) As the Affine transformation is a special case of the projective transformation,it has the same &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;properties.It preserves parallelism.







                                      
