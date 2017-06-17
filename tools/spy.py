#!/usr/bin/env python2

# This file is loosely based on selfspy/sniff_x.py by David Fendrich

import sys

from Xlib import X, XK, display
from Xlib.ext import record
from Xlib.error import XError
from Xlib.protocol import rq


def state_to_idx(state):  # this could be a dict, but I might want to extend it.
    if state == 1:
        return 1
    if state == 128:
        return 4
    if state == 129:
        return 5
    return 0

keysymdict = {}
for name in dir(XK):
    if name.startswith("XK_"):
        keysymdict[getattr(XK, name)] = name[3:]


record_display = display.Display()
keymap = record_display._keymap_codes
ctx = record_display.record_create_context(
        0,
        [record.AllClients],
        [{
                'core_requests': (0, 0),
                'core_replies': (0, 0),
                'ext_requests': (0, 0, 0, 0),
                'ext_replies': (0, 0, 0, 0),
                'delivered_events': (0, 0),
                'device_events': tuple([X.KeyPress, X.MotionNotify]),
                'errors': (0, 0),
                'client_started': False,
                'client_died': False,
        }])

def handle_event(event):
    if event.category != record.FromServer:
        return

    if event.client_swapped:
        print "* received swapped protocol data, cowardly ignored"
        return

    if not len(event.data) or ord(event.data[0]) < 2:
        # not an event
        return

    data = event.data
    while len(data):
        ef = rq.EventField(None)
        event, data = ef.parse_binary_value(data, record_display.display, None, None)

        if event.type in [X.KeyPress, X.KeyRelease]:
            handle_keyboard(event)

        elif event.type in [X.ButtonPress, X.ButtonRelease, X.MotionNotify]:
            handle_mouse(event)

        elif event.type == X.MappingNotify:
            record_display.refresh_keyboard_mapping()
            keymap = record_display._keymap_codes
            print('Changed keymap!')

def get_key_name(keycode, state):
    cn = keymap[keycode][state_to_idx(state)]
    if cn < 256:
        return chr(cn).decode('latin1')
    elif cn in keysymdict:
        return keysymdict[cn]
    return "[%d]" % cn

def handle_mouse(event):
    print('mouse: {}, type: {}, x: {}, y: {}'.format(event.detail, event.type, event.root_x, event.root_y))

# dt = np.dtype(('uint64', 'uint16', 'uint8',
# rows = np.zeros(dtype=dt)

def handle_keyboard( event):
    # if event.state & X.ControlMask:  Ctrl
    # if event.state & X.Mod1Mask:  Alt
    # if event.state & X.Mod4Mask:  Super
    # if event.state & X.ShiftMask: Shift
    name = get_key_name(event.detail, event.state),
    repeat = event.sequence_number >= 1
    press = event.type == X.KeyPress
    print('key: {}, press: {}, mods: {}, repeat: {}'.format(event.detail, press, event.state, repeat))

record_display.record_enable_context(ctx, handle_event)
record_display.record_free_context(ctx)

