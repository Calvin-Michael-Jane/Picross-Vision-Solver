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
CMAKE_SOURCE_DIR = /Users/MAB/Downloads/testopencv/face_track

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/MAB/Downloads/testopencv/face_track

# Include any dependencies generated for this target.
include CMakeFiles/objectDetection.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/objectDetection.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/objectDetection.dir/flags.make

CMakeFiles/objectDetection.dir/objectDetection.o: CMakeFiles/objectDetection.dir/flags.make
CMakeFiles/objectDetection.dir/objectDetection.o: objectDetection.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /Users/MAB/Downloads/testopencv/face_track/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object CMakeFiles/objectDetection.dir/objectDetection.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/objectDetection.dir/objectDetection.o -c /Users/MAB/Downloads/testopencv/face_track/objectDetection.cpp

CMakeFiles/objectDetection.dir/objectDetection.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/objectDetection.dir/objectDetection.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /Users/MAB/Downloads/testopencv/face_track/objectDetection.cpp > CMakeFiles/objectDetection.dir/objectDetection.i

CMakeFiles/objectDetection.dir/objectDetection.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/objectDetection.dir/objectDetection.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /Users/MAB/Downloads/testopencv/face_track/objectDetection.cpp -o CMakeFiles/objectDetection.dir/objectDetection.s

CMakeFiles/objectDetection.dir/objectDetection.o.requires:
.PHONY : CMakeFiles/objectDetection.dir/objectDetection.o.requires

CMakeFiles/objectDetection.dir/objectDetection.o.provides: CMakeFiles/objectDetection.dir/objectDetection.o.requires
	$(MAKE) -f CMakeFiles/objectDetection.dir/build.make CMakeFiles/objectDetection.dir/objectDetection.o.provides.build
.PHONY : CMakeFiles/objectDetection.dir/objectDetection.o.provides

CMakeFiles/objectDetection.dir/objectDetection.o.provides.build: CMakeFiles/objectDetection.dir/objectDetection.o

# Object files for target objectDetection
objectDetection_OBJECTS = \
"CMakeFiles/objectDetection.dir/objectDetection.o"

# External object files for target objectDetection
objectDetection_EXTERNAL_OBJECTS =

objectDetection: CMakeFiles/objectDetection.dir/objectDetection.o
objectDetection: CMakeFiles/objectDetection.dir/build.make
objectDetection: CMakeFiles/objectDetection.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX executable objectDetection"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/objectDetection.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/objectDetection.dir/build: objectDetection
.PHONY : CMakeFiles/objectDetection.dir/build

CMakeFiles/objectDetection.dir/requires: CMakeFiles/objectDetection.dir/objectDetection.o.requires
.PHONY : CMakeFiles/objectDetection.dir/requires

CMakeFiles/objectDetection.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/objectDetection.dir/cmake_clean.cmake
.PHONY : CMakeFiles/objectDetection.dir/clean

CMakeFiles/objectDetection.dir/depend:
	cd /Users/MAB/Downloads/testopencv/face_track && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/MAB/Downloads/testopencv/face_track /Users/MAB/Downloads/testopencv/face_track /Users/MAB/Downloads/testopencv/face_track /Users/MAB/Downloads/testopencv/face_track /Users/MAB/Downloads/testopencv/face_track/CMakeFiles/objectDetection.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/objectDetection.dir/depend
