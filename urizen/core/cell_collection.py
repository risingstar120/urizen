#!/usr/bin/python3

from urizen.core.cell import Cell

# Dungeon cells

cell_void = type('cell_void', (Cell,), {
    'height': 0,
    'terrain': None,
    'cell_type': None,
    'symbol': ' ',
    'bg_color': '#000000',
    'fg_color': '#FFFFFF',
    'pixel_color': '#000000',
    'sprite': None,
    'passable': False,
    'tags': []
})

cell_dungeon_floor = type('cell_dungeon_floor', (Cell,), {
    'height': 0,
    'terrain': 'dungeon',
    'cell_type': 'floor',
    'symbol': '.',
    'bg_color': '#000000',
    'fg_color': '#FFFFFF',
    'pixel_color': '#909090',
    'sprite': None,
    'passable': True,
    'tags': []
})

cell_dungeon_wall = type('cell_dungeon_wall', (Cell,), {
    'height': 1,
    'terrain': 'dungeon',
    'cell_type': 'wall',
    'symbol': '#',
    'bg_color': '#000000',
    'fg_color': '#FFFFFF',
    'pixel_color': '#303030',
    'sprite': None,
    'passable': False,
    'tags': []
})

cell_dungeon_closed_door = type('cell_dungeon_closed_door', (Cell,), {
    'height': 1,
    'terrain': 'dungeon',
    'cell_type': 'door',
    'symbol': '+',
    'bg_color': '#000000',
    'fg_color': '#FFFFFF',
    'pixel_color': '#905000',
    'sprite': None,
    'passable': False,
    'tags': []
})

cell_dungeon_open_door = type('cell_dungeon_open_door', (Cell,), {
    'height': 1,
    'terrain': 'dungeon',
    'cell_type': 'door',
    'symbol': '\'',
    'bg_color': '#000000',
    'fg_color': '#FFFFFF',
    'pixel_color': '#905000',
    'sprite': None,
    'passable': True,
    'tags': []
})


# World terrain cells

cell_terrain_grassland = type('cell_terrain_grassland', (Cell,), {
    'height': 0,
    'terrain': 'terrain',
    'cell_type': 'terrain',
    'symbol': '"',
    'bg_color': '#000000',
    'fg_color': '#00FF00',
    'pixel_color': '#00C000',
    'sprite': None,
    'passable': True,
    'tags': []
})

cell_terrain_forest = type('cell_terrain_forest', (Cell,), {
    'height': 1,
    'terrain': 'terrain',
    'cell_type': 'terrain',
    'symbol': 'T',
    'bg_color': '#000000',
    'fg_color': '#00FF00',
    'pixel_color': '#008000',
    'sprite': None,
    'passable': True,
    'tags': []
})

cell_terrain_mountain = type('cell_terrain_mountain', (Cell,), {
    'height': 1,
    'terrain': 'terrain',
    'cell_type': 'terrain',
    'symbol': '^',
    'bg_color': '#000000',
    'fg_color': '#FFFFFF',
    'pixel_color': '#909090',
    'sprite': None,
    'passable': True,
    'tags': []
})

cell_terrain_pinnacle = type('cell_terrain_pinnacle', (Cell,), {
    'height': 1,
    'terrain': 'terrain',
    'cell_type': 'terrain',
    'symbol': '^',
    'bg_color': '#000000',
    'fg_color': '#FF0000',
    'pixel_color': '#FFFFFF',
    'sprite': None,
    'passable': False,
    'tags': []
})

cell_terrain_water = type('cell_terrain_water', (Cell,), {
    'height': 0,
    'terrain': 'terrain',
    'cell_type': 'terrain',
    'symbol': '~',
    'bg_color': '#000000',
    'fg_color': '#0000FF',
    'pixel_color': '#0000C0',
    'sprite': None,
    'passable': False,
    'tags': []
})

cell_terrain_deep_water = type('cell_terrain_deep_water', (Cell,), {
    'height': 0,
    'terrain': 'terrain',
    'cell_type': 'terrain',
    'symbol': '~',
    'bg_color': '#0000FF',
    'fg_color': '#000000',
    'pixel_color': '#000070',
    'sprite': None,
    'passable': False,
    'tags': []
})


# Medieval building cells

cell_building_floor_wooden = type('cell_building_floor_wooden', (Cell,), {
    'height': 0,
    'terrain': 'building',
    'cell_type': 'floor',
    'symbol': '.',
    'bg_color': '#000000',
    'fg_color': '#FFFFFF',
    'pixel_color': '#251000',
    'sprite': None,
    'passable': True,
    'tags': ['medieval']
})

cell_building_floor_stone = type('cell_building_floor_stone', (Cell,), {
    'height': 0,
    'terrain': 'building',
    'cell_type': 'floor',
    'symbol': '.',
    'bg_color': '#000000',
    'fg_color': '#FFFFFF',
    'pixel_color': '#202020',
    'sprite': None,
    'passable': True,
    'tags': ['medieval']
})

cell_building_floor_dirt = type('cell_building_floor_dirt', (Cell,), {
    'height': 0,
    'terrain': 'building',
    'cell_type': 'floor',
    'symbol': '.',
    'bg_color': '#000000',
    'fg_color': '#FFFFFF',
    'pixel_color': '#201005',
    'sprite': None,
    'passable': True,
    'tags': ['medieval']
})

cell_building_wall_wooden = type('cell_building_wall_wooden', (Cell,), {
    'height': 1,
    'terrain': 'building',
    'cell_type': 'wall',
    'symbol': '#',
    'bg_color': '#000000',
    'fg_color': '#FFFFFF',
    'pixel_color': '#703810',
    'sprite': None,
    'passable': False,
    'tags': ['medieval']
})

cell_building_wall_stone = type('cell_building_wall_stone', (Cell,), {
    'height': 1,
    'terrain': 'building',
    'cell_type': 'wall',
    'symbol': '#',
    'bg_color': '#000000',
    'fg_color': '#FFFFFF',
    'pixel_color': '#808080',
    'sprite': None,
    'passable': False,
    'tags': ['medieval']
})

cell_building_closed_door = type('cell_building_closed_door', (Cell,), {
    'height': 1,
    'terrain': 'building',
    'cell_type': 'door',
    'symbol': '+',
    'bg_color': '#000000',
    'fg_color': '#FFFFFF',
    'pixel_color': '#804500',
    'sprite': None,
    'passable': False,
    'tags': ['medieval']
})

cell_building_open_door = type('cell_building_open_door', (Cell,), {
    'height': 1,
    'terrain': 'building',
    'cell_type': 'door',
    'symbol': '\'',
    'bg_color': '#000000',
    'fg_color': '#FFFFFF',
    'pixel_color': '#804500',
    'sprite': None,
    'passable': True,
    'tags': ['medieval']
})

cell_fence_wooden = type('cell_fence_wooden', (Cell,), {
    'height': 1,
    'terrain': 'building',
    'cell_type': 'wall',
    'symbol': '\"',
    'bg_color': '#000000',
    'fg_color': '#FFFFFF',
    'pixel_color': '#703800',
    'sprite': None,
    'passable': False,
    'tags': ['medieval']
})
