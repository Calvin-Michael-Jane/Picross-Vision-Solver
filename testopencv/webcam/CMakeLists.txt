project( webcam )
find_package( OpenCV REQUIRED )
add_executable( webcam webcam )
target_link_libraries( webcam ${OpenCV_LIBS} )
SET_TARGET_PROPERTIES(webcam PROPERTIES LINKER_LANGUAGE C)
