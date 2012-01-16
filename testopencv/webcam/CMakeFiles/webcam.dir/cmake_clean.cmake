FILE(REMOVE_RECURSE
  "webcam.pdb"
  "webcam"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/webcam.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
