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
CMAKE_SOURCE_DIR = /Users/MAB/Downloads/testopencv/webcam

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/MAB/Downloads/testopencv/webcam

# Include any dependencies generated for this target.
include CMakeFiles/webcam.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/webcam.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/webcam.dir/flags.make

CMakeFiles/webcam.dir/webcam.o: CMakeFiles/webcam.dir/flags.make
CMakeFiles/webcam.dir/webcam.o: webcam.c
	$(CMAKE_COMMAND) -E cmake_progress_report /Users/MAB/Downloads/testopencv/webcam/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building C object CMakeFiles/webcam.dir/webcam.o"
	/usr/bin/gcc  $(C_DEFINES) $(C_FLAGS) -o CMakeFiles/webcam.dir/webcam.o   -c /Users/MAB/Downloads/testopencv/webcam/webcam.c

CMakeFiles/webcam.dir/webcam.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/webcam.dir/webcam.i"
	/usr/bin/gcc  $(C_DEFINES) $(C_FLAGS) -E /Users/MAB/Downloads/testopencv/webcam/webcam.c > CMakeFiles/webcam.dir/webcam.i

CMakeFiles/webcam.dir/webcam.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/webcam.dir/webcam.s"
	/usr/bin/gcc  $(C_DEFINES) $(C_FLAGS) -S /Users/MAB/Downloads/testopencv/webcam/webcam.c -o CMakeFiles/webcam.dir/webcam.s

CMakeFiles/webcam.dir/webcam.o.requires:
.PHONY : CMakeFiles/webcam.dir/webcam.o.requires

CMakeFiles/webcam.dir/webcam.o.provides: CMakeFiles/webcam.dir/webcam.o.requires
	$(MAKE) -f CMakeFiles/webcam.dir/build.make CMakeFiles/webcam.dir/webcam.o.provides.build
.PHONY : CMakeFiles/webcam.dir/webcam.o.provides

CMakeFiles/webcam.dir/webcam.o.provides.build: CMakeFiles/webcam.dir/webcam.o

# Object files for target webcam
webcam_OBJECTS = \
"CMakeFiles/webcam.dir/webcam.o"

# External object files for target webcam
webcam_EXTERNAL_OBJECTS =

webcam: CMakeFiles/webcam.dir/webcam.o
webcam: CMakeFiles/webcam.dir/build.make
webcam: CMakeFiles/webcam.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking C executable webcam"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/webcam.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/webcam.dir/build: webcam
.PHONY : CMakeFiles/webcam.dir/build

CMakeFiles/webcam.dir/requires: CMakeFiles/webcam.dir/webcam.o.requires
.PHONY : CMakeFiles/webcam.dir/requires

CMakeFiles/webcam.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/webcam.dir/cmake_clean.cmake
.PHONY : CMakeFiles/webcam.dir/clean

CMakeFiles/webcam.dir/depend:
	cd /Users/MAB/Downloads/testopencv/webcam && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/MAB/Downloads/testopencv/webcam /Users/MAB/Downloads/testopencv/webcam /Users/MAB/Downloads/testopencv/webcam /Users/MAB/Downloads/testopencv/webcam /Users/MAB/Downloads/testopencv/webcam/CMakeFiles/webcam.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/webcam.dir/depend
