# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canoncical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /opt/local/bin/cmake

# The command to remove a file.
RM = /opt/local/bin/cmake -E remove -f

# The program to use to edit the cache.
CMAKE_EDIT_COMMAND = /opt/local/bin/ccmake

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/MAB/Downloads/testopencv/face_track/2nd

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/MAB/Downloads/testopencv/face_track/2nd

# Include any dependencies generated for this target.
include CMakeFiles/objectDetection2.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/objectDetection2.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/objectDetection2.dir/flags.make

CMakeFiles/objectDetection2.dir/objectDetection2.o: CMakeFiles/objectDetection2.dir/flags.make
CMakeFiles/objectDetection2.dir/objectDetection2.o: objectDetection2.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /Users/MAB/Downloads/testopencv/face_track/2nd/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object CMakeFiles/objectDetection2.dir/objectDetection2.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/objectDetection2.dir/objectDetection2.o -c /Users/MAB/Downloads/testopencv/face_track/2nd/objectDetection2.cpp

CMakeFiles/objectDetection2.dir/objectDetection2.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/objectDetection2.dir/objectDetection2.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /Users/MAB/Downloads/testopencv/face_track/2nd/objectDetection2.cpp > CMakeFiles/objectDetection2.dir/objectDetection2.i

CMakeFiles/objectDetection2.dir/objectDetection2.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/objectDetection2.dir/objectDetection2.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /Users/MAB/Downloads/testopencv/face_track/2nd/objectDetection2.cpp -o CMakeFiles/objectDetection2.dir/objectDetection2.s

CMakeFiles/objectDetection2.dir/objectDetection2.o.requires:
.PHONY : CMakeFiles/objectDetection2.dir/objectDetection2.o.requires

CMakeFiles/objectDetection2.dir/objectDetection2.o.provides: CMakeFiles/objectDetection2.dir/objectDetection2.o.requires
	$(MAKE) -f CMakeFiles/objectDetection2.dir/build.make CMakeFiles/objectDetection2.dir/objectDetection2.o.provides.build
.PHONY : CMakeFiles/objectDetection2.dir/objectDetection2.o.provides

CMakeFiles/objectDetection2.dir/objectDetection2.o.provides.build: CMakeFiles/objectDetection2.dir/objectDetection2.o

# Object files for target objectDetection2
objectDetection2_OBJECTS = \
"CMakeFiles/objectDetection2.dir/objectDetection2.o"

# External object files for target objectDetection2
objectDetection2_EXTERNAL_OBJECTS =

objectDetection2: CMakeFiles/objectDetection2.dir/objectDetection2.o
objectDetection2: CMakeFiles/objectDetection2.dir/build.make
objectDetection2: CMakeFiles/objectDetection2.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX executable objectDetection2"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/objectDetection2.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/objectDetection2.dir/build: objectDetection2
.PHONY : CMakeFiles/objectDetection2.dir/build

CMakeFiles/objectDetection2.dir/requires: CMakeFiles/objectDetection2.dir/objectDetection2.o.requires
.PHONY : CMakeFiles/objectDetection2.dir/requires

CMakeFiles/objectDetection2.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/objectDetection2.dir/cmake_clean.cmake
.PHONY : CMakeFiles/objectDetection2.dir/clean

CMakeFiles/objectDetection2.dir/depend:
	cd /Users/MAB/Downloads/testopencv/face_track/2nd && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/MAB/Downloads/testopencv/face_track/2nd /Users/MAB/Downloads/testopencv/face_track/2nd /Users/MAB/Downloads/testopencv/face_track/2nd /Users/MAB/Downloads/testopencv/face_track/2nd /Users/MAB/Downloads/testopencv/face_track/2nd/CMakeFiles/objectDetection2.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/objectDetection2.dir/depend
