// Copyright 2023 shukie (@shukie)
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

enum {
  _BASE_LAYER = 0,
  _LOWER_LAYER,
  _RAISE_LAYER,
  _ADJUST_LAYER
};

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
  [_BASE_LAYER] = LAYOUT_46_10x13(
    //,--------.                                                                                                              ,--------.
         KC_ESC,                                                                                                                KC_BSPC,
    //,--------+--------------------------------------------.                    ,--------------------------------------------+--------.
         KC_TAB,    KC_Q,    KC_W,    KC_E,    KC_R,    KC_T,                         KC_Y,    KC_U,    KC_I,    KC_O,   KC_P,  KC_MINS,
    //|--------+--------+--------+--------+--------+--------|                    |--------+--------+--------+--------+--------+--------|
        KC_LCTL,    KC_A,    KC_S,    KC_D,    KC_F,    KC_G,                         KC_H,    KC_J,    KC_K,    KC_L, KC_SCLN, KC_QUOT,
    //|--------+--------+--------+--------+--------+--------|                    |--------+--------+--------+--------+--------+--------|
        KC_LSFT,    KC_Z,    KC_X,    KC_C,    KC_V,    KC_B,                         KC_N,    KC_M, KC_COMM,  KC_DOT, KC_SLSH, KC_RSFT,
    //|--------+--------+--------+--------+--------+--------+--------|  |--------+--------+--------+--------+--------+--------+--------|
                          KC_LALT, KC_LGUI, MO(_LOWER_LAYER),  KC_SPC,     KC_ENT, MO(_RAISE_LAYER), KC_RGUI, KC_RALT
    //                  `--------------------------------------------'  `--------------------------------------------'
  ),
  [_LOWER_LAYER] = LAYOUT_46_10x13(
    //,--------.                                                                                                              ,--------.
         KC_ESC,                                                                                                                KC_BSPC,
    //,--------+--------------------------------------------.                    ,--------------------------------------------+--------.
         KC_TAB,    KC_1,    KC_2,    KC_3,    KC_4,    KC_5,                         KC_6,    KC_7,    KC_8,    KC_9,    KC_0, _______,
    //|--------+--------+--------+--------+--------+--------|                    |--------+--------+--------+--------+--------+--------|
        KC_LCTL, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                      KC_LEFT, KC_DOWN,   KC_UP,KC_RIGHT, XXXXXXX, XXXXXXX,
    //|--------+--------+--------+--------+--------+--------|                    |--------+--------+--------+--------+--------+--------|
        KC_LSFT, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                      KC_HOME, KC_PGDN, KC_PGUP,  KC_END, XXXXXXX, KC_RSFT,
    //|--------+--------+--------+--------+--------+--------+--------|  |--------+--------+--------+--------+--------+--------+--------|
                          KC_LALT, KC_LGUI,          _______,  KC_SPC,     KC_ENT,MO(_ADJUST_LAYER), KC_RGUI, KC_RALT
    //                  `--------------------------------------------'  `--------------------------------------------'
  ),
  [_RAISE_LAYER] = LAYOUT_46_10x13(
    //,--------.                                                                                                              ,--------.
         KC_ESC,                                                                                                                KC_BSPC,
    //,--------+--------------------------------------------.                    ,--------------------------------------------+--------.
         KC_TAB, KC_EXLM,   KC_AT, KC_HASH,  KC_DLR, KC_PERC,                      KC_CIRC, KC_AMPR, KC_ASTR, KC_LPRN, KC_RPRN, _______,
    //|--------+--------+--------+--------+--------+--------|                    |--------+--------+--------+--------+--------+--------|
        KC_LCTL,  KC_GRV, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                      KC_MINS,  KC_EQL, XXXXXXX, KC_LBRC, KC_RBRC, KC_BSLS,
    //|--------+--------+--------+--------+--------+--------|                    |--------+--------+--------+--------+--------+--------|
        KC_LSFT, KC_TILD, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                      KC_UNDS, KC_PLUS, XXXXXXX, KC_LCBR, KC_RCBR, KC_PIPE,
    //|-----------------+--------+--------+--------+--------+--------|  |--------+--------+--------+--------+--------+-----------------|
                          KC_LALT, KC_LGUI,MO(_ADJUST_LAYER),  KC_SPC,     KC_ENT,          _______, KC_RGUI, KC_RALT
    //                  `--------------------------------------------'  `--------------------------------------------'
  ),
  [_ADJUST_LAYER] = LAYOUT_46_10x13(
    //,--------.                                                                                                              ,--------.
        KC_SLEP,                                                                                                                 KC_DEL,
    //,--------+--------------------------------------------.                    ,--------------------------------------------+--------.
         KC_TAB,   KC_F1,   KC_F2,   KC_F3,   KC_F4,   KC_F5,                        KC_F6,   KC_F7,   KC_F8,   KC_F9,  KC_F10, XXXXXXX,
    //|--------+--------+--------+--------+--------+--------|                    |--------+--------+--------+--------+--------+--------|
        KC_LCTL, KC_BRID, KC_BRIU, KC_MUTE, KC_VOLD, KC_VOLU,                      XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
    //|--------+--------+--------+--------+--------+--------|                    |--------+--------+--------+--------+--------+--------|
        KC_LSFT,  KC_F11,  KC_F12,  KC_F13,  KC_F14,  KC_F15,                       KC_F16,  KC_F17,  KC_F18,  KC_F19, XXXXXXX, KC_RSFT,
    //|--------+--------+--------+--------+--------+--------+--------|  |--------+--------+--------+--------+--------+--------+--------|
                          KC_LALT, KC_LGUI,          _______,  KC_SPC,     KC_ENT,          _______, KC_RGUI, KC_RALT
    //                  `--------------------------------------------'  `--------------------------------------------'
  )
};
