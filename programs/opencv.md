# OpenCV 2.4

> Source: http://www.opencv.org

$ Key Classes
    `Point_                        {{Template 2D Point Class}} 
    `Point3_                       {{Template 3D Point Class}} 
    `Size_                         {{Template Size Class}} 
    `Vec                           {{Template Short Vector Class}} 
    `Matx                          {{Template Small Matrix Class}} 
    `Range                         {{Integer Val Range}} 
    `SparseMat                     {{Multidimensional Sparse Array}} 
    `Ptr                           {{Template Smart Pointer Class}} 

$ Geometrical Transformations
    `resize()                      {{Resize Image}} 
    `getRectSubPix()               {{Extract image patch}} 
    `warpAffine()                  {{Warp image affinely}} 
    `warpPerspective()             {{Warp image perspectively}} 
    `remap()                       {{Generic image warping}} 
    `convertMaps()                 {{Optimise images for faster remap()}} 

$ Image Transformations
    `cvtColor()                    {{Convert image to different color space}} 
    `threshold()                   {{Convert greyscale image to binary image}} 
    `integral()                    {{Compute integral image}} 
    `distanceTransform()           {{Build distance map}} 
    `watershed()                   {{[Marker based image segmentation]}} 

$ Histograms
    `calcHist()                    {{Compute image histogram}} 
    `calcBackProject()             {{Back project the histogram}} 
    `equalizeHist()                {{Normalize brightness and contrast}} 
    `compareHist()                 {{Compare two histograms}} 

$ Matrix Manipulations
    `src.copyTo(dst)               {{Copy matrix to another one}} 
    `m.clone()                     {{Make deep copy of matrix}} 
    `m.row(i)                      {{Take a matrix row}} 
    `m.repeat(ny,nx)               {{Make a bigger matrix from smaller one}} 
    `split(...)                    {{Split multi channel matrix into separate channels}} 
    `merge(...)                    {{Make a multi channel matrix from separate channels}} 

$ Filtering
    `filter2D()                    {{Non-separable linear filter}} 
    `sepFilter2D()                 {{Separable linear filter}} 
    `Sobel()                       {{Compute spatial image derivative}} 
    `Laplacian()                   {{Compute Laplacian}} 
    `erode()                       {{Morphological Operation}} 

$ Simple GUI
    `namedWindow(winname,flags)    {{Create named highgui window}} 
    `destroyWindow(winname)        {{Destroy specified window}} 
    `imshow(winname,mtx)           {{Show image in window}} 
    `setMouseCallback(...)         {{Set callback on mouse clicks}} 

$ Camera
    `calibrateCamera()             {{Calibrate camera from several views}} 
    `solvePnP()                    {{Find object pose from known projections}} 
    `stereoCalibrate()             {{Calibrate stereo camera}} 
    `stereoRectify()               {{Compute rectification transforms}} 
    `findHomography()              {{Find best fit perspective transform}} 

$ Object Detection
    `matchTemplate                 {{Compute proximity map for given template}} 
    `CascadeClassifier             {{Suits for detecting facial features and some other objects}} 
    `HOGDescriptor                 {{Object detector using Histogram-of-Oriented-Gradients}} 

