extends Node2D

enum RoomPhase {
	PREVIEW,
	DEPLOY,
	COMBAT,
	RESULT
}

var current_phase: RoomPhase = RoomPhase.PREVIEW

@onready var lbl_state: Label = $CanvasLayer/HUD/VBoxContainer/LblState
@onready var lbl_hint: Label = $CanvasLayer/HUD/VBoxContainer/LblHint
@onready var btn_advance: Button = $CanvasLayer/HUD/VBoxContainer/HBoxContainer/BtnAdvanceState
@onready var btn_reset: Button = $CanvasLayer/HUD/VBoxContainer/HBoxContainer/BtnResetState
@onready var btn_back: Button = $CanvasLayer/HUD/VBoxContainer/HBoxContainer/BtnBackToMap

func _ready() -> void:
	btn_advance.pressed.connect(_on_advance_pressed)
	btn_reset.pressed.connect(_on_reset_pressed)
	btn_back.pressed.connect(_on_back_pressed)
	_apply_phase(RoomPhase.PREVIEW)

func _unhandled_input(event: InputEvent) -> void:
	if event.is_action_pressed("tod_back"):
		_on_back_pressed()
	elif event.is_action_pressed("tod_debug_next_state"):
		_on_advance_pressed()

func _on_advance_pressed() -> void:
	match current_phase:
		RoomPhase.PREVIEW:
			_apply_phase(RoomPhase.DEPLOY)
		RoomPhase.DEPLOY:
			_apply_phase(RoomPhase.COMBAT)
		RoomPhase.COMBAT:
			_apply_phase(RoomPhase.RESULT)
		RoomPhase.RESULT:
			_apply_phase(RoomPhase.PREVIEW)

func _on_reset_pressed() -> void:
	_apply_phase(RoomPhase.PREVIEW)

func _on_back_pressed() -> void:
	SceneRouter.go_to_chapter_map()

func _apply_phase(new_phase: RoomPhase) -> void:
	current_phase = new_phase

	var phase_name := ""
	var hint_text := ""

	match current_phase:
		RoomPhase.PREVIEW:
			phase_name = "Preview"
			hint_text = "Room preview placeholder. Later this will show guards, waves, and room modifiers."
		RoomPhase.DEPLOY:
			phase_name = "Deploy"
			hint_text = "Deployment placeholder. Later this will handle slots, Supply cost, and unit placement."
		RoomPhase.COMBAT:
			phase_name = "Combat"
			hint_text = "Combat placeholder. Later this will run automated battle and enemy waves."
		RoomPhase.RESULT:
			phase_name = "Result"
			hint_text = "Result placeholder. Later this will show victory/defeat and carryover outcomes."

	GameSession.current_room_state = phase_name
	lbl_state.text = "Current State: %s" % phase_name
	lbl_hint.text = hint_text
	EventBus.room_state_changed.emit(phase_name)
