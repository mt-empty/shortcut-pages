# vcgencmd

> Source: http://elinux.org/RPI_vcgencmd_usage

> Aliases: raspberry-pi-firmware, raspi-firmware

$ Utility
    `vcgencmd commands             {{Shows a list of all the available commands}} 
    `vcgencmd version              {{Shows the firmware version}} 
    `vcgencmd get_config [config|int|str]
>                                  {{Will print the configurations you have set. Argument can ether be - 'config', a specific option or 'int', showing all configs with number-datatype or 'str', showing all configurations with datatype string (aka text)}} 
    `vcgencmd codec_enabled <codec>
>                                  {{Shows if the specified codec is enabled, codec can be one of 'H264', 'MPG2', 'WVC1', 'MPG4', 'MJPG', 'WMV9'}} 
    `vcgencmd get_mem arm/gpu      {{Shows how much memory is split between the CPU (arm) and GPU}} 
    `vcgencmd cache_flush          {{Flush GPU's L1 cache}} 
    `vcgencmd otp_dump             {{Displays the contents of the OTP (One Time Programmable) memory embedded inside the SoC}} 
    `vcgencmd display_power [0|1]  {{Turns video output off or on. '0' turns it off, '1' turns it on}} 
    `vcgencmd mem_oom              {{Reports statistics on Out of Memory events}} 
    `vcgencmd mem_reloc_stats      {{Reports statics on relocatable memory}} 
    `vcgencmd render_bar           {{Debug function created by Dom}} 

$ Sensors
    `vcgencmd measure_temp         {{Shows core temperature}} 
    `vcgencmd measure_volts <id>   {{Shows voltage. id can be one of 'core', 'sdram_c', 'sdram_i', 'sdram_p', and defaults to 'core' if not specified}} 
    `vcgencmd measure_clock <clock>
>                                  {{Shows clock frequency, clock can be one of 'arm', 'core', 'h264', 'isp', 'v3d', 'uart', 'pwm', 'emmc', 'pixel', 'vec', 'hdmi' and 'dpi'}} 

