# URDF

> Source: http://wiki.ros.org/urdf

> Aliases: unified-robot-description-format

$ Joint Types
    `revolute                      {{1 limited revolute DOF}} 
    `continuous                    {{1 revolute DOF}} 
    `prismatic                     {{1 limited prismatic DOF}} 
    `fixed                         {{0 DOF}} 
    `floating                      {{6 DOF}} 
    `planar                        {{2 DOF}} 

$ Joint Attributes
    `name                          {{required}} 
    `type                          {{required}} 

$ Link Attributes
    `name                          {{required}} 

$ Joint Elements
    `origin                        {{optional (defaults to origin)}} 
    `parent                        {{required}} 
    `child                         {{required}} 
    `axis                          {{optional (defaults to (1,0,0))}} 
    `calibration                   {{optional}} 
    `dynamics                      {{optional}} 
    `limit                         {{required only for revolute or prismatic joints}} 
    `mimic                         {{optional}} 
    `safety_controller             {{optional}} 

$ Link Elements
    `inertial                      {{optional}} 
    `visual                        {{optional}} 
    `collision                     {{optional}} 

