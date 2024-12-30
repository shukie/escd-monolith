import pcbnew
import math

class MonolithPlugin(pcbnew.ActionPlugin):
  OFFSET = pcbnew.VECTOR2I_MM(39.0, 90.0)
  PITCH = 19.05
  AXIS = 169.705
  BUTTONS = [
    {'id':  1, 'x': 0, 'y': 0, 'offset-x': -0.76,   'offset-y':  0, 'unit': 1.5, 'orientation': 0},

    {'id':  2, 'x': 0, 'y': 1, 'offset-x': 0,   'offset-y':  0, 'unit': 1,   'orientation': 0},
    {'id':  8, 'x': 0, 'y': 2, 'offset-x': 0,   'offset-y':  0, 'unit': 1,   'orientation': 0},
    {'id': 14, 'x': 0, 'y': 3, 'offset-x': 0,   'offset-y':  0, 'unit': 1,   'orientation': 0},

    {'id':  3, 'x': 1, 'y': 1, 'offset-x': 0,   'offset-y':  0, 'unit': 1,   'orientation': 0},
    {'id':  9, 'x': 1, 'y': 2, 'offset-x': 0,   'offset-y':  0, 'unit': 1,   'orientation': 0},
    {'id': 15, 'x': 1, 'y': 3, 'offset-x': 0,   'offset-y':  0, 'unit': 1,   'orientation': 0},

    {'id':  4, 'x': 2, 'y': 1, 'offset-x': 0,   'offset-y': -PITCH / 8, 'unit': 1,   'orientation': 0},
    {'id': 10, 'x': 2, 'y': 2, 'offset-x': 0,   'offset-y': -PITCH / 8, 'unit': 1,   'orientation': 0},
    {'id': 16, 'x': 2, 'y': 3, 'offset-x': 0,   'offset-y': -PITCH / 8, 'unit': 1,   'orientation': 0},

    {'id':  5, 'x': 3, 'y': 1, 'offset-x': 0,   'offset-y': -PITCH / 3, 'unit': 1,   'orientation': 0},
    {'id': 11, 'x': 3, 'y': 2, 'offset-x': 0,   'offset-y': -PITCH / 3, 'unit': 1,   'orientation': 0},
    {'id': 17, 'x': 3, 'y': 3, 'offset-x': 0,   'offset-y': -PITCH / 3, 'unit': 1,   'orientation': 0},

    {'id':  6, 'x': 4, 'y': 1, 'offset-x': 0,   'offset-y': -PITCH / 8, 'unit': 1,   'orientation': 0},
    {'id': 12, 'x': 4, 'y': 2, 'offset-x': 0,   'offset-y': -PITCH / 8, 'unit': 1,   'orientation': 0},
    {'id': 18, 'x': 4, 'y': 3, 'offset-x': 0,   'offset-y': -PITCH / 8, 'unit': 1,   'orientation': 0},

    {'id':  7, 'x': 5, 'y': 1, 'offset-x': 0,   'offset-y': -PITCH / 8, 'unit': 1,   'orientation': 0},
    {'id': 13, 'x': 5, 'y': 2, 'offset-x': 0,   'offset-y': -PITCH / 8, 'unit': 1,   'orientation': 0},
    {'id': 19, 'x': 5, 'y': 3, 'offset-x': 0,   'offset-y': -PITCH / 8, 'unit': 1,   'orientation': 0},

    {'id': 20, 'x': 2, 'y': 4, 'offset-x': PITCH - 4.5,   'offset-y':  0, 'unit': 1,   'orientation': 0},
    {'id': 21, 'x': 3, 'y': 4, 'offset-x': PITCH - 4.5,   'offset-y':  0, 'unit': 1,   'orientation': 0},
    {'id': 22, 'x': 4, 'y': 4, 'offset-x': 7.39 - 0.0 + PITCH / 2, 'offset-y':  2.3, 'unit': 1,   'orientation': 12},
    {'id': 23, 'x': 5, 'y': 4, 'offset-x': 8.52 - 0.0 + PITCH / 2, 'offset-y': 12.6, 'unit': 1.5, 'orientation': 30},
  ]

  DIODES = [
    {'id':  1, 'x': 59.4, 'y': -5.0, 'offset-x': 3.6 *  0, 'offset-y':  0,       'orientation': -90 },
    {'id':  2, 'x': 59.4, 'y': -5.0, 'offset-x': 3.6 *  1, 'offset-y':  1.6,     'orientation': -90 },
    {'id':  8, 'x': 59.4, 'y': -5.0, 'offset-x': 3.6 *  2, 'offset-y':  1.6 * 2, 'orientation': -90 },
    {'id':  3, 'x': 59.4, 'y': -5.0, 'offset-x': 3.6 *  3, 'offset-y':  1.6,     'orientation': -90 },
    {'id':  9, 'x': 59.4, 'y': -5.0, 'offset-x': 3.6 *  4, 'offset-y':  1.6 * 2, 'orientation': -90 },
    {'id':  4, 'x': 59.4, 'y': -5.0, 'offset-x': 3.6 *  5, 'offset-y':  1.6,     'orientation': -90 },
    {'id': 10, 'x': 59.4, 'y': -5.0, 'offset-x': 3.6 *  6, 'offset-y':  1.6 * 2, 'orientation': -90 },
    {'id':  5, 'x': 59.4, 'y': -5.0, 'offset-x': 3.6 *  7, 'offset-y':  1.6,     'orientation': -90 },
    {'id': 11, 'x': 59.4, 'y': -5.0, 'offset-x': 3.6 *  8, 'offset-y':  1.6 * 2, 'orientation': -90 },
    {'id':  6, 'x': 59.4, 'y': -5.0, 'offset-x': 3.6 *  9, 'offset-y':  1.6,     'orientation': -90 },
    {'id': 12, 'x': 59.4, 'y': -5.0, 'offset-x': 3.6 * 10, 'offset-y':  1.6 * 2, 'orientation': -90 },
    {'id':  7, 'x': 59.4, 'y': -5.0, 'offset-x': 3.6 * 11, 'offset-y':  1.6,     'orientation': -90 },
    {'id': 13, 'x': 59.4, 'y': -5.0, 'offset-x': 3.6 * 12, 'offset-y':  1.6 * 2, 'orientation': -90 },

    {'id': 14, 'x': 11.0, 'y': 68.4, 'offset-x':  0, 'offset-y': 0, 'orientation': 180 },
    {'id': 15, 'x': 11.0, 'y': 68.4, 'offset-x':  8, 'offset-y': 0, 'orientation': 0 },
    {'id': 16, 'x': 11.0, 'y': 68.4, 'offset-x': 16, 'offset-y': 0, 'orientation': 0 },

    {'id': 17, 'x': 51.6, 'y': 62.0, 'offset-x':  0.0, 'offset-y': 0,   'orientation': 180 },
    {'id': 20, 'x': 51.6, 'y': 62.0, 'offset-x':  0.0, 'offset-y': 3.4, 'orientation': 180 },
    {'id': 18, 'x': 51.6, 'y': 62.0, 'offset-x': 11.2, 'offset-y': 0,   'orientation': 180 },
    {'id': 21, 'x': 51.6, 'y': 62.0, 'offset-x': 11.2, 'offset-y': 3.4, 'orientation': 180 },
    {'id': 22, 'x': 51.6, 'y': 62.0, 'offset-x': 24.0, 'offset-y': 3.4, 'orientation': 0 },
    {'id': 19, 'x': 51.6, 'y': 62.0, 'offset-x': 38.0, 'offset-y': 3.4, 'orientation': 0 },

    {'id': 23, 'x': 123.5, 'y': 79.1, 'offset-x': 0, 'offset-y': 0, 'orientation': -30 },
  ]

  pcb = pcbnew.GetBoard()

  def plate(self):
    ce = self.pcb.GetDrawings()[0]
    ce.SetPosition(self.OFFSET + pcbnew.VECTOR2I_MM(339.92, -22.0))

  def leftSide(self):
    for b in self.BUTTONS:
      sw = self.pcb.FindFootprintByReference('SW%d' % (b['id']))
      sw.SetPosition(
        self.OFFSET + pcbnew.VECTOR2I_MM(
          b['x'] * self.PITCH + b['offset-x'] + (b['unit'] - 1) * self.PITCH * 0.5,
          b['y'] * self.PITCH + b['offset-y']
        )
      )
      sw.SetOrientationDegrees(-b['orientation'])

  def rightSide(self):
    for b in self.BUTTONS:
      sw = self.pcb.FindFootprintByReference('SW%d' % (b['id'] + 23))
      x = b['x'] * self.PITCH + b['offset-x'] + (b['unit'] - 1) * self.PITCH * 0.5
      sw.SetPosition(
        self.OFFSET + pcbnew.VECTOR2I_MM(
          (self.AXIS - x) + self.AXIS,
          b['y'] * self.PITCH + b['offset-y']
        )
      )
      sw.SetOrientationDegrees(b['orientation'])

  def controller(self):
    sw14 = self.pcb.FindFootprintByReference('SW14')
    u1 = self.pcb.FindFootprintByReference('U1')
    u1.SetPosition(
      sw14.GetPosition() + pcbnew.VECTOR2I_MM(9.5, 25.85)
    )

  def ground(self):
    sw14 = self.pcb.FindFootprintByReference('SW14')
    mh1 = self.pcb.FindFootprintByReference('MH1')
    mh1.SetPosition(
      sw14.GetPosition() + pcbnew.VECTOR2I_MM(-3.5, 11.35)
    )
    mh1.SetOrientationDegrees(-70)

  def diode(self):
    for d in self.DIODES:
      df = self.pcb.FindFootprintByReference('D%d' % (d['id']))
      df.SetPosition(self.OFFSET +
        pcbnew.VECTOR2I_MM(d['x'], d['y']) +
        pcbnew.VECTOR2I_MM(d['offset-x'], d['offset-y'])
      )
      df.SetOrientationDegrees(d['orientation'])

    for d in self.DIODES:
      df = self.pcb.FindFootprintByReference('D%d' % (d['id'] + 23))
      df.SetPosition(self.OFFSET +
        pcbnew.VECTOR2I_MM(
          (self.AXIS - (d['x'] + d['offset-x'])) + self.AXIS,
          d['y'] + d['offset-y']
        )
      )
      df.SetOrientationDegrees(180 - d['orientation'])

  def Run(self):
    self.plate()
    self.leftSide()
    self.rightSide()
    self.controller()
    self.ground()
    self.diode()
    pcbnew.Refresh()

  def defaults(self):
    self.name = "escd monolith layout"
    self.category = "escd"
    self.description = "escd monolith layout"

MonolithPlugin().register()
