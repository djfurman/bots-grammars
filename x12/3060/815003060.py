from bots.botsconfig import *
from records003060 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'CS',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'CSM', MIN: 1, MAX: 1},
    {ID: 'CSB', MIN: 1, MAX: 99999},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
