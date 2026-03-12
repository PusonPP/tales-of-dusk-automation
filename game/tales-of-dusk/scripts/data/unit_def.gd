class_name UnitDef
extends Resource

@export_group("Identity")
@export var unit_id: StringName
@export var display_name: String
@export_multiline var description: String = ""

@export_group("Economy")
@export var supply_cost: int = 1

@export_group("Stats")
@export var max_hp: int = 10
@export var attack_power: int = 1
@export var attack_interval: float = 1.0
@export var move_speed: float = 50.0

@export_group("Presentation")
@export var world_scene: PackedScene
@export var icon: Texture2D