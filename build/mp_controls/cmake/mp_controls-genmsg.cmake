# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "mp_controls: 1 messages, 0 services")

set(MSG_I_FLAGS "-Imp_controls:/home/parthag/mech_ws/src/mp_controls/msg;-Igeometry_msgs:/opt/ros/noetic/share/geometry_msgs/cmake/../msg;-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(mp_controls_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/parthag/mech_ws/src/mp_controls/msg/Path.msg" NAME_WE)
add_custom_target(_mp_controls_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "mp_controls" "/home/parthag/mech_ws/src/mp_controls/msg/Path.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(mp_controls
  "/home/parthag/mech_ws/src/mp_controls/msg/Path.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/mp_controls
)

### Generating Services

### Generating Module File
_generate_module_cpp(mp_controls
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/mp_controls
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(mp_controls_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(mp_controls_generate_messages mp_controls_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/parthag/mech_ws/src/mp_controls/msg/Path.msg" NAME_WE)
add_dependencies(mp_controls_generate_messages_cpp _mp_controls_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(mp_controls_gencpp)
add_dependencies(mp_controls_gencpp mp_controls_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS mp_controls_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(mp_controls
  "/home/parthag/mech_ws/src/mp_controls/msg/Path.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/mp_controls
)

### Generating Services

### Generating Module File
_generate_module_eus(mp_controls
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/mp_controls
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(mp_controls_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(mp_controls_generate_messages mp_controls_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/parthag/mech_ws/src/mp_controls/msg/Path.msg" NAME_WE)
add_dependencies(mp_controls_generate_messages_eus _mp_controls_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(mp_controls_geneus)
add_dependencies(mp_controls_geneus mp_controls_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS mp_controls_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(mp_controls
  "/home/parthag/mech_ws/src/mp_controls/msg/Path.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/mp_controls
)

### Generating Services

### Generating Module File
_generate_module_lisp(mp_controls
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/mp_controls
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(mp_controls_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(mp_controls_generate_messages mp_controls_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/parthag/mech_ws/src/mp_controls/msg/Path.msg" NAME_WE)
add_dependencies(mp_controls_generate_messages_lisp _mp_controls_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(mp_controls_genlisp)
add_dependencies(mp_controls_genlisp mp_controls_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS mp_controls_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(mp_controls
  "/home/parthag/mech_ws/src/mp_controls/msg/Path.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/mp_controls
)

### Generating Services

### Generating Module File
_generate_module_nodejs(mp_controls
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/mp_controls
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(mp_controls_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(mp_controls_generate_messages mp_controls_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/parthag/mech_ws/src/mp_controls/msg/Path.msg" NAME_WE)
add_dependencies(mp_controls_generate_messages_nodejs _mp_controls_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(mp_controls_gennodejs)
add_dependencies(mp_controls_gennodejs mp_controls_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS mp_controls_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(mp_controls
  "/home/parthag/mech_ws/src/mp_controls/msg/Path.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/mp_controls
)

### Generating Services

### Generating Module File
_generate_module_py(mp_controls
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/mp_controls
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(mp_controls_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(mp_controls_generate_messages mp_controls_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/parthag/mech_ws/src/mp_controls/msg/Path.msg" NAME_WE)
add_dependencies(mp_controls_generate_messages_py _mp_controls_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(mp_controls_genpy)
add_dependencies(mp_controls_genpy mp_controls_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS mp_controls_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/mp_controls)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/mp_controls
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_cpp)
  add_dependencies(mp_controls_generate_messages_cpp geometry_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/mp_controls)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/mp_controls
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_eus)
  add_dependencies(mp_controls_generate_messages_eus geometry_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/mp_controls)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/mp_controls
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_lisp)
  add_dependencies(mp_controls_generate_messages_lisp geometry_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/mp_controls)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/mp_controls
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_nodejs)
  add_dependencies(mp_controls_generate_messages_nodejs geometry_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/mp_controls)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/mp_controls\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/mp_controls
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_py)
  add_dependencies(mp_controls_generate_messages_py geometry_msgs_generate_messages_py)
endif()
