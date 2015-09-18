# These and other macros are documented in
# ../droid-configs-device/droid-configs.inc

%define device moto_msm8960_jbbl
%define vendor motorola

%define vendor_pretty Motorola
%define device_pretty Photon Q

%define dcd_path ./

# Adjust this for your device
%define pixel_ratio 1.7778

# We assume most devices will
%define have_modem 1

%include droid-configs-device/droid-configs.inc
