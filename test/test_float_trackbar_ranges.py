
from unittest import TestCase 
from exolib import FloatTrackBarRanges
from exofile import FloatTrackBarRange, TrackBarType

class TestFloatTrackBarRanges (TestCase):

  def test_deserialize (self):

    #without parameter

    trackrange = FloatTrackBarRanges.deserialize("-100.5,100.5,1")
    self.assertEqual(len(trackrange.values), 2)
    self.assertEqual(trackrange.values[0], -100.5)
    self.assertEqual(trackrange.values[1], 100.5)
    self.assertEqual(trackrange.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrange.accelerate, False)
    self.assertEqual(trackrange.decelerate, False)
    self.assertEqual(trackrange.parameter, None)

    trackrange = FloatTrackBarRanges.deserialize("-100.5,100.5,65")
    self.assertEqual(len(trackrange.values), 2)
    self.assertEqual(trackrange.values[0], -100.5)
    self.assertEqual(trackrange.values[1], 100.5)
    self.assertEqual(trackrange.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrange.accelerate, True)
    self.assertEqual(trackrange.decelerate, False)
    self.assertEqual(trackrange.parameter, None)

    trackrange = FloatTrackBarRanges.deserialize("-100.5,100.5,33")
    self.assertEqual(len(trackrange.values), 2)
    self.assertEqual(trackrange.values[0], -100.5)
    self.assertEqual(trackrange.values[1], 100.5)
    self.assertEqual(trackrange.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrange.accelerate, False)
    self.assertEqual(trackrange.decelerate, True)
    self.assertEqual(trackrange.parameter, None)

    trackrange = FloatTrackBarRanges.deserialize("-100.5,100.5,97")
    self.assertEqual(len(trackrange.values), 2)
    self.assertEqual(trackrange.values[0], -100.5)
    self.assertEqual(trackrange.values[1], 100.5)
    self.assertEqual(trackrange.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrange.accelerate, True)
    self.assertEqual(trackrange.decelerate, True)
    self.assertEqual(trackrange.parameter, None)

    #with parameter

    trackrange = FloatTrackBarRanges.deserialize("-100.5,100.5,1,100")
    self.assertEqual(len(trackrange.values), 2)
    self.assertEqual(trackrange.values[0], -100.5)
    self.assertEqual(trackrange.values[1], 100.5)
    self.assertEqual(trackrange.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrange.accelerate, False)
    self.assertEqual(trackrange.decelerate, False)
    self.assertEqual(trackrange.parameter, 100)

    trackrange = FloatTrackBarRanges.deserialize("-100.5,100.5,65,100")
    self.assertEqual(len(trackrange.values), 2)
    self.assertEqual(trackrange.values[0], -100.5)
    self.assertEqual(trackrange.values[1], 100.5)
    self.assertEqual(trackrange.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrange.accelerate, True)
    self.assertEqual(trackrange.decelerate, False)
    self.assertEqual(trackrange.parameter, 100)

    trackrange = FloatTrackBarRanges.deserialize("-100.5,100.5,33,100")
    self.assertEqual(len(trackrange.values), 2)
    self.assertEqual(trackrange.values[0], -100.5)
    self.assertEqual(trackrange.values[1], 100.5)
    self.assertEqual(trackrange.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrange.accelerate, False)
    self.assertEqual(trackrange.decelerate, True)
    self.assertEqual(trackrange.parameter, 100)

    trackrange = FloatTrackBarRanges.deserialize("-100.5,100.5,97,100")
    self.assertEqual(len(trackrange.values), 2)
    self.assertEqual(trackrange.values[0], -100.5)
    self.assertEqual(trackrange.values[1], 100.5)
    self.assertEqual(trackrange.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrange.accelerate, True)
    self.assertEqual(trackrange.decelerate, True)
    self.assertEqual(trackrange.parameter, 100)

    #single value

    trackrange = FloatTrackBarRanges.deserialize("-100.5")
    self.assertEqual(len(trackrange.values), 1)
    self.assertEqual(trackrange.values[0], -100.5)
    self.assertEqual(trackrange.trackbartype, TrackBarType.NONE)
    self.assertEqual(trackrange.accelerate, False)
    self.assertEqual(trackrange.decelerate, False)
    self.assertEqual(trackrange.parameter, None)

  def test_serialize (self):

    #single value without parameter

    trackrange = FloatTrackBarRanges(-100.5)
    self.assertEqual(len(trackrange.values), 1)
    self.assertEqual(trackrange.values[0], -100.5)
    self.assertEqual(trackrange.trackbartype, TrackBarType.NONE)
    self.assertEqual(trackrange.accelerate, False)
    self.assertEqual(trackrange.decelerate, False)
    self.assertEqual(trackrange.parameter, None)
    self.assertEqual(trackrange.serialize(), "-100.5")
    trackrangeat = trackrange.value_at(0)
    self.assertIsInstance(trackrangeat, FloatTrackBarRange)
    self.assertEqual(trackrangeat.start, -100.5)
    self.assertEqual(trackrangeat.end, -100.5)
    self.assertEqual(trackrangeat.trackbartype, TrackBarType.NONE)
    self.assertEqual(trackrangeat.accelerate, False)
    self.assertEqual(trackrangeat.decelerate, False)
    self.assertEqual(trackrangeat.parameter, None)
    self.assertEqual(trackrangeat.serialize(), "-100.5")
    trackrangeat = trackrange.value_at(1) #if overflow, return .value_at(max).
    self.assertIsInstance(trackrangeat, FloatTrackBarRange)
    self.assertEqual(trackrangeat.start, -100.5)
    self.assertEqual(trackrangeat.end, -100.5)
    self.assertEqual(trackrangeat.trackbartype, TrackBarType.NONE)
    self.assertEqual(trackrangeat.accelerate, False)
    self.assertEqual(trackrangeat.decelerate, False)
    self.assertEqual(trackrangeat.parameter, None)
    self.assertEqual(trackrangeat.serialize(), "-100.5")

    #2 values without parameter

    trackrange = FloatTrackBarRanges((-100.5, 100.5), TrackBarType.LINEAR)
    self.assertEqual(len(trackrange.values), 2)
    self.assertEqual(trackrange.values[0], -100.5)
    self.assertEqual(trackrange.values[1], 100.5)
    self.assertEqual(trackrange.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrange.accelerate, False)
    self.assertEqual(trackrange.decelerate, False)
    self.assertEqual(trackrange.parameter, None)
    self.assertEqual(trackrange.serialize(), "-100.5,100.5,1")
    trackrangeat = trackrange.value_at(0)
    self.assertIsInstance(trackrangeat, FloatTrackBarRange)
    self.assertEqual(trackrangeat.start, -100.5)
    self.assertEqual(trackrangeat.end, 100.5)
    self.assertEqual(trackrangeat.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrangeat.accelerate, False)
    self.assertEqual(trackrangeat.decelerate, False)
    self.assertEqual(trackrangeat.parameter, None)
    self.assertEqual(trackrangeat.serialize(), "-100.5,100.5,1")
    trackrangeat = trackrange.value_at(1) #if overflow, return .value_at(max).
    self.assertIsInstance(trackrangeat, FloatTrackBarRange)
    self.assertEqual(trackrangeat.start, 100.5)
    self.assertEqual(trackrangeat.end, 100.5)
    self.assertEqual(trackrangeat.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrangeat.accelerate, False)
    self.assertEqual(trackrangeat.decelerate, False)
    self.assertEqual(trackrangeat.parameter, None)
    self.assertEqual(trackrangeat.serialize(), "100.5,100.5,1")

    #2 values with parameter

    trackrange = FloatTrackBarRanges((-100.5, 100.5), TrackBarType.LINEAR, accelerate=True)
    self.assertEqual(len(trackrange.values), 2)
    self.assertEqual(trackrange.values[0], -100.5)
    self.assertEqual(trackrange.values[1], 100.5)
    self.assertEqual(trackrange.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrange.accelerate, True)
    self.assertEqual(trackrange.decelerate, False)
    self.assertEqual(trackrange.parameter, None)
    self.assertEqual(trackrange.serialize(), "-100.5,100.5,65")
    trackrangeat = trackrange.value_at(0)
    self.assertIsInstance(trackrangeat, FloatTrackBarRange)
    self.assertEqual(trackrangeat.start, -100.5)
    self.assertEqual(trackrangeat.end, 100.5)
    self.assertEqual(trackrangeat.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrangeat.accelerate, True)
    self.assertEqual(trackrangeat.decelerate, False)
    self.assertEqual(trackrangeat.parameter, None)
    self.assertEqual(trackrangeat.serialize(), "-100.5,100.5,65")
    trackrangeat = trackrange.value_at(1) #if overflow, return .value_at(max).
    self.assertIsInstance(trackrangeat, FloatTrackBarRange)
    self.assertEqual(trackrangeat.start, 100.5)
    self.assertEqual(trackrangeat.end, 100.5)
    self.assertEqual(trackrangeat.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrangeat.accelerate, True)
    self.assertEqual(trackrangeat.decelerate, False)
    self.assertEqual(trackrangeat.parameter, None)
    self.assertEqual(trackrangeat.serialize(), "100.5,100.5,65")

    trackrange = FloatTrackBarRanges((-100.5, 100.5), TrackBarType.LINEAR, accelerate=True, parameter=100)
    self.assertEqual(len(trackrange.values), 2)
    self.assertEqual(trackrange.values[0], -100.5)
    self.assertEqual(trackrange.values[1], 100.5)
    self.assertEqual(trackrange.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrange.accelerate, True)
    self.assertEqual(trackrange.decelerate, False)
    self.assertEqual(trackrange.parameter, 100)
    self.assertEqual(trackrange.serialize(), "-100.5,100.5,65,100")
    trackrangeat = trackrange.value_at(0)
    self.assertIsInstance(trackrangeat, FloatTrackBarRange)
    self.assertEqual(trackrangeat.start, -100.5)
    self.assertEqual(trackrangeat.end, 100.5)
    self.assertEqual(trackrangeat.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrangeat.accelerate, True)
    self.assertEqual(trackrangeat.decelerate, False)
    self.assertEqual(trackrangeat.parameter, 100)
    self.assertEqual(trackrangeat.serialize(), "-100.5,100.5,65,100")
    trackrangeat = trackrange.value_at(1) #if overflow, return .value_at(max).
    self.assertIsInstance(trackrangeat, FloatTrackBarRange)
    self.assertEqual(trackrangeat.start, 100.5)
    self.assertEqual(trackrangeat.end, 100.5)
    self.assertEqual(trackrangeat.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrangeat.accelerate, True)
    self.assertEqual(trackrangeat.decelerate, False)
    self.assertEqual(trackrangeat.parameter, 100)
    self.assertEqual(trackrangeat.serialize(), "100.5,100.5,65,100")

    #3 values without parameter

    trackrange = FloatTrackBarRanges((-100.5, 100.5, -100.5), TrackBarType.LINEAR)
    self.assertEqual(len(trackrange.values), 3)
    self.assertEqual(trackrange.values[0], -100.5)
    self.assertEqual(trackrange.values[1], 100.5)
    self.assertEqual(trackrange.values[2], -100.5)
    self.assertEqual(trackrange.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrange.accelerate, False)
    self.assertEqual(trackrange.decelerate, False)
    self.assertEqual(trackrange.parameter, None)
    self.assertEqual(trackrange.serialize(), "-100.5,100.5,1") #.serialize() always serialize first serializable-value.
    trackrangeat = trackrange.value_at(0)
    self.assertIsInstance(trackrangeat, FloatTrackBarRange)
    self.assertEqual(trackrangeat.start, -100.5)
    self.assertEqual(trackrangeat.end, 100.5)
    self.assertEqual(trackrangeat.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrangeat.accelerate, False)
    self.assertEqual(trackrangeat.decelerate, False)
    self.assertEqual(trackrangeat.parameter, None)
    self.assertEqual(trackrangeat.serialize(), "-100.5,100.5,1")
    trackrangeat = trackrange.value_at(1)
    self.assertIsInstance(trackrangeat, FloatTrackBarRange)
    self.assertEqual(trackrangeat.start, 100.5)
    self.assertEqual(trackrangeat.end, -100.5)
    self.assertEqual(trackrangeat.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrangeat.accelerate, False)
    self.assertEqual(trackrangeat.decelerate, False)
    self.assertEqual(trackrangeat.parameter, None)
    self.assertEqual(trackrangeat.serialize(), "100.5,-100.5,1")
    trackrangeat = trackrange.value_at(2) #if overflow, return .value_at(max).
    self.assertIsInstance(trackrangeat, FloatTrackBarRange)
    self.assertEqual(trackrangeat.start, -100.5)
    self.assertEqual(trackrangeat.end, -100.5)
    self.assertEqual(trackrangeat.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrangeat.accelerate, False)
    self.assertEqual(trackrangeat.decelerate, False)
    self.assertEqual(trackrangeat.parameter, None)
    self.assertEqual(trackrangeat.serialize(), "-100.5,-100.5,1")

    #3 values with parameter

    trackrange = FloatTrackBarRanges((-100.5, 100.5, -100.5), TrackBarType.LINEAR, accelerate=True)
    self.assertEqual(len(trackrange.values), 3)
    self.assertEqual(trackrange.values[0], -100.5)
    self.assertEqual(trackrange.values[1], 100.5)
    self.assertEqual(trackrange.values[2], -100.5)
    self.assertEqual(trackrange.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrange.accelerate, True)
    self.assertEqual(trackrange.decelerate, False)
    self.assertEqual(trackrange.parameter, None)
    self.assertEqual(trackrange.serialize(), "-100.5,100.5,65") #.serialize() always serialize first serializable-value.
    trackrangeat = trackrange.value_at(0)
    self.assertIsInstance(trackrangeat, FloatTrackBarRange)
    self.assertEqual(trackrangeat.start, -100.5)
    self.assertEqual(trackrangeat.end, 100.5)
    self.assertEqual(trackrangeat.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrangeat.accelerate, True)
    self.assertEqual(trackrangeat.decelerate, False)
    self.assertEqual(trackrangeat.parameter, None)
    self.assertEqual(trackrangeat.serialize(), "-100.5,100.5,65")
    trackrangeat = trackrange.value_at(1)
    self.assertIsInstance(trackrangeat, FloatTrackBarRange)
    self.assertEqual(trackrangeat.start, 100.5)
    self.assertEqual(trackrangeat.end, -100.5)
    self.assertEqual(trackrangeat.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrangeat.accelerate, True)
    self.assertEqual(trackrangeat.decelerate, False)
    self.assertEqual(trackrangeat.parameter, None)
    self.assertEqual(trackrangeat.serialize(), "100.5,-100.5,65")
    trackrangeat = trackrange.value_at(2) #if overflow, return .value_at(max).
    self.assertIsInstance(trackrangeat, FloatTrackBarRange)
    self.assertEqual(trackrangeat.start, -100.5)
    self.assertEqual(trackrangeat.end, -100.5)
    self.assertEqual(trackrangeat.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrangeat.accelerate, True)
    self.assertEqual(trackrangeat.decelerate, False)
    self.assertEqual(trackrangeat.parameter, None)
    self.assertEqual(trackrangeat.serialize(), "-100.5,-100.5,65")

    trackrange = FloatTrackBarRanges((-100.5, 100.5, -100.5), TrackBarType.LINEAR, accelerate=True, parameter=100)
    self.assertEqual(len(trackrange.values), 3)
    self.assertEqual(trackrange.values[0], -100.5)
    self.assertEqual(trackrange.values[1], 100.5)
    self.assertEqual(trackrange.values[2], -100.5)
    self.assertEqual(trackrange.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrange.accelerate, True)
    self.assertEqual(trackrange.decelerate, False)
    self.assertEqual(trackrange.parameter, 100)
    self.assertEqual(trackrange.serialize(), "-100.5,100.5,65,100") #.serialize() always serialize first serializable-value.
    trackrangeat = trackrange.value_at(0)
    self.assertIsInstance(trackrangeat, FloatTrackBarRange)
    self.assertEqual(trackrangeat.start, -100.5)
    self.assertEqual(trackrangeat.end, 100.5)
    self.assertEqual(trackrangeat.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrangeat.accelerate, True)
    self.assertEqual(trackrangeat.decelerate, False)
    self.assertEqual(trackrangeat.parameter, 100)
    self.assertEqual(trackrangeat.serialize(), "-100.5,100.5,65,100")
    trackrangeat = trackrange.value_at(1)
    self.assertIsInstance(trackrangeat, FloatTrackBarRange)
    self.assertEqual(trackrangeat.start, 100.5)
    self.assertEqual(trackrangeat.end, -100.5)
    self.assertEqual(trackrangeat.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrangeat.accelerate, True)
    self.assertEqual(trackrangeat.decelerate, False)
    self.assertEqual(trackrangeat.parameter, 100)
    self.assertEqual(trackrangeat.serialize(), "100.5,-100.5,65,100")
    trackrangeat = trackrange.value_at(2) #if overflow, return .value_at(max).
    self.assertIsInstance(trackrangeat, FloatTrackBarRange)
    self.assertEqual(trackrangeat.start, -100.5)
    self.assertEqual(trackrangeat.end, -100.5)
    self.assertEqual(trackrangeat.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrangeat.accelerate, True)
    self.assertEqual(trackrangeat.decelerate, False)
    self.assertEqual(trackrangeat.parameter, 100)
    self.assertEqual(trackrangeat.serialize(), "-100.5,-100.5,65,100")

  def test_merge (self):

    #merge single values 

    trackrange = FloatTrackBarRanges(-100.5)
    trackrange2 = FloatTrackBarRanges(-100.5)
    trackrangemerged = trackrange.merge(trackrange2)
    self.assertEqual(len(trackrangemerged.values), 1)
    self.assertEqual(trackrangemerged.values[0], -100.5)
    self.assertEqual(trackrangemerged.trackbartype, TrackBarType.NONE)
    self.assertEqual(trackrangemerged.accelerate, False)
    self.assertEqual(trackrangemerged.decelerate, False)
    self.assertEqual(trackrangemerged.parameter, None)

    #merge 2 values without parameter

    trackrange = FloatTrackBarRanges((-100.5, 100.5), TrackBarType.LINEAR)
    trackrange2 = FloatTrackBarRanges((100.5, -100.5), TrackBarType.LINEAR)
    trackrangemerged = trackrange.merge(trackrange2)
    self.assertEqual(len(trackrangemerged.values), 3)
    self.assertEqual(trackrangemerged.values[0], -100.5)
    self.assertEqual(trackrangemerged.values[1], 100.5)
    self.assertEqual(trackrangemerged.values[2], -100.5)
    self.assertEqual(trackrangemerged.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrangemerged.accelerate, False)
    self.assertEqual(trackrangemerged.decelerate, False)
    self.assertEqual(trackrangemerged.parameter, None)

    #merge 2 values with parameter

    trackrange = FloatTrackBarRanges((-100.5, 100.5), TrackBarType.LINEAR, accelerate=True)
    trackrange2 = FloatTrackBarRanges((100.5, -100.5), TrackBarType.LINEAR, accelerate=True)
    trackrangemerged = trackrange.merge(trackrange2)
    self.assertEqual(len(trackrangemerged.values), 3)
    self.assertEqual(trackrangemerged.values[0], -100.5)
    self.assertEqual(trackrangemerged.values[1], 100.5)
    self.assertEqual(trackrangemerged.values[2], -100.5)
    self.assertEqual(trackrangemerged.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrangemerged.accelerate, True)
    self.assertEqual(trackrangemerged.decelerate, False)
    self.assertEqual(trackrangemerged.parameter, None)

    trackrange = FloatTrackBarRanges((-100.5, 100.5), TrackBarType.LINEAR, accelerate=True, parameter=100)
    trackrange2 = FloatTrackBarRanges((100.5, -100.5), TrackBarType.LINEAR, accelerate=True, parameter=100)
    trackrangemerged = trackrange.merge(trackrange2)
    self.assertEqual(len(trackrangemerged.values), 3)
    self.assertEqual(trackrangemerged.values[0], -100.5)
    self.assertEqual(trackrangemerged.values[1], 100.5)
    self.assertEqual(trackrangemerged.values[2], -100.5)
    self.assertEqual(trackrangemerged.trackbartype, TrackBarType.LINEAR)
    self.assertEqual(trackrangemerged.accelerate, True)
    self.assertEqual(trackrangemerged.decelerate, False)
    self.assertEqual(trackrangemerged.parameter, 100)

  def test_merge_error (self):

    #merge single values 

    trackrange = FloatTrackBarRanges(100.5)
    trackrange2 = FloatTrackBarRanges(-100.5)
    with self.assertRaises(ValueError):
      trackrange.merge(trackrange2)

    #merge 2 values without parameter

    trackrange = FloatTrackBarRanges((100.5, -100.5), TrackBarType.LINEAR)
    trackrange2 = FloatTrackBarRanges((100.5, -100.5), TrackBarType.LINEAR) #non-connectable values.
    with self.assertRaises(ValueError):
      trackrange.merge(trackrange2)

    trackrange = FloatTrackBarRanges((100.5, -100.5), TrackBarType.LINEAR)
    trackrange2 = FloatTrackBarRanges((-100.5, 100.5), TrackBarType.ACCELERATION) #different TrackBarType.
    with self.assertRaises(ValueError):
      trackrange.merge(trackrange2)

    #merge 2 values with parameter

    trackrange = FloatTrackBarRanges((100.5, -100.5), TrackBarType.LINEAR, accelerate=False)
    trackrange2 = FloatTrackBarRanges((-100.5, 100.5), TrackBarType.LINEAR, accelerate=True) #different .accelerate.
    with self.assertRaises(ValueError):
      trackrange.merge(trackrange2)

    trackrange = FloatTrackBarRanges((100.5, -100.5), TrackBarType.LINEAR, accelerate=True, parameter=100)
    trackrange2 = FloatTrackBarRanges((-100.5, 100.5), TrackBarType.LINEAR, accelerate=True, parameter=0) #different .parameter.
    with self.assertRaises(ValueError):
      trackrange.merge(trackrange2)
