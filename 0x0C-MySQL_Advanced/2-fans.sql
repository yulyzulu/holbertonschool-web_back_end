-- Script that ranks country origins of bands ordered by fans
SELECT origin, fans as nb_fans FROM metal_bands ORDER BY fans;
