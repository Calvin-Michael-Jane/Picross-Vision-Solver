project( webcam )
find_package( OpenCV REQUIRED )
add_executable( webcam webcam )
target_link_libraries( webcam ${OpenCV_LIBS} )
