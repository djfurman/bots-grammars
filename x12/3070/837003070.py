from bots.botsconfig import *
from records003070 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'HC',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BHT', MIN: 1, MAX: 1},
    {ID: 'REF', MIN: 0, MAX: 3},
    {ID: 'NM1', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 2},
        {ID: 'PER', MIN: 0, MAX: 2},
    ]},
    {ID: 'HL', MIN: 1, MAX: 99999, LEVEL: [
        {ID: 'PRV', MIN: 0, MAX: 1},
        {ID: 'SBR', MIN: 0, MAX: 1},
        {ID: 'PAT', MIN: 0, MAX: 1},
        {ID: 'DTP', MIN: 0, MAX: 5},
        {ID: 'CUR', MIN: 0, MAX: 1},
        {ID: 'NM1', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'DMG', MIN: 0, MAX: 1},
            {ID: 'REF', MIN: 0, MAX: 20},
            {ID: 'PER', MIN: 0, MAX: 2},
        ]},
        {ID: 'CLM', MIN: 0, MAX: 100, LEVEL: [
            {ID: 'DTP', MIN: 0, MAX: 150},
            {ID: 'CL1', MIN: 0, MAX: 1},
            {ID: 'DN1', MIN: 0, MAX: 1},
            {ID: 'DN2', MIN: 0, MAX: 35},
            {ID: 'PWK', MIN: 0, MAX: 10},
            {ID: 'CN1', MIN: 0, MAX: 1},
            {ID: 'DSB', MIN: 0, MAX: 1},
            {ID: 'UR', MIN: 0, MAX: 1},
            {ID: 'AMT', MIN: 0, MAX: 40},
            {ID: 'REF', MIN: 0, MAX: 30},
            {ID: 'K3', MIN: 0, MAX: 10},
            {ID: 'NTE', MIN: 0, MAX: 20},
            {ID: 'CR1', MIN: 0, MAX: 1},
            {ID: 'CR2', MIN: 0, MAX: 1},
            {ID: 'CR3', MIN: 0, MAX: 1},
            {ID: 'CR4', MIN: 0, MAX: 3},
            {ID: 'CR5', MIN: 0, MAX: 1},
            {ID: 'CR6', MIN: 0, MAX: 1},
            {ID: 'CR8', MIN: 0, MAX: 1},
            {ID: 'CRC', MIN: 0, MAX: 100},
            {ID: 'HI', MIN: 0, MAX: 25},
            {ID: 'QTY', MIN: 0, MAX: 10},
            {ID: 'HCP', MIN: 0, MAX: 1},
            {ID: 'CR7', MIN: 0, MAX: 6, LEVEL: [
                {ID: 'HSD', MIN: 0, MAX: 12},
            ]},
            {ID: 'NM1', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'PRV', MIN: 0, MAX: 1},
                {ID: 'N2', MIN: 0, MAX: 2},
                {ID: 'N3', MIN: 0, MAX: 2},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'REF', MIN: 0, MAX: 20},
                {ID: 'PER', MIN: 0, MAX: 2},
            ]},
            {ID: 'SBR', MIN: 0, MAX: 10, LEVEL: [
                {ID: 'CAS', MIN: 0, MAX: 1},
                {ID: 'AMT', MIN: 0, MAX: 15},
                {ID: 'DMG', MIN: 0, MAX: 1},
                {ID: 'OI', MIN: 0, MAX: 1},
                {ID: 'MIA', MIN: 0, MAX: 1},
                {ID: 'MOA', MIN: 0, MAX: 1},
                {ID: 'NM1', MIN: 0, MAX: 10, LEVEL: [
                    {ID: 'N2', MIN: 0, MAX: 2},
                    {ID: 'N3', MIN: 0, MAX: 2},
                    {ID: 'N4', MIN: 0, MAX: 1},
                    {ID: 'PER', MIN: 0, MAX: 2},
                    {ID: 'DTP', MIN: 0, MAX: 9},
                    {ID: 'REF', MIN: 0, MAX: 3},
                ]},
            ]},
            {ID: 'LX', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'SV1', MIN: 0, MAX: 1},
                {ID: 'SV2', MIN: 0, MAX: 1},
                {ID: 'SV3', MIN: 0, MAX: 1},
                {ID: 'TOO', MIN: 0, MAX: 32},
                {ID: 'SV4', MIN: 0, MAX: 1},
                {ID: 'SV5', MIN: 0, MAX: 1},
                {ID: 'SV6', MIN: 0, MAX: 1},
                {ID: 'SV7', MIN: 0, MAX: 1},
                {ID: 'HI', MIN: 0, MAX: 25},
                {ID: 'PWK', MIN: 0, MAX: 10},
                {ID: 'CR1', MIN: 0, MAX: 1},
                {ID: 'CR2', MIN: 0, MAX: 5},
                {ID: 'CR3', MIN: 0, MAX: 1},
                {ID: 'CR4', MIN: 0, MAX: 3},
                {ID: 'CR5', MIN: 0, MAX: 1},
                {ID: 'CRC', MIN: 0, MAX: 3},
                {ID: 'DTP', MIN: 0, MAX: 15},
                {ID: 'QTY', MIN: 0, MAX: 5},
                {ID: 'MEA', MIN: 0, MAX: 20},
                {ID: 'CN1', MIN: 0, MAX: 1},
                {ID: 'REF', MIN: 0, MAX: 30},
                {ID: 'AMT', MIN: 0, MAX: 15},
                {ID: 'K3', MIN: 0, MAX: 10},
                {ID: 'NTE', MIN: 0, MAX: 10},
                {ID: 'PS1', MIN: 0, MAX: 1},
                {ID: 'HSD', MIN: 0, MAX: 1},
                {ID: 'HCP', MIN: 0, MAX: 1},
                {ID: 'LIN', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'CTP', MIN: 0, MAX: 1},
                    {ID: 'REF', MIN: 0, MAX: 1},
                ]},
                {ID: 'NM1', MIN: 0, MAX: 10, LEVEL: [
                    {ID: 'PRV', MIN: 0, MAX: 1},
                    {ID: 'N2', MIN: 0, MAX: 2},
                    {ID: 'N3', MIN: 0, MAX: 2},
                    {ID: 'N4', MIN: 0, MAX: 1},
                    {ID: 'REF', MIN: 0, MAX: 20},
                    {ID: 'PER', MIN: 0, MAX: 2},
                ]},
                {ID: 'SVD', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'CAS', MIN: 0, MAX: 99},
                    {ID: 'DTP', MIN: 0, MAX: 9},
                ]},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
