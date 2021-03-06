from bots.botsconfig import *
from records003040 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'WB',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'ZC1', MIN: 0, MAX: 1},
    {ID: 'BX', MIN: 0, MAX: 1},
    {ID: 'BNX', MIN: 0, MAX: 1},
    {ID: 'N9', MIN: 0, MAX: 30},
    {ID: 'CM', MIN: 0, MAX: 2},
    {ID: 'DTM', MIN: 0, MAX: 5},
    {ID: 'N7', MIN: 1, MAX: 255, LEVEL: [
        {ID: 'EM', MIN: 0, MAX: 1},
        {ID: 'VC', MIN: 0, MAX: 21, LEVEL: [
            {ID: 'N1', MIN: 0, MAX: 2, LEVEL: [
                {ID: 'N3', MIN: 0, MAX: 2},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'H3', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: 'IC', MIN: 0, MAX: 1},
        {ID: 'IM', MIN: 0, MAX: 1},
        {ID: 'M12', MIN: 0, MAX: 1},
        {ID: 'G4', MIN: 0, MAX: 1},
        {ID: 'M7', MIN: 0, MAX: 5},
        {ID: 'N5', MIN: 0, MAX: 1},
        {ID: 'H5', MIN: 0, MAX: 1},
        {ID: 'E1', MIN: 0, MAX: 1},
        {ID: 'E4', MIN: 0, MAX: 1},
        {ID: 'E5', MIN: 0, MAX: 13},
    ]},
    {ID: 'IMA', MIN: 0, MAX: 3},
    {ID: 'N8', MIN: 0, MAX: 499},
    {ID: 'V9', MIN: 0, MAX: 1},
    {ID: 'F9', MIN: 1, MAX: 1},
    {ID: 'D9', MIN: 1, MAX: 1},
    {ID: 'N1', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'PER', MIN: 0, MAX: 2},
        {ID: 'BL', MIN: 0, MAX: 1},
    ]},
    {ID: 'S1', MIN: 0, MAX: 6, LEVEL: [
        {ID: 'S2', MIN: 0, MAX: 2},
        {ID: 'S9', MIN: 0, MAX: 1},
    ]},
    {ID: 'R2', MIN: 1, MAX: 13},
    {ID: 'RE', MIN: 0, MAX: 1},
    {ID: 'E1', MIN: 0, MAX: 1},
    {ID: 'E4', MIN: 0, MAX: 1},
    {ID: 'E5', MIN: 0, MAX: 12},
    {ID: 'H3', MIN: 0, MAX: 20},
    {ID: 'PS', MIN: 0, MAX: 1},
    {ID: 'LX', MIN: 1, MAX: 25, LEVEL: [
        {ID: 'L5', MIN: 0, MAX: 15},
        {ID: 'LS', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'LX', MIN: 1, MAX: 25, LEVEL: [
                {ID: 'L0', MIN: 0, MAX: 10},
                {ID: 'L1', MIN: 0, MAX: 10},
            ]},
            {ID: 'LE', MIN: 1, MAX: 1},
        ]},
        {ID: 'L7', MIN: 0, MAX: 30},
    ]},
    {ID: 'T1', MIN: 0, MAX: 64, LEVEL: [
        {ID: 'T2', MIN: 0, MAX: 30},
        {ID: 'T3', MIN: 0, MAX: 12},
        {ID: 'T6', MIN: 0, MAX: 1},
        {ID: 'T8', MIN: 0, MAX: 99},
    ]},
    {ID: 'L3', MIN: 0, MAX: 1},
    {ID: 'LS', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'LH1', MIN: 1, MAX: 100, LEVEL: [
            {ID: 'LH2', MIN: 0, MAX: 4},
            {ID: 'LH3', MIN: 0, MAX: 10},
            {ID: 'LFH', MIN: 0, MAX: 20},
            {ID: 'LEP', MIN: 0, MAX: 3},
            {ID: 'LH4', MIN: 0, MAX: 1},
            {ID: 'LHT', MIN: 0, MAX: 3},
            {ID: 'LHR', MIN: 0, MAX: 5},
            {ID: 'PER', MIN: 0, MAX: 5},
        ]},
        {ID: 'LE', MIN: 1, MAX: 1},
    ]},
    {ID: 'PER', MIN: 0, MAX: 5},
    {ID: 'LH2', MIN: 0, MAX: 6},
    {ID: 'LHR', MIN: 0, MAX: 1},
    {ID: 'X7', MIN: 0, MAX: 10},
    {ID: 'GA', MIN: 0, MAX: 1},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
