project( objectDetection2 )
find_package( OpenCV REQUIRED )
add_executable( objectDetection2 objectDetection2 )
target_link_libraries( objectDetection2 ${OpenCV_LIBS} )
