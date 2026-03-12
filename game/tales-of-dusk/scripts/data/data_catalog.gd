class_name DataCatalog
extends RefCounted

const CHAPTER_01_PATH := "res://data/defs/chapters/chapter_01.tres"
const UNIT_GUARD_PATH := "res://data/defs/units/unit_guard.tres"
const UNIT_ARCHER_PATH := "res://data/defs/units/unit_archer.tres"

static func load_chapter_01() -> ChapterDef:
    return ResourceLoader.load(CHAPTER_01_PATH) as ChapterDef

static func load_default_units() -> Array[UnitDef]:
    return [
        ResourceLoader.load(UNIT_GUARD_PATH) as UnitDef,
        ResourceLoader.load(UNIT_ARCHER_PATH) as UnitDef,
    ]