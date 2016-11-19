from bots.botsconfig import *
from records003060 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'RT',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BTR', MIN: 1, MAX: 1},
    {ID: 'REF', MIN: 0, MAX: 12},
    {ID: 'DTM', MIN: 0, MAX: 10},
    {ID: 'PID', MIN: 0, MAX: 200},
    {ID: 'TMD', MIN: 0, MAX: 1},
    {ID: 'MEA', MIN: 0, MAX: 20},
    {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 12},
        {ID: 'PER', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'REF', MIN: 0, MAX: 99999},
        ]},
    ]},
    {ID: 'LIN', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'PID', MIN: 0, MAX: 1000},
        {ID: 'TMD', MIN: 0, MAX: 1},
        {ID: 'MEA', MIN: 0, MAX: 20},
        {ID: 'PSD', MIN: 0, MAX: 99999},
        {ID: 'SPS', MIN: 0, MAX: 99999},
        {ID: 'QTY', MIN: 0, MAX: 10},
        {ID: 'DTM', MIN: 0, MAX: 10},
        {ID: 'REF', MIN: 0, MAX: 1000},
        {ID: 'N1', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'REF', MIN: 0, MAX: 10},
            {ID: 'PER', MIN: 0, MAX: 3},
            {ID: 'QTY', MIN: 0, MAX: 10},
        ]},
        {ID: 'CID', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'UIT', MIN: 0, MAX: 1},
            {ID: 'PSD', MIN: 0, MAX: 99999},
            {ID: 'SPS', MIN: 0, MAX: 99999},
            {ID: 'DTM', MIN: 0, MAX: 10},
            {ID: 'REF', MIN: 0, MAX: 10},
            {ID: 'MEA', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 10},
                {ID: 'REF', MIN: 0, MAX: 10},
                {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'LQ', MIN: 1, MAX: 99999},
                ]},
            ]},
            {ID: 'STA', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 10},
                {ID: 'REF', MIN: 0, MAX: 10},
                {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'LQ', MIN: 1, MAX: 99999},
                ]},
            ]},
            {ID: 'TMD', MIN: 0, MAX: 100, LEVEL: [
                {ID: 'MEA', MIN: 0, MAX: 99999},
                {ID: 'DTM', MIN: 0, MAX: 10},
                {ID: 'REF', MIN: 0, MAX: 10},
            ]},
            {ID: 'TSP', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'MEA', MIN: 0, MAX: 99999},
                {ID: 'DTM', MIN: 0, MAX: 10},
                {ID: 'REF', MIN: 0, MAX: 10},
                {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'LQ', MIN: 1, MAX: 99999},
                ]},
            ]},
        ]},
    ]},
    {ID: 'CTT', MIN: 0, MAX: 1},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
